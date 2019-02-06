from telegram.ext import CommandHandler

from teleBot import updater
from teleBot.domain.service.CommandLineService import CommandLineService

dispatcher = updater.dispatcher
commandLineService = CommandLineService()
start_handler = CommandHandler('start', commandLineService.start_service)
dispatcher.add_handler(start_handler)
