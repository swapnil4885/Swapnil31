import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import gspread
from google.oauth2.service_account import Credentials
from config import TELEGRAM_BOT_TOKEN, GOOGLE_SHEET_URL, SERVICE_ACCOUNT_FILE

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Google Sheets auth
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open_by_url(GOOGLE_SHEET_URL).sheet1

def start(update, context):
    update.message.reply_text("🚀 Swapnil Bot Live! Type your message and I’ll save it to Google Sheet.")

def save_message(update, context):
    user = update.message.from_user
    text = update.message.text
    sheet.append_row([user.username or user.first_name, text])
    update.message.reply_text("✅ Message saved in Google Sheet!")

def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, save_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
