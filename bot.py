from importlib.metadata import entry_points
from turtle import update
import sys
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

STATE1 = 1
STATE2 = 2

def welcome(update, context):
    message = 'Olá, ' + update.message.from_user.first_name + ', escolha uma opção.'
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def faq(update, context):
    message = '''texto aleatorio onde você substitui por algo referente ao seu serviço e etc?\n
        1 - TODO Botao A \n
        2 - TODO Botao B \n'''
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True))
    return STATE1

def inputFaq1(update, context):
    escolhaUsuario = (update.message.text).lower() #recebe o que o usuario digitar
    print(escolhaUsuario)#pra ver no console
    
    if (escolhaUsuario == '1' or escolhaUsuario == 'escolha 1' or escolhaUsuario == 'opcao 1'):
        message = "https://fousin.github.io/Apresentacao/index.html"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
    elif (escolhaUsuario == '2' or escolhaUsuario == 'escolha 2' or escolhaUsuario == 'opcao 2'):
        message = "https://www.instagram.com/f.ousin/"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
    

def inputFim(update, context):
    #feedback = update.message.text
    message = "em breve um bot mais complexo"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def cancel(update, context):
    return ConversationHandler.END

def main():
    token = '5748916825:AAHlmxwXRFdwCkRBnJOW7C4HMuqt9pnKXYs'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome)) #cria comando start e chama metodo welcome
    
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('FAQ', faq)], #estado' 0
        states ={
            STATE1: [MessageHandler(Filters.text, inputFaq1)],
            STATE2: [MessageHandler(Filters.text, inputFim)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)

    
    updater.start_polling()
    print('oi, eu sou o updater ' + str(updater))
    updater.idle()

if __name__ == "__main__":
    main()
