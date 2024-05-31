import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
page=response.content
#html_code = response.text 
soup = BeautifulSoup(page, "html.parser")

categories = soup.find_all("a", class_="nav-list")