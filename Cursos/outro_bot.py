import telebot

bot = telebot.TeleBot("1723578764:AAHqoQKbR5R19dREGQOAJUW9NKOxB9fTVSc")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()