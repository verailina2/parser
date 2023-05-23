from bs4 import BeautifulSoup
import requests

url = 'http://books.toscrape.com/catalogue/category/books/classics_6/index.html'
response = requests.get(url)
print(response)
bs = BeautifulSoup(response.text, "lxml")
print(bs)
