import telebot

bot = telebot.TeleBot('1240641183:AAEYMBx8u9nKU2pdvjGIvMHfWbR5OTDDIJU')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Здравствуй, хозяин.')

bot.polling()