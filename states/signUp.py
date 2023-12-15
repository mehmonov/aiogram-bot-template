from aiogram.fsm.state import State, StatesGroup


class signup(StatesGroup):
    fullname = State()
    phone_number = State()
    location =  State()