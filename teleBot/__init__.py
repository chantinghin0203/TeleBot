import logging
import os

from telegram.ext import Updater

TOKEN = "786280876:AAE7S9sEdzmnFcxff4otomvtYicy7JL8kuw"
PORT = int(os.environ.get('PORT', '8443'))

updater = Updater(token=TOKEN)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

from teleBot.domain.service import *
