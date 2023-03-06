import telebot

CHAVE_API = "5825409100:AAEGyA1XeJQPddg2EvqP1u4mv0DPW3GYFJQ"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["iphone11"])
def iphone11(mensagem):
    bot.send_message(mensagem.chat.id, "Seu Iphone 11 está saindo para entrega! Previsão de entrega em sua casa dia 11/02")

@bot.message_handler(commands=["iphone13"])
def iphone13(mensagem):
    bot.send_message(mensagem.chat.id, "Seu Iphone 13 está saindo para entrega! Previsão de entrega em sua casa dia 19/02")

@bot.message_handler(commands=["iphone14"])
def iphone14(mensagem):
    bot.send_message(mensagem.chat.id, "Seu Iphone 14 Pro Max está saindo para entrega! Previsão de entrega em sua casa dia 28/02")


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto="""
    O que você quer? (Clique em uma opção)
    /iphone11 Iphone 11
    /iphone13 Iphone 13
    /iphone14 Iphone 14 Pro Max
    """
    bot.send_message(mensagem.chat.id, texto)
@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "Pronto, confirmando a chegada do pedido")
@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "Muito bom o produto, nota 10")




def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
  texto = """
  Escolha uma opção para continuar (Clique no item):
  /opcao1 Fazer um pedido
  /opcao2 Confirmar o pedido
  /opcao3 Mandar um feedback do pedido
  Responder qualquer outra coisa não vai funcionar, clique em uma das opções
  """
  bot.reply_to(mensagem, texto)

bot.polling()
