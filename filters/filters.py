from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery



class IsGroup(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == 'supergroup'
    
    
class IsPrivate(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == 'private'
