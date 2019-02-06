from telegram.ext import CommandHandler

from teleBot import updater
from teleBot.domain.service.CommandLineService import CommandLineService

dispatcher = updater.dispatcher
commandLineService = CommandLineService()

dispatcher.add_handler(CommandHandler('start', commandLineService.start_service))
dispatcher.add_handler(CommandHandler(commandLineService.start_callback_service))
