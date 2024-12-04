from aiogram import Router, F
from aiogram.types import Message
from filters.group import GroupFilter
from guruhlar.inspection import group_router


@group_router.message(F.text=="salom", GroupFilter())
async def get_guruh(message: Message):
    await message.answer(f"{message.chat.title}\n{message.chat.type}\n{message.chat.id}")