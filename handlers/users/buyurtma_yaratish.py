from aiogram import types
from aiogram.dispatcher import FSMContext
from states.steit import steit
from keyboards.default.soxa2 import soxa2,nomi
from keyboards.default.tugma import tugma
from keyboards.default.men_buyurtmachiman import men_buyurtmachiman
from states.buyurtma_yaratish_state import buyurtma_yaratish_state
from loader import dp,baza,bot

@dp.message_handler(state=buyurtma_yaratish_state.soxa,text='⬅️ Orqaga')
async def bot_echo(message: types.Message,state:FSMContext):
    await message.answer(text=message.text,reply_markup=men_buyurtmachiman)
    await steit.men_b.set()


@dp.message_handler(state=buyurtma_yaratish_state.soxa,text='/start')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(message.text,reply_markup=tugma)
    await state.finish()

@dp.message_handler(state=buyurtma_yaratish_state.soxa,text='🏠 Bosh Menyuga')
async def bot_echo(message: types.Message):
    await message.answer(text=message.text,reply_markup=tugma)

# Echo bot
from states.royxattan_otish import royxattan_otish

@dp.message_handler(state=buyurtma_yaratish_state.ism,text='⬅️ Orqaga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(message.text,reply_markup=soxa2)
    await buyurtma_yaratish_state.soxa()

@dp.message_handler(state=buyurtma_yaratish_state.ism,text='/start')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(message.text,reply_markup=tugma)
    await state.finish()

@dp.message_handler(state=buyurtma_yaratish_state.ism,text='🏠 Bosh Menyuga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(message.text,reply_markup=tugma)
    await state.finish()


''

@dp.message_handler(state=buyurtma_yaratish_state.xaqida,text='⬅️ Orqaga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(message.text,reply_markup=soxa2)
    await buyurtma_yaratish_state.ism.set()

@dp.message_handler(state=buyurtma_yaratish_state.xaqida,text='/start')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(message.text,reply_markup=tugma)
    await state.finish()

@dp.message_handler(state=buyurtma_yaratish_state.xaqida,text='🏠 Bosh Menyuga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(message.text,reply_markup=tugma)
    await state.finish()

@dp.message_handler(state=steit.men_b,text='📥 Buyurtma yaratish')
async def bot_echo(message: types.Message):
 await message.answer(text="Ro'yxatdan kategoriyalarni tanlang", reply_markup=soxa2)
#  if '📥 Buyurtma yaratish' in message.text:
#     print(yigindi + 1)
#     a = son + 1
#     print(a)
# royxat = [1]
# yigindi = 0
# for son in royxat:
#     yigindi = yigindi + son
#     print(yigindi)
#
# class salom(yigindi):


 await buyurtma_yaratish_state.soxa.set()


@dp.message_handler(state=buyurtma_yaratish_state.soxa)
async def bot_echo(message: types.Message,state:FSMContext):
    soxa=message.text
    await state.update_data({'soxa':soxa})
    await message.answer(text="Proyektning qisqacha nomini yozing.\nMisol uchun: Telegram bot, mebellar katalogi",reply_markup=nomi)
    await buyurtma_yaratish_state.ism.set()

@dp.message_handler(state=buyurtma_yaratish_state.ism)
async def bot_echo(message: types.Message,state:FSMContext):
    ism=message.text
    await state.update_data({'ism':ism})
    await message.answer(text="Proyektning qisqacha nomini, proyektning funksionalligini va \nqancha vaqt ichida proyektni bajarish mumkinligini yozing.\n\nAgar qandaydir qiynchiliklar yuzaga kelgan bo'lsa, administratorga\n @asilbek77738 yozing",reply_markup=nomi)
    await buyurtma_yaratish_state.xaqida.set()

@dp.message_handler(state=buyurtma_yaratish_state.xaqida)
async def bot_echo(message: types.Message, state: FSMContext):
    xaqida=message.text
    await state.update_data({'xaqida':xaqida})
    await message.answer(text="Proyektning narxini kiriting\nMisol uchun: 500000\n❗️Bizning maydonimizda eng kam narx 50000 sum",reply_markup=nomi)
    await buyurtma_yaratish_state.narx.set()

@dp.message_handler(state=buyurtma_yaratish_state.narx)
async def bot_echo(message: types.Message,state:FSMContext):
    narx=message.text
    await state.update_data({'narx':narx})
    maluotlar=await state.get_data()
    ism=maluotlar.get('ism')
    narx=maluotlar.get('narx')
    xaqida=maluotlar.get('xaqida')
    soxa=maluotlar.get('soxa')


    jonatish=f"Kategoriya: {soxa}\n" \
                 f"Proyektning nomi: {ism}\n" \
                 f"Proyektning ta'rifi: {xaqida}\n" \
                 f"Proyektning narxi: {narx} sum\n\n" \
                 f"Frilanserlar sizning buyurtmangizni ko'rishi uchun, ✅ Tasdiqlash tugmasini bosib buyurtmangizni tasdiqlang!"


    baza.buyurtma_yaratish(kategoriya=soxa,proekt_nomi=ism,proekt_tarifi=xaqida,proekt_narxi=narx,user_id=message.from_user.id)

    son = baza.buyurtma_raqami()
    for s in son:
     son=s
    jonatish = f"Buyurtma raqami # {son}\n" \
                   f"Kategoriya: {soxa}\n" \
                   f"Proyektning nomi: {ism}\n" \
                   f"Proyektning ta'rifi: {xaqida}\n" \
                   f"Proyektning narxi: {narx} sum\n\n" \
                   f"Frilanserlar sizning buyurtmangizni ko'rishi uchun, ✅ Tasdiqlash tugmasini bosib buyurtmangizni tasdiqlang!"
    await message.answer(text=jonatish,reply_markup=tugma)
    await state.finish()

#     await message.answer(f"Ismingiz va familiyangizni kiriting")
#     await royxattan_otish.ism.set()
#
# @dp.message_handler(state=royxattan_otish.ism)
# async def bot_start(message: types.Message, state:FSMContext):
#     ism=message.text
#     await state.update_data({'ism':ism})
#     await message.answer(f"Telefon raqamingizni kiriting",reply_markup=contact)
#     await royxattan_otish.telefon.set()
#
#
# @dp.message_handler(content_types='contact',state=royxattan_otish.telefon)
# async def bot_start(message: types.Message,state:FSMContext):
#
#     telefon=message.contact.phone_number
#     await state.update_data({'telefon':telefon})
#     await message.answer(f"Soxangizni Tanlang",reply_markup=soxa)
#     await royxattan_otish.soxa.set()
#
# @dp.message_handler(state=royxattan_otish.soxa)
# async def bot_start(message: types.Message, state:FSMContext):
#     soxa=message.text
#     await state.update_data({'soxa':soxa})
#     malumotlar=await state.get_data()
#     ism=malumotlar.get('ism')
#     telefon=malumotlar.get('telefon')
#     soxa=malumotlar.get('soxa')
#     jonatish=f"{ism},,{telefon},{soxa}"
#
#     try:
#         baza.royxattan_otish(ism=ism,telefon=telefon,soxa=soxa,tg_id=message.from_user.username)
#     except Exception  as s:
#         print(s)



