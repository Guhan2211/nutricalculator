import requests
import json
def callit(inp):
    APP_ID = "*****"
    APP_KEY = "*****"

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
