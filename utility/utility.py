months_list = [None, 'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

def read_csv():
    with open("datas/files/episodes.csv", "r", encoding="utf-8", newline="") as csvfile:
        # Ignorer l'en-tête du fichier CSV
        next(csvfile)

        table = []

        for line in csvfile:
            cells = line.split(",")

            show = cells[0]
            episode = cells[1]
            season = cells[2]
            country = cells[3]
            channel = cells[4]
            date = cells[5]
            link = cells[6]

            table.append((show, episode, season, country, channel, date, link))

    print(table)


def get_month(month_id):
    return months_list[int(month_id)]