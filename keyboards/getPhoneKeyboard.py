from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)
        ],
    ],
         resize_keyboard=True,

)