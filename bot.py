from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler,CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove

STATEF = 0
STATE1 = 1
STATE2 = 2
STATE3 = 3

def welcome(update, context):
    try:
        firstName = update.message.from_user.first_name 
        message = 'Olá, ' + firstName + ', eu sou o Fousin, o bot curriculo de Anderson Carlos!'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except Exception as e:
        print(str(e))


def faq(update, context):
    message = '''  
            Meu curriculo\n
        1 - Informações Pessoais \n
        2 - Formação Acadêmica \n
        3 - Experiências Profissionais\n
        4 - Formações Complementares\n
        5 - Portifólio e Contato\n
        0 - voltar'''  
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
    return STATE1


def inputFaq(update, context): #state 1
    escolhaUsuario = (update.message.text).lower() #recebe o que o usuario digitar
    print(escolhaUsuario)#pra ver no console

    if (escolhaUsuario == '1' or escolhaUsuario == 'escolha 1' or escolhaUsuario == 'opcao 1'):
        message = '''ANDERSON CARLOS SALES DE JESUS\n
        19 ANOS, BRASILEIRO, SOLTEIRO\n
        ALAMEDA BONFIM, 17. PAU DA LIMA.\n
        CEP: 41245-020. SALVADOR - BA\n
        (71) 98205-8550\n
        ANDERSONCARLOS01@HOTMAIL.COM\n'''
        context.bot.send_message(chat_id=update.effective_chat.id, text=message) 
        return STATE1
    elif(escolhaUsuario == '2' or escolhaUsuario == 'escolha 2' or escolhaUsuario == 'opcao 2'):
        message = '''Faculdade Ruy Barbosa Wyden - (cursando 7º semestre)\n
        Ciência da Computação.\n'''
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE1
    elif(escolhaUsuario == '3' or escolhaUsuario == 'escolha 3' or escolhaUsuario == 'opcao 3'):
        message = '''\n
**Só chevrolet autopeças – 09/2019 a 09/2022\n
        Função: Auxiliar Administrativo\n\n
    **Centro de Distribuição Walmart – 03/2018 a 04/2019\n
        Função: Aprendiz Auxiliar Administrativo\n\n
    **Associação dos Moradores Colina Azul – 04/2017 a 05/2017\n
        Função: Auxiliar Administrativo (voluntário)\n
                    '''
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE1
    elif(escolhaUsuario == '4' or escolhaUsuario == 'escolha 4' or escolhaUsuario == 'opcao 4'):
        message = '''Desenvolvimento Web – Udemy\n
    Aprendizado sobre HTML5, CSS3, Bootstrap 4, JavaScript, ECMAScript, PHP 7 e Orientação a Objetos, Banco de dados MySQL, Ajax, PHP com PDO, JQuery (Em andamento)\n\n

        Segurança de redes - Cisco\n
    Descrever as ameaças de segurança, implementar o AAA no Roteadores Cisco, mitigar ameaças aos roteadores e redes Cisco usando ACLs.\n\n

        CCNAv7: Introdução às redes – Cisco\n
    Aprendizado sobre segurança de redes, protocolos das camadas, Configuração de roteadores e esquemas de endereçamento\n\n

        Cybersecurity Essentials - Cisco\n
    Aprendizado sobre segurança digital, princípios de confidencialidade, integridade e disponibilidade e a finalidade das leis relacionadas à segurança cibernética.\n\n

        OpenShift I: Containers & Kubernetes (DO180) - Red Hat\n
    Aprendizado sobre arquitetura de contêiners e OpenShift\n\n

        LPI Linux Essentials - Cisco\n
    Entender o funcionamento do sistema operacional Linux e suas funcionalidades\n\n

        Assistente de Controle de Qualidade – Senai 180h\n
    Aprendizado sobre custos relacionados aos processos como custos da qualidade, identificação de Normas Técnicas, Definições e termos relativos à qualidade.\n\n

        Aprendizagem comercial em Serviços Administrativos 1.080h\n
    Serviço Nacional de Aprendizagem Comercial – SENAC.\n\n

        Relações Interpessoais no Trabalho – SENAC 20 h\n
    Aprendizado sobre trabalho em equipe e comunicação em grupo.\n\n

        Liderança no varejo – Projeto Escola Social do Varejo 300 h\n
    Formação profissional para o varejo nas áreas de Desenvolvimento Pessoal e Social (DPS), Contexto das Relações do Varejo (CRV), Tecnologia da Informação e Comunicação (TIC).\n\n

        Habilidades Digitais para professores – Cresça com o Google 3 h\n
    Fundamentos de segurança e cidadania on-line e ferramentas e soluções digitais do Google para ser usado como suporte didático em aula.\n\n

        Marketing Digital – Cresça com o Google 3 h\n
    Conceitos de marketing digital como web sites, mídias sociais e analytics incluindo ferramentas e soluções digitais do Google.\n\n

        Informática Básica – Centro Caminho da Redenção 200 h\n
    Módulos de Microsoft Word, Microsoft Excel, Microsoft PowerPoint.\n
                    '''
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE1
    elif(escolhaUsuario == '5' or escolhaUsuario == 'escolha 5' or escolhaUsuario == 'opcao 5'):
        message = '''Portifólio: https://fousin.github.io/Apresentacao/projetos.html\n
        Instagram: https://www.instagram.com/f.ousin/\n
        Facebook: https://www.facebook.com/anderson.carlos.s.j\n
        Linkedin: https://www.linkedin.com/in/anderson-carlos-sales-30b684208/\n
                    '''
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE1
    elif(escolhaUsuario == '0' or escolhaUsuario == 'escolha 0' or escolhaUsuario == 'opcao 0'):
        message = "voltando"
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return faq(update, context)
    else:
        message = 'Opção Inválida' 
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)



def inputFim(update, context): #fim do bot
    #feedback = update.message.text
    message = "em breve um bot mais complexo"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return ConversationHandler.END

def meio():
    return STATE3
    

def cancel(update, context):
    return ConversationHandler.END
    

def main():

    token = '5748916825:AAHlmxwXRFdwCkRBnJOW7C4HMuqt9pnKXYs'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))
        
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('FAQ', faq)],
        states={
            STATE1: [MessageHandler(Filters.text, inputFaq)],
            STATE2: [MessageHandler(Filters.text, meio)],
            STATEF: [MessageHandler(Filters.text, inputFim)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)

    print("Updater no ar1: " + str(updater))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()