import telebot
from telebot import types
TOKEN = '1417817254:AAFWuFukx49eBbRChAYIm1CvC_Fhrf3dFCA'

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('API')
itembtn2 = types.KeyboardButton('Зашифровать')
itembtn3 = types.KeyboardButton('Расшифровать')
itembtn4 = types.KeyboardButton('Добавить в БД')
markup.add(itembtn1, itembtn2, itembtn3, itembtn4)

markup_st = types.ReplyKeyboardMarkup()
itembtnst = types.KeyboardButton('В начало')
markup_st.add(itembtnst)

markup_api = types.ReplyKeyboardMarkup()
itembtn1_api = types.KeyboardButton('Получить API_TOKEN')
itembtn2_api = types.KeyboardButton('Документация к API')
itembtn3_api = types.KeyboardButton('В начало')
markup_api.add(itembtn1_api, itembtn2_api, itembtn3_api)