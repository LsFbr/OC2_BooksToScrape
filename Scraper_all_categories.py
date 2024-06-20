from utils import *
from Scraper_category import main_scraper_category


def main_scraper_all_categories():
    url_site_index="https://books.toscrape.com/index.html"
    urls_categories = extract_urls_categories(url_site_index)

    for url_category in urls_categories:
        main_scraper_category(url_category)


if __name__ == "__main__":
    main_scraper_all_categories()
