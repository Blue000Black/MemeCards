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
    global status
    if status == 'not logined':
        await update.message.reply_text('Введите логин и пароль в формате <логин> - <пароль>, чтобы войти, или команду /reg, чтобы зарегистрироваться')
    elif status == 'loginned':
        await update.message.reply_text(f'http://{ip}:{port}')
    await update.message.reply_text(f'http://{ip}:{port}')


if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    port = 5000
    application = Application.builder().token('7937526409:AAEuaGYvZ5il_vwTe4WXrfo7pAdL6XOF3XA').build()
    text_handler = MessageHandler(filters.TEXT, answer)
    application.add_handler(text_handler)
    status = 'not logined'
    application.run_polling()
