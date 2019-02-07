from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler, RegexHandler, MessageHandler, \
    Filters

from teleBot import updater
from teleBot.domain.service.CommandLineService import CommandLineService
from teleBot.domain.service.ConversationService import ConversationService

dispatcher = updater.dispatcher
commandLineService = CommandLineService()
conversationService = ConversationService()

dispatcher.add_handler(CommandHandler('start', commandLineService.start_service, pass_args=True))
# dispatcher.add_handler(CallbackQueryHandler(commandLineService.start_callback_service))
dispatcher.add_handler(
    ConversationHandler(entry_points=[CommandHandler('conversation', conversationService.conversation_service)],
                        states={
                            conversationService.CHOOSING: [
                                RegexHandler('^(Age|Favourite colour|Number of siblings)$',
                                             conversationService.regular_choice,
                                             pass_user_data=True),
                                RegexHandler('^Something else...$',
                                             conversationService.custom_choice),
                            ],
                            conversationService.TYPING_CHOICE: [MessageHandler(Filters.text,
                                                                               conversationService.regular_choice,
                                                                               pass_user_data=True),
                                                                ],
                            conversationService.TYPING_REPLY: [MessageHandler(Filters.text,
                                                                              conversationService.received_information,
                                                                              pass_user_data=True),
                                                               ]
                        },
                        fallbacks=[
                            RegexHandler('^Done$', conversationService.done, pass_user_data=True)]
                        ))
