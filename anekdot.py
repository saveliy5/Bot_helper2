

def anekdot():
    import requests
    from bs4 import BeautifulSoup as bs
    import random

    r = requests.get("https://vse-shutochki.ru/anekdoty/")

    html = bs(r.content, 'html.parser')

    els = html.find_all('div', class_='post')

    spisok_anekdot = []
    for i in range(len(els)):
        try:
            if (els[i].a.text == 'похожие'):
                first_line = els[i].text
                need_text = (first_line.split('\n\n')[0])
                spisok_anekdot.append(need_text.replace('-', '\n'))
        except:
            b = 0

    ran = random.randint(0, len(spisok_anekdot)-1)
    text_anek = spisok_anekdot[ran]
    return text_anek