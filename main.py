import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

API_TOKEN = '7706578873:AAHeThjzgtL9YR6toT97zGDk34AnRxnL43s'

bot = telebot.TeleBot(API_TOKEN)

WEBAPP_URL = "https://narmipython.github.io/another_tg_bot/"

@bot.message_handler(commands=['start'])
def start(message):
    send_button(message.chat.id)

@bot.message_handler(func=lambda message: True)
def send_on_every_message(message):
    send_button(message.chat.id)

def send_button(chat_id):
    markup = InlineKeyboardMarkup()
    webapp = WebAppInfo(url=WEBAPP_URL)
    btn = InlineKeyboardButton("▶️ Open Game", web_app=webapp)
    markup.add(btn)
    bot.send_message(chat_id, "Click below", reply_markup=markup)

bot.polling(none_stop=True)
