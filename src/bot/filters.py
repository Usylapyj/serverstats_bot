from aiogram.dispatcher.filters import Filter
from aiogram.types import Message, CallbackQuery
from typing import Union

from database.utils import is_admin


# Фильтр доступа

class IsAdmin(Filter):
    key = "is_admin"

    async def check(self, obj: Union[Message, CallbackQuery]):
        user_id = obj.from_user.id
        return await is_admin(user_id)