from service.scraper import Scraper
from utility import utility
from entity.episode import Episode


def main():
    scraper = Scraper()
    print(scraper.scrape_last_month())
    scraper.export_to_csv()
    scraper.populate_episodes_table_database()
    Episode.get_number_of_episode_by_channel_by_month("11")


if __name__ == "__main__":
    main()
