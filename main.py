# pip install python-telegram-bot[ext] --upgrade
# pip install logging
# pip install config
import logging
from telegram.ext import Application, MessageHandler, filters
from flask import Flask
import os
from random import randint
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
    app = Flask(__name__)
    memes = list(name for name in os.listdir(os.getcwd() + '/imgs'))
    meme = memes[randint(0, len(memes))]
    style = open('style.css', 'r').read()
    @app.route('/')
    def index():
        return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>MemeCards</title>
                      </head>
                      <body>
                        <h1>MemeCards</h1>
                        <img src="imgs/{meme}">
                      </body>
                    <style>
                    {style}
                    <style>
                    </html>"""
    app.run(host=ip, port=port)
    application = Application.builder().token('7937526409:AAEuaGYvZ5il_vwTe4WXrfo7pAdL6XOF3XA').build()
    text_handler = MessageHandler(filters.TEXT, answer)
    application.add_handler(text_handler)
    application.run_polling()
