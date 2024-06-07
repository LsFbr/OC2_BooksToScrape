import requests
from bs4 import BeautifulSoup
import csv


# Pour un Livre
# Load

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

def extract_book(url):
    infos_to_csv ={}
    
    infos_to_csv["product_page_url"] = url

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")


    # find product information
    product_information = []

    trs = soup.find_all("tr")

    for tr in trs:
        td = tr.find("td")
        product_information.append(td.text)

    infos_to_csv["universal_ product_code"] = product_information[0]
    infos_to_csv["price_excluding_tax"] = product_information[2]
    infos_to_csv["price_including_tax"] = product_information[3]
    infos_to_csv["number_available"] = product_information[5]
    

    # find title and category
    nav = []

    ul = soup.find("ul", {"class": "breadcrumb"})
    links = ul.find_all("a")
    for link in links:
        nav.append(link.text)
    
    print(nav)


    print(infos_to_csv)

extract_book(url)






"""
product_page_url                
0 universal_ product_code (upc)
title
3 price_including_tax
2 price_excluding_tax
5 number_available
product_description
category
review_rating
image_url
"""