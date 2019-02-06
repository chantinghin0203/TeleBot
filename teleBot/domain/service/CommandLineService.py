from telegram import Update


class CommandLineService:
    def start_service(self, bot, update: Update):
        bot.send_message(chat_id=update.message.chat_id,
                         text=f"I'm a dummy bot, please talk to me! {update.effective_user['first_name']}")
