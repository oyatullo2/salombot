from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

panell=InlineKeyboardMarkup(
    inline_keyboard=[
        [
InlineKeyboardButton('tugma',callback_data='tugma'),
InlineKeyboardButton('tugma chiqishi',callback_data='tugma chiqishi')

        ],
        [
InlineKeyboardButton('⬅️orqaga',callback_data='orqaga1')
        ]
    ]
)


panell2=InlineKeyboardMarkup(
    inline_keyboard=[
        [
InlineKeyboardButton('Tugma qoshish',callback_data='Tugma qoshish'),
InlineKeyboardButton('Tugma ochirish',callback_data='Tugma ochirish')

        ],
        [
InlineKeyboardButton('⬅️orqaga',callback_data='orqaga2')
        ]
    ]
)


from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from loader import baza

tugma = baza.tugma_olish()

index = 0
keys = []
j = 0
regions = baza.tugma_olish()
for region in regions:
    if j % 2 == 0 and j != 0:
        index +=1
    if j % 2 == 0:
        keys.append([InlineKeyboardButton(text=f'{region[1]}',callback_data='1'),])
    else:
        keys[index].append(InlineKeyboardButton(text=f'{region[1]}',callback_data='1'))
    j +=1

menu_buttons = InlineKeyboardMarkup(inline_keyboard=keys,resize_keyboard=True)