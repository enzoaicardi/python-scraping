from service.scraper import Scraper
from utility import utility
from entity.episode import Episode
import argparse


def summarize_episodes(month):
    scraper = Scraper()
    print(
        f"[{scraper.scrape_month(month)}] episodes seront diffusés pendant le mois de [{utility.get_month(month)}]"
    )
    country, episodes_country = Episode.country_with_highest_episode_number_for_month(
        month
    )
    print(
        f"C'est [{country}] qui diffusera le plus d'épisodes avec [{episodes_country}] épisodes."
    )
    channel, episodes_channels = Episode.channel_with_highest_episode_number_for_month(
        month
    )
    print(
        f"C'est [{channel}] qui diffusera le plus d'episodes avec [{episodes_channels}] épisodes."
    )
    channel, days = Episode.channel_with_highest_consecutive_diffusion_days(month)
    print(
        f"C'est [{channel}] qui diffusera des épisodes pendant le plus grand nombre de jours consécutifs avec [{days}] de jours consécutifs."
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Summarize episodes for a given month."
    )
    parser.add_argument("--month", type=str, help="Month (e.g., 11)")

    args = parser.parse_args()
    month = args.month

    if month:
        summarize_episodes(month)
    else:
        print("Veuillez spécifier le mois en utilisant l'argument --month.")
