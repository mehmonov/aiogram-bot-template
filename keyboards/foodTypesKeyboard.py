
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import db

async def create_food_category_buttons():

    categories = await db.get_distinct_food_categories()

    buttons = [[InlineKeyboardButton(text=category['category'], callback_data=f"oziq_{category['category']}")] for category in categories]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
   
    return keyboard