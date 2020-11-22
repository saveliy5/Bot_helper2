def predobraboka(town):
    if (town in ('Питер', 'Петербург')):
        need = 'Санкт-Петербург'
    else:
        need = town
    return need


def weather(town):
    import requests
    s_city = predobraboka(town)
    appid = 'd946d36a1951f500918d478c37667b83'

    res = requests.get("http://api.openweathermap.org/data/2.5/find",
                       params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
    data = res.json()
    cities = ["{} ({})".format(d['name'], d['sys']['country'])
              for d in data['list']]

    city_id = data['list'][0]['id']
    res2 = requests.get("http://api.openweathermap.org/data/2.5/weather"
                        , params={'id': city_id, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': appid})

    data_need = res2.json()
    conditions = data_need['weather'][0]['description']
    temp = data_need['main']['temp']
    temp_min = data_need['main']['temp_min']
    temp_max = data_need['main']['temp_max']

    d = dict();
    d['conditions'] = conditions
    d['temp'] = temp
    return d



