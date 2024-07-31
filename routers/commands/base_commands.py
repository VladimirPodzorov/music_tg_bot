from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router(name=__name__)


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {message.from_user.full_name}")
