import telebot
import random
import os
import time

bot = telebot.TeleBot('<Token>');
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
        files = os.listdir('/home/a1123295/tgbot/pictures1/')
        photopath = os.path.join('/home/a1123295/tgbot/pictures1/', random.choice(files))
        bot.send_photo(message.chat.id, photo = open(photopath, 'rb'))
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
def languagegame(message):
    bot.send_message(message.from_user.id, '''Привет! В этой игре тебе нужно будет отгадать язык по одному предложению. После каждой неудачной попытки тебе будет предлагаться подсказка. Всего у тебя 3 попытки. 
Начнём игру?''')
    bot.register_next_step_handler(message, main)
def main(message):
    if message.text.lower() == 'да' or message.text.lower() == 'конечно':
        all_func = [start_english, start_espanol, start_chinese, start_french, start_japanese, start_korean, start_sanskrit, start_arabic, start_gypsy, start_georgian, start_armenian, start_german, start_polish, start_hebrew, start_hungarian, start_greek, start_finnish, start_russian, start_euskara, start_nahuatl]
        get_random = random.choice(all_func)
        return get_random(message)
    else:
        bot.send_message(message.from_user.id, 'Хорошо! Хочешь поиграть во что-то другое? Напиши /games')
def continue_game(message):
    if message.text.lower() == "да" or message.text.lower() == "конечно":
        bot.send_message(message.from_user.id, "Напиши /language")
        bot.register_next_step_handler(message, main)
    else:
        bot.send_message(message.from_user.id, 'Спасибо за игру! Пока!')

# Испанский для игры
def start_espanol(message):
    bot.send_message(message.from_user.id,"Какой это язык? Hola, amigos!")
    bot.register_next_step_handler(message, check1_espanol)
def check1_espanol(message):
    answer = message.text.lower()
    if answer == 'испанский':
        bot.send_message(message.from_user.id, "Да! Молодец! Хочешь сыграть еще?")
        bot.register_next_step_handler(message, continue_game)
    else:
        bot.send_message(message.from_user.id, "Нет. Хочешь подсказку?")
        bot.register_next_step_handler(message, hint1_espanol)
def hint1_espanol(message):
    if message.text.lower() == "да":
        bot.send_message(message.from_user.id, "Это язык романской группы")
        bot.register_next_step_handler(message, check2_espanol)
    else:
        bot.send_message(message.from_user.id, 'Это испанский. Хочешь сыграть еще?')
        bot.register_next_step_handler(message, continue_game)
def check2_espanol(message):
    answer = message.text.lower()
    if answer == 'испанский':
        bot.send_message(message.from_user.id, "Да! Молодец! Хочешь сыграть еще?")
        bot.register_next_step_handler(message, continue_game)
    else:
        bot.send_message(message.from_user.id, "Нет. Хочешь ещё подсказку?")
        bot.register_next_step_handler(message, hint2_espanol)
def hint2_espanol(message):
    if message.text.lower() == "да":
        bot.send_message(message.from_user.id, "Это язык Дон Кихота")
        bot.register_next_step_handler(message, check3_espanol)
    else:
        bot.send_message(message.from_user.id, 'Это испанский. Хочешь сыграть еще?')
        bot.register_next_step_handler(message, continue_game)
def check3_espanol(message):
    answer = message.text.lower()
    if answer == 'испанский':
        bot.send_message(message.from_user.id, "Да! Молодец! Хочешь сыграть еще?")
        bot.register_next_step_handler(message, continue_game)
    else:
        bot.send_message(message.from_user.id, 'Нет, это испанский. Хочешь сыграть еще?')
        bot.register_next_step_handler(message, continue_game)

# Английский для игры
def start_english(message):
    bot.send_message(message.from_user.id,"Какой это язык? Hello, guys!")
    bot.register_next_step_handler(message, check1_english)
def check1_english(message):
    answer = message.text.lower()
    if answer == 'английский':
        bot.send_message(message.from_user.id, "Да! Молодец! Хочешь сыграть еще?")
        bot.register_next_step_handler(message, continue_game)
    else:
        bot.send_message(message.from_user.id, "Нет. Хочешь подсказку?")
        bot.register_next_step_handler(message, hint1_english)
def hint1_english(message):
    if message.text.lower() == "да":
        bot.send_message(message.from_user.id, "Это язык германской группы")
        bot.register_next_step_handler(message, check2_english)
    else:
        bot.send_message(message.from_user.id, 'Это английский. Хочешь сыграть еще?')
        bot.register_next_step_handler(message, continue_game)
def check2_english(message):
    answer = message.text.lower()
    if answer == 'английский':
        bot.send_message(message.from_user.id, "Да! Молодец! Хочешь сыграть еще?")
        bot.register_next_step_handler(message, continue_game)
    else:
        bot.send_message(message.from_user.id, "Нет. Хочешь ещё подсказку?")
        bot.register_next_step_handler(message, hint2_english)
def hint2_english(message):
    if message.text.lower() == "да":
        bot.send_message(message.from_user.id, "Это язык Шерлока Холмса")
        bot.register_next_step_handler(message, check3_english)
    else:
        bot.send_message(message.from_user.id, 'Это английский. Хочешь сыграть еще?')
        bot.register_next_step_handler(message, continue_game)
def check3_english(message):
    answer = message.text.lower()
    if answer == 'английский':
        bot.send_message(message.from_user.id, "Да! Молодец! Хочешь сыграть еще?")
        bot.register_next_step_handler(message, continue_game)
    else:
        bot.send_message(message.from_user.id, 'Нет, это английский. Хочешь сыграть еще?')
        bot.register_next_step_handler(message, continue_game)


# Виселица

# Функция, чтобы бот все время принимал сообщения без ошибки ReadTimeout. 
# Когда бот не может подключиться, он печатает ошибку и продолжает пытаться подключиться спустя 5 секунд
if __name__=='__main__':
    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue
