from email import message
from turtle import update
from telegram.ext import Updater,CommandHandler

def welcome(update, context):
    message = 'Olá, ' + update.message.from_user.first_name + '!'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def comando2(update, context):
    message = 'problemas demais em '
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)



#main

def main():
    token = '5748916825:AAHlmxwXRFdwCkRBnJOW7C4HMuqt9pnKXYs'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start',welcome))#cria comando start e chama metodo welcome
    updater.dispatcher.add_handler(CommandHandler('2_comando',comando2))

    updater.start_polling()
    print('oi, eu sou o updater ' + str(updater))
    updater.idle()

if __name__ =="__main__":
    main()

