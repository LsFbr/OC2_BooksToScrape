from utils import extract_book, create_csv, find_url_book
# urls exemples :
# url_book = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
# url_book = "https://books.toscrape.com/catalogue/neither-here-nor-there-travels-in-europe_198/index.html"
# url_book = "https://books.toscrape.com/catalogue/at-the-existentialist-cafe-freedom-being-and-apricot-cocktails-with-jean-paul-sartre-simone-de-beauvoir-albert-camus-martin-heidegger-edmund-husserl-karl-jaspers-maurice-merleau-ponty-and-others_459/index.html"

title_input = input("Please enter a product's title : ")

def main_one_book_scraper():
    
    url_book = find_url_book(title_input)
    print(url_book)
    infos_to_csv = extract_book(url_book)        
    create_csv(infos_to_csv)

if __name__ == "__main__":
    main_one_book_scraper()

