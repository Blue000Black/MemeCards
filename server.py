from flask import Flask, url_for
import os
from random import randint
import socket


if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    port = 5000
    app = Flask(__name__)
    memes = list(name for name in os.listdir('static/img'))
    meme = memes[randint(0, len(memes))]
    print(meme)
    style = open('static/css/style.css', 'r').read()
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
                        <img src="{url_for('static', filename='img/' + meme)}">
                      </body>
                    <style>
                    {style}
                    <style>
                    </html>"""
    app.run(host=ip, port=port)