from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('👋 Welcome to Autopostbot! Use /search to find content or browse categories.')
