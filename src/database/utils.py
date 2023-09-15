
import logging

from .base import db
from .models import Admins, Stats

from datetime import datetime, timedelta

# Создание таблиц по моделям

def init_db():
    db.create_tables([Admins, Stats])
    logging.info("::initialized db")


# Проверка администратора по tguid

async def is_admin(tguid: int):
    user = Admins.select().where(Admins.tguid == tguid)
    if user:
        return True
    else:
        return False


# Получение истории измерений

async def get_history():
    history = Stats.select().where(Stats.timestamp > datetime.now() - timedelta(days=1))
    return history


# Запись измерений

async def write_stats(stats: dict):
    stats_record = Stats(
        timestamp = stats['timestamp'],
        cpu_usage = stats['cpu_usage'],
        memory_usage = stats['memory_usage'],
        swap_usage = stats['swap_usage'],
        disk_usage = stats['disk_usage'],
        cpu_temperature = stats['cpu_temperature']
    )
    stats_record.save()