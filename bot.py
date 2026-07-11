import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🚀 Welcome to Crypto Creator AI V2

Available Commands:

/post - Generate crypto content
/image - AI image prompt
/hashtags - Trending hashtags
/calendar - 30-day content calendar
/help - Help
"""
    await update.message.reply_text(text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/post\n"
        "/image\n"
        "/hashtags\n"
        "/calendar"
    )

async def post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Sample Binance Square Post\n\n"
        "Bitcoin is testing a key resistance level.\n"
        "A breakout could trigger strong bullish momentum.\n\n"
        "DYOR before investing."
    )

async def image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Prompt:\n"
        "Futuristic Bitcoin city, glowing BTC logo, Binance black & gold theme, ultra realistic, cinematic lighting, 4K."
    )

async def hashtags(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "#Bitcoin #BTC #Crypto #Binance #Ethereum #BNB #Trading #Blockchain"
    )

async def calendar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "30-Day Content Plan\n\n"
        "Day 1 - BTC Analysis\n"
        "Day 2 - ETH Update\n"
        "Day 3 - Altcoin Watch\n"
        "Day 4 - Market News\n"
        "Day 5 - Meme\n"
        "..."
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("post", post))
    app.add_handler(CommandHandler("image", image))
    app.add_handler(CommandHandler("hashtags", hashtags))
    app.add_handler(CommandHandler("calendar", calendar))

    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
