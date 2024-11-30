from aiogram import Router, F
from aiogram.types import Message

# Foydalanuvchilar bilan ishlash uchun router
user_router = Router()

# Guruhlar bilan ishlash uchun router
group_router = Router()

@group_router.message(F.text == "salom")
async def group_message_handler(message: Message):
    await message.answer("Bu guruhdan kelgan xabar!")

# User xabarlarini qayta ishlash
@user_router.message(F.text == "xayr")
async def user_message_handler(message: Message):
    await message.answer("Bu foydalanuvchidan kelgan xabar!")

# Guruhdagi xabarlarni qayta ishlash
