import logging
from telegram.ext import Application, MessageHandler, filters
import socket


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


async def answer(update, context):
    global port
    global ip
    await update.message.reply_text(f'http://{ip}:{port}')


if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    port = 5000
    application = Application.builder().token('7937526409:AAEuaGYvZ5il_vwTe4WXrfo7pAdL6XOF3XA').build()
    text_handler = MessageHandler(filters.TEXT, answer)
    application.add_handler(text_handler)
    application.run_polling()