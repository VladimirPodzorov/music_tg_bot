__all__ = ("router",)

from aiogram import Router
from .commands import router as commands_router
from .user_routs import router as user_router
from .callback_query import router as callback_router

router = Router(name=__name__)

router.include_routers(
    commands_router,
    user_router,
    callback_router,
)
