
from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.panel import menu_buttons
from keyboards.inline.panel import panell, panell2
from loader import dp, baza, bot
from states.steit import tugma_yaratish

@dp.message_handler(text='/panel')
async def bot_echo(message: types.Message):
    await message.answer(text='Tanlang',reply_markup=panell)

# Echo bot
@dp.callback_query_handler(text='tugma')
async def bot_echo(message: types.callback_query):

    await bot.send_message(chat_id=message.from_user.id,text='Tanlang',reply_markup=panell2)

@dp.callback_query_handler(text='Tugma qoshish')
async def bot_echo(message: types.callback_query):
    await message.message.answer(text='Tugmani ismini kiriting')

    await tugma_yaratish.ism.set()

@dp.message_handler(state=tugma_yaratish)
async def bot_echo(message: types.Message,state:FSMContext):
    await state.update_data({'ism':message.text})
    malumot=await state.get_data()
    ism=malumot.get('ism')
    print(ism)
    baza.tugma_yaratish(ism=ism)
    await message.answer(text='Tugma qoshildi')
    await message.answer(text='Tanlang',reply_markup=panell)

@dp.callback_query_handler(text='Tugma ochirish')
async def bot_echo(message: types.callback_query):
    await message.message.answer(text='Tanlang',reply_markup=menu_buttons)
    await tugma_yaratish.ism.set()

@dp.callback_query_handler(state=tugma_yaratish)
async def bot_echo(message: types.callback_query, state: FSMContext):
        await state.update_data({'ism': message.message.text})
        malumot = await state.get_data()
        ism = malumot.get('ism')
        print(ism)
        baza.delete_userss(ism=ism)
        await message.answer(text="Tugma o'chirildi")
        await message.answer(text='Tanlang', reply_markup=panell)



@dp.callback_query_handler(text='tugma chiqishi')
async def bot_echo(message: types.callback_query):
    await message.message.answer(text='tanlang',reply_markup=menu_buttons)
