from aiogram.dispatcher.filters.state import State,StatesGroup

class isb_ber(StatesGroup):
   state=State()
   ism=State()
   telefon_Raqami=State()
   tg_id=State()
   kategoriya=State()
   vaqt=State()
   manzil=State()
   narx=State()
   tasdiq=State()


class isb_ol(StatesGroup):
    state=State()