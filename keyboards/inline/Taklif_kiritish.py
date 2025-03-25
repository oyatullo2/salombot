from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

taklif=InlineKeyboardMarkup(
    inline_keyboard=[

            [
            InlineKeyboardButton('Xodim kerak',callback_data=f"Xodim kerak"),
            InlineKeyboardButton(text='IT',callback_data=f"IT"),
            InlineKeyboardButton(text='Qurilish',callback_data=f"Qurilish"),


            ],
            [
                    InlineKeyboardButton(text='Savdo', callback_data=f"Savdo"),
                    InlineKeyboardButton(text='Kiyim Kechak', callback_data=f"Kiyim Kechak"),
                    InlineKeyboardButton(text='Chevarchilik', callback_data=f"Chevarchilik"),

            ],
            [
                    InlineKeyboardButton('Oziq Ovqat', callback_data=f"Oziq Ovqat"),
                    InlineKeyboardButton('⬅️ Orqaga',callback_data='⬅️ Orqaga')
            ]
    ]
)