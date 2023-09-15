from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


# Клавиатура главного меню

menu_ikbd = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Статистика", callback_data="stats")
        ],
        [
            InlineKeyboardButton(text="История", callback_data="history")
        ]
    ]
)