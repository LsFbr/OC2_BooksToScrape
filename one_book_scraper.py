from utils import extract_book, create_csv
# urls exemples :
# url_book = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
# url_book = "https://books.toscrape.com/catalogue/neither-here-nor-there-travels-in-europe_198/index.html"
# url_book = "https://books.toscrape.com/catalogue/at-the-existentialist-cafe-freedom-being-and-apricot-cocktails-with-jean-paul-sartre-simone-de-beauvoir-albert-camus-martin-heidegger-edmund-husserl-karl-jaspers-maurice-merleau-ponty-and-others_459/index.html"

url_book = input("Please enter a product's url : ")

def main_scraper_booksToScrape_oneBook():
    infos_to_csv = extract_book(url_book)        
    create_csv(infos_to_csv)

if __name__ == "__main__":
    main_scraper_booksToScrape_oneBook()

