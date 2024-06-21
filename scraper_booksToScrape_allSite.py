from utils import *


def main_scraper_booksToScrape_allSite_():
    url_site_index="https://books.toscrape.com/index.html"
    urls_categories = extract_urls_categories(url_site_index)

    for url_category in urls_categories:
        scraper_booksToScrape_oneCategory(url_category)


if __name__ == "__main__":
    main_scraper_booksToScrape_allSite_()
