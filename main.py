import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8768142893:AAE5EQUnEB5KhdJD3z9WIpZXUyL0yzrdizE"

IMAGE_URL = "https://share.google/images/dytCOr19tz2hhYYed"

TEXTE_1 = "🎰 Bienvenue sur le bot mystake !"
TEXTE_2 = "💰 As-tu déjà un compte sur Stake.com ?"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("✅ OUI", callback_data="oui"),
            InlineKeyboardButton("❌ NON", callback_data="non"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo=IMAGE_URL,
        caption=f"{TEXTE_1}\n\n{TEXTE_2}",
        reply_markup=reply_markup
    )

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "oui":
        await query.edit_message_caption(
            caption="✅ Super ! Tu as déjà un compte.\n\n👉 [À configurer plus tard]"
        )
    elif query.data == "non":
        await query.edit_message_caption(
            caption="❌ Pas encore de compte ?\n\n👉 [À configurer plus tard]"
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_response))

print("Bot démarré ✅")
app.run_polling()
