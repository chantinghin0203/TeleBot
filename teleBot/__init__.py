import logging
import os

from telegram.ext import Updater

TOKEN = "786280876:AAE7S9sEdzmnFcxff4otomvtYicy7JL8kuw"
PORT = int(os.environ.get('PORT', '8443'))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

updater = Updater(token=TOKEN)
