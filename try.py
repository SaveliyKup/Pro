import telebot, configparser
from telebot  import types, apihelper
from googletrans import Translator

config = configparser.ConfigParser()
config.read("settings.ini")
token    = config["tgbot"]["token"]

bot = telebot.TeleBot('5156143852:AAEXSpRve7QvpnRQBtCkPq96R4GYNNKjfkg')

translator = Translator()
@bot.message_handler(commands=["start"])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Перевод',callback_data=3))
    bot.send_message(message.chat.id, "Добро пожаловать! \nЯ бот-переводчик и готов переводить твои фразы.", reply_markup = markup)

@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text == "Перевод":
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='RU',callback_data=1))
        markup.add(telebot.types.InlineKeyboardButton(text='EN ', callback_data=2))

        bot.send_message(message.chat.id, "Выбери язык на который хотите перевести текст.", reply_markup = markup)
    else:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='RU',callback_data=1))
        markup.add(telebot.types.InlineKeyboardButton(text='EN ', callback_data=2))
        bot.send_message(message.chat.id, "Выбери язык на который хотите перевести текст.", reply_markup = markup)

def next_trans2(message):
    try:
        text = int(message.text)
        bot.send_message(message.chat.id, "Это не текст!")
    except:
        text =  message.text
        lang = 'ru'
        res = translator.translate(text, dest=lang)
        bot.send_message(message.chat.id, res.text)

def next_trans3(message):
    try:
        text = int(message.text)
        bot.send_message(message.chat.id, "Это не текст!")
    except:
        text =  message.text
        lang = 'en'
        res = translator.translate(text, dest=lang)
        bot.send_message(message.chat.id, res.text)



@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id)
    answer = ''
    if call.data == '1':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Выбрать другой язык', callback_data=3))
        markup.add(telebot.types.InlineKeyboardButton(text='Отмена', callback_data=4))
        msg = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Введите текст для перевода", reply_markup = markup)
        bot.register_next_step_handler(msg, next_trans2)
    elif call.data == '2':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Выбрать другой язык', callback_data=3))
        markup.add(telebot.types.InlineKeyboardButton(text='Отмена', callback_data=4))
        msg = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Введите текст для перевода", reply_markup = markup)
        bot.register_next_step_handler(msg, next_trans3)
    elif call.data == '3':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='RU',callback_data=1))
        markup.add(telebot.types.InlineKeyboardButton(text='EN ', callback_data=2))
        msg = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Выбери язык на который хотите перевести текст.", reply_markup = markup)
    elif call.data == '4':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Перевод', callback_data=3))
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = "Вы вернулись в главное меню!", reply_markup = markup)
      

bot.polling()