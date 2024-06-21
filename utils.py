import requests
from bs4 import BeautifulSoup
import csv
import os
import re

def extract_product_informations(soup):

    product_informations = []

    trs = soup.find_all("tr")

    for tr in trs:
        td = tr.find("td")
        product_informations.append(td.text)
    
    
    return product_informations

def extract_category(soup):
    breadcrumb = []

    links = soup.find("ul", {"class": "breadcrumb"}).find_all("a")
    for link in links:
        breadcrumb.append(link.text)
    
    return breadcrumb    

def extract_title(soup):
    title = soup.find("li", {"class": "active"})
    
    return title.text
    
def extract_image_url(soup):
    div = soup.find("div", {"class": "item active"}).find("img")
    image_url = div.get("src")
    image_url = image_url.split("/", 2)[2]
    image_url = "https://books.toscrape.com/" + image_url
    
    return image_url   

def sanitize_filename(filename, max_length=50):
    sanitized = re.sub(r'[\\/*?:"<>|]', "_", filename)
    return sanitized[:max_length]

def download_image_file(soup):

    save_path = "books_images"
    image_name = sanitize_filename(extract_title(soup)) + "_thumbnail.jpg"
    image_url = extract_image_url(soup)
    
    response = requests.get(image_url)
    response.encoding = "utf-8"

    if response.status_code == 200:
        os.makedirs(save_path, exist_ok = True)
        file_path = os.path.join(save_path, image_name)
        with open(file_path, "wb") as file:
            file.write(response.content)

def extract_product_description(soup):  
    try: 
        product_description = soup.find("article", {"class": "product_page"}).find("p", recursive=False)
        
        return product_description.text
    
    except: 
        return "No description"
        
def extract_review_rating(soup):
    str_to_int = {
        "One":1 ,
        "Two":2,
        "Three":3,
        "Four":4,
        "Five":5
    }
    rating_class = soup.find("p",{"class": "star-rating"}).attrs
    rating_class = rating_class["class"]
    rating_class = rating_class[1]
    review_rating = str_to_int[rating_class]

    return review_rating
    
def extract_page_urls_books(soup): # Extracts all books's urls from a category page
    page_urls_books = []
    lis = soup.find_all("li", {"class": "col-xs-6"})
    
    for li in lis:
        url_book = li.find("h3").find("a")["href"]
        url_book = url_book.split("/", 3)[3]        
        url_book = "https://books.toscrape.com/catalogue/" + url_book       
        page_urls_books.append(url_book)
    return page_urls_books

def extract_book(url_book): # Extracts datas from a book page
    infos_to_csv ={}

    # parse the web page
    response = requests.get(url_book)
    response.encoding = "utf-8"
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

    download_image_file(soup)
    
    return infos_to_csv

def extract_category_urls_books(url_category): # Extracts all books urls in a category
    urls_books = []

    base_url = url_category.rsplit("/", 1)[0] + "/"
    page = "index.html"
    page_number = 1

    while True:
        full_url = base_url + page

        response = requests.get(full_url)
        response.encoding = "utf-8"
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

def extract_titles(soup):
    titles_list = []
    ul = soup.find("ul", {"class": "nav"}).find("ul")
    titles = ul.find_all("a")

    for title in titles:
        titles_list.append(title.text.strip())

    return titles_list

def build_urls_categories(titles_list):
    base_url = "https://books.toscrape.com/catalogue/category/books/"
    url_end = "/index.html"

    urls_categories = []
    index = 2

    for title in titles_list:
        title = title.replace(" ","-").lower()
        url_category = base_url + title + "_" + str(index) + url_end
        urls_categories.append(url_category)
        index += 1

    return urls_categories

def extract_urls_categories(url_site_index):
    

    response = requests.get(url_site_index)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    titles_list = extract_titles(soup)

    urls_categories = build_urls_categories(titles_list)
    
    return urls_categories

def create_csv(infos_to_csv): # Creates csv and/or add new line in it
    headers = ["product_page_url", "universal_ product_code", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"]
    file_exists = os.path.isfile("datas_books.csv") 
    if not file_exists: # Checks if csv file already exists. If not :
        with open("datas_books.csv", "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)        
            writer.writeheader()
            writer.writerow(infos_to_csv)
    else : 
        with open("datas_books.csv", "a", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)        
            writer.writerow(infos_to_csv)

def scraper_booksToScrape_oneCategory(url_category):
    urls_books = extract_category_urls_books(url_category)
    for url_book in urls_books:
        info_to_csv = extract_book(url_book)
        print(info_to_csv["title"])
        create_csv(info_to_csv)


            
    