import telebot

bot = telebot.TeleBot("Вставь токен бота")
CHAT_ID = 'Вставь свой id'

with open('Сюда вставь название своего файла', 'rb') as file_to_send:
        ret_msg = bot.send_document(CHAT_ID, file_to_send)

bot.infinity_polling()
