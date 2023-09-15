import asyncio

from datetime import datetime

from aiogram import executor

from bot.main import loop, dp
from bot.utils import set_default_commands
from bot.handlers import *

from database.utils import init_db

from config import APP_CONF

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores import memory


async def on_startup(dp):
    await set_default_commands(dp)


async def job():
    stats = await get_stats()
    await write_stats(stats)


if __name__ == "__main__":
    init_db() # Инициализируем БД
    sched = AsyncIOScheduler(event_loop=loop)
    sched.add_job(job, 'cron', hour='00-23', minute='00')
    sched.start()
    asyncio.set_event_loop(loop) # Устанавливаем текущий цикл событий
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True) # Создаем подключение к серверам Telegram
