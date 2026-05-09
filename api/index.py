import os
import telebot
from flask import Flask, request

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

WELCOME_TEXT = (
    "O sistema identificou o teu rastro. O Protocolo está activo. ♟️\n\n"
    "Não foi inteligência, foi acesso. Parei de lutar contra o semestre quando "
    "percebi que o Modo Proibido já estava lá, à espera de ser activado.\n\n"
    "👇 **ACEDER AO PROTOCOLO:**\n"
    "https://modo-proibido-2026.netlify.app/"
)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, WELCOME_TEXT, parse_mode="Markdown")

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@app.route('/')
def index():
    return "Protocolo Modo Proibido - Ativo", 200

# Só roda localmente, na Vercel usa webhook
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
