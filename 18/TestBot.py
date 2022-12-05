import telebot

TOKEN = "5919770435:AAGXTgMSJPo4ymY7kucnzP_wGeXBCoDR1F0"
bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start', 'help'])
# def handle_start_help(message):
#     bot.send_message(message.chat.id, f'Привет, {message.chat.username}')


@bot.message_handler(content_types=['document', 'photo'])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)
