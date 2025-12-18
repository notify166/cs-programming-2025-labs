from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await update.message.reply_text("Привет! Я твой первый бот!")

app = ApplicationBuilder().token("8512856664:AAGO249BDQnDqV-s0IYfTbVMAQiE_aXcu1Y").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
