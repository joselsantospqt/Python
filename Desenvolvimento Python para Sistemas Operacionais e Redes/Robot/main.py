import telegram
from telegram.ext import Updater

TOKEN ='1693982914:AAEp5Tf7HwmcY7SAyTzU-yM1pGVktJ6OGnw'

updater = Updater(token='TOKEN', use_context=False)

def start(update, context):
    chat_id = update.effective_chat.chat.id
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Bem Vindo {chat_id}")


