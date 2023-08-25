from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

TOKEN = "6372799289:AAHNFkVjfCBvllvQE7p8U4sdHpSl2wgge2I"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
users = {}

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = request.get_json()
    chat_id = update['message']['chat']['id']
    text = update['message']['text']

    if text == '/comecar':
        users[chat_id] = {'state': 'ASK_NAME'}
        response = "Bem-vindo ao zapCORRETOR! Qual é o seu nome?"
    elif chat_id in users:
        if users[chat_id]['state'] == 'ASK_NAME':
            users[chat_id]['name'] = text
            users[chat_id]['state'] = 'ASK_CITY'
            response = f"Obrigado, {text}! Em qual cidade ou região você está mais interessado?"
        elif users[chat_id]['state'] == 'ASK_CITY':
            users[chat_id]['city'] = text
            users[chat_id]['state'] = 'ASK_PROPERTY_TYPE'
            response = "Perfeito! Você se especializa em que tipo de propriedade? (Residencial, Comercial, etc.)"
        elif users[chat_id]['state'] == 'ASK_PROPERTY_TYPE':
            users[chat_id]['property_type'] = text
            users[chat_id]['state'] = 'COMPLETED'
            response = f"Obrigado por fornecer as informações, {users[chat_id]['name']}! Agora você pode começar a listar ou buscar propriedades."
        else:
            response = "Como posso ajudar você hoje?"
    else:
        response = "Como posso ajudar você hoje?"
        
    send_message(chat_id, response)
    return jsonify(success=True)

def send_message(chat_id, text):
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(TELEGRAM_URL, data=payload)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
