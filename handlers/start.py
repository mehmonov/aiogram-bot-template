from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import  FSMContext
from states.signUp import signup


from states.menuState import menuState
from keyboards.menuKeyboard import menu


from loader import db
start_router: Router = Router()

@start_router.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    user_id = message.from_user.id
   
    user = await db.get_user_by_id(user_id=user_id)

    if  user:
        await message.answer("Salom, keling ro'yhatdan o'tamiz ")
        await message.answer("Iltimos ismingizni kiriting ")
        
        await state.set_state(signup.fullname)

    else:
        await message.answer("Siz allaqachon ro'yhatdan o'tdingiz", reply_markup=menu)
      
        await db.add_product(
            name="mahsulot 3",
            price="100",
            amount="22",
            type="oziq-ovqat",
            category="sabzavotlar",
            image='None'
        )
        # await db.delete_all_products()

        await state.set_state(menuState.menu)
