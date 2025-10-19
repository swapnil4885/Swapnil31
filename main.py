from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 नमस्कार Swapnil! Bot चालू आहे 🚀")

# Any text message
async def reply_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📨 Swapnil, तुझा मेसेज मिळाला! (Sheet शी कनेक्शन नाही).")

def main():
    app = ApplicationBuilder().token("8306875717:AAG34WyLvyi9qvCzQ4mppqUpu3TweHSTrO4").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_msg))

    app.run_polling()

if __name__ == "__main__":
    main()
