from flask import *
import os
from random import randint

app = Flask(__name__)
memes = list(name for name in os.listdir(os.getcwd() + '/imgs'))
meme = memes[randint(0, len(memes))]
style = open('style.css', 'r').read()
print(*memes, end='\n')
print(meme)
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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
