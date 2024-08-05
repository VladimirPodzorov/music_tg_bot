__all__ = ("router",)

from aiogram import Router
from .handle_callback_query import router as callback_query_router

router = Router(name=__name__)

router.include_routers(
    callback_query_router,
)
