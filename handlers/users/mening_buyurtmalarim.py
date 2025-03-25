from aiogram import types

from loader import dp,baza
# @dp.message_handler(text="📝 Mening buyurtmalarim")
# async def bot_start(message: types.Message):
#     await message.answer(f"<b>Sizning buyurtmalaringiz</b>")
#
#     user_id2 = message.from_user.id
#     id_send = baza.select_zakaz(user_id=user_id2)
#
#     print(id_send)
#
#     for idsend in id_send:
#         sql_id = idsend[4]
#         await message.answer(f"{sql_id}")
#
#         pass
#
#     await message.answer(f"faefdeafefwa{id_send[1][3]}" )
#
# # Echo bot
from states.steit import steit


@dp.message_handler(state=steit.men_b,text='📝 Mening buyurtmalarim')
async def bot_echo(message: types.Message):
    user_id=message.from_user.id
    malumot=baza.filter4(user_id=user_id)

    for s in malumot:


        print(s)



        await message.answer(text=f"Buyurtma raqami # {s[0]}\n\n" \
                              f"Kategoriya: {s[4]}\n\n" \
                              f"Proyektning nomi: {s[1]}\n\n" \
                              f"Proyektning ta'rifi: {s[2]}\n\n" \
                              f"Proyektning narxi: {s[3]} sum\n\n")



@dp.message_handler(state=steit.men_b,text='✅ Freelancer takliflar')
async def bot_echo(message: types.Message):
    malumot = baza.filter3(foydalanuvchi_id=message.from_user.id)
    for s in malumot:
        print(s)
        await message.answer(text=f"Sizning manavi buyurtmangizga💼:\n\n{s[0]}\n\n Frilanser Taklifi🧑🏻‍💻:\n\n{s[3]}")




@dp.message_handler(state=steit.men_f,text='📝 Mening buyurtmalarim')
async def bot_echo(message: types.Message):

    malumot=baza.filter3(user_id=message.from_user.id)
    for s in malumot:



        print(s)
        await message.answer(text=f"{s[0]}")