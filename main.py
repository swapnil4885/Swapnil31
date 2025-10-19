from flask import Flask, request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import os

TOKEN = os.getenv(8306875717:AAG34WyLvyi9qvCzQ4mppqUpu3TweHSTrO4)
APP_URL = os.getenv(https://swapnil31-4.onrender.com)

app = Flask(__name__)

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("नमस्कार Swapnil! तुझा bot चालू आहे 🚀")

dispatcher.add_handler(CommandHandler("start", start))

@app.route(f'/{TOKEN}', methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), updater.bot)
    updater.dispatcher.process_update(update)
    return 'ok'

@app.route('/')
def index():
    return "Bot is running!"

if __name__ == '__main__':
    updater.bot.setWebhook(f"{APP_URL}/{TOKEN}")
    app.run(host='0.0.0.0', port=5000)
