from utils import *

url_book = input("Please enter a product's url : ")

def main_scraper_book():
    extract_book(url_book)
    infos_to_csv = extract_book(url_book)        
    create_csv(infos_to_csv)

if __name__ == "__main__":
    main_scraper_book()

