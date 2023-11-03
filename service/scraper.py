from service.database import DatabaseSingleton
from entity.episode import Episode
import requests
import re
import bs4
from config.config import Config
import csv


class Scraper:
    def __init__(self):
        self.db = DatabaseSingleton().get_cursor()
        self.episodes = []

    def scrape_last_month(self):
        response = requests.get(Config.BASE_URL + "/calendrier_des_series.html").content
        page = bs4.BeautifulSoup(response, "html")

        columns = page.find_all("td", class_="td_jour")

        calendar = [
            {
                "date": column.find("div", class_="div_jour").get("id")[5:],
                "names": [
                    re.sub(" +saison [0-9]+ episode .+$", "", name.get("title"))
                    for name in column.find_all("a", class_="liens")
                ],
                "episodes": [
                    {"season": num[0], "episode": num[1]}
                    for num in (
                        name.getText().split(".")
                        for name in column.find_all("a", class_="liens")
                    )
                ],
                "countries": [
                    country.find_previous_sibling().find_previous_sibling().get("alt")
                    for country in column.find_all("span", class_="calendrier_episodes")
                ],
                "channels": [
                    channel.find_previous_sibling().get("alt")
                    for channel in column.find_all("span", class_="calendrier_episodes")
                ],
                "links": [
                    link.get("href") for link in column.find_all("a", class_="liens")
                ],
            }
            for column in columns
            if column.find("div", class_="div_jour")
        ]
        for column in calendar:
            for i in range(0, len(column["names"])):
                self.episodes.append(
                    Episode(
                        column["names"][i],
                        # Les épisodes spéciaux sont notés 'XX' et ne peuvent donc pas êtres convertis
                        # en entiers, on utilisera donc -1
                        int(column["episodes"][i]["episode"])
                        if column["episodes"][i]["episode"] != "XX"
                        else -1,
                        int(column["episodes"][i]["season"]),
                        column["countries"][i],
                        column["channels"][i],
                        column["date"],
                        column["links"][i],
                    )
                )

        return len(self.episodes)

    def export_to_csv(self):
        with open(
            "datas/files/episodes.csv", "w", encoding="utf-8", newline=""
        ) as csvfile:
            fieldnames = [
                "show",
                "episode",
                "season",
                "country",
                "channel",
                "date",
                "link",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Écriture de l'en-tête du fichier CSV
            writer.writeheader()

            # Écriture des données des épisodes dans le fichier CSV
            for episode in self.episodes:
                writer.writerow(
                    {
                        "show": episode.show,
                        "episode": episode.episode,
                        "season": episode.season,
                        "country": episode.country,
                        "channel": episode.channel,
                        "date": episode.date,
                        "link": episode.link,
                    }
                )

        print("CSV file created successfuly")

    def populate_episodes_table_database(self):
        for episode in self.episodes:
            self.db.execute(
                "INSERT OR IGNORE INTO episodes (show, episode, season, country, channel, date, link) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    episode.show,
                    episode.episode,
                    episode.season,
                    episode.country,
                    episode.channel,
                    episode.date,
                    episode.link,
                ),
            )
        self.db.connection.commit()

        print("Base de données peuplée avec succès.")
