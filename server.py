from flask import *
import os
from random import randint
import socket


if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    port = 8080
    app = Flask(__name__)
    memes = list(name for name in os.listdir('static/img'))
    meme = memes[randint(0, len(memes) - 1)]
    print(meme)
    style = open('static/css/style.css', 'r').read()
    @app.route('/', methods=['POST', 'GET'])
    def index():
        global meme
        global memes
        if request.method == 'GET':
            return f"""<!doctype html>
                        <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>MemeCards</title>
                            </head>
                            <body>
                                <form method="post">
                                <h1>MemeCards</h1>
                                <img src="{url_for('static', filename='img/' + meme)}">
                                <br></br>
                                <button class="update" type="submit">Новая картинка<button>
                                </form>
                            </body>
                            <style>
                                {style}
                            <style>
                        </html>"""
        if request.method == 'POST':
            meme = memes[randint(0, len(memes) - 1)]
            return f"""<!doctype html>
                       <html lang="en">
                           <head>
                               <meta charset="utf-8">
                               <title>MemeCards</title>
                           </head>
                           <body>
                               <form method="post">
                               <h1>MemeCards</h1>
                               <img src="{url_for('static', filename='img/' + meme)}">
                               <br></br>
                               <button class="update" type="submit">Новая картинка<button>
                               </form>
                           </body>
                           <style>
                               {style}
                           <style>
                       </html>"""
    app.run(host=ip, port=port)
