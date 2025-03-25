# import turtle
# import colorsys
# t=turtle.Turtle()
# turtle.Screen()
# s=turtle.bgcolor('black')
#
# n=150
# h=0
# turtle.left(180)
#
# for son in range(360):
#     c=colorsys.hsv_to_rgb(h,1,0.8)
#     h+=1/n
#     t.color(c)
#     t.left(144)
#     t.forward(son*5)
#     turtle.speed(90)
# turtle.mainloop()
# import datetime
#
from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentTypes

from keyboards.default.boshi import boshi
from keyboards.default.contact import contact
from keyboards.default.nastroyka import nastroyka
from states import xammasi
from states.ism_ozgartirish import ism
from states.steit import steit, steit2
from loader import dp,baza

#
#
# @dp.message_handler(state=steit.men_f,text="Ismni o'zgartirish")
# async def bot_echo(message: types.Message, state:FSMContext):
#     await message.answer(text='Familiya Ismingizni kiriting')
#     await ism.ismi.set()
#
# @dp.message_handler(state=ism.ismi)
# async def bot_echo(message: types.Message, state:FSMContext):
#     ism=message.text
#     await state.update_data({'ism':ism})
#     malumot=await state.get_data()
#     ismi=malumot.get('ism')
#
#
#
#
#
#
#
#     qoshish=baza.royxattan_otish(ism=ismi,tg_id=message.from_user.id,soxa=3,telefon=4)
#
#     user_id = message.from_user.username
#     check = baza.kirish(ism.)
#     if check:
#
# @dp.message_handler(text='salom')
# async def bot_echo(message: types.Message):
#     vaqt = datetime.datetime.now()
#     if int(vaqt.hour) < 9:
#         print('salom')



@dp.message_handler(state=steit2.men_ish_b,text="Ismni o'zgartirish")
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Familiya Ismingizni kiriting')
    await ism.ismi.set()


@dp.message_handler(state=ism.ismi)
async def bot_echo(message: types.Message, state: FSMContext):
    ism = message.text
    await state.update_data({'ism': ism})
    malumot = await state.get_data()
    ismi = malumot.get('ism')


    oz=baza.update(tg_id=message.from_user.id,ism=ismi)
    await steit2.men_ish_b.set()


@dp.message_handler(state=steit2.men_ish_b,text="Raqamni o'zgartirish")
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer("Telefon raqamingizni Kiriting 📱:\nMasalan: +998907785435", reply_markup=contact)
    await ism.telefon.set()


@dp.message_handler(content_types=ContentTypes.CONTACT, state=ism.telefon)
async def bot_echo(message: types.Message, state: FSMContext):
    await state.update_data({'telefon': message.contact.phone_number})
    await ism.telefon.set()





@dp.message_handler(state=ism.telefon)
async def bot_echo(message: types.Message, state: FSMContext):
    telefon = message.text
    await state.update_data({'telefon': telefon})
    malumot = await state.get_data()
    ismi = malumot.get('telefon')

    oz = baza.update2(tg_id=message.from_user.id, telefon=ismi)
    await steit2.men_ish_b.set()


@dp.message_handler(state=steit2.men_ish_b,text="🏠 Bosh Menyuga")
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Tugmalardan birini tanlang', reply_markup=boshi)
    await state.finish()