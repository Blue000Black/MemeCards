# pip install python-telegram-bot[ext] --upgrade
# pip install logging
# pip install config
import subprocess

if __name__ == "__main__":
    subprocess.run("server.py", shell=True)
    subprocess.run("bot.py", shell=True)
