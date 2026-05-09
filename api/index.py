import os
import telebot
from flask import Flask, request

# Configurações do Mestre
TOKEN = "8765826139:AAGtcXbU8uFWRr6ENdaskMzvezpcir1ZHo4"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Mensagem de Sequestro Cognitivo
WELCOME_TEXT = (
    "O sistema identificou o teu rastro. O Protocolo está activo. ♟️\n\n"
    "Não foi inteligência, foi acesso. Parei de lutar contra o semestre quando "
    "percebi que o Modo Proibido já estava lá, à espera de ser activado.\n\n"
    "🔓 **ACEDER AO PROTOCOLO:** [LINK_DA_TUA_PAGINA_NETLIFY]"
)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, WELCOME_TEXT, parse_mode="Markdown")

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    # A URL abaixo será gerada pela Vercel após o deploy
    # bot.set_webhook(url='https://TEU-PROJETO.vercel.app/' + TOKEN)
    return "Protocolo Ativo", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
