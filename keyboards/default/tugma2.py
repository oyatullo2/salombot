from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

tugma2=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🧑🏻‍💻 Я фрилансер'),
            KeyboardButton(text='👤 Я заказчик')
        ],
        [
            KeyboardButton(text='💼 Вакансии/Разместить вакансии')

        ],
        [
            KeyboardButton(text="🇺🇿 Tilni o'zgartirish")
        ]
    ],
    resize_keyboard=True
)