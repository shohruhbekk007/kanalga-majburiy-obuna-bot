from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand
from data.config import token
from guruhlar.main import group_router
from users.main import user_router
from guruhlar.inspection import group_router

BOT_TOKEN = token

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(user_router)
dp.include_router(group_router)

# Asosiy ishga tushirish funksiyasi
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
