from aiogram import Bot

from config import Config, load_config

config: Config = load_config()

bot: Bot = Bot(token=config.tg_bot.token, parse_mode="HTML")