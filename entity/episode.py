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
    def get_number_of_episodes_by_month(month):
        db = DatabaseSingleton().get_cursor()

        query = """
                SELECT COUNT(*) AS episode_count
                FROM episodes
                WHERE SUBSTR(date, 4, 2) = ?;
                """

        # Exécution de la requête
        db.execute(query, (month,))

        # Récupération des résultats
        results = db.fetchall()
        (number,) = results
        return number[0]

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

        return results

    @staticmethod
    def channel_with_highest_episode_number_for_month(month):
        channels = Episode.get_number_of_episode_by_channel_by_month(month)
        return channels[0]

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

        return results

    @staticmethod
    def country_with_highest_episode_number_for_month(month):
        countries = Episode.get_number_of_episode_by_country_by_month(month)
        return countries[0]

    @staticmethod
    def channel_with_highest_consecutive_diffusion_days(month):
        db = DatabaseSingleton().get_cursor()

        # Requête SQL pour récupérer les épisodes diffusés en Octobre
        query = """
                SELECT channel, date
                FROM episodes
                WHERE SUBSTR(date, 4, 2) = ?
                ORDER BY channel, date;
            """

        # Exécution de la requête
        db.execute(query, (month,))
        records = db.fetchall()

        # Dictionnaire pour stocker le nombre de jours consécutifs par chaîne
        consecutive_days = {}
        current_channel = ""
        consecutive_days_count = 0

        # Calcul du nombre de jours consécutifs par chaîne
        for record in records:
            channel, date_str = record
            current_date = int(date_str.split("-")[0])  # Récupérer le jour du mois

            if channel != current_channel or not current_date - previous_date == 1:  # noqa: F821
                # Changement de chaîne ou jour non consécutif, réinitialiser le compteur
                consecutive_days_count = 1
            else:
                # Même chaîne et jour suivant, augmenter le compteur
                consecutive_days_count += 1

            if (
                channel not in consecutive_days
                or consecutive_days_count > consecutive_days[channel]
            ):
                # Mettre à jour le nombre de jours consécutifs si nécessaire
                consecutive_days[channel] = consecutive_days_count

            # Mettre à jour le canal actuel et la date précédente
            current_channel = channel
            previous_date = current_date  # noqa: F841

        # Trouver la chaîne avec le plus grand nombre de jours consécutifs
        max_consecutive_days_channel = max(consecutive_days, key=consecutive_days.get)
        max_consecutive_days = consecutive_days[max_consecutive_days_channel]

        return max_consecutive_days_channel, max_consecutive_days
