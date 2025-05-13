import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
import socket
import csv
from random import randint


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)


async def answer(update, context):
    global port
    global ip
    global status
    global data
    global users
    global symbols
    global login
    global password
    global started
    if not started:
        started = True
        await update.message.reply_text(f'Введите логин и пароль в формате <логин> - <пароль>')
    if status == 'not loginned' and update.message.text == 'log':
        status = 'log'
        await update.message.reply_text(f'Введите логин и пароль в формате <логин> - <пароль>')
    elif status == 'log':
        login = update.message.text.split(' - ')[0]
        password = update.message.text.split(' - ')[1]
        b = True
        for i in data:
            if i[0] == login and password == i[1]:
                b = False
                status = 'logined'
                await update.message.reply_text(f'Вход выполнен!')
            else:
                status = 'not logined'
                await update.message.reply_text(f'Неверный логин или пароль! Введите команду log ещё раз.')
    elif status == 'not loginned' and update.message.text == 'reg':
        status = 'reg'
        login = symbols[randint(0, len(symbols) - 1)] + symbols[randint(0, len(symbols) - 1)] + symbols[randint(0, len(symbols) - 1)] + symbols[randint(0, len(symbols) - 1)]
        password = randint(1000, 9999)
        f = open('plantis.csv', 'w', newline='', encoding='utf8')
        writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['login', 'password', 'unlocked'])
        for i in data:
            writer.writerow(i)
        f.close()
        writer.writerow([login, password, ''])
        status = 'logined'
        await update.message.reply_text(f'Учётная запись создана!\nВаш логин: {login}\nВаш пароль: {password}')
    elif status == 'loginned' and update.message.text == '/play':
        await update.message.reply_text(f'Удачной игры! Перейдите по ссылке: http://{ip}:{port}')


if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    port = 5000
    application = Application.builder().token('7937526409:AAEuaGYvZ5il_vwTe4WXrfo7pAdL6XOF3XA').build()
    text_handler = MessageHandler(filters.TEXT, answer)
    application.add_handler(text_handler)
    status = 'not logined'
    reader = csv.reader(open('users.csv', encoding="utf8"), delimiter=',', quotechar='"')
    data = list(row for index, row in enumerate(reader) if index > 0)
    users = dict()
    started = False
    application.run_polling()
    symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
