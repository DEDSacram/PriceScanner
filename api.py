import requests
import json

# r = requests.get("https://api.skinport.com/v1/items", params={
#     "app_id":  252490,
#     "currency": "EUR",
#     "tradable": 0
# }).json()



with open('data.json', 'r') as f:
    r = json.load(f)

filtered = [item for item in r if item.get('suggested_price', 0) < item.get('min_price', float('inf'))]


with open('test.json', 'w') as f:
    json.dump(r, filtered)