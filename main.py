import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import TOKEN
from routers import router as main_router

# @dp.message(F.audio)
# async def handler_audio(message: Message):
#     await message.bot.send_audio(
#         chat_id=message.chat.id,
#         audio=message.audio.file_id
#     )


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(main_router)
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
