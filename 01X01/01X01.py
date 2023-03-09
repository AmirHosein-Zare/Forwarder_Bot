from decouple import config
api_token = config("API_TOKEN")

from telegram import Update
from telegram.ext import Updater, CallbackContext, MessageHandler, filters

updater = Updater(api_token)
dispatcher = updater.dispatcher



updater.start_polling()