import telebot

# Crea una instancia del bot con tu token de API de Telegram
bot_token = input('Introduce tu token de API de Telegram: ')
bot = telebot.TeleBot(bot_token)

# Código para responder al mensaje /help
@bot.message_handler(commands=['help'])
def send_help(message):
    # Envía un mensaje de ayuda al usuario
    bot.reply_to(message, "¡Hola! Soy utn bot de ayuda. ¿En qué puedo ayudarte?")


# Código para responder a cualquier otro mensaje
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Responde al mensaje del usuario
    bot.reply_to(message, "¡Hola! Soy un bot y estoy aquí para ayudarte.")

# Inicia el bot
bot.polling()
