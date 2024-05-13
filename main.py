import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher

from handlers import router

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

async def main() -> None:
    bot = Bot(token=TOKEN)
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
