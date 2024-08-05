from aiogram import Router
from aiogram.types import Message

from database.crud import get_artist
from keyboards.inline_keyboards import build_artist_kb

router = Router(name=__name__)


@router.message()
async def search_song(message: Message):
    artist = message.text.title()
    result = get_artist(artist)
    await message.answer(text="Альбомы", reply_markup=build_artist_kb(result))
