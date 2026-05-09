import os
import json
from flask import Flask, request, Response

TOKEN = os.getenv('BOT_TOKEN')
app = Flask(__name__)

WELCOME_TEXT = (
    "O sistema identificou o teu rastro. O Protocolo está activo. ♟️\n\n"
    "Não foi inteligência, foi acesso. Parei de lutar contra o semestre quando "
    "percebi que o Modo Proibido já estava lá, à espera de ser activado.\n\n"
    "👇 **ACEDER AO PROTOCOLO:**\n"
    "https://modo-proibido-2026.netlify.app/"
)

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    try:
        data = json.loads(request.data)
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        
        if text == '/start':
            # Envia resposta via API diretamente
            import requests
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": WELCOME_TEXT,
                "parse_mode": "Markdown"
            }
            requests.post(url, json=payload)
        
        return Response("OK", status=200)
    except Exception as e:
        return Response(str(e), status=200)

@app.route('/')
def index():
    return "Protocolo Modo Proibido - Ativo", 200
