import telebot
import random
from requests import get
from glob import glob


bot = telebot.TeleBot('7551432095:AAG1Lm_evaPSpoDeMQYtyJ222RCy4OgEmQA');
@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, напиши /help")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Привет! Этот бот может присылать информацию о предметах на ФиКЛе, а также присылать мемы и играть в игры. Напиши '/info', '/games' или '/memes'")
    elif message.text == '/info':
        information(message)
    elif message.text == '/games':
        games(message)
    elif message.text == '/language':
        bot.send_message(message.from_user.id, "Временно недоступно")
    elif message.text == '/age':
        bot.send_message(message.from_user.id, "В разработке")
    elif message.text == '/hangman':
        bot.send_message(message.from_user.id, "В разработке")
    elif message.text == '/memes':
        photos = glob('pictures1/*')
        photo = random.choice(photos)
        bot.send_photo(message.chat.id, photo = open(photo, 'rb'))


    elif message.text.lower() == 'дискретная математика' or message.text.lower() == 'дискра' or message.text.lower() == 'математика':
        math(message)
    else:
        bot.send_message(message.from_user.id, "Не понимаю. Напиши /help.")


def information(message):
    bot.send_message(message.from_user.id, '''Конечно! Вот список предметов, про которые у меня есть информация:
        Дискретная математика
Про какой из них ты хочешь узнать?''')
    
    

def games(message):
    bot.send_message(message.from_user.id, "Отлично! В какую игру ты хочешь поиграть: виселица, угадай язык или угадайка возраста? Напиши '/hangman', '/language' или '/age'")



# Предметы
def math(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет. 

Формула оценки: 
2-3 модуль: 0.27 * активность + 0.11 * ДЗ + 0.08 * большое ДЗ + 0.27 * КР + 0.27 * экзамен
4 модуль: 0.25 * активность + 0.1 * ДЗ + 0.05 * большое ДЗ + 0.6 * экзамен
Итог: 0.55 * оценка за 4 модуль + 0.45 * оценка за 2-3 модуль
                     
Информация о преподавателях: 
Вадим Васильевич Кочергин, почта: vvkoch@yandex.ru
Анна Витальевна Михайлович, почта: avmikhailovich@yandex.ru
                     
Сайт предмета: https://math-info.hse.ru/2024-25/Дискретная_математика''')

# Языковая игра


# Виселица


bot.polling(none_stop=True, interval=0)
