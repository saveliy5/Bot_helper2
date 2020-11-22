from weather import weather
def bot():
    import telebot;
    bot = telebot.TeleBot('1264478324:AAGGVyWuVPr0-skz81CFDSWdm8y0RMVnfEo');

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        town = message.text
        if message.text == "/help":
            bot.send_message(message.from_user.id, "Напиши город, в котором хочешь узнать погоду")
        elif message.text == "/start":
            bot.send_message(message.from_user.id, "Привет, напиши город, в котором хочешь узнать погоду")
        elif message.text in ("Пока", "До свидания", "Прощай"):
            bot.send_message(message.from_user.id, "Пока")
        elif message.text in ("Привет", "Здравствуйте", "Добрый день"):
            bot.send_message(message.from_user.id, "Приветсвую, напишите город, и я скажу, какая там сейчас погода")
        else:
            try:
                x = weather(town)
                bot.send_message(message.from_user.id, f"В городе {town} {x['conditions']}, а температура {x['temp']}")
            except:
                bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

    bot.polling(none_stop=True, interval=0)