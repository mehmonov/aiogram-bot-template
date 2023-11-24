import asyncio
import logging

from aiogram import  Dispatcher

from handlers import echo
from loader import bot

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
       
    )

    logger.info("Starting bot")

  
    dp: Dispatcher = Dispatcher()

    dp.include_router(echo.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
