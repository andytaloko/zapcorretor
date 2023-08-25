from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Updater, MessageHandler, Filters

# For logging
import logging
logging.basicConfig(level=logging.INFO)

# Replace 'YOUR_TOKEN' with your bot's token
TOKEN = "6372799289:AAHNFkVjfCBvllvQE7p8U4sdHpSl2wgge2I"
users = {}

def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    users[chat_id] = {'state': 'ASK_NAME'}
    update.message.reply_text('Bem-vindo ao zapCORRETOR! Qual é o seu nome?')

def handle_message(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    text = update.message.text

    # Handle different states
    if chat_id in users:
        if users[chat_id]['state'] == 'ASK_NAME':
            users[chat_id]['name'] = text
            users[chat_id]['state'] = 'ASK_CITY'
            update.message.reply_text(f"Obrigado, {text}! Em qual cidade ou região você está mais interessado?")
            
        elif users[chat_id]['state'] == 'ASK_CITY':
            users[chat_id]['city'] = text
            users[chat_id]['state'] = 'ASK_PROPERTY_TYPE'
            update.message.reply_text("Perfeito! Você se especializa em que tipo de propriedade? (Residencial, Comercial, etc.)")
            
        elif users[chat_id]['state'] == 'ASK_PROPERTY_TYPE':
            users[chat_id]['property_type'] = text
            users[chat_id]['state'] = 'COMPLETED'
            update.message.reply_text(f"Obrigado por fornecer as informações, {users[chat_id]['name']}! Agora você pode começar a listar ou buscar propriedades.")
        else:
            update.message.reply_text("Como posso ajudar você hoje?")
    else:
        update.message.reply_text("Como posso ajudar você hoje?")

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # You can set use_context=True to use the new context based callbacks
    # JobQueue requires context based callbacks
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
