import asyncio

from datetime import datetime

from aiogram import executor

from bot.main import loop, dp
from bot.utils import set_default_commands
from bot.handlers import *

from database.utils import init_db

from config import APP_CONF


async def on_startup(dp):
    await set_default_commands(dp)


if __name__ == "__main__":
    init_db() # Инициализируем БД
    asyncio.set_event_loop(loop) # Устанавливаем текущий цикл событий
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True) # Создаем подключение к серверам Telegram
