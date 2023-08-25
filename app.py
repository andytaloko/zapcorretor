import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Temporary in-memory storage for the MVP
# In a production environment, you'd replace this with a proper database
users = {}

@app.route('/6372799289:AAHNFkVjfCBvllvQE7p8U4sdHpSl2wgge2I', methods=['POST'])
def webhook():
    update = request.get_json()
    chat_id = update['message']['chat']['id']
    text = update['message']['text']

    # User starts the bot
    if text == '/comecar':
        users[chat_id] = {'state': 'ASK_NAME'}
        response = "Bem-vindo ao zapCORRETOR! Qual é o seu nome?"
        
    # Handle different states
    elif chat_id in users:
        if users[chat_id]['state'] == 'ASK_NAME':
            users[chat_id]['name'] = text
            users[chat_id]['state'] = 'ASK_CITY'
            response = "Obrigado, {}! Em qual cidade ou região você está mais interessado?".format(text)
            
        elif users[chat_id]['state'] == 'ASK_CITY':
            users[chat_id]['city'] = text
            users[chat_id]['state'] = 'ASK_PROPERTY_TYPE'
            response = "Perfeito! Você se especializa em que tipo de propriedade? (Residencial, Comercial, etc.)"
            
        elif users[chat_id]['state'] == 'ASK_PROPERTY_TYPE':
            users[chat_id]['property_type'] = text
            users[chat_id]['state'] = 'COMPLETED'
            response = "Obrigado por fornecer as informações, {}! Agora você pode começar a listar ou buscar propriedades.".format(users[chat_id]['name'])
        else:
            response = "Como posso ajudar você hoje?"

    else:
        response = "Como posso ajudar você hoje?"
        
    # Send the response back to the user on Telegram
    # This is a simplified representation. You'd typically use the Telegram Bot API's sendMessage method.

    return jsonify(success=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
