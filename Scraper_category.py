import requests
from bs4 import BeautifulSoup
import csv
import os
from utils import *

url_category = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"  


    
def extract_book(url_book): # Extracts datas from a book page
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

def extract_category_urls_books(url_category): # Extracts all books urls in a category
    urls_books = []

    base_url = url_category.rsplit("/", 1)[0] + "/"
    page = "index.html"
    page_number = 1

    while True:
        full_url = base_url + page

        response = requests.get(full_url)
        soup = BeautifulSoup(response.text, "html.parser")
       

        page_urls_books = extract_page_urls_books(soup)

        for i in page_urls_books:
            urls_books.append(i)
        

        # check for other pages 
        next_page = soup.find("li", {"class" : "next"})
        if next_page:
            page_number += 1 
            page = f"page-{page_number}.html"
        else: 
            break # no more pages 
    
    return urls_books 

def create_csv(infos_to_csv): # Creates csv and/or add new line in it
    headers = ["product_page_url", "universal_ product_code", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"]
    file_exists = os.path.isfile("datas_category_book.csv") 
    if not file_exists: # Checks if csv file already exists. If not :
        with open("datas_category_book.csv", "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)        
            writer.writeheader()
            writer.writerow(infos_to_csv)
    else : 
        with open("datas_category_book.csv", "a", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)        
            writer.writerow(infos_to_csv)

url_category = input("Please enter a category url : ")
#extract_category_urls_books(url_category)

def main_scraper_category():
    extract_category_urls_books(url_category)
    urls_books = extract_category_urls_books(url_category)
    for url_book in urls_books:
        info_to_csv = extract_book(url_book)
        print(info_to_csv["title"])
        create_csv(info_to_csv)

if __name__ == "__main__":
    main_scraper_category()


        
