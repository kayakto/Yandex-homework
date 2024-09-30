import requests

BASE_URL = "https://fakestoreapi.com"
path = "/products"

products = requests.get(BASE_URL + path)
json_format = products.json()
categories = []

for product in json_format:
    categories.append(product["category"])

print(set(categories))