from bs4 import BeautifulSoup
import requests
import telebot
from telebot import types
bot = telebot.TeleBot('5141476622:AAEEnQhrxsNsPX9OmLQCYrKTP89MEGKs8bQ')

@bot.message_handler(commands=['start'])
def send_xyz(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        niws= types.KeyboardButton("Новости")
        itembtn1 = types.KeyboardButton("Приветствие")
        itembtn2 = types.KeyboardButton("Гороскоп на сегодня")
        itembtn3 = types.KeyboardButton("Гороскоп на завтра")
        itembtn4 = types.KeyboardButton("Гороскоп на вчера")
        itembtn5 = types.KeyboardButton("Гороскоп на неделю")
        itembtn6 = types.KeyboardButton("Гороскоп на месяц")
        itembtn7 = types.KeyboardButton("Гороскоп на год")
        znak1 = types.KeyboardButton("Овен ♈️")
        znak2 = types.KeyboardButton("Телец ♉️")
        znak3 = types.KeyboardButton("Близнецы ♊️")
        znak4 = types.KeyboardButton("Рак ♋️")
        znak5 = types.KeyboardButton("Лев ♌️")
        znak6 = types.KeyboardButton("Дева ♍️")
        znak7 = types.KeyboardButton("Весы ♎️")
        znak8 = types.KeyboardButton("Скорпион ♏️")
        znak9 = types.KeyboardButton("Стрелец ♐️")
        znak10 = types.KeyboardButton("Козерог ♑️")
        znak11 = types.KeyboardButton("Водолей ♒️")
        znak12 = types.KeyboardButton("Рыбы ♓️")
        markup.add(niws)
        markup.add(itembtn1, itembtn2)
        markup.add(itembtn3, itembtn4)
        markup.add(itembtn5, itembtn6)
        markup.add(itembtn7)
        markup.add(znak1)
        markup.add(znak2)
        markup.add(znak3)
        markup.add(znak4)
        markup.add(znak5)
        markup.add(znak6)
        markup.add(znak7)
        markup.add(znak8)
        markup.add(znak9)
        markup.add(znak10)
        markup.add(znak11)
        markup.add(znak12)
        bot.send_message(message.chat.id, "Привет! Нажми на кнопочки внизу",reply_markup=markup)
       # bot.send_message(message.chat.id, {message} )

def niw(message):
    url = 'https://meduza.io'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('h2', class_='BlockTitle-root BlockTitle-is1to2 BlockTitle-isInSimple') 
    times = soup.find('div', class_='SimpleBlock-footer')
    res =times.text +"\n"+ quotes.text
    bot.send_message(message.chat.id, res)


def today(message):
    url = 'https://horo.mail.ru/prediction/today'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', class_='article__text')
    titles = soup.find('h1', class_='hdr__inner')
    days = soup.find('div', class_='p-prediction__date-day')
    mons = soup.find('span', class_='p-prediction__date__text__inner')
    res = days.text +" "+ mons.text +"\n"+ titles.text +"\n"+ quotes.text
    bot.send_message(message.chat.id, res)

def tomorrow(message):
    url = 'https://horo.mail.ru/prediction/tomorrow'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes= soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    days = soup.find('div', class_='p-prediction__date-day')
    mons = soup.find('span', class_='p-prediction__date__text__inner')
    res = days.text  +" "+ mons.text +"\n"+ titles.text +"\n"+ quotes.text
    bot.send_message(message.chat.id, res)

def yesterday(message):
    url = 'https://horo.mail.ru/prediction/yesterday'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes= soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    days = soup.find('div', class_='p-prediction__date-day')
    mons = soup.find('span', class_='p-prediction__date__text__inner')
    res = days.text +" "+ mons.text +"\n"+ titles.text  +"\n"+  quotes.text
    bot.send_message(message.chat.id, res)

def week(message):
    url = 'https://horo.mail.ru/prediction/week'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes= soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    days = soup.find('div', class_='p-prediction__date-day p-prediction__date-day_small-text')
    mons = soup.find('span', class_='p-prediction__date__text__inner')
    res = days.text +" "+ mons.text+"\n"+titles.text+"\n"+quotes.text
    bot.send_message(message.chat.id, res)

def month(message):
    url = 'https://horo.mail.ru/prediction/month'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes= soup.find('div', class_='article article_white article_prediction article_collapsed margin_top_20')
    titles = soup.find('h1', class_='hdr__inner')
    mons = soup.find('span', class_='p-prediction__date__text__inner')
    res =mons.text+"\n"+titles.text+"\n"+ quotes.text
    bot.send_message(message.chat.id, res)

def year(message):
    url = 'https://horo.mail.ru/prediction/year'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes= soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    days = soup.find('div', class_='p-prediction__date-day')
    mons = soup.find('span', class_='p-prediction__date__text__inner')
    res = days.text+' '+mons.text+"\n"+ titles.text +"\n"+ quotes.text
    bot.send_message(message.chat.id, res)




def znak1(message):
    url = 'https://horo.mail.ru/prediction/aries/today/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    res = titles.text+"\n"+quotes.text
    bot.send_message(message.chat.id, res)

def znak2(message):
    url = 'https://horo.mail.ru/prediction/taurus/today/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    res = titles.text+"\n"+quotes.text
    bot.send_message(message.chat.id, res)

def znak3(message):
    url = 'https://horo.mail.ru/prediction/gemini/today/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    res = titles.text+"\n"+quotes.text
    bot.send_message(message.chat.id, res)

def znak4(message):
    url = 'https://horo.mail.ru/prediction/cancer/today/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    res = titles.text+"\n"+quotes.text
    bot.send_message(message.chat.id, res)

def znak5(message):
    url = 'https://horo.mail.ru/prediction/leo/today/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    res = titles.text+"\n"+quotes.text
    bot.send_message(message.chat.id, res)

def znak6(message):
    url = 'https://horo.mail.ru/prediction/virgo/today/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    res = titles.text+"\n"+quotes.text
    bot.send_message(message.chat.id, res)

def znak7(message):
    url = 'https://horo.mail.ru/prediction/libra/today/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    res = titles.text+"\n"+quotes.text
    bot.send_message(message.chat.id, res)

def znak8(message):
    url = 'https://horo.mail.ru/prediction/scorpio/today/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    res = titles.text+"\n"+quotes.text
    bot.send_message(message.chat.id, res)

def znak9(message):
    url = 'https://horo.mail.ru/prediction/sagittarius/today/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    res = titles.text+"\n"+quotes.text
    bot.send_message(message.chat.id, res)

def znak10(message):
    url = 'https://horo.mail.ru/prediction/capricorn/today/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    res = titles.text+"\n"+quotes.text
    bot.send_message(message.chat.id, res)

def znak11(message):
    url = 'https://horo.mail.ru/prediction/aquarius/today/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    res = titles.text+"\n"+quotes.text
    bot.send_message(message.chat.id, res)

def znak12(message):
    url = 'https://horo.mail.ru/prediction/pisces/today/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', class_='article__item article__item_alignment_left article__item_html')
    titles = soup.find('h1', class_='hdr__inner')
    res = titles.text+"\n"+quotes.text
    bot.send_message(message.chat.id, res)




@bot.message_handler(content_types=['text'])    
def get_text_messages(message):
    if message.text == "Приветствие":
        bot.send_message(message.chat.id,f"Привет,{message.from_user.first_name}! Твой ID:{message.from_user.id}. Хорошего дня)" )
    elif message.text == "Гороскоп на сегодня":
        today(message)
    elif message.text == "Гороскоп на вчера":
        yesterday(message)
    elif message.text == "Гороскоп на завтра":
        tomorrow(message)
    elif message.text == "Гороскоп на неделю":
        week(message)
    elif message.text == "Гороскоп на месяц":
        month(message)    
    elif message.text == "Гороскоп на год":
        year(message)
    elif message.text == "Овен ♈️":
        znak1(message)
    elif message.text == "Телец ♉️":
        znak2(message)
    elif message.text == "Близнецы ♊️":
        znak3(message)
    elif message.text == "Рак ♋️":
        znak4(message)
    elif message.text == "Лев ♌️":
        znak5(message)
    elif message.text == "Дева ♍️":
        znak6(message)
    elif message.text == "Весы ♎️":
        znak7(message)
    elif message.text == "Скорпион ♏️":
        znak8(message)
    elif message.text == "Стрелец ♐️":
        znak9(message)
    elif message.text == "Козерог ♑️":
        znak10(message)
    elif message.text == "Водолей ♒️":
        znak11(message)
    elif message.text == "Рыбы ♓️":
        znak12(message)
    elif message.text == "Новости":
        niw(message)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start")
    elif message.text == "Миу":
        bot.send_message(message.from_user.id, "Все котики!!! День будет очень удачным и классным")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True)
