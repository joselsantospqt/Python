import time
import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Robot import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)



updater = Updater(token=config.TOKEN, use_context=True)

def msg(update, context):
    chat_id = update.effective_chat.id
    texto = update.effective_messag.text
    context.bot.send_message(chat_id=chat_id, text='processando')
    context.bot.send_chatt_action(chat_id=chat_id, action='typing')
    time.sleep(2)
    context.bot.send_message(chat_id=chat_id, text=texto.upper())




def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Bem Vindo {chat_id}")

msg_handler = MessageHandler(Filters.text, msg)

start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(msg_handler)

updater.start_polling()

