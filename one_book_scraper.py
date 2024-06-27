from utils import extract_book, create_csv_book, find_url_book

title_input = input("Please enter a product's title : ")

def main_one_book_scraper():
    
    url_book = find_url_book(title_input)
    infos_to_csv = extract_book(url_book)         
    create_csv_book(infos_to_csv)

if __name__ == "__main__":
    main_one_book_scraper()

