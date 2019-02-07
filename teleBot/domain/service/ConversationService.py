from telegram import Bot, Update, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler
import fix_yahoo_finance as yf

class ConversationService:
    REPLY_KEYBOARD = [['Age', 'Favourite colour'],
                      ['Number of siblings', 'Something else...'],
                      ['Done']]
    CONVERSATION_MARKUP = ReplyKeyboardMarkup(REPLY_KEYBOARD, one_time_keyboard=False)
    CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

    def conversation_service(self, bot: Bot, update: Update):
        update.message.reply_text(
            "Hi! My name is Doctor Botter. I will hold a more complex conversation with you. "
            "Why don't you tell me something about yourself?",
            reply_markup=self.CONVERSATION_MARKUP)

        return self.CHOOSING

    def received_information(self, bot: Bot, update: Update, user_data: {}):
        text = update.message.text
        category = user_data['choice']
        user_data[category] = text
        del user_data['choice']

        update.message.reply_text("Neat! Just so you know, this is what you already told me:"
                                  f"{self.facts_to_str(user_data)}"
                                  "You can tell me more, or change your opinion on something.",
                                  reply_markup=self.CONVERSATION_MARKUP)

        return self.CHOOSING

    def regular_choice(self, bot: Bot, update: Update, user_data: {}):
        text = update.message.text
        user_data['choice'] = text
        update.message.reply_text(
            'Your {}? Yes, I would love to hear about that!'.format(text.lower()))

        return self.TYPING_REPLY

    def custom_choice(self, bot: Bot, update: Update):
        update.message.reply_text('Alright, please send me the category first, '
                                  'for example "Most impressive skill"')

        return self.TYPING_CHOICE

    def done(self, bot, update, user_data):
        if 'choice' in user_data:
            del user_data['choice']

        update.message.reply_text("I learned these facts about you:"
                                  f"{self.facts_to_str(user_data)}"
                                  "Until next time!")

        user_data.clear()

        return ConversationHandler.END

    @staticmethod
    def facts_to_str(user_data):
        facts = list()

        for key, value in user_data.items():
            facts.append('{} - {}'.format(key, value))

        return "\n".join(facts).join(['\n', '\n'])
