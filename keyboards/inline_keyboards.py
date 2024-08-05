from typing import List

from aiogram.utils.keyboard import InlineKeyboardBuilder


def build_artist_kb(lst_name_button: List):
    builder = InlineKeyboardBuilder()
    for name_button in lst_name_button:
        builder.button(text=f"{name_button}", callback_data="artist")
    builder.adjust(1)
    return builder.as_markup()
