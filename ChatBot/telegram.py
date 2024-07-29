import telebot

api_key =  ''
bot = telebot.TeleBot(api_key)


# OPÇÕES
@bot.message_handler(commands=['opcao1'])
def opcao1(msg):
    bot.send_message(msg.chat.id, 'opção 1 selecionada')

@bot.message_handler(commands=['opcao2'])
def opcao2(msg):
    bot.reply_to(msg, 'opção 2 selecionada')
    
@bot.message_handler(commands=['opcao3'])
def opcao3(msg):
    print(msg)
    bot.reply_to(msg, 'opção 3 selecionada')
    
    
    
# MENSAGEM PADRÃO
def verificar(msg):
    return True

@bot.message_handler(func=verificar)
def responder(msg):
    texto = """
Escolha uma opção para continuar (Clique no item):
    /opcao1 A
    /opcao2 B
    /opcao3 C
Responder qualquer outra coisa não vai funcionar, clique em uma das opções.
    """
    bot.reply_to(msg, texto)

bot.polling()