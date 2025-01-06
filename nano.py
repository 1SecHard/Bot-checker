# Telegram Bot Example

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Your Bot Token
TOKEN = "8119310975:AAG6Ll6eUqG_mb1ZwcEnv6_XImlfqtTvqgY"

# Function: /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! This is your bot. Use /help to see what I can do.")

# Function: /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Here are the available commands:\n"
        "- /start: Start the bot\n"
        "- /help: Display this help message\n"
        "- Send any log or text to process"
    )

# Function: Handle messages (log checker)
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log_text = update.message.text
    await update.message.reply_text(f"Your log:\n{log_text}\n\nResult: No issues found!")

# Main function to run the bot
if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()