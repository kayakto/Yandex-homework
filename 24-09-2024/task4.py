import requests

BASE_URL = "https://fakestoreapi.com"
path = "/users"

res = requests.get(BASE_URL + path)
print(res.json())