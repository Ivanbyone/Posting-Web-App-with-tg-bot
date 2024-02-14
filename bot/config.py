import os

from dotenv import load_dotenv
from pathlib import Path
from aiogram import Bot, Dispatcher

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN, parse_mode="html")
dp = Dispatcher()
