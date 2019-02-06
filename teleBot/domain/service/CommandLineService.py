from telegram import Update, Bot


class CommandLineService:
    def start_service(self, bot: Bot, update: Update):
        bot.send_message(chat_id=update.message.chat_id,
                         text=f"I'm a dummy bot, please talk to me! {update.effective_user['first_name']}")

    def start_callback_service(self, bot: Bot, update: Update):
        query = update.callback_query

        bot.edit_message_text(text="CallBack!!!!",
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
