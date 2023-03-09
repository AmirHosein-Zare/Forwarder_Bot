from decouple import config
api_token = config("API_TOKEN")

from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, filters

updater = Updater(api_token)
dispatcher = updater.dispatcher

# replace with the chatID of the user group/channel you want to forward message to
FORWARD_TO_CHAT_ID = 'your_chat_id_here'

def forwarder_message(update: Update, context: CallbackContext):
    message = update.message
    chat_id = update.message.chat_id

    # forward the message
    forwarded_message = message.forward(FORWARD_TO_CHAT_ID)

updater.start_polling()