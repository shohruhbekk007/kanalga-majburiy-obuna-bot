from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand

from guruhlar.main import user_router, group_router
# Bot token
BOT_TOKEN = "7720505731:AAHke1ybIGrc3nhCIDHo4wx0ZF4gEwSDMQM"

# Bot va Dispatcher yaratish
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Routerlarni birlashtirish
dp.include_router(user_router)
dp.include_router(group_router)

# Asosiy ishga tushirish funksiyasi
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
