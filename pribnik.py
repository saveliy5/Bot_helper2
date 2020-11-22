import requests
import json
from bs4 import BeautifulSoup as bs
import random


def vybrat_serial():
    r = requests.get("https://www.themoviedb.org/tv?language=ru-RU")

    html = bs(r.content, 'html.parser')

    spisok_serial = []
    els = html.find_all('div', class_='card style_1')

    for i in range(len(els)):
        els2 = els[i].find('div', class_='content')
        need = (els2.h2.text)
        spisok_serial.append(need)

    ran = random.randint(0, len(spisok_serial) - 1)
    nazvanie_serial = spisok_serial[ran]
    return nazvanie_serial

def vybrat_film():
    r = requests.get("https://www.themoviedb.org/movie?language=ru-RU")

    html = bs(r.content, 'html.parser')

    spisok_serial = []
    els = html.find_all('div', class_='card style_1')

    for i in range(len(els)):
        els2 = els[i].find('div', class_='content')
        need = (els2.h2.text)
        spisok_serial.append(need)

    ran = random.randint(0, len(spisok_serial) - 1)
    nazvanie_serial = spisok_serial[ran]
    return nazvanie_serial

