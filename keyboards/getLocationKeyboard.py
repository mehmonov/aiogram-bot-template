from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Manzilni yuborish", request_location=True)
        ]
    ],
            resize_keyboard=True,

)