import asyncio
import logging

from aiogram import Bot, Dispatcher
from environs import Env

from handlers.user.text import router as user_text_router

# aiogram, environs, bs4, aiohttp


env = Env()
env.read_env('.env')


BOT_TOKEN = env.str('BOT_TOKEN')
ADMIN_CHAT_ID = env.int('ADMIN_CHAT_ID')


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=BOT_TOKEN)

    dp = Dispatcher()
    dp.include_router(user_text_router)

    await dp.start_polling(bot)


asyncio.run(main())
