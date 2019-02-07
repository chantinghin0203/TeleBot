from pandas_datareader import data as pdr
from telegram import Update, Bot
from datetime import datetime, timedelta


class CommandLineService:
    def start_service(self, bot: Bot, update: Update, args: str):
        # keyboard = [[InlineKeyboardButton("Male", callback_data='Male'),
        #              InlineKeyboardButton("Female", callback_data='Female')]]
        for stock in args:
            stock_data = pdr.get_data_yahoo(stock,
                                            start=datetime.now().date() - timedelta(days=10),
                                            end=datetime.now().date())
            update.message.reply_text(f"{stock} : {stock_data.to_dict(orient='records')[-1]}")

    def start_callback_service(self, bot: Bot, update: Update):
        query = update.callback_query

        bot.edit_message_text(text="Selected option: {}".format(query.data),
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
