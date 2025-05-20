import telebot
import random
import os
import time
import datetime
from telebot import types

bot = telebot.TeleBot('<Token>');
@bot.message_handler(content_types=['text'])

# Базовая функция получения сообщений и реакции на них. Из этой функции вызываются функции всех игр и информации о предметах
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет, напиши /help")
    elif message.text == "/help" or message.text == "/start":
        bot.send_message(message.from_user.id, "Привет! Этот бот может присылать информацию о предметах на ФиКЛе, а также присылать мемы и играть в игры. Напиши '/info', '/games' или '/memes'")
    elif message.text == '/info':
        information(message)
    elif message.text == '/games':
        games(message)
    elif message.text == '/language':
        languagegame(message)
    elif message.text == '/age':
        age_guesser(message)
    elif message.text == '/hangman':
        bot.send_message(message.from_user.id, "В разработке")
    # Функция считывает названия всех файлов в папке pictures1 по указанному пути. Потом создается путь к самому фото, выбранному случайно
    # После этого бот присылает выбранное фото 
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
#Основная функция: выводит фразу на языке, который нужно угадать
def main(message):
    global current_language, all_languages
    all_languages = {'английский': ['Hello, guys!','Это язык германской группы', 'Это язык Шерлока Холмса'],
                     'арабский': ['أحسنت', 'Это язык семитской группы, аравийской подгруппы', 'Это язык шейхов, цифр, магии и странной письменности'],
                     'армянский': ['Ողջույն Լավ արեցիր։', 'Это язык индоевропейской семьи', 'Это язык гранатов и горы Арарат'],
                     'баскский': ['Kaixo, denoi! Oso ondo!', 'Это изолят', 'На этом языке говорят на берегу Бискайского залива'],
                     'венгерский': ['Helló! Gratulálok!', 'Это язык уральской семьи', 'Это язык Кальмана'],
                     'греческий': ['Γειά σου! Μπράβο!', 'Это язык индоевропейской семьи', 'Это язык Пифагора'],
                     'грузинский': ['გამარჯობა! კარგად გააკეთე!', 'Это язык картвельской семьи', 'Это язык хачапури и оджахури'],
                     'иврит': ['שלום! כל הכבוד!', 'Это один из семитских языков', 'Это язык, на котором говорят в Израиле'],
                     'испанский': ['Hola, amigos!', 'Это язык романской группы', 'Это язык Дон Кихота'],
                     'китайский': ['你好！你很漂亮！', 'Это один из сино-тибетских языков', 'Это язык риса, драконов и братьев Лю'],
                     'корейский': ['안녕하세요! 당신은 똑똑해요!', 'Это язык алтайской семьи', 'Это язык самых милых дорам'],
                     'науатль': ['Piali! Kuali kichtol!', 'Это один из ацтекских языков', 'Это язык индейцев и древней культуры'],
                     'немецкий': ['Hallo! Gut gemacht!', 'Это язык германской группы', 'Это язык сосисок, колбасок, пива, Баха и Гёте'],
                     'польский': ['Cześć! Dobrze zrobiony!', 'Это язык славянской группы', 'Это язык пончиков, польки и Шопена'],
                     'русский': ['Привет! Ты молодец!', 'Это язык славянской группы', 'Это язык медведей, матрёшек и балалайки'],
                     'санскрит': ['सद् कृत!', 'Это древний язык индоевропейской семьи', 'Это язык древних сутр, Ситы и Рамы'],
                     'финский': ['Hei! Hyvin tehty!', 'Это язык уральской семьи', 'Это язык мумми-троллей'],
                     'французский': ['Bonjour, mis ami!', 'Это язык романской группы', 'Это язык мушкетёров, Жюля Верна и багетов'],
                     'цыганский': ['Bachtalo amala!', 'Это язык индоарийской ветви индоевропейских языков', 'Это язык сумасшедших песен, плясок, жульничества и шарабана'],
                     'японский': ['よくやった!', 'Это один из алтайских языков', 'Это язык аниме и самураев']}
    all_languages_list = ['английский', 'арабский', 'армянский', 'баскский', 'венгерский','греческий',
                          'грузинский', 'иврит', 'испанский', 'китайский', 'корейский', 'науатль','немецкий',
                          'польский', 'русский', 'санскрит', 'финский', 'французский',  'цыганский', 'японский']
    current_language = random.choice(all_languages_list)
    if message.text.lower() == 'да' or message.text.lower() == 'конечно' or message.text.lower() == '/language':
        bot.send_message(message.from_user.id,f"Какой это язык? {all_languages[current_language][0]}")
        bot.register_next_step_handler(message, check1)
    else:
        bot.send_message(message.from_user.id, 'Хорошо! Хочешь поиграть во что-то другое? Напиши /games')
#Функция продолжить игру
def continue_game(message):
    if message.text.lower() == "да" or message.text.lower() == "конечно":
        bot.send_message(message.from_user.id, "Напиши /language")
        bot.register_next_step_handler(message, main)
    else:
        bot.send_message(message.from_user.id, 'Спасибо за игру! Пока!')
#Первая попытка угадать язык
def check1(message):
    global current_language, all_languages
    answer = message.text.lower()
    if answer == current_language:
        bot.send_message(message.from_user.id, "Да! Молодец! Хочешь сыграть еще?")
        bot.register_next_step_handler(message, continue_game)
    else:
        bot.send_message(message.from_user.id, "Нет. Хочешь подсказку?")
        bot.register_next_step_handler(message, hint1)
#Первая подсказка
def hint1(message):
    global current_language, all_languages
    if message.text.lower() == "да":
        bot.send_message(message.from_user.id, all_languages[current_language][1])
        bot.register_next_step_handler(message, check2)
    else:
        bot.send_message(message.from_user.id, f'Это {current_language}. Хочешь сыграть еще?')
        bot.register_next_step_handler(message, continue_game)
#Вторая попытка угадать язык
def check2(message):
    global current_language, all_languages
    answer = message.text.lower()
    if answer == current_language:
        bot.send_message(message.from_user.id, "Да! Молодец! Хочешь сыграть еще?")
        bot.register_next_step_handler(message, continue_game)
    else:
        bot.send_message(message.from_user.id, "Нет. Хочешь ещё подсказку?")
        bot.register_next_step_handler(message, hint2)
#Вторая подсказка
def hint2(message):
    global current_language, all_languages
    if message.text.lower() == "да":
        bot.send_message(message.from_user.id, all_languages[current_language][2])
        bot.register_next_step_handler(message, check3)
    else:
        bot.send_message(message.from_user.id, f'Это {current_language}. Хочешь сыграть еще?')
        bot.register_next_step_handler(message, continue_game)
#Третья попытка угадать язык
def check3(message):
    global current_language, all_languages
    answer = message.text.lower()
    if answer == current_language:
        bot.send_message(message.from_user.id, "Да! Молодец! Хочешь сыграть еще?")
        bot.register_next_step_handler(message, continue_game)
    else:
        bot.send_message(message.from_user.id, f'Нет, это {current_language}. Хочешь сыграть еще?')
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

#Угадайка даты рождения

#Словарь для красивого отображения месяцев
MONTH_NAMES = {
    1: "января", 2: "февраля", 3: "марта", 4: "апреля",
    5: "мая", 6: "июня", 7: "июля", 8: "августа",
    9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
}

#Функция, которая выбирает первую случайную дату
def random_date(start, end):
    return start + datetime.timedelta(
        days=random.randint(0, (end - start).days)
    )

#Функция, которая красиво оформляет даты (из 01.01.2000 в 1 января 2020, например)
def format_date_russian(date):
    day = date.day
    month = MONTH_NAMES[date.month]
    year = date.year
    return f"{day} {month} {year}"

#Основная функция игры. Предлагает рандомную дату. Если это день рождения игрока, игра успешно заканчивается.
#Если нет, то игрок пишет "раньше" или "позже", если он родился раньше или позже, и бот предлагает новую дату.
#На успешное угадывание обычно требуется не больше 10-15 ходов, но если игроку надоест, из игры можно выйти.
#Ту би континуед
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Волшебник Кох угадал! Теперь вы свободны.")
        break
    elif call.data == "before":
        end_date = current_date
        current_date = start_date + (current_date - start_date) // 2
    elif call.data == "after":
        start_date = current_date
        current_date = current_date + (end_date - current_date) // 2

def age_guesser(message):
    start_date = datetime.date(1950, 1, 1)
    end_date = datetime.date(2020, 12, 31)
    
    bot.send_message(message.from_user.id, """О нет! Злой волшебник Кох запер вас в своем замке и не отпустит, пока не угадает вашу дату рождения!
    Правила игры: волшебник Кох покажет дату. Выберите подходящий ответ.
    Если игра вам наскучила, напишите «Выход».""")

    current_date = random_date(start_date, end_date)
    bot.send_message(message.from_user.id, f"Волшебник Кох воскликнул: {format_date_russian(current_date)}!")
    
    while True:
        
        keyboard = types.InlineKeyboardMarkup();
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');
        keyboard.add(key_yes);
        key_before= types.InlineKeyboardButton(text='Раньше', callback_data='before');
        keyboard.add(key_before);
        key_after= types.InlineKeyboardButton(text='Позже', callback_data='after');
        keyboard.add(key_after);        

        question = 'Вы родились в этот день?';
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

        if message.text.lower() == 'выход':
            break
            
        bot.send_message(message.from_user.id, f"Волшебник Кох воскликнул: {format_date_russian(current_date)}!")
