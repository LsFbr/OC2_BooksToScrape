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
    
    return image_url   

def extract_product_description(soup):   
    product_description = soup.find("article", {"class": "product_page"}).find("p", recursive=False)
    
    return product_description.text
    
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
