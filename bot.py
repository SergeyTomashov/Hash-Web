import telebot
import sqlite3
import sql
import datetime
import hashlib, os
from telebot import types
import config

db = sql.sqll('database.db')
bot = telebot.TeleBot(token=config.TOKEN)

def generate_API_TOKEN(user_id, reg_data, salt):
    API_TOKEN = str(user_id) + reg_data + str(salt)
    API_TOKEN = API_TOKEN.encode('utf-8')
    return hashlib.sha1(API_TOKEN).hexdigest().upper()

@bot.message_handler(commands=['start'])
def start(message):
    if not db.user_in_base(message.chat.id):
        db.add_user(user_id=message.chat.id, reg_date=str(datetime.datetime.now()), API_TOKEN=generate_API_TOKEN(message.chat.id, str(datetime.datetime.now()), os.urandom(32)).upper(), subscription=True)
        bot.send_message(message.chat.id, "Всем привет!", reply_markup=config.markup)
    else:
        bot.send_message(message.chat.id, "Всем привет!", reply_markup=config.markup)
        bot.send_message(message.chat.id, "Вы уже начали работать с ботом!")

@bot.message_handler(content_types=['text'])
def API(message):
    if not db.user_in_base(message.chat.id):
        db.add_user(user_id=message.chat.id, reg_date=str(datetime.datetime.now()), API_TOKEN=generate_API_TOKEN(message.chat.id, str(datetime.datetime.now()), os.urandom(32)).upper(), subscription=True)
    if message.text == 'API':
        bot.send_message(message.chat.id, "Вы можете узнать свой API_TOKEN и получить информацию о работе с API", reply_markup=config.markup_api)
    elif message.text == 'Получить API_TOKEN':
        TOKEN1 = db.get_api_token(message.chat.id)
        bot.send_message(message.chat.id, f'Ваш API_TOKEN: {TOKEN1}', reply_markup=config.markup_st)
    elif message.text == 'В начало':
        bot.send_message(message.chat.id, 'Вы вернулись в начало!', reply_markup=config.markup)
bot.polling()