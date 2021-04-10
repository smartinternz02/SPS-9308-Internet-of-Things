Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests

URL = "https://geocode.search.hereapi.com/v1/geocode"
location = input("Enter the location here: ") #taking user input
api_key = 'YOUR_API_KEY' # Acquire from developer.here.com
PARAMS = {'apikey':api_key,'q':location} 

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
data = r.json()

latitude = data['items'][0]['position']['lat']
longitude = data['items'][0]['position']['lng']