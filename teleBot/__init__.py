import logging
import os

from telegram.ext import Updater

from teleBot.resource.applicationConfig import Config, ProdConfig


def get_config(param: str) -> Config:
    if os.environ.get(param) is None:
        return Config()
    else:
        return ProdConfig()


CONFIG = get_config('APP_SETTINGS')

updater = Updater(token=CONFIG.TOKEN)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

from teleBot.domain.service import *
