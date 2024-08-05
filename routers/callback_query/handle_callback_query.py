from aiogram import Router
from aiogram.types import CallbackQuery

from database.crud import get_playlist

router = Router(name=__name__)


@router.callback_query()
async def handle_album(callback_query: CallbackQuery):
    await callback_query.answer()
    album = get_playlist(callback_query.data)
    for audio_id in album:
        await callback_query.message.answer_audio(audio=audio_id)
