from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from keyboards.default.tugma import tugma
from states.steit import *
from states.buyurtma_yaratish_state import *
from states.taklif_kiritish import *
from states.royxattan_otish import *


from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=steit.buyurtma_topish,text='⬅️ Orqaga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(message.text,reply_markup=tugma)
    await state.finish()

@dp.message_handler(state=steit.buyurtma_topish,text='/start')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(message.text,reply_markup=tugma)
    await state.finish()




@dp.message_handler(state=buyurtma_yaratish_state.ism,text='⬅️ Orqaga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(message.text,reply_markup=tugma)
    await state.finish()

@dp.message_handler(state=buyurtma_yaratish_state.ism,text='/start')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(message.text,reply_markup=tugma)
    await state.finish()



