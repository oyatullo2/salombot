from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

tugma=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🧑🏻‍💻 Men Frilanserman'),
            KeyboardButton(text='👤 Men buyurtmachiman')
        ],
        [
            KeyboardButton(text='💼 Vakasiyalar/Vakansiya joylashtirish')

        ],
        [
            KeyboardButton(text='🇷🇺 Поменять язык')
        ]
    ],
    resize_keyboard=True
)