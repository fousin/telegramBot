from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          RegexHandler, ConversationHandler, CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


def welcome(update, context):
    try:
        username = update.message.from_user.username
        firstName = update.message.from_user.first_name
        lastName = update.message.from_user.last_name
        message = 'Olá, ' + firstName + '!'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except Exception as e:
        print(str(e))



def main():
    try:
        # token = os.getenv('TELEGRAM_BOT_TOKEN', None)
        token = '5748916825:AAHlmxwXRFdwCkRBnJOW7C4HMuqt9pnKXYs'
        updater = Updater(token=token, use_context=True)

        updater.dispatcher.add_handler(CommandHandler('start', welcome))

        

        print("Updater no ar: " + str(updater))
        updater.start_polling()
        updater.idle()
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()

    