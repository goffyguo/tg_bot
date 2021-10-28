import telebot
TOKEN = ''
tb = telebot.TeleBot(TOKEN)
text = "Hello Telegram!"
tb.send_message(1, text)