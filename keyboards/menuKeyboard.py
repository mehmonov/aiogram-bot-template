from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mahsulotlar")
        ],
        [
            KeyboardButton(text="Yordam"),
            KeyboardButton(text="Profil"),

        ]

    ],
    resize_keyboard=True
)