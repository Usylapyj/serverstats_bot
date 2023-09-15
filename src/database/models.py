from datetime import datetime

from peewee import (
    CharField,
    DateTimeField,
    Model,
    BigIntegerField,
    FloatField
)

from .base import db


# Модель таблицы записей для статистики

class Stats(Model):
    timestamp = DateTimeField(default=datetime.now())
    cpu_usage = FloatField(null=None)
    memory_usage = FloatField(null=None)
    swap_usage = FloatField(null=None)
    disk_usage = FloatField(null=None)
    cpu_temperature = FloatField(null=None)

    class Meta:
        database = db
        table_name = "stats"

    def __str__(self):
        return f"<Stats {self.timestamp}>"


# Модель таблицы администраторов

class Admins(Model):
    name = CharField(null=None)
    tguid = BigIntegerField(null=None)

    class Meta:
        database = db
        table_name = "admins"

    def __str__(self):
        return f"<Admin {self.name}>"