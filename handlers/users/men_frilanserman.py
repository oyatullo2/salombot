from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default.tugma import tugma
from states.steit import steit
from states.taklif_kiritish import state_taklif
from loader import dp, baza, bot

from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


# Echo bot
@dp.message_handler(state=steit.men_f,text='🔎 Buyurtmani toping')
async def bot_echo(message: types.Message):
    await message.answer('Buyurtma id kiriting')
    await steit.buyurtma_topish.set()

@dp.message_handler(state=steit.buyurtma_topish)
async def bot_echo(message: types.Message,state:FSMContext):
    top=message.text
    await state.update_data({'top':top})
    malumot=await state.get_data()
    topish=malumot.get('top')


    malumot=baza.filter(id=topish)



    for s in malumot:


        print(s)



        await message.answer(text=f"Buyurtma raqami # {s[0]}\n\n" \
                              f"Kategoriya: {s[4]}\n\n" \
                              f"Proyektning nomi: {s[1]}\n\n" \
                              f"Proyektning ta'rifi: {s[2]}\n\n" \
                              f"Proyektning narxi: {s[3]} sum\n\n")
        await steit.men_f.set()





@dp.message_handler(state=steit.men_f,text='📥 Buyurtma olish')
async def bot_echo(message: types.Message,state:FSMContext):

    await state_taklif.men_f_tak.set()
    await message.answer(message.text)
    user_id = message.from_user.id
    malumot = baza.select_all_foydalanuvchilar()



    for s in malumot:



        await message.answer(text=f"Buyurtma raqami # {s[0]}\n\n" \
                                  f"Kategoriya: {s[4]}\n\n" \
                                  f"Proyektning nomi: {s[1]}\n\n" \
                                  f"Proyektning ta'rifi: {s[2]}\n\n" \
                                  f"Proyektning narxi: {s[3]} sum\n\n",

                             reply_markup=InlineKeyboardMarkup( inline_keyboard=[
                                 [ InlineKeyboardButton('Taklif Kiritish',callback_data=f"inline {s[5]}\n{s[0]}",)
        ]
    ]
))


@dp.callback_query_handler(state=state_taklif.men_f_tak)
async def bot_echo(message: CallbackQuery, state:FSMContext):
    print(message.data)
    user_id=message.data[7:17]
    print(user_id)
    buyurtma_id=message.data[18:]
    print(buyurtma_id)
    await state.update_data({'d':user_id})
    print(buyurtma_id)







    q=baza.filter(id=buyurtma_id)
    print(q)





    await bot.send_message(chat_id=int(user_id),text='Sizning manabu buyurtmangizni frilanser kormoqda')
    await bot.send_message(chat_id=int(user_id),text=f"Buyurtma raqami # {q[0]}\n\n" \
                                                                 f"Kategoriya: {q[4]}\n\n" \
                                                                 f"Proyektning nomi: {q[1]}\n\n" \
                                                                 f"Proyektning ta'rifi: {q[2]}\n\n" f"Proyektning narxi: {q[3]} sum\n\n")
    f=message.message.text
    await state.update_data({'f':f})



    await bot.send_message(chat_id=message.from_user.id,text=f"📝Aynan qanday yo'l bilan bu \n\ntopshiriqni yechishingizni izohlang.\n📥 Muvaffaqiyatli bajarilgan proyektlaringiz ssilkasini qo'shing.\n\nVa ozingizni manzilingizni yozishni unutmang")
    await state_taklif.malumot.set()

@dp.message_handler(state=state_taklif.malumot)
async def bot_echo(message: types.Message, state:FSMContext):

    q=message.text
    await state.update_data({'q':q})

    malumot=await state.get_data()
    mal=malumot.get('q')
    id_if=malumot.get('d')
    f=malumot.get('f')
    nomer=baza.filter2(tg_id=message.from_user.id)
    for r in nomer:
        print(r)


    link=message.from_user.username
    jonatish=f"Frilanser taklifi👨🏻‍💻:{mal}\n" \
             f"Frilanser raqami💻:+{nomer[4]}\n" \
             f"Frilanser telegram user_ismi👨🏻:{link}"


    await bot.send_message(chat_id=id_if,text=jonatish,reply_markup=tugma)



    baza.buyurtma_yaratish3(salom=f,user_id=message.from_user.id,foydalanuvchi_id=id_if,taklif=mal)
    await message.answer(text='Murojaatingiz yetkazildi',reply_markup=tugma)

    await state.finish()



