import telebot
import random
import os
import time

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
        bot.send_message(message.from_user.id, "В разработке")
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
words = ['фонема', 'морфема', 'синтакс', 'клауза', 'лексема', 'спирант', 'сибилянт', 'звук', 'слог', 'мора', 'щелчок', 'префикс', 'суффикс', 'корень'] #слова, которые могут быть загаданы
max_attempts = 8 
#начало игры
def hangstart_game(message):
    global current_word, guessed_letters, attempts_left
    current_word = random.choice(words)
    guessed_letters = []
    attempts_left = max_attempts
    bot.send_message(message.from_user.id, f'''Привет! Это классическая виселица. Тебе будет загадано слово на лингвистическую тему, которое тебе нужно отгадывать, вводя каждый раз по одной букве. Все слова русские и написаны кириллицей. Всего у тебя 8 попыток.
Начнем игру! Отгадываем слово из {len(current_word)} букв.''')
    bot.register_next_step_handler(message, guess)
#угадывание буквы
def guess(message):
    global guessed_letters, attempts_left
    user_input = message.text.lower()
    display_word = ''.join([char if char in guessed_letters else '_' for char in current_word])
    if user_input == 'заново':
        hangoncemore(message)
    elif user_input == 'закончить':
        endgame(message)
    elif len(user_input) > 1:
        bot.send_message(message.from_user.id,'Вводи только одну букву!')
        bot.register_next_step_handler(message, guess)
    elif user_input in guessed_letters:
        bot.send_message(message.from_user.id,'Эту букву ты уже пробовал/а')
        bot.send_message(message.from_user.id,f'''{display_word}
Осталось попыток: {attempts_left}''')
        bot.register_next_step_handler(message, guess)
    elif user_input not in current_word:
        attempts_left -= 1
        bot.send_message(message.from_user.id, "Этой буквы нет в слове. Попробуй еще раз")
        guessed_letters.append(user_input)
        pictures(message)
        if attempts_left == 0:
            bot.send_message(message.from_user.id,f'''Попытки кончились:
Правильный ответ: "{current_word}"''')
            bot.send_message(message.from_user.id,'Чтобы продолжить играть или прекратить, напиши "заново" или "закончить"')
            bot.register_next_step_handler(message, guess)
        else:
            bot.send_message(message.from_user.id,f'''{display_word}
Осталось попыток: {attempts_left}''')
            bot.register_next_step_handler(message, guess)
    elif user_input in current_word:
        bot.send_message(message.from_user.id,"Отлично, эта буква есть в слове")
        guessed_letters.append(user_input)
        display_word = ''.join([char if char in guessed_letters else '_' for char in current_word])
        bot.send_message(message.from_user.id,f'''{display_word}
Осталось попыток: {attempts_left}''')
        bot.register_next_step_handler(message, guess)
        if '_' not in display_word:
            bot.send_message(message.from_user.id,f'Ура! Ты отгадал/а слово: {current_word}')
            bot.send_message(message.from_user.id,'Чтобы продолжить играть или прекратить, напиши "заново" или "закончить"')
#картинка виселицы
def pictures(message):
    global attempts_left
    if attempts_left == 7:
        bot.send_message(message.from_user.id, """
     ______
     |    
     |
     |
     |
     |
     |
    _|________
    """)
    elif attempts_left == 6:
        bot.send_message(message.from_user.id, """
     _______
     |    |
     |
     |
     |
     |
     |
    _|_______
    """ )
    elif attempts_left == 5:
        bot.send_message(message.from_user.id, """
     ________
     |    |
     |    O
     |    
     | 
     |   
     |    
    _|________
    """)            
    elif attempts_left == 4:
        bot.send_message(message.from_user.id, """
     ________
     |    |
     |    O
     |    |
     |   
     |   
     |   
    _|_________
    """  )
    elif attempts_left == 3:
        bot.send_message(message.from_user.id, """
     _________
     |    |
     |    O
     |    |\\
     |   
     |   
     |     
    _|__________
    """ )
    elif attempts_left == 2:
        bot.send_message(message.from_user.id, """
     ________
     |    |
     |    O
     |   /|\\
     |   
     |   
     |    
    _|_________
    """ )
    elif attempts_left == 1:
        bot.send_message(message.from_user.id, """
     ________
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |   
    _|_________
    """ )
    elif attempts_left == 0:
        bot.send_message(message.from_user.id, """
     _________
     |    |
     |    O
     |   /|\\
     |   / \\
     |
     |   
    _|__________
    """ )
                       

#конец игры
def endgame(message):
    bot.send_message(message.from_user.id, 'Спасибо за игру!')
def hangoncemore(message):
    bot.send_message(message.from_user.id, 'Напиши /hangman')

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
