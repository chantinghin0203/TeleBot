from telegram import Update
from telegram.ext import CommandHandler
import logging
from telegram.ext import Updater

import os

TOKEN = "786280876:AAE7S9sEdzmnFcxff4otomvtYicy7JL8kuw"
PORT = int(os.environ.get('PORT', '8443'))

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(bot, update: Update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=f"I'm a bot, please talk to me! {update.effective_user['first_name']}")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.set_webhook("https://tele-bot-dummy.herokuapp.com/" + TOKEN)
updater.idle()
