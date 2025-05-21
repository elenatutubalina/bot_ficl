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
        bot.send_message(message.from_user.id, "Привет! Этот бот может присылать информацию о предметах на ФиКЛе, а также присылать мемы и играть в игры. Напиши '/info', '/games', '/memes' или спроси, какой сегодня день")
    elif message.text == '/info':
        information(message)
    elif message.text == '/games':
        games(message)
    elif message.text == '/language':
        languagegame(message)
    elif message.text == '/age':
        age_guesser(message)
    elif message.text == '/hangman':
        hangstart_game(message)
    # Код считывает названия всех файлов в папке pictures1 по указанному пути. Потом создается путь к самому фото, выбранному случайно
    # После этого бот присылает выбранное фото 
    elif message.text == '/memes':
        files = os.listdir('/home/a1123295/tgbot/pictures1/')
        photopath = os.path.join('/home/a1123295/tgbot/pictures1/', random.choice(files))
        bot.send_photo(message.chat.id, photo = open(photopath, 'rb'))
    # Аналогично с командой /memes, но картинки берутся из папки days и присылаются как стикеры
    elif message.text.lower() == 'какой сегодня день?' or 'какой сегодня день':
        files = os.listdir('/home/a1123295/tgbot/days/')
        stickerpath = os.path.join('/home/a1123295/tgbot/days/', random.choice(files))
        bot.send_sticker(message.chat.id, sticker = open(stickerpath, 'rb'))
    elif message.text.lower() == 'дискретная математика' or message.text.lower() == 'дискра' or message.text.lower() == 'математика':
        math(message)
    elif message.text.lower() == 'история' or message.text.lower() == 'история россии':
        history(message)
    elif message.text.lower() == 'бжд' or message.text.lower() == 'безопасность жизнедеятельности':
        bzd(message)
    elif message.text.lower() == 'теория языка' or message.text.lower() == 'теоръяз' or message.text.lower() == 'теоряз':
        theory(message)
    elif message.text.lower() == 'академическое письмо' or message.text.lower() == 'акап':
        acap(message)
    elif message.text.lower() == 'введение в лингвистику' or message.text.lower() == 'ввл' or message.text.lower() == 'языки россии':
        intro(message)
    elif message.text.lower() == 'арабский' or message.text.lower() == 'арабский язык':
        arab(message)
    elif message.text.lower() == 'китайский' or message.text.lower() == 'китайский язык':
        chin(message)
    elif message.text.lower() == 'испанский' or message.text.lower() == 'испанский язык':
        span(message)
    elif message.text.lower() == 'немецкий' or message.text.lower() == 'немецкий язык':
        germ(message)
    elif message.text.lower() == 'французский' or message.text.lower() == 'французский язык':
        fren(message)
    elif message.text.lower() == 'древние языки' or message.text.lower() == 'латынь' or message.text.lower() == 'старославянский':
        ancient(message)
    elif message.text.lower() == 'древнерусская филология' or message.text.lower() == 'введение в древнерусскую филологию':
        philology(message)
    elif message.text.lower() == 'грамматика ошибок' or message.text.lower() == 'грош':
        errors(message)
    elif message.text.lower() == 'лингвистические и логические задачи' or message.text.lower() == 'лингвистические задачи':
        problems(message)
    elif message.text.lower() == 'основы русского жестового языка' or message.text.lower() == 'ржя':
        rzy(message)
    elif message.text.lower() == 'романские языки в перспективе языкового разнообразия' or message.text.lower() == 'романские языки':
        roman(message)
    elif message.text.lower() == 'эмпирические данные и грамматическая теория' or message.text.lower() == 'эмпирические данные' or message.text.lower() == 'эмпданные':
        empir(message)
    elif message.text.lower() == 'введение в лингвистическую антропологию' or message.text.lower() == 'лингвистическая антропология' or message.text.lower() == 'лингантро':
        anthro(message)
    elif message.text.lower() == 'программирование и лингвистические данные' or message.text.lower() == 'линда' or message.text.lower() == 'прога':
        prog(message)
    elif message.text.lower() == 'социолингвистика' or message.text.lower() == 'соцлинг':
        social(message)
    elif message.text.lower() == 'цифровая грамотность' or message.text.lower() == 'цг':
        cyber(message)
    else:
        bot.send_message(message.from_user.id, "Не понимаю :(. Напиши /help.")


def information(message):
    bot.send_message(message.from_user.id, '''Конечно! Вот список предметов, про которые у меня есть информация:
    Дискретная математика
    История России
    Безопасность жизнедеятельности
    Теория языка
    Академическое письмо
    Введение в лингвистику
    Программирование и лингвистические данные
    Социолингвистика
    Цифровая грамотность
    Языки:
        Арабский язык
        Китайский язык
        Испанский язык
        Немецкий язык
        Французский язык
    Древние языки
    НИСы:
        Основы русского жестового языка
        Введение в лингвистическую антропологию
        Лингвистические и логические задачи
        Романские языки в перспективе языкового разнообразия
        Эмпирические данные и грамматическая теория
        Введение в древнерусскую филологию
        Грамматика ошибок
Про какой из них ты хочешь узнать?''')
    
    

def games(message):
    bot.send_message(message.from_user.id, "Отлично! В какую игру ты хочешь поиграть: виселица, угадай язык или угадайка возраста? Напиши '/hangman', '/language' или '/age'")
    


# Предметы
def math(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.

Формула оценки:
1 курс, 3 модуль
0.27 * Контрольная работа + 0.08 * Письменное домашнее задание + 0.27 * Работа на занятиях + 0.11 * Текущее домашнее задание + 0.27 * Экзамен

1 курс, 4 модуль
0.05 * Письменное домашнее задание + 0.25 * Работа на занятиях + 0.1 * Текущее домашнее задание + 0.6 * Экзамен

Итог: 0.55 * оценка за 4 модуль + 0.45 * оценка за 2-3 модуль

Информация о преподавателях:
Вадим Васильевич Кочергин, почта: vvkoch@yandex.ru
Анна Витальевна Михайлович, почта: avmikhailovich@yandex.ru

Сайт с материалами курса: http://math-info.hse.ru/2024-25/Дискретная_математика 

Сайт предмета: https://www.hse.ru/ba/ling/courses/916898861.html''')

def history(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.

Формула оценки:

1 курс, 2 модуль
0.25 * Работа с СмартЛМС + 0.3 * Семинарские занятия + 0.45 * Экзамен

1 курс, 4 модуль
0.2 * Проектная деятельность + 0.25 * Работа с СмартЛМС + 0.3 * Семинарские занятия + 0.25 * Экзамен

Информация о преподавателях:
Волкова Ирина Владимировна, почта: ivolkova@hse.ru
Стреляев Вячеслав Иванович, почта: vistrelyaev@hse.ru, телеграм: @Sikarus_cpt

Яндекс-диск: https://disk.yandex.ru/client/aa/d_fW3F1_fFjFW0XQ/

Сайт предмета: https://www.hse.ru/ba/ling/courses/916869660.html''')

def bzd(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.

Формула оценки:
0.15 * Домашнее задание №1 + 0.3 * Домашнее задание №2 + 0.2 * Домашнее задание №3 + 0.1 * Просмотр онлайн-курса + 0.25 * Тестирование

Техподдержка: bzd@hse.ru

Сайт предмета: https://www.hse.ru/ba/ling/courses/916877035.html''')

def theory(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
Формула оценки:

1 курс, 4 модуль - Фонетика и Фонология
0,25 * домашние КР по фонетике + 0,25 * домашние КР по фонологии + 0,1 * среднее за квизы + 0,4 * экзамен

2 курс, 1 модуль - Морфология
Накопленная письменная =ОКРУГЛ(0.5 * квизы + 0.5 * контрольные)
Итоговая накопленная = МИН(8; Накопленная письменная)
Стартовая оценка на экзамене = Итоговая накопленная - 1
На экзамене можно повысить стартовую оценку на максимум 3 балла
Более подробно о системе оценивания морфологии: https://docs.google.com/document/d/1u9jhvW19np4nNjLyqKELb0OPY6sGb_WUt88pY1Gqrps/edit?tab=t.0

2 курс, 2 модуль - Семантика
экзамен по семантике * 0.37 + от шести до девяти домашних заданий по семантике с равным весом * 0.63

2 курс, 3 модуль - Синтаксис
контрольные работы по синтаксису * 0.4 + экзамен по синтаксису * 0.6

2 курс, 4 модуль
Активность на семинарах по русскому синтаксису * 0.15 + Экзамен по русскому синтаксису * 0.35 + 2-3 домашних задания по русскому синтаксису * 0.3 + Контрольная работа по русскому синтаксису * 0.2

Информация о преподавателях:
Алексеева Анастасия Павловна, почта: a.alekseeva@hse.ru
Бузанов Антон Олегович, почта: anton.buzanov.00@gmail.com, телеграм: @vantral
Виняр Алексей Игоревич, почта: alexvinyar@yandex.ru
Зибер Инна Арнольдовна, почта: innasieber@gmail.com, телеграм: @innasieber
Подобряев Александр Владимирович, почта: sasha.podobryaev@gmail.com
Сафонова Анастасия Александровна, почта: an.saphonova@gmail.com
Стенин Иван Андреевич, почта: ystein88@gmail.com

Сайт с материалами курса фонетики и фонологии: https://phonphon.pythonanywhere.com/ 
Папка с материалами курса фонетики: https://drive.google.com/drive/folders/1BL3In_wSWnoJtSIrv3EeMgwRJJ9jsNoH


Папка с материалами курса морфологии: https://drive.google.com/drive/folders/13ZLgOCQyTzcMIxLKL8l0xUDDG5P2G2B3 

Сайт предмета: https://www.hse.ru/ba/ling/courses/916897150.html''')

def acap(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
Формула оценки:
Академическое письмо:
0.2 * Доклад по статье + 0.2 * ДЗ + 0.1 * Предзащита темы курсовой + 0.1 * Сбор и разметка данных + 0.2 * Планомерное написание курсовой + 0.2 * Проверочная по оформлению библиографии (актуально для французов-241, может отличаться по группам)

Курсовая:
0.7 * Текст + 0.3 * Защита

Информация о преподавателях:
Альбицкий Павел Олегович, почта: poalbitskiy@hse.ru
Ахапкина Яна Эмильевна, почта: yakhapkina@hse.ru
Бажуков Максим Олегович, почта: oa.bazhukov@gmail.com, телеграм: @bamaxi
Макарчук Илья Владимирович, почта: ilya.makarchuk@gmail.com
Маринина Валерия Владимировна, почта: vmarinina@hse.ru
Яковлева Анастасия Владимировна, почта: yaknastak@gmail.com

Папка с материалами курса: https://drive.google.com/drive/u/0/folders/1jCtsA1YN0gnV-S-zb7ajvwMMFMuq0vxF 

Сайт предмета: https://www.hse.ru/ba/ling/courses/916886308.html''')

def intro(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
Формула оценки:
0,15 * первая КР введение proper + 0.1 * первый квиз введение proper + 0.15 * вторая КР введение proper + 0.1 * второй квиз введение proper + 0.15 * КР по ЯРам + 0.35 * Экзамен по ЯРам (только при условии сдачи диктантов)
Информация о преподавателях:
Алексеева Анастасия Павловна, почта: a.alekseeva@hse.ru
Волков Олег Сергеевич, почта: kot_gitarist@mail.ru, телеграм: @kotmorozkafas
Дедов Тимофей Геннадьевич, почта: tgdedov@gmail.com
Казакова Татьяна Борисовна, почта: tanusha.kazakova@gmail.com, телеграм: @tbkazak
Ландер Юрий Александрович, почта: yulander@yandex.ru
Рахилина Екатерина Владимировна, почта: rakhilina@gmail.com
Русских Алина Алексеевна, почта: allruss@list.ru
Степанянц Максим Гургенович, почта: maximstepanyants@gmail.com

Сайт предмета: https://www.hse.ru/ba/ling/courses/916893036.html''')

def arab(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
Формула оценки:

1 курс, 1 модуль
0,1 домашние работы + 0,2*лексические диктанты + 0,3*контрольная работа + 0,4*экзамен (в форме устного ответа)

1 курс, 4 модуль
0,1*аудиторные работы + 0,15*лексические диктанты + 0,15*домашние работы + 0,2*контрольные работы + 0,4*экзамен

2 курс, 1 модуль
0,1*лексические диктанты + 0,2*домашние работы + 0,3*контрольные работы + 0,4*экзамен

2 курс, 4 модуль
0,2*аудиторные работы + 0,1*домашние работы + 0,1*лексические диктанты + 0,2*контрольные работы + 0,4*экзамен

3 курс, 1 модуль
0,3*домашние работы + 0,1*аудиторные работы + 0,2*контрольные работы + 0,4*экзамен

3 курс, 4 модуль
0,1*домашние работы + 0,2*аудиторные работы + 0,15*презентация + 0,15*контрольные работы + 0,4*экзамен

Информация о преподавателях:
Леконцев Филипп Эдуардович, почта: flekontsev@hse.ru, телеграм: @flekontsev
Смулянский Михаил Олегович, почта: msmulyanskii@hse.ru, телеграм: @migalum

Гугл-диск: https://drive.google.com/drive/folders/1bUhFN_2ph6IoAHuSmxWJGVaj7r_gbeYv

Сайт предмета: https://www.hse.ru/ba/ling/courses/916894987.html''')

def chin(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
Формула оценки:

1 курс, 1 модуль
0,2 за итоговый аудио-диктант + 0,2 за итоговый иероглифический диктант + 0,2 дз + 0,2 активность на паре + 0,2 аудиторный контроль

1 курс, 4 модуль
0.1 * Активность на паре + 0.2 * Аудиторный контроль (мини-тесты, фонетические и иероглифические диктанты, перевод, говорение) + 0.15 * Домашние задания + 0.25 * Итоговые контрольные по темам, пройденным в модуле (в конце каждого модуля) + 0.3 * Экзамен

2 курс, 1 модуль
0.1 * Активность на паре + 0.2 * Аудиторный контроль (мини-тесты, фонетические и иероглифические диктанты, перевод, говорение) + 0.15 * Домашние задания + 0.25 * Итоговая контрольная по темам, пройденным в модуле + 0.3 * Устный опрос по пройденным темам

2 курс, 4 модуль
0.1 * Активность на паре + 0.2 * Аудиторный контроль (мини-тесты, фонетические и иероглифические диктанты, перевод, говорение) + 0.15 * Домашние задания + 0.25 * Итоговые контрольные по темам, пройденным в модуле (в конце каждого модуля) + 0.3 * Экзамен

3 курс, 1 модуль
0.1 * Активность на паре + 0.2 * Аудиторный контроль (мини-тесты, фонетические и иероглифические диктанты, перевод, говорение) + 0.15 * Домашние задания + 0.25 * Итоговые контрольные по темам, пройденным в модуле (в конце каждого модуля) + 0.3 * Экзамен

3 курс, 4 модуль
0.1 * Активность на паре + 0.2 * Аудиторный контроль (мини-тесты, фонетические и иероглифические диктанты, перевод, говорение) + 0.15 * Домашние задания + 0.25 * Итоговые контрольные по темам, пройденным в модуле (в конце каждого модуля) + 0.3 * Экзамен

Информация о преподавателях:
Дурыманова Анастасия Дмитриевна, почта: adurymanova@hse.ru

Яндекс диск: https://disk.yandex.ru/d/Y0_FgS8OzhgOmg

Сайт предмета: https://www.hse.ru/ba/ling/courses/916885282.html''')

def span(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
Формула оценки:
1 курс, 1 модуль
Аудиторная работа (мини- тесты по пройденным темам) * 0.25 + Домашние задания * 0.25 + Экзамен * 0.5

1 курс, 4 модуль
Аудиторная работа (мини- тесты по пройденным темам) * 0.2 + Домашние задания * 0.10 + Контрольные работы 0.2 + Экзамен * 0.5

2 курс, 1 модуль
Аудиторная работа (мини- тесты по пройденным темам) * 0.25 + Домашние задания * 0.25 + Экзамен * 0.5

2 курс, 4 модуль
Аудиторная работа (мини- тесты по пройденным темам) * 0.2 + Домашние задания * 0.10 + Контрольные работы 0.2 + Экзамен * 0.5

3 курс, 1 модуль
Аудиторная работа (мини- тесты по пройденным темам) * 0.25 + Домашние задания * 0.25 + Экзамен * 0.5

3 курс, 4 модуль
Аудиторная работа (мини- тесты по пройденным темам) * 0.2 + Домашние задания * 0.10 + Контрольные работы 0.2 + Экзамен * 0.5

Информация о преподавателях:
Коган Пётр Леонидович, почта: pkogan@hse.ru, телеграм: @pkogan

Сайт предмета: https://www.hse.ru/ba/ling/courses/916870873.html''')

def germ(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
Формула оценки:
1 курс, 1 модуль
0.400 Экзамен, 0.250 Контрольные работы, 0.200 Аудиторная, 0.150 Домашние задания

1 курс, 4 модуль
0.500 Экзамен, 0.200 Контрольные работы, 0.200 Аудиторная, 0.100 Домашние задания

2 курс, 1 модуль
Аудиторная работа: мини-тесты по пройденным темам * 0.2 + Домашние задания * 0.15 + Контрольные работы 0.25 + Экзамен * 0.4

2 курс, 4 модуль
Аудиторная работа: мини-тесты по пройденным темам * 0.2 + Домашние задания * 0.15 + Контрольные работы 0.25 + Экзамен * 0.4

3 курс, 1 модуль
Аудиторная работа: мини-тесты по пройденным темам * 0.25 + Домашние задания * 0.25 Экзамен * 0.5

3 курс, 4 модуль
Аудиторная работа: мини-тесты по пройденным темам * 0.2 + Домашние задания * 0.15 + Контрольные работы 0.25 + Экзамен * 0.4

Информация о преподавателях:
Пименова Наталья Борисовна, почта: nb.pimenova@hse.ru

Сайт предмета: https://www.hse.ru/ba/ling/courses/916892087.html''')

def fren(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
Формула оценки:

1 курс, 1 модуль
0.3 * домашние и самостоятельные работы + 0.4 * итоговая контрольная работа + 0.3 * экзамен

1 курс, 4 модуль
0.1 * активность на практических занятиях + 0.2 * домашняя/проверочная работа + 0.3 * контрольная работа + 0.1 * посещаемость + 0.3 * экзамен


Информация о преподавателях:
Никишина Елена Андреевна, почта: helene_nikichina@mail.ru, телеграм: @helene_nikichina
Поливанова Дарья Константиновна, почта: dpolivanova@hse.ru
Юдина Ирина Юрьевна, почта: iyudina@hse.ru, телеграм: @irina_small_school

Сайт предмета: https://www.hse.ru/ba/ling/courses/916887537.html''')

def ancient(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
Формула оценки:

1 курс, 1 модуль
1 * Латинский язык: определение формы слов

1 курс, 3 модуль
0.3 * Итоговый экзамен по латыни + 0.25 * Итоговый экзамен по старославянскому + 0.25 * Контрольные по латинскому языку + 0.2 * Контрольные по старославянскому

Информация о преподавателях:
Ермолова Мария Вадимовна, почта: mskachedubova@hse.ru
Зибер Инна Арнольдовна, почта: innasieber@gmail.com, телеграм: @innasieber
Козлов Алексей Андреевич, почта: aakozlov@hse.ru, телеграм: @dr_dulcamara
Орлов Александр Викторович, почта: alexander.orlov98@gmail.com
Файер Владимир Владимирович, почта: vvfire@hse.ru, телеграм: @VFayer
Яковлева Анастасия Владимировна, почта: yaknastak@gmail.com
Иордани Наталья Павловна, почта: niordani@hse.ru, телеграм: @n_pawlowna
Седукова Надежда Александровна, почта: nsedukova@hse.ru, телеграм: @nadya_sedukova

Папка с материалами по латыни: https://drive.google.com/drive/folders/1GhHjIJsMWXW0yTEocs7uh4nadCcSz56V?hl=ru 

Сайт предмета: https://www.hse.ru/ba/ling/courses/916881259.html''')

def philology(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
3-4 модуль

Формула оценки:
0.5 * активность студентов при обсуждении проблематики курса + 0.5 * итоговое собеседование на последних занятиях

Информация о преподавателях:
Гиппиус Алексей Алексеевич, почта: agippius@hse.ru

Папка с материалами курса: https://disk.yandex.ru/d/z9JxmAOeHaTH0A 

Сайт предмета: https://www.hse.ru/ba/ling/courses/916873423.html''')

def anthro(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
1-2 модуль

Формула оценки:
0.5 * письменный экзамен + 0.3 * самостоятельные работы + 0.2 эссе + дополнительные баллы за активность

Информация о преподавателях:
Сомин Антон Александрович, почта: somin@tut.by

Сайт предмета: https://www.hse.ru/ba/ling/courses/916872610.html''')

def errors(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
3-4 модуль

Формула оценки:
0.1 * Classroom activity + 0.3 * Essay + 0.3 * Home Assignment + 0.3 * Mid-term test

Информация о преподавателях:
Выренкова Анастасия Сергеевна, почта: anastasia.marushkina@gmail.com, телеграм: @anastasiavyrenkova
Рахилина Екатерина Владимировна, почта: rakhilina@gmail.com

Сайт предмета: https://www.hse.ru/ba/ling/courses/916897759.html''')

def problems(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
1-2 модуль

Формула оценки:
0.33 * Домашнее задание 1 + 0.33 * Домашнее задание 2 + 0.34 * Домашнее задание 3

Информация о преподавателях:
Наследскова Полина Леонидовна, почта: polli2498@gmail.com

Сайт предмета: https://www.hse.ru/ba/ling/courses/916897413.html''')

def rzy(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
1-4 модуль

Формула оценки:

1 курс, 2 модуль
0.25 * Аудиторная работа + 0.25 * Коллоквиум + 0.25 * Самостоятельная работа + 0.25 * Экзамен

1 курс, 4 модуль
0.25 * Аудиторная работа + 0.25 * Коллоквиум + 0.25 * Самостоятельная работа + 0.25 * Экзамен

Информация о преподавателях:
Переверзева Светлана Игоревна, почта: spereverzeva@hse.ru

Сайт предмета:
1-2 модуль https://www.hse.ru/ba/ling/courses/916867282.html 
3-4 модуль https://www.hse.ru/ba/ling/courses/916867278.html''')

def roman(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
1-2 модуль

Формула оценки:
0.2 * Контрольная работа + 0.3 * Работа на семинарах + 0.5 * Экзамен

Информация о преподавателях:
Кичигин Кирилл Валерьевич, почта: kkichigin@hse.ru, телеграм: @KirillKichigin

Сайт предмета: https://www.hse.ru/ba/ling/courses/916883467.html ''')

def empir(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
3-4 модуль

Формула оценки:
0.3 * Анализ методологии в статье на выбор + 0.3 * Вопросы и комментарии к статьям + 0.4 * Эссе на тему по выбору

Информация о преподавателях:
Русских Алина Алексеевна, почта: allruss@list.ru

Сайт с материалами курса: https://sites.google.com/view/data-theory?usp=sharing 

Сайт предмета:
https://www.hse.ru/ba/ling/courses/916871988.html''')

def prog(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
Формула оценки:

1 курс, 2 модуль
0.3 * Домашние задания по лингвистическим данным + 0.2 * Контрольная работа по лингвистическим данным + 0.3 * Проект по лингвистическим данным + 0.2 * Экзамен по лингвистическим данным

1 курс, 3 модуль
1 * Предзащита проекта по программированию

1 курс, 4 модуль
0.3 * Домашние задания по программированию + 0.2 * Контрольные работы по программированию + 0.3 * Проект по программированию + 0.2 * Экзамен по программированию

Информация о преподавателях:
Бузанов Антон Олегович, почта: anton.buzanov.00@gmail.com, телеграм: @vantral
Казакова Татьяна Борисовна, почта: tanusha.kazakova@gmail.com, телеграм: @tbkazak
Козлова Екатерина Руслановна, почта: e.kozlova@hse.ru, телеграм: @da_budet_tak
Ляшевская Ольга Николаевна, почта: olesar@yandex.ru, телеграм: @olesar
Стрельцов Артём Дмитриевич, почта: astreltsov@hse.ru, телеграм: @in_chainz
Степанова Ангелина Михайловна, почта: angelina.stepanova.m@gmail.com, телеграм:@life_on_maaars

Страница программирования на github: https://github.com/pykili/intro2python_2024/ 
Страница лингвистических данных на github: https://olesar.github.io/lingdata/ 

Сайт предмета: https://www.hse.ru/ba/ling/courses/916871498.html''')

def social(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
Формула оценки:
0.3 * Итоговая письменная работа + 0.2 * Проект "Отношение к языку" + 0.2 * Проект: "Вариативность в языке" + 0.15 * Ревью исследовательской статьи + 0.15 * Эссе "Многоязычие"

Информация о преподавателях:
Виняр Алексей Игоревич, почта: alexvinyar@yandex.ru
Ронько Роман Витальевич, почта: romanronko@gmail.com
Сомин Антон Александрович, почта: somin@tut.by

Папка с материалами курса: https://drive.google.com/drive/folders/1Q_mNx8e6W9D-NAiqmh7BVhc8Eu_e0F9l 

Сайт предмета: https://www.hse.ru/ba/ling/courses/916898062.html''')

def cyber(message):
    bot.send_message(message.from_user.id,'''Хорошо! Вот, что я могу сказать про этот предмет.
Формула оценки:
=0.25 * КонтрольнаяНЭ + 0.25 * Аудиторные и домашние практические работы +0.3 * Проект (но не больше 8)

Информация о преподавателях:
Степанова Ангелина Михайловна, почта: angelina.stepanova.m@gmail.com, телеграм:@life_on_maaars
Камаева Элина Петровна, почта: ekamaeva@hse.ru, телеграм: @elinkamaeva

Сайт предмета: https://www.hse.ru/ba/ling/courses/916895383.html''')

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
    if answer == current_language or answer == f'{current_language} язык':
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
    if answer == current_language or answer == f'{current_language} язык':
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
    if answer == current_language or answer == f'{current_language} язык':
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
            bot.register_next_step_handler(message, ending)
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
        if '_' not in display_word:
            bot.send_message(message.from_user.id,f'Ура! Ты отгадал/а слово: {current_word}')
            bot.send_message(message.from_user.id,'Чтобы продолжить играть или прекратить, напиши "заново" или "закончить"')
            bot.register_next_step_handler(message, ending)
        else:
            bot.register_next_step_handler(message, guess)
            
def ending(message):
    if message.text.lower() == 'заново':
        hangoncemore(message)
    elif message.text.lower() == 'закончить':
        endgame(message)
    else:
        bot.send_message(message.from_user.id,'Игра закончена. Чтобы продолжить играть или прекратить, напиши "заново" или "закончить"')
        bot.register_next_step_handler(message, ending)
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
    elif call.data == "before":
        end_date = current_date
        current_date = start_date + (current_date - start_date) // 2
        return current_date
    elif call.data == "after":
        start_date = current_date
        current_date = current_date + (end_date - current_date) // 2
        return current_date

start_date = datetime.date(1950, 1, 1)
end_date = datetime.date(2020, 12, 31)
current_date = random_date(start_date, end_date)
def age_guesser(message):
    
    bot.send_message(message.from_user.id, """О нет! Злой волшебник Кох запер вас в своем замке и не отпустит, пока не угадает вашу дату рождения!
    Правила игры: волшебник Кох покажет дату. Выберите подходящий ответ.
    Если игра вам наскучила, напишите «Выход».""")


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


        
        
        
# Функция, чтобы бот все время принимал сообщения без ошибки ReadTimeout. 
# Когда бот не может подключиться, он печатает ошибку и продолжает пытаться подключиться спустя 5 секунд
while True:
    try:
        bot.polling(non_stop=True, interval=0)
    except Exception as e:
        print(e)
        time.sleep(5)
        continue
