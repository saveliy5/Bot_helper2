import requests
import json


def valuta(name):
    appid = '4ac76bf8cec609d4fbd09e4b'
    url = f'https://v6.exchangerate-api.com/v6/{appid}/latest/{name}'
    response = requests.get(url)
    data = response.json()
    return (data['conversion_rates']['RUB'])