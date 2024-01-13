from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import db
async def create_product_buttons( category, type):
    
    products = await db.get_products_by_category_and_type(category, type)
    
    buttons = [[InlineKeyboardButton(text=product['name'], callback_data=f"product_{product['id']}")] for product in products]
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
