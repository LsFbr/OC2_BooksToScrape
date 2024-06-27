from utils import build_one_category_url, extract_category_urls_books, extract_category_urls_books, create_csv_category, extract_book
category_input = input("Please enter a category name : ")

def main_scraper_booksToScrape_oneCategory():
    url_category = build_one_category_url(category_input)
    
    urls_books = extract_category_urls_books(url_category)
    for url_book in urls_books:
        info_to_csv = extract_book(url_book)
        print(info_to_csv["title"])
        create_csv_category(info_to_csv)

if __name__ == "__main__":
    main_scraper_booksToScrape_oneCategory()


        
