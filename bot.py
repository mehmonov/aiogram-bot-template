import asyncio
import logging

from aiogram import  Dispatcher

from handlers.echo import router
from handlers.start import start_router
from handlers.sign_up import signup_router
from handlers.menu import menu_router
from loader import bot,  db

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
       
    )

    logger.info("Starting bot")


    dp: Dispatcher = Dispatcher()

    dp.include_routers(
        menu_router,
        signup_router, 
        start_router, 
        router
    )

    await db.create()
    await db.create_table_users()
    await db.create_table_products()

        
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
