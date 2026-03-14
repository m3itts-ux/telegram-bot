from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем токен бота из переменной окружения
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Функция для обработки команды /start
async def start(update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Я твой первый бот 🤖")

# Функция для обработки команды /help
async def help_command(update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Я пока умею немного, но скоро научусь большему!")

# Функция для обработки команды /about
async def about(update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Я бот созданный на Python. Умею отвечать на команды и скоро научусь большему!")

# Функция для обработки текстовых сообщений
async def handle_message(update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()
    if text == "привет":
        await update.message.reply_text("Привет! Напиши /help чтобы узнать что я умею")
    else:
        await update.message.reply_text("Я пока не понимаю эту команду. Попробуй /help")

def main() -> None:
    # Создаем приложение с токеном
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))

    # Добавляем обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()