from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from fsm_form import Form


router = Router(name=__name__)


@router.message(Command("add", prefix="%"))
async def admin_handler(message: Message, state: FSMContext):
    await state.set_state(Form.band)
    await message.answer("Hi admin!\nКакую группу хочешь добавить?")


@router.message(Form.band)
async def add_band(message: Message, state: FSMContext):
    await state.update_data(band=message.text)
    await state.set_state(Form.album)
    await message.answer("Название альбома?")


@router.message(Form.album)
async def add_album(message: Message, state: FSMContext):
    await state.update_data(album=message.text)
    await state.set_state(Form.year)
    await message.answer("Год выхода альбома?")


@router.message(Form.year)
async def add_year(message: Message, state: FSMContext):
    await state.update_data(year=message.text)
    await state.set_state(Form.song)
    await message.answer("Название песни?")
