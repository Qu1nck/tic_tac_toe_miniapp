from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = '7552782372:AAEeX-8etzDiB1EPAfslGsqd1nvdAvc7H3w'  # Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего бота

# Функция для отправки ссылки на мини-приложение
async def start(update: Update, context) -> None:
    keyboard = [
        [InlineKeyboardButton("Играть в Крестики-Нолики", web_app=WebAppInfo(url="https://your-domain.com/webapp/index.html"))]  # Замените URL на ваш
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Нажмите кнопку, чтобы начать игру:", reply_markup=reply_markup)

# Основной запуск бота
def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == '__main__':
    main()
