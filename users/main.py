from aiogram import Router, F
from aiogram.types import Message
from filters.users import UserPrivateFilter

user_router = Router()



@user_router.message(UserPrivateFilter(), F.text == "xayr")
async def BotStart(message: Message):
    await message.answer(f"Bot exo {message.text}")

