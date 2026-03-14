from telegram.ext import Application, CommandHandler, ContextTypes
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

def main() -> None:
    # Создаем приложение с токеном
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()