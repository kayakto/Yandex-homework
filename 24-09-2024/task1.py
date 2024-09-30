import requests

BASE_URL = "https://fakestoreapi.com"
path = "/products"

products = requests.get(BASE_URL + path)
json_format = products.json()

for product in json_format:
    if product["price"] < 20:
        print(product)
