import requests

BASE_URL = "https://fakestoreapi.com"
path = "/users"

data = {'email': 'Egor@gmail.com',
        'username': 'Egor',
        'password': 'm38rmF$',
        'name': {
            'firstname': 'EGOR',
            'lastname': 'EGOR'
        },
        'address': {
            'city': 'Samara',
            'street': '7835 new road',
            'number': 3,
            'zipcode': '12926-3874',
            'geolocation': {
                'lat': '-37.3159',
                'long': '81.1496'
            }
        },
        'phone': '1-228-236-7033'
        }

res = requests.post(BASE_URL + path, data=data)
print(res.status_code, "\n")
print(res.text)