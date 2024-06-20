from utils import *

#url_category = "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"  

#url_category = input("Please enter a category url : ")

def main_scraper_category(url_category):
    urls_books = extract_category_urls_books(url_category)
    for url_book in urls_books:
        info_to_csv = extract_book(url_book)
        print(info_to_csv["title"])
        create_csv(info_to_csv)

#if __name__ == "__main__":
    #main_scraper_category()


        
