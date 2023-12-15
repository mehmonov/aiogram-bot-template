from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import  FSMContext
from states.signUp import signup

from states.menuState import menuState
from keyboards.menuKeyboard import menu

from keyboards.getPhoneKeyboard import btn
from keyboards.getLocationKeyboard import btn2
from utils.get_location import get_location_details
from loader import db
signup_router: Router = Router()

@signup_router.message(signup.fullname)
async def get_phone_number(message: Message, state: FSMContext ):
    await state.update_data(fullname=message.text)
    await state.set_state(signup.phone_number)
    await message.answer("Telefon raqamingizni kiriting", reply_markup=btn)
    
@signup_router.message(signup.phone_number)
async def get_location(message: Message, state: FSMContext ):
    await state.update_data(phone_number=message.contact.phone_number)
    await state.set_state(signup.location)

    await message.answer("Manzilni kiriting", reply_markup=btn2)
    
@signup_router.message(signup.location)
async def finish(message: Message, state: FSMContext):
    location = get_location_details(message.location.latitude, message.location.longitude)

    await state.update_data(location=location)

    datas = await state.get_data()

    fullname = datas['fullname']
    phone_number = datas['phone_number']
    location = datas['location']
    username = message.from_user.username
    telegram_id = message.from_user.id
    
    
    await state.clear()
    
    try:
        await db.add_user(
            full_name=fullname,
            username=username,
            telegram_id=telegram_id,
            location=location['full_address'],
            phone_number=phone_number
        )
        await message.answer("Tabriklaymiz! ro'yhatdan o'tdingiz", reply_markup=menu)
        
        await state.set_state(menuState.menu)

    except Exception as e:
        print(f"Xatolik turi: {type(e)}")
        print(f"Xatolik xabari: {e}")

        print(f"all users { await db.get_all_users() }")

   