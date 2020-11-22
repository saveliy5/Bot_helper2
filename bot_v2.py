from weather import weather
from anekdot import anekdot
from telebot import types
from valuta import valuta
from vybor_prosmotr import vybrat_film, vybrat_serial
import requests

def bot():
    import telebot;
    bot = telebot.TeleBot('1264478324:AAGGVyWuVPr0-skz81CFDSWdm8y0RMVnfEo');

    def knopki():
        markup = types.ReplyKeyboardMarkup(True)
        key1 = types.KeyboardButton('Что ты умеешь?')
        markup.add(key1)
        return markup

    def menu_kurs():
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('EUR', callback_data='get-EUR'),
            telebot.types.InlineKeyboardButton('JPY', callback_data='get-JPY')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('USD', callback_data='get-USD'),
            telebot.types.InlineKeyboardButton('CHF', callback_data='get-CHF')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('GBP', callback_data='get-GBP'),
            telebot.types.InlineKeyboardButton('TRY', callback_data='get-TRY')
        )
        return keyboard

    def menu_watch():
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Фильм', callback_data='watch-movie'),
            telebot.types.InlineKeyboardButton('Сериал', callback_data='watch-serial')
        )
        # keyboard.row(
        #     telebot.types.InlineKeyboardButton('YouTube', callback_data='watch-youtube')
        # )
        return keyboard


    def osn_menu():
        keyboard = types.InlineKeyboardMarkup();  # наша клавиатура
        key_weather = types.InlineKeyboardButton(text='Узнаю погоду в нужном городе', callback_data='weather');
        keyboard.add(key_weather);  # добавляем кнопку в клавиатуру
        key_joke = types.InlineKeyboardButton(text='Расскажу анекдот', callback_data='joke');
        keyboard.add(key_joke);
        key_kurs = types.InlineKeyboardButton(text='Сообщу курс валют', callback_data='kurs');
        keyboard.add(key_kurs);
        sovet_film = types.InlineKeyboardButton(text='Подскажу, что посмотреть', callback_data='watch_sov');
        keyboard.add(sovet_film);
        return keyboard

    def after_navyk(i):
        #погода
        if i == 1:
            text_nadpis = 'Другой город'
            type_type = 'new_town'
        #анекдоты
        elif i == 2:
            text_nadpis = 'Еще анекдот'
            type_type = 'new_joke'
        elif i == 3:
            text_nadpis = 'Другая валюта'
            type_type = 'new_kurs'

        elif i == 4:
            text_nadpis = 'Еще фильм'
            type_type = 'watch-movie'

        elif i == 5:
            text_nadpis = 'Еще сериал'
            type_type = 'watch-serial'

        keyboard2 = types.InlineKeyboardMarkup();
        povtor_nayk = types.InlineKeyboardButton(text=text_nadpis, callback_data=type_type);
        keyboard2.add(povtor_nayk);
        menu = types.InlineKeyboardButton(text='Другой навык', callback_data='osn_menu');
        keyboard2.add(menu);
        return keyboard2



    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        town = message.text
        if message.text in ("/help", "help"):
            bot.send_message(message.from_user.id, "Я бот, который может подсказать тебе погоду, курс валют и рассказать анекдот, нажми на /main и погнали", reply_markup=knopki())
        elif message.text in ("/start", "/main", "Что ты умеешь?"):
            if (message.text == "/start"):
                fir_text = 'Привет, вот, что я могу:'
            else:
                fir_text = 'Вот, что я могу:'

            bot.send_message(message.from_user.id, text=fir_text, reply_markup=osn_menu())
            # bot.send_message(message.from_user.id, text='привет', reply_markup=knopki())

        elif message.text in ("Пока", "До свидания", "Прощай"):
            bot.send_message(message.from_user.id, "Пока")

        elif message.text in ("Привет", "Здравствуйте", "Добрый день", "Добрый вечер", "Доброе утро"):
            bot.send_message(message.from_user.id, "Приветсвую, нажмите на /main или на кнопку", reply_markup=knopki())

        # сюда потом добавить регулярок на фразы, которые тоже будут вызывать функции

        else:
            try:
                x = weather(town)
                otvet =  f"В городе {town} {x['conditions']}, а температура {x['temp']}"
                keyboard2 = after_navyk(1)
                bot.send_message(message.from_user.id, text=otvet, reply_markup=keyboard2)
            except:
                bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.", reply_markup=knopki())


    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data in ("weather", "new_town"):
            bot.send_message(call.message.chat.id, 'Напишите город, в котором хотите узнать погоду');
        elif call.data in ("kurs", "new_kurs"):
            bot.send_message(call.message.chat.id, 'Выберите валюту', reply_markup=menu_kurs());
        elif call.data in ("joke", "new_joke"):
            text_anekdota = anekdot()
            bot.send_message(call.message.chat.id, text_anekdota, reply_markup=after_navyk(2));
        elif call.data == "osn_menu":
            fir_text = 'Вот, что я могу:'
            bot.send_message(call.message.chat.id, text=fir_text, reply_markup=osn_menu())

        elif call.data in ("get-EUR", "get-USD", "get-GBP", "get-JPY", "get-CHF", "get-TRY"):
            need_name = call.data.split('-')[1]
            kurs = valuta(need_name)
            fir_text = f'1 {need_name} стоит {kurs} RUB'
            bot.send_message(call.message.chat.id, text=fir_text, reply_markup=after_navyk(3))

        elif call.data == "watch_sov":
            bot.send_message(call.message.chat.id, 'Выберите, что хотите посмотреть:', reply_markup=menu_watch());
            # bot.send_photo(call.message.chat.id, requests.get("https://cdn2.static1-sima-land.com/items/2390826/2/700-nw.jpg").content)

        elif call.data in ("watch-movie", "watch-serial", "watch-youtube"):
            if call.data == "watch-movie":
                nazvanie = vybrat_film()
                type = 'Фильм'
                index = 4
            elif call.data == "watch-serial":
                nazvanie = vybrat_serial()
                type = 'Сериал'
                index = 5

            fir_text = f'Можете посмотреть {type}:\n{nazvanie}'
            bot.send_message(call.message.chat.id, text=fir_text, reply_markup=after_navyk(index))





    bot.polling(none_stop=True, interval=0)






