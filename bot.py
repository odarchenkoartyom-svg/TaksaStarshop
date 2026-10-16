import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "⭐ Добро пожаловать в Taksa starshop!\n\n"
        "🛍 Магазин готовится к запуску.\n"
        "📦 Каталог скоро появится!\n"
        "💬 По вопросам обращайтесь к администратору."
    )

bot.infinity_polling()
