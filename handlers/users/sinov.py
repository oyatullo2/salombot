# from aiogram import types
# from aiogram.dispatcher import FSMContext
# from aiogram.types import ContentType
# from aiogram.utils.deep_linking import get_start_link
#
# from states.steit import steit
# from loader import dp, bot
# from pprint import pprint
# from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
# # Echo bot

#     await message.answer(text='rasmni yuboring yuboring')
#     await steit.men_f.set()
#
# @dp.message_handler(text="Pul ishlash 💸")
# async def Money(message: types.Message):
#     user_id =message.from_user
#     link = await get_start_link(user_id.id)
#     bot_get = await bot.get_me()
#     await message.answer("<b>✅ «Axcha Pul» konkursi rasmiy boti.</b>\n\n"
#                          f"🎈<a href='{user_id.url}'>{message.from_user.first_name}</a> do'stingizdan unikal havola-taklifnoma.\n\n"
#                          f"<b>👇 Boshlash uchun bosing:</b>\n"
#                          f"{link}",disable_web_page_preview=True,reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Ulashish ♻️", switch_inline_query=f"{user_id.id}")))
#
# @dp.inline_handler()
# async def referals(inline_query: types.InlineQuery):
#     user_id =inline_query.from_user
#     link = await get_start_link(user_id.id)
#     bot_get = await bot.get_me()
#     text = f"<b>✅ «Axcha Pul» konkursi rasmiy boti.</b>\n\n"\
#            f"🎈<a href='{user_id.url}'>{inline_query.from_user.first_name}</a> do'stingizdan unikal havola-taklifnoma.\n\n"\
#            f"📣 <a href='{'https://t.me/+Q6TsT4YXvXplZDUy'}'>{'<b>«About Me : Portfolio»</b>'}</a> kanalining rasmiy botiga do'stlaringizni taklif qiling va kuniga 100.000 so'mdan ko'proq pul toping!\n\n" \
#            f"<b>👇 Boshlash uchun bosing:</b>\n"\
#            f"{link}"
#
#     input_content = types.InputTextMessageContent(text,disable_web_page_preview=True)
#     inl = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("✅ Boshlash ✅", url=f"{link}"))
#     referal = types.InlineQueryResultArticle(
#         id='01',
#         thumb_url=None,
#         title="Do'stlarga yuborish 📲",
#         description="Do'stlarga yuborish uchun shu yerni bosing",
#         input_message_content=input_content,
#         reply_markup=inl,
#     )
#     lis = [referal]
#     msg = await inline_query.answer(results=lis, cache_time=1)
#
#
# @dp.message_handler(state=steit.men_f,content_types='photo')
# async def bot_echo(message: types.Message,state:FSMContext):
#
#
#
#
#
#     rasm = message.photo[-1].file_id
#     await state.update_data({'rasm':rasm})
#     await message.answer(text='textni yuboring')
#     await steit.buyurtma_topish.set()
#
# @dp.message_handler(state=steit.buyurtma_topish)
# async def bot_echo(message: types.Message,state:FSMContext):
#
#     await state.update_data({'text':message.text})
#     await message.answer(text='linkni yuboring')
#     await steit.men_b_rus.set()
#
#
# @dp.message_handler(state=steit.men_b_rus)
# async def bot_echo(message: types.Message, state: FSMContext):
#     await state.update_data({'link': message.text})
#
#     malumot=await state.get_data()
#     rasmi=malumot.get('rasm')
#     link=malumot.get('link')
#     text=malumot.get('text')
#
#     await bot.send_photo(chat_id=message.from_user.id, photo=rasmi,caption=text,reply_markup=InlineKeyboardMarkup(
#     inline_keyboard=[
#
#             [
#             InlineKeyboardButton('qale',callback_data="qale",send=link)
#     ]
#         ]
# )
#                          )
#     # a=steit.men_b.set()
#     # await state.update_data({'q':message.audio})
#     # malumot=await state.get_data()
#     # ism=malumot.get('q')
#     # await message.answer(text=ism)
#     # s=message.audio.file_name.
#
#
#
#
#
# @dp.message_handler(text="sinov")
# async def Money(message: types.Message):
#     son=0
#
#     await message.answer(text='dadf',reply_markup=
# InlineKeyboardMarkup(inline_keyboard=[
#
#             [
#             InlineKeyboardButton('+',callback_data=f"+"),
#             InlineKeyboardButton(text=f"{son}",callback_data=f"0"),
#             InlineKeyboardButton(text='-',callback_data=f"-")
#     ],
#     ]
# )
#                          )
#
#
#
# @dp.callback_query_handler(text="+")
# async def Money(message: types.Message):
#  import openai
# import apikey
# import pyttsx3
# import speech_recognition as sr
# import webbrowser
#
# openai.api_key=api_data
#
# completion=openai.Completion()
#
# def Reply(question):
#     prompt=f'Chando: {question}\n Jarvis: '
#     response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Chando'], max_tokens=200)
#     answer=response.choices[0].text.strip()
#     return answer
#
# engine=pyttsx3.init('sapi5')
# voices=engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
#
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
#
# speak("Hello How Are You? ")
#
# def takeCommand():
#     r=sr.Recognizer()
#     with sr.Microphone() as source:
#         print('Listening....')
#         r.pause_threshold = 1
#         audio = r.listen(source)
#     try:
#         print("Recognizing.....")
#         query=r.recognize_google(audio, language='en-in')
#         print("Chando Said: {} \n".format(query))
#     except Exception as e:
#         print("Say That Again....")
#         return "None"
#     return query
#
#
# if __name__ == '__main__':
#     while True:
#         query=takeCommand().lower()
#         ans=Reply(query)
#         print(ans)
#         speak(ans)
#         if 'open youtube' in query:
#             webbrowser.open("www.youtube.com")
#         if 'open google' in query:
#             webbrowser.open("www.google.com")
#         if 'bye' in query:
#             break   await message.answer(text='s')



































































def exit_keyboard(volume=1):
    # max_count = db.count_order(volume)
    markup = types.InlineKeyboardMarkup(row_width=3).add(
                types.InlineKeyboardButton(text="➖",callback_data=f"minus:{volume}"),
                types.InlineKeyboardButton(text=f"{volume}",callback_data=f"volume"),
                types.InlineKeyboardButton(text="➕",callback_data=f"plus:{volume}"),
                types.InlineKeyboardButton(text="🛒 Savatga qo'shish", callback_data=f"savat:{volume}"))
    return markup

from aiogram import types

from loader import dp

#Mahsulot qoshishb uchun
@dp.callback_query_handler(text_contains = "plus")
async def get_produzsdct(call: types.CallbackQuery):
    data = call.data.rsplit(':')
    print(data)
    num = int(data[1])
    print(num)
    num += 1
    print(num)
    markup =exit_keyboard(volume=num)
    await call.message.edit_reply_markup(reply_markup=markup)
    print(markup)

#Mahsulot ayirish uchun
@dp.callback_query_handler(text_contains = "minus")
async def get_produzsdct(call: types.CallbackQuery):
    data = call.data.rsplit(':')
    print(data)
    num = int(data[1])
    print(num)
    if num == 1:
        await call.answer("Eng kamida bitta mahsulot sotib olishingiz mumkin ! 😉",show_alert=True)
    elif num> 1:
        num -= 1
        markup =exit_keyboard(volume=num)
        await call.message.edit_reply_markup(reply_markup=markup)

@dp.callback_query_handler(text_contains = "savat")
async def get_produzsdct(call: types.CallbackQuery):
    data = call.data.rsplit(':')
    print(data)
    num = int(data[1])
    print(num)
    await call.answer(num)

@dp.message_handler(text='fayil')
async def bot_echo(message: types.Message):
    await message.answer(text='salom',reply_markup=exit_keyboard())