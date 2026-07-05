from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = ' '.join(context.args)
    if not query:
        await update.message.reply_text('Usage: /search <title>')
        return
    await update.message.reply_text(f'🔎 Searching for: {query}\n(Search engine integration coming next.)')
