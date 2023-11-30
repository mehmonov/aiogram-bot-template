from aiogram import Router
from aiogram.types import Message
from loader import db
import sqlite3
router: Router = Router()


@router.message()
async def process_any_message(message: Message):
    name =  message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except:
        await message.reply('avval bor')
        
    await message.reply(text=message.text)
