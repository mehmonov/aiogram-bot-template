from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.geetProducts import create_product_buttons
from states.menuState import menuState
from keyboards.foodTypesKeyboard import create_food_category_buttons
from loader import bot, db
menu_router: Router = Router()

@menu_router.message(F.text == "Mahsulotlar", menuState.menu)
async def get_products(message: Message):
   
    types = ReplyKeyboardMarkup(
        keyboard=[
           [
                KeyboardButton(text="Oziq-ovqat"),
                KeyboardButton(text="Texnikalar")
           ]
        ],
        resize_keyboard=True
    ) 

    await message.answer("Menudan birini tanlang", reply_markup=types)

@menu_router.message(F.text == "Oziq-ovqat", menuState.menu)
async def get_food(message: Message):
    keyboard =  await create_food_category_buttons()

    await message.answer("Iltimos mahsulotlar turlarini tanlang", reply_markup=keyboard)

@menu_router.callback_query(lambda c: c.data and c.data.startswith('oziq_'), menuState.menu)

async def handle_category_callback(query: CallbackQuery):
    category = query.data[5:]  # bu yerda 'oziq_' prefiksini tashlab, qolgan qismni ushlab olamiz
    keyboard = await create_product_buttons(category, 'oziq-ovqat')  
    await bot.send_message(query.from_user.id, "Iltimos, mahsulotni tanlang:", reply_markup=keyboard)

@menu_router.callback_query(lambda c: c.data and c.data.startswith('product_'), menuState.menu)
async def handle_product_callback(query: CallbackQuery, state: FSMContext):
    product_id = int(query.data[8:])  # bu yerda 'product_' prefiksini tashlab, qolgan qismni ushlab olamiz
    product = await db.get_product_by_id(product_id) 

    if product['image'] != None  :  
        
        await bot.send_photo(query.from_user.id, photo=product['image'], caption=f"Mahsulot nomi: {product['name']}\nNarxi: {product['price']}\nTuri: {product['type']}\nKategoriyasi: {product['category']} \n Miqdori: {product['amount']}")

    else:  # aks holda, faqat matnni yuboramiz
        await bot.send_message(query.from_user.id, f"Mahsulot nomi: {product['name']}\nNarxi: {product['price']}\nTuri: {product['type']}\nKategoriyasi: {product['category']} \n Miqdori: {product['amount']}")