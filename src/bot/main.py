import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import APP_CONF

loop = asyncio.new_event_loop() # Создаем цикл событий
bot = Bot(APP_CONF.BOT_TOKEN, parse_mode=types.ParseMode.HTML) # Создаем объект бота
dp = Dispatcher(bot, storage=MemoryStorage()) # Создаем диспетчер
