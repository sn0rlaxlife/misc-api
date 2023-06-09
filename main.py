import json
import requests
from requests.exceptions import HTTPError

response = requests.get('https://api.punkapi.com/v2/beers/random')
response.raise_for_status()
#access json
beer_data = response.json()[0]
print("Entire JSON Response")
beer_name = beer_data['name']
beer_details = beer_data['description']
food_pair = beer_data['food_pairing']
img_url = beer_data['image_url']

# Print results
print(f"Beer Name: {beer_name}")
print(f"Beer Details: {beer_details}")
print(f"Beer Image URL: {img_url}")
print(f"Food pairings: {food_pair}")
