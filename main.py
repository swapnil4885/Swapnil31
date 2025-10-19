import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# लॉगिंग सुरू करतो
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# /start कमांड
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 नमस्कार Swapnil! मी तुझा बोट चालू आहे ✅")

# साधा text message
async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📩 मेसेज मिळाला! धन्यवाद 🙏")

# मुख्य फंक्शन
def main():
    app = ApplicationBuilder().token("8306875717:AAG34WyLvyi9qvCzQ4mppqUpu3TweHSTrO4").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_message))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
