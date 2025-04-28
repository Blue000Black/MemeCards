# pip install python-telegram-bot[ext] --upgrade
# pip install logging
# pip install config
import logging
from telegram.ext import Application, MessageHandler, filters
from random import randint


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)
async def answer(update, context):
    answers = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7'
    ]
    await update.message.reply_text(answers[randint(0, len(answers) - 1)])


def main():
    application = Application.builder().token('7937526409:AAEuaGYvZ5il_vwTe4WXrfo7pAdL6XOF3XA').build()
    text_handler = MessageHandler(filters.TEXT, answer)
    application.add_handler(text_handler)
    application.run_polling()


if __name__ == '__main__':
    main()
