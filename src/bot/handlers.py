from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import IDFilter

from bot.main import dp, bot
from bot.filters import IsAdmin

from typing import Union

from bot.keyboards import menu_ikbd
from bot.utils import get_stats, draw_plots
from database.utils import get_history, write_stats





# Обработчик команды /start

@dp.message_handler(
    IsAdmin(),
    state="*",
    commands=["start"],
    chat_type=[types.ChatType.PRIVATE],
)
async def main_menu(obj: Union[types.Message, types.CallbackQuery], state: FSMContext):
    text = "Главное меню"

    if isinstance(obj, types.Message):
        await obj.answer(text, reply_markup=menu_ikbd)
    elif isinstance(obj, types.CallbackQuery):
        await obj.message.answer(text, reply_markup=menu_ikbd)


# Обработчик кнопки "Статистика"

@dp.callback_query_handler(
    IsAdmin(),
    text = 'stats',
    state="*",
    chat_type=[types.ChatType.PRIVATE]
)
async def stats_handler(callback: types.CallbackQuery, state: FSMContext):
    stats = await get_stats()
    text = (f"{stats['timestamp'].strftime('%H:%M:%S %d.%m.%Y')}\n"
            f"CPU: {stats['cpu_usage']}%, {stats['cpu_temperature']}°C\n"
            f"RAM: {stats['memory_usage']}%\n"
            f"Swap: {stats['swap_usage']}%\n"
            f"Disk: {stats['disk_usage']}%\n")
    await callback.message.answer(text)
    await write_stats(stats)
    await main_menu(callback, state)
    await callback.answer()


# Обработчик кнопки "История"

@dp.callback_query_handler(
    IsAdmin(),
    text = 'history',
    state="*",
    chat_type=[types.ChatType.PRIVATE]
)
async def history_handler(callback: types.CallbackQuery, state: FSMContext):
    history = await get_history()
    plots = await draw_plots(history)
    media = types.MediaGroup()
    for p in plots:
        p.seek(0)
        media.attach_photo(types.InputFile(p))
    await callback.message.answer_media_group(media)
    await main_menu(callback, state)
    await callback.answer()