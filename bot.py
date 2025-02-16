import telebot
import os

TOKEN = os.getenv("7749914056:AAFkiR0h3JYtCMClbYinrzxonyqQywm65e4")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Your bot is running successfully.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
