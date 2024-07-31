from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


router = Router(name=__name__)


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {message.from_user.full_name}")


@router.message(Command("help"))
async def command_help_handler(message: Message):
    await message.answer("Введите в поиск название группы или название песни.")
