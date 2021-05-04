import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')
soup = BeautifulSoup(response.text, 'html.parser')
products = soup.findAll(class_='thumbnail')

with open('scrapped_data.csv', 'w') as file:
    _writer=writer(file)
    headers=['price','image','description']
    _writer.writerow(headers)
    for product in products:
        price = product.find(class_='pull-right price').get_text()
        img = product.find(class_='img-responsive')['src']
        description = product.find(class_='description').get_text()
        _writer.writerow([price,img,description])

