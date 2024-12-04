from aiogram import Router, F
from aiogram.types import Message, ChatPermissions
from filters.group import GroupFilter
from aiogram.filters import and_f
from datetime import datetime, timedelta
import asyncio

group_router = Router()

# Guruhga kirdi chiqdilarni filtirlash uchun biz quydagicha codelardan foydalana

@group_router.message(and_f(GroupFilter(), F.new_chat_members))
async def get_new_chat(message: Message):
    for new_chat in message.new_chat_members:
        await message.answer(f"Assalomu alaykum guruhga xush kelibsiz {new_chat.full_name}")
        await message.delete()


@group_router.message(and_f(GroupFilter(), F.left_chat_member ))
async def get_left_chat(message: Message):
    await message.answer(f"Xayr bro {message.left_chat_member.full_name}")

# Guruhda obunachilarni haydash va taklif ilovaga ruhsat berish

@group_router.message(GroupFilter(),and_f(F.text == "ban", F.reply_to_message))
async def get_bann_chat(message: Message):
   user_id = message.reply_to_message.from_user.id
   await message.chat.ban_sender_chat(user_id)
   await message.answer(f"Siz guruhdan haydaldingiz\n ❌ {message.reply_to_message.from_user.full_name}")



@group_router.message(GroupFilter(), and_f(F.text == "unban", F.reply_to_message))
async def get_unbann_chat(message: Message):
   user_id = message.reply_to_message.from_user.id
   await message.chat.unban_sender_chat(user_id)
   await message.answer(f"Siz endi guruhga qo'shila olasiz\n 🆗 {message.reply_to_message.from_user.full_name}")


# Guruhdagi obunachilar yozish yoki yozmaslik xuquqlarini boshqarish

# @group_router.message(GroupFilter(), and_f(F.text == "yozma", F.reply_to_message))
# async def get_banned_chat(message: Message): 
#    user_id = message.reply_to_message.from_user.id
#    permsions = ChatPermissions(can_send_messages=False)
#    await message.chat.restrict(user_id, permsions)
#    await message.answer(f"Siz notog'ri so'zdan foydlaandizngiz\n🚫 {message.reply_to_message.from_user.full_name}")


@group_router.message(GroupFilter(), and_f(F.text == "yozma", F.reply_to_message))
async def get_banned_chat(message: Message): 
    user_id = message.reply_to_message.from_user.id
    # vaqt bilan yozishni taqiqlash
    until_date = datetime.now() + timedelta(minutes=1)
    permissions = ChatPermissions(can_send_messages=False)
    await message.chat.restrict(user_id, permissions, until_date=until_date)
    await message.answer(
        f"Siz notog'ri so'zdan foydalandingiz\n🚫 {message.reply_to_message.from_user.full_name}\n")

@group_router.message(GroupFilter(),and_f(F.text == "yoz", F.reply_to_message))
async def get_not_ban_chat(message: Message):
   user_id = message.reply_to_message.from_user.id
   permsions = ChatPermissions(can_send_messages=True)
   await message.chat.restrict(user_id, permsions)
   await message.answer(f"Siz endi yoza olasiz\n🆗 {message.reply_to_message.from_user.full_name}")





