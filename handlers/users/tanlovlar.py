from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ContentTypes

from keyboards.default.boshi import boshi, boshi2
from keyboards.default.contact import contact
from keyboards.default.nastroyka import nastroyka
from keyboards.default.men_frilanserman import men_frilanserman
from keyboards.default.men_buyurtmachiman import men_buyurtmachiman, men_buyurtmachiman2
from keyboards.default.soxa2 import nomi
from keyboards.default.tastiqlash import tastiqlash
from keyboards.default.tugma import tugma
from keyboards.default.tugma2 import tugma2
from keyboards.default.men_buyurtmachiman_rus import men_buyurtmachiman_rus
from keyboards.default.nastroyka_rus import nastroyka_rus
from keyboards.default.men_frilanserman_rus import men_frilanserman_rus

from states import xammasi
from states.steit import steit, steit2
from keyboards.inline.Taklif_kiritish import taklif
from loader import dp, bot, baza


# Echo bot
@dp.message_handler(text='💼 Вакансии/Разместить вакансии')
async def bot_echo(message: types.Message):
    id=message.from_user.id
    await bot.send_photo(chat_id=id,photo='https://t.me/asilbekzor/648',caption='https://t.me/rewrwe4r43')



@dp.message_handler(text='💼 Vakasiyalar/Vakansiya joylashtirish')
async def bot_echo(message: types.Message):
    id=message.from_user.id
    await bot.send_photo(chat_id=id,photo='https://t.me/asilbekzor/648',caption='https://t.me/rewrwe4r43')





@dp.message_handler(text='🧑🏻‍💻 Men Frilanserman')
async def bot_echo(message: types.Message):
    await message.answer(text='Shaxsiy kabinetingizga xush kelibsiz!',reply_markup=men_frilanserman)
    await steit.men_f.set()

@dp.message_handler(state=steit.men_f,text='⬅️ Orqaga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='⬅️ Orqaga',reply_markup=tugma)
    await state.finish()


@dp.message_handler(text='👤 Men buyurtmachiman')
async def bot_echo(message: types.Message):
    await message.answer(text='Shaxsiy kabinetingizga xush kelibsiz!',reply_markup=men_buyurtmachiman)
    await steit.men_b.set()

@dp.message_handler(state=steit.men_b,text='⬅️ Orqaga')
async def bot_echo(message: types.Message, state: FSMContext):
    await message.answer(text='⬅️ Orqaga',reply_markup=tugma)
    await state.finish()



@dp.message_handler(text='🧑🏻‍💻 Я фрилансер')
async def bot_echo(message: types.Message):
    await message.answer(text='🧑🏻‍💻 Я фрилансер',reply_markup=men_frilanserman_rus)
    await steit.men_f_rus.set()


@dp.message_handler(state=steit.men_f_rus,text='⬅️ назад')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='⬅️ назад', reply_markup=tugma2)
    await state.finish()



@dp.message_handler(text='👤 Я заказчик')
async def bot_echo(message: types.Message):
    await message.answer(text='👤 Я заказчик',reply_markup=men_buyurtmachiman_rus)
    await steit.men_f_rus.set()


@dp.message_handler(state=steit.men_f_rus,text='⬅️ назад')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='⬅️ назад', reply_markup=tugma2)
    await state.finish()


@dp.message_handler(state=steit.men_f_rus,text='🏠 На главную')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='🏠 На главную', reply_markup=tugma2)
    await state.finish()

@dp.message_handler(state=steit.men_b_rus,text='🏠 На главную')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='🏠 На главную', reply_markup=tugma2)
    await state.finish()

@dp.message_handler(state=steit.men_b_rus,text='⚙️ Настройки')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='⚙️ Настройки', reply_markup=nastroyka_rus)


@dp.message_handler(state=steit.men_f_rus,text='⚙️ Настройки')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='⚙️ Настройки', reply_markup=nastroyka_rus)


@dp.message_handler(state=steit.men_b,text='⚙️ Sozlamalar')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='⚙️ Sozlamalar', reply_markup=nastroyka)

@dp.message_handler(state=steit.men_b,text='🏠 Bosh Menyuga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='🏠 Bosh Menyuga', reply_markup=tugma)
    await state.finish()

@dp.message_handler(state=steit.men_f,text='⚙️ Sozlamalar')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='⚙️ Sozlamalar', reply_markup=nastroyka)


@dp.message_handler(state=steit.men_f,text='🏠 Bosh Menyuga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='🏠 Bosh Menyuga', reply_markup=tugma)
    await state.finish()


@dp.message_handler(text='🧑 Ish olish')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Kategoriyalardan birini tanlang', reply_markup=taklif)
    await xammasi.isb_ol.state.set()







@dp.message_handler(text='🧑 Ish beruvchiman')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Kategoriyalardan birini tanlang', reply_markup=boshi2)
    await steit2.men_ish_b.set()

@dp.message_handler(state=steit2.men_ish_b,text='📝 Mening buyurtmalarim')
async def bot_echo(message: types.Message, state:FSMContext):
    salom=baza.filter_ish_b(tg_id=message.from_user.id)

    for s in salom:
        salom=s

        await message.answer(text=f"Buyurtma raqami #{salom[0]}\n"
                                  f"Kategoriya💼 : {salom[1]}\n" 
                         f"Ish vaqti🕜: {salom[5]}\n" 
                         f"Manzil🇺🇿: {salom[4]}\n" 
                         f"Ish narxi💰: {salom[3]}\n" 
                         f"Ish beruvchining ismi👨🏻‍💻: {salom[2]}\n" 
                         f"Telefon📱: {salom[7]}",reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("Buyurtmani o'chirish",callback_data=f"inline {s[0]}",)]]))



@dp.callback_query_handler(state=steit2.men_ish_b)
async def bot_echo(message: types.Message, state:FSMContext):
    salom=(message.data[7:])

    print(salom)

    a=baza.ochirishsh(id=salom,ismi='asilbek')
    print(a)

@dp.message_handler(state=steit2.men_ish_b,text='⚙️Sozlamalar')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Tugmalardan birinitanlang', reply_markup=nastroyka)

@dp.message_handler(state=steit2.men_ish_b,text='⚙️Sozlamalar')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Tugmalardan birinitanlang', reply_markup=nastroyka)



@dp.message_handler(text='👤 Ish oluvchiman')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Tugmalardan birini tanlang',reply_markup=men_buyurtmachiman2)
    await steit2.men_ish_ol.set()

@dp.message_handler(state=steit2.men_ish_ol,text='⬅️ Orqaga')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bosh menyuga hush kelibsiz',reply_markup=boshi)
    await state.finish()
@dp.message_handler(state=steit2.men_ish_ol,text='/start')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Bosh menyuga hush kelibsiz',reply_markup=boshi)
    await state.finish()






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




@dp.message_handler(state=steit2.men_ish_ol,text='📥 Buyurtma olish')
async def bot_echo(message: types.Message, state:FSMContext):
    await message.answer(text='Kategoriyalardan birini tanlang 💼',reply_markup=taklif)
    await xammasi.isb_ber.state.set()


@dp.callback_query_handler(state=xammasi.isb_ber.state)
async def bot_echo(message: types.callback_query, state:FSMContext):
    kategoriya2=message.message.text
    print(kategoriya2)
    await state.update_data({'kategoriya':kategoriya2})

    user_id = message.from_user.username
    check = baza.ish_olish(kategoriya=kategoriya2)
    await message.message.answer(text=check)
    if kategoriya2 in check:
        await message.answer(text='bor')
    else:
        await message.answer(text='yoq')



#     await message.message.answer(text='Ismingizni kiriting 👨🏻‍💻:\nMasalan: Asilbek:',reply_markup=nomi)
#     await xammasi.isb_ber.ism.set()
#
# @dp.message_handler(state=xammasi.isb_ber.ism)
# async def bot_echo(message: types.Message,state:FSMContext):
#     await state.update_data({'ism':message.text})
#     await message.answer(text='Ishning narxini kiriting 💰:\nMasalan:50000',reply_markup=nomi)
#
#     await xammasi.isb_ber.narx.set()
#
# @dp.message_handler(state=xammasi.isb_ber.narx)
# async def bot_echo(message: types.Message,state:FSMContext):
#     await state.update_data({'narx':message.text})
#
#     await message.answer("Telefon raqamingizni Kiriting 📱:\nMasalan: +998907785435",reply_markup=contact)
#     await xammasi.isb_ber.telefon_Raqami.set()
#
#
# @dp.message_handler(content_types=ContentTypes.CONTACT,state=xammasi.isb_ber.telefon_Raqami)
# async def bot_echo(message: types.Message, state: FSMContext):
#         await state.update_data({'telefon': message.contact.phone_number})
#         malumot = await state.get_data()
#         ism = malumot.get('ism')
#         vaqt = malumot.get('vaqt')
#         kategotiya = malumot.get('kategoriya')
#         manzil = malumot.get('manzil')
#         narx = malumot.get('narx')
#         telefon = malumot.get('telefon')
#         jonatish = f"Kategoriya💼: {kategotiya}\n\n" \
#                    f"Ish narxi💰: {narx}\n\n" \
#                    f"Ish beruvchining ismi👨🏻‍💻: {ism}\n\n" \
#                    f"Telefon📱: {telefon}"
#         await message.answer(text=jonatish, reply_markup=tastiqlash)
#         await xammasi.isb_ber.tasdiq.set()
#
#
# @dp.message_handler(state=xammasi.isb_ber.tasdiq, text='Xa ✅')
# async def bot_echo(message: types.Message, state: FSMContext):
#     malumot = await state.get_data()
#     ism = malumot.get('ism')
#     vaqt = malumot.get('vaqt')
#     kategotiya = malumot.get('kategoriya')
#     manzil = malumot.get('manzil')
#     narx = malumot.get('narx')
#     telefon = malumot.get('telefon')
#     baza.ish_berish(ismi=ism, vaqt=vaqt, kategoriya=kategotiya, manzil=manzil, narxi=narx, tg_id=message.from_user.id,
#                     telefon_Raqami=telefon)
#     await message.answer(text='Tanlang', reply_markup=boshi2)
#     await steit2.men_ish_b.set()
#
#
# @dp.message_handler(state=xammasi.isb_ber.tasdiq, text='Yoq ❌')
# async def bot_echo(message: types.Message, state: FSMContext):
#     await message.answer(text='Bosh menyuga xush kelibsiz', reply_markup=boshi)
#     await state.finish()


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
