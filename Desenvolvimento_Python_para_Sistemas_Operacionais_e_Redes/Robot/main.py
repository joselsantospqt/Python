import dataclasses
import logging
import time

import requests
from telegram import Update
from telegram.constants import CHATACTION_TYPING
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler, CallbackContext, ConversationHandler
from telegram.ext import CommandHandler
import telegram
from Robot import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token=config.TOKEN, use_context=True)


def msg(update, context):
    chat_id = update.effective_chat.id
    nome = update.effective_chat['first_name']
    context.bot.send_message(chat_id=chat_id, text=' <- - - Processando - - ->')
    context.bot.send_chat_action(chat_id=chat_id, action='typing')
    response = requests.get(
        'https://raw.githubusercontent.com/joselsantospqt/JavaScript202/master/JavaScript/vinhos.json')
    response.headers['content-type']
    response.text
    dados = response.json()

    context.bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    time.sleep(2)

    sim = telegram.InlineKeyboardButton(text='sim', callback_data='sim')
    nao = telegram.InlineKeyboardButton(text='não', callback_data='sim')
    custom_keyboard = [[sim, nao]]
    replay_markup = telegram.InlineKeyboardMarkup(custom_keyboard)

    context.bot.send_message(chat_id=chat_id, text=f"Seu nome é {nome}",
                             reply_markup=replay_markup)


    ''' 
    time.sleep(2)
    for i in dados:
        mensagem = (f'*Nome*: {dados[i]["nome"]} \n' \
                    f'*produtor*:{dados[i]["produtor"]} \n' \
                    f'*alcool*:{dados[i]["alcool"]} \n' \
                    f'*temperatura*:{dados[i]["temperatura"]} \n' \
                    f'*uvas*:{dados[i]["uvas"]} \n' \
                    f'*harmonização*:{dados[i]["harmonizacao"]} \n' \
                    f'*notas*:{dados[i]["notas"]} \n')

        context.bot.send_message(chat_id=chat_id, text=mensagem)

     image_str = urlopen(usuario[0].foto).read()
      image_file = io.BytesIO(image_str)
      img = pygame.image.load(image_file)
      img = pygame.transform.scale(img, (200, 200))
      tela.blit(img, dest=(50, 150))'''


def start(update, context):
    chat_id = update.effective_chat.id
    nome = update.effective_chat['first_name']
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Bem Vindo {nome} - id :  {chat_id}")

msg_interacao_usuario = MessageHandler(Filters.text, msg)

start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(msg_interacao_usuario)

updater.start_polling()
