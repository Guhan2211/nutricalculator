import requests
import json
def callit(inp):
    APP_ID = "4bbd1ade"
    APP_KEY = "d51d946d282fff71d41148d3f7f6cff3"

    api_endpoint = "https://api.edamam.com/api/nutrition-details"

    url = api_endpoint + "?app_id=" + APP_ID + "&app_key=" + APP_KEY

    headers = {
        'Content-type': 'application/json'
    }
    recipe = {

        'title': 'something',
        'ingr': inp
        }
    r = requests.post(url, headers = headers, json = recipe)
    
    return r.__dict__
