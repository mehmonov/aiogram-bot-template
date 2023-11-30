from aiogram import Bot

from config import Config, load_config
from models.sqlite import Database
config: Config = load_config()

bot: Bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
db = Database(path_to_db="main.db")