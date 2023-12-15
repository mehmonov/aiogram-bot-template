from aiogram import Router, F
from aiogram.types import Message, chat_member_updated
from aiogram.types.chat_member import ChatMember

router: Router = Router()





@router.message()
async def process_any_message(message: Message):
    await message.reply("Iltimos faqatgina menudan foydanalaning")

