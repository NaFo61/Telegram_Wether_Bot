import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
RapidAPI_Key_TOKEN = os.getenv("RapidAPI_Key_TOKEN")
RapidAPI_Host_TOKEN = os.getenv("RapidAPI_Host_TOKEN")

