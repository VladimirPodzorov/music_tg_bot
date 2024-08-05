from aiogram import Router
from aiogram.types import Message

from database.crud import get_albums_or_song
from keyboards.inline_keyboards import build_artist_kb

router = Router(name=__name__)


@router.message()
async def search_song(message: Message):
    artist = message.text.title()
    result = get_albums_or_song(artist)
    if isinstance(result, list):
        await message.answer(text="Альбомы", reply_markup=build_artist_kb(result))
    else:
        await message.answer("backend пока не готов")
