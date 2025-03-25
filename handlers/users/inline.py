from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import ContentTypes

from keyboards.default.boshi import boshi, boshi2
from keyboards.default.contact import contact
from keyboards.default.soxa2 import soxa2, nomi
from keyboards.default.tastiqlash import tastiqlash
from loader import dp,baza
from keyboards.default.men_buyurtmachiman import men_buyurtmachiman
from keyboards.inline.Taklif_kiritish import taklif
from states.steit import steit2
from keyboards.default.boshi import boshi
from states.xammasi import isb_ber
# Echo bot
from states import xammasi
'Bosh menyuga xush kelibsiz'
@dp.callback_query_handler(state=xammasi.isb_ber.state,text='⬅️ Orqaga')
async def bot_echo(message: types.callback_query, state:FSMContext):
    await message.message.answer(text='Tanlang',reply_markup=men_buyurtmachiman)
    await steit2.men_ish_b.set()
@dp.message_handler(state=steit2.men_ish_b,text='⬅️ Orqaga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bosh menyuga xush kelibsiz',reply_markup=boshi)
    await state.finish()

@dp.message_handler(state=steit2.men_ish_b,text='/start')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bosh menyuga xush kelibsiz',reply_markup=boshi)
    await state.finish()

@dp.message_handler(state=xammasi.isb_ber,text='/start')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bosh menyuga xush kelibsiz',reply_markup=boshi)
    await state.finish()



@dp.message_handler(state=xammasi.isb_ber.ism,text='/start')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bosh menyuga xush kelibsiz',reply_markup=boshi)
    await state.finish()

@dp.message_handler(state=xammasi.isb_ber.ism,text='⬅️ Orqaga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Kategoriyalardan birini tanlang 💼', reply_markup=taklif)
    await xammasi.isb_ber.state.set()

@dp.message_handler(state=xammasi.isb_ber.ism,text='🏠 Bosh Menyuga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bosh menyuga xush kelibsiz',reply_markup=boshi)
    await state.finish()

@dp.message_handler(state=xammasi.isb_ber.narx,text='/start')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bosh menyuga xush kelibsiz',reply_markup=boshi)
    await state.finish()

@dp.message_handler(state=xammasi.isb_ber.narx,text='⬅️ Orqaga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='    Ismingizni kiriting 👨🏻‍💻:\nMasalan: Asilbek', reply_markup=nomi)
    await xammasi.isb_ber.ism.set()

@dp.message_handler(state=xammasi.isb_ber.narx,text='🏠 Bosh Menyuga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bosh menyuga xush kelibsiz',reply_markup=boshi)
    await state.finish()



@dp.message_handler(state=xammasi.isb_ber.manzil,text='/start')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bosh menyuga xush kelibsiz',reply_markup=boshi)
    await state.finish()

@dp.message_handler(state=xammasi.isb_ber.manzil,text='⬅️ Orqaga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Ishning narxini kiriting 💰:\nMasalan:50000', reply_markup=nomi)
    await xammasi.isb_ber.narx.set()

@dp.message_handler(state=xammasi.isb_ber.manzil,text='🏠 Bosh Menyuga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bosh menyuga xush kelibsiz',reply_markup=boshi)
    await state.finish()


@dp.message_handler(state=xammasi.isb_ber.vaqt,text='/start')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bosh menyuga xush kelibsiz',reply_markup=boshi)
    await state.finish()

@dp.message_handler(state=xammasi.isb_ber.vaqt,text='⬅️ Orqaga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text="Ish manzilni kiriting 🇺🇿:\nMasalan: Marg'ilon", reply_markup=nomi)
    await xammasi.isb_ber.manzil.set()

@dp.message_handler(state=xammasi.isb_ber.vaqt,text='🏠 Bosh Menyuga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bosh menyuga xush kelibsiz',reply_markup=boshi)
    await state.finish()

''''''
@dp.message_handler(state=xammasi.isb_ber.telefon_Raqami,text='/start')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bosh menyuga xush kelibsiz',reply_markup=boshi)
    await state.finish()

@dp.message_handler(state=xammasi.isb_ber.telefon_Raqami,text='⬅️ Orqaga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Ish vaqtini kiriting 🕜:\nMasalan: 8:00 dan 20:00 gacha', reply_markup=nomi)
    await xammasi.isb_ber.vaqt.set()

@dp.message_handler(state=xammasi.isb_ber.telefon_Raqami,text='🏠 Bosh Menyuga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bosh menyuga xush kelibsiz',reply_markup=boshi)
    await state.finish()
''''''
@dp.message_handler(state=steit2.men_ish_b,text='📥 Buyurtma yaratish')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Kategoriyalardan birini tanlang 💼',reply_markup=taklif)
    await xammasi.isb_ber.state.set()


@dp.callback_query_handler(state=xammasi.isb_ber.state)
async def bot_echo(message: types.callback_query, state:FSMContext):
    kategoriya2=message.message.text
    print(kategoriya2)
    await state.update_data({'kategoriya':kategoriya2})


    await message.message.answer(text='Ismingizni kiriting 👨🏻‍💻:\nMasalan: Asilbek:',reply_markup=nomi)
    await xammasi.isb_ber.ism.set()

@dp.message_handler(state=xammasi.isb_ber.ism)
async def bot_echo(message: types.Message,state:FSMContext):
    await state.update_data({'ism':message.text})
    await message.answer(text='Ishning narxini kiriting 💰:\nMasalan:50000',reply_markup=nomi)

    await xammasi.isb_ber.narx.set()

@dp.message_handler(state=xammasi.isb_ber.narx)
async def bot_echo(message: types.Message,state:FSMContext):
    await state.update_data({'narx':message.text})
    await message.answer(text="Ish manzilni kiriting 🇺🇿:\nMasalan: Marg'ilon",reply_markup=nomi)

    await xammasi.isb_ber.manzil.set()

@dp.message_handler(state=xammasi.isb_ber.manzil)
async def bot_echo(message: types.Message,state:FSMContext):
    await state.update_data({'manzil':message.text})
    await message.answer(text='Ish vaqtini kiriting 🕜:\nMasalan: 8:00 dan 20:00 gacha',reply_markup=nomi)
    await xammasi.isb_ber.vaqt.set()


@dp.message_handler(state=xammasi.isb_ber.vaqt)
async def bot_echo(message: types.Message, state: FSMContext):
    await state.update_data({'vaqt':message.text})
    await message.answer("Telefon raqamingizni Kiriting 📱:\nMasalan: +998907785435",reply_markup=contact)
    await xammasi.isb_ber.telefon_Raqami.set()


@dp.message_handler(content_types=ContentTypes.CONTACT,state=xammasi.isb_ber.telefon_Raqami)
async def bot_echo(message: types.Message, state: FSMContext):
        await state.update_data({'telefon': message.contact.phone_number})
        malumot = await state.get_data()
        ism = malumot.get('ism')
        vaqt = malumot.get('vaqt')
        kategotiya = malumot.get('kategoriya')
        manzil = malumot.get('manzil')
        narx = malumot.get('narx')
        telefon = malumot.get('telefon')
        jonatish = f"Kategoriya💼: {kategotiya}\n\n" \
                   f"Ish vaqti🕜: {vaqt}\n\n" \
                   f"Manzil🇺🇿: {manzil}\n\n" \
                   f"Ish narxi💰: {narx}\n\n" \
                   f"Ish beruvchining ismi👨🏻‍💻: {ism}\n\n" \
                   f"Telefon📱: {telefon}"
        await message.answer(text=jonatish, reply_markup=tastiqlash)
        await xammasi.isb_ber.tasdiq.set()


@dp.message_handler(state=xammasi.isb_ber.tasdiq, text='Xa ✅')
async def bot_echo(message: types.Message, state: FSMContext):
    malumot = await state.get_data()
    ism = malumot.get('ism')
    vaqt = malumot.get('vaqt')
    kategotiya = malumot.get('kategoriya')
    manzil = malumot.get('manzil')
    narx = malumot.get('narx')
    telefon = malumot.get('telefon')
    baza.ish_berish(ismi=ism, vaqt=vaqt, kategoriya=kategotiya, manzil=manzil, narxi=narx, tg_id=message.from_user.id,
                    telefon_Raqami=telefon)
    await message.answer(text='Tanlang', reply_markup=boshi2)
    await steit2.men_ish_b.set()


@dp.message_handler(state=xammasi.isb_ber.tasdiq, text='Yoq ❌')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Bosh menyuga xush kelibsiz', reply_markup=boshi)
    await state.finish()


@dp.message_handler(state=xammasi.isb_ber.telefon_Raqami)
async def bot_echo(message: types.Message, state: FSMContext):
    await state.update_data({'telefon': message.text})
    malumot=await state.get_data()
    ism=malumot.get('ism')
    vaqt=malumot.get('vaqt')
    kategotiya=malumot.get('kategoriya')
    manzil=malumot.get('manzil')
    narx=malumot.get('narx')
    telefon=malumot.get('telefon')
    jonatish=f"Kategoriya💼: {kategotiya}\n\n" \
             f"Ish vaqti🕜: {vaqt}\n\n" \
             f"Manzil🇺🇿: {manzil}\n\n" \
             f"Ish narxi💰: {narx}\n\n" \
             f"Ish beruvchining ismi👨🏻‍💻: {ism}\n\n" \
             f"Telefon📱: {telefon}"
    await message.answer(text=jonatish,reply_markup=tastiqlash)
    await xammasi.isb_ber.tasdiq.set()

@dp.message_handler(state=xammasi.isb_ber.tasdiq,text='Xa ✅')
async def bot_echo(message: types.Message, state: FSMContext):
    malumot=await state.get_data()
    ism=malumot.get('ism')
    vaqt=malumot.get('vaqt')
    kategotiya=malumot.get('kategoriya')
    manzil=malumot.get('manzil')
    narx=malumot.get('narx')
    telefon = malumot.get('telefon')
    baza.ish_berish(ismi=ism,vaqt=vaqt,kategoriya=kategotiya,manzil=manzil,narxi=narx,tg_id=message.from_user.id,telefon_Raqami=telefon)
    await message.answer(text='Tanlang',reply_markup=boshi2)
    await steit2.men_ish_b.set()

@dp.message_handler(state=xammasi.isb_ber.tasdiq,text='Yoq ❌')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='Bosh menyuga xush kelibsiz',reply_markup=boshi)
    await state.finish()
