import requests
from bs4 import BeautifulSoup
import csv


# Pour un Livre
# Load

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

def extract_book(url):
    infos_to_csv ={}

# add product url to info_to_csv dictionary   
    infos_to_csv["product_page_url"] = url


#parse the web page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")


# extract product informations
    product_informations = []

    trs = soup.find_all("tr")

    for tr in trs:
        td = tr.find("td")
        product_informations.append(td.text)
# add the desired product informations to infos_to_csv dictionary
    infos_to_csv["universal_ product_code"] = product_informations[0]
    infos_to_csv["price_excluding_tax"] = product_informations[2]
    infos_to_csv["price_including_tax"] = product_informations[3]
    infos_to_csv["number_available"] = product_informations[5]
    

# extract category
    breadcrumb = []

    ul = soup.find("ul", {"class": "breadcrumb"})
    links = ul.find_all("a")
    for link in links:
        breadcrumb.append(link.text)
# extract title
    title = soup.find("li", {"class": "active"})
    breadcrumb.append(title.text)
# add the title and category to infos_to_csv dictionary
    infos_to_csv["title"] = breadcrumb[-1]
    infos_to_csv["category"] = breadcrumb[-2]



# extract image's url
    div = soup.find("div", {"class": "item active"})
    image = div.find("img")
    image_url = image.get("src")
# add the image's url to infos_to_csv dictionary
    infos_to_csv["image_url"] = image_url
    


    print(infos_to_csv)

extract_book(url)






"""
- product_page_url                
- 0 universal_ product_code (upc)
- title
- 3 price_including_tax
- 2 price_excluding_tax
- 5 number_available
product_description
- category
review_rating
-image_url
"""