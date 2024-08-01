from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    band = State()
    album = State()
    year = State()
    song = State()
