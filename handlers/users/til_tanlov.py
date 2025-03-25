from aiogram import types
from keyboards.default.tugma2 import tugma2
from keyboards.default.tugma import tugma
from loader import dp


# Echo bot
@dp.message_handler(text='🇷🇺 Поменять язык')
async def bot_echo(message: types.Message):
    await message.answer(text='Добро пожаловать в бот Kwork',reply_markup=tugma2)

@dp.message_handler(text="🇺🇿 Tilni o'zgartirish")
async def bot_echo(message: types.Message):
    await message.answer(text='Kwork botiga xush kelibsiz',reply_markup=tugma)