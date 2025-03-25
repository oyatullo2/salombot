from aiogram.dispatcher.filters.state import State,StatesGroup

class steit(StatesGroup):
    men_b=State()
    men_f=State()
    men_b_rus=State()
    men_f_rus=State()
    buyurtma_topish=State()

class steit2(StatesGroup):
    men_ish_b=State()
    men_ish_ol=State()
    men_ish_ol_rus=State()
    men_ish_b_rus=State()
    buyurtma_topish=State()

class tugma_yaratish(StatesGroup):
    ism=State()