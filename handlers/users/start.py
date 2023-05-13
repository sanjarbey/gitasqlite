import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp, bot, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name=message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)
    await message.answer(f"Salom, {message.from_user.full_name}! botga xush kelibsiz")

    count=db.count_users()[0]
    msg=f"{message.from_user.full_name} bazaga qo'shildi hozirda bazada {count} foydalanuvchi bor "
    await bot.send_message(chat_id=ADMINS[0], text=msg)


@dp.message_handler(commands="yugur")
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! o'zing yugur men shu yerda turaman")