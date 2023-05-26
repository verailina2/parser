import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/category/books/classics_6/index.html'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
books = soup.find_all('article', class_='product_pod')

for book in books:
    title = book.h3.a['title']
    price = book.find("p", class_="price_color").text.replace("Â", "")

    print("Название: ", title)
    print("Цена: ", price)
    print()
