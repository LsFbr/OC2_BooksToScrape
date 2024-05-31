import requests
from bs4 import BeautifulSoup


# Pour un Livre
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(url)
page=response.content
soup = BeautifulSoup(page, "html.parser")
infos =[]
trs = soup.find_all("tr")
for tr in trs:
    td = tr.find("td")
    infos.append(td)
print(infos)

"""
product_page_url
universal_ product_code (upc)
title
price_including_tax
price_excluding_tax
number_available
product_description
category
review_rating
image_url
"""