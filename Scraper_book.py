import requests
from bs4 import BeautifulSoup
import csv
from utils import *

# For one book
  
def extract_book(url_book):
    infos_to_csv ={}

    # parse the web page
    response = requests.get(url_book)
    soup = BeautifulSoup(response.text, "html.parser")

    # add product url to info_to_csv dictionary   
    infos_to_csv["product_page_url"] = url_book

    extract_product_informations(soup)
    infos_to_csv["universal_ product_code"] = extract_product_informations(soup)[0]
    infos_to_csv["price_excluding_tax"] = extract_product_informations(soup)[2]
    infos_to_csv["price_including_tax"] = extract_product_informations(soup)[3]
    infos_to_csv["number_available"] = extract_product_informations(soup)[5]

    extract_category(soup)
    infos_to_csv["category"] = extract_category(soup)[-1]

    extract_title(soup)
    infos_to_csv["title"] = extract_title(soup)

    extract_image_url(soup)
    infos_to_csv["image_url"] = extract_image_url(soup)

    extract_product_description(soup)
    infos_to_csv["product_description"] = extract_product_description(soup)

    extract_review_rating(soup)
    infos_to_csv["review_rating"] = extract_review_rating(soup)
    
    return infos_to_csv

def create_csv(infos_to_csv):
    headers = ["product_page_url", "universal_ product_code", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"]
    
    with open("datas_book.csv", "w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerow(infos_to_csv)

url_book = input("Please enter a product's url : ")

def main_scraper_book():
    extract_book(url_book)
    infos_to_csv = extract_book(url_book)        
    create_csv(infos_to_csv)

if __name__ == "__main__":
    main_scraper_book()

