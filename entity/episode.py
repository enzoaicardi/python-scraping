from service.database import DatabaseSingleton


class Episode:
    def __init__(self, show, episode, season, country, channel, date, link):
        self.show = show
        self.episode = episode
        self.season = season
        self.country = country
        self.channel = channel
        self.date = date
        self.link = link

    @staticmethod
    def get_number_of_episode_by_channel_by_month(month):
        db = DatabaseSingleton().get_cursor()

        query = """
                SELECT channel, COUNT(*) AS episode_count
                FROM episodes
                WHERE SUBSTR(date, 4, 2) = ?
                GROUP BY channel
                ORDER BY episode_count DESC;
            """

        # Exécution de la requête
        db.execute(query, (month,))

        # Récupération des résultats
        results = db.fetchall()

        # Affichage des résultats
        for row in results:
            channel, episode_count = row
            print(
                f"Chaîne : {channel}, Nombre d'épisodes diffusés en Octobre : {episode_count}"
            )

    @staticmethod
    def get_number_of_episode_by_country_by_month(month):
        db = DatabaseSingleton().get_cursor()

        query = """
            SELECT country, COUNT(*) AS episode_count
            FROM episodes
            WHERE SUBSTR(date, 4, 2) = ?
            GROUP BY country
            ORDER BY episode_count DESC;
        """

        # Exécution de la requête
        db.execute(query, (month,))

        # Récupération des résultats
        results = db.fetchall()

        # Affichage des résultats
        for row in results:
            country, episode_count = row
            print(
                f"Pays : {country}, Nombre d'épisodes diffusés en Octobre : {episode_count}"
            )
