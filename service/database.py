import sqlite3


class DatabaseSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseSingleton, cls).__new__(cls)
            cls._instance.conn = sqlite3.connect("datas/database/database.db")
            cls._instance.cursor = cls._instance.conn.cursor()
            cls._instance.create_tables()
        return cls._instance

    def get_cursor(self):
        return self.cursor

    def create_tables(self):
        # Créer la table "durations" si elle n'existe pas déjà
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS durations
                              (episode_id INTEGER PRIMARY KEY,
                              duration INTEGER NOT NULL,
                              FOREIGN KEY (episode_id) REFERENCES episodes(id))"""
        )

        # Créer la table "episodes" si elle n'existe pas déjà
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS episodes
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              show TEXT NOT NULL,
                              episode INTEGER NOT NULL,
                              season INTEGER NOT NULL,
                              country TEXT NOT NULL,
                              channel TEXT NOT NULL,
                              date TEXT NOT NULL,
                              link TEXT NOT NULL UNIQUE) """
        )

        # Valider les changements dans la base de données
        self.conn.commit()
