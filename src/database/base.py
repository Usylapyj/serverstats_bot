from peewee import PostgresqlDatabase, SqliteDatabase

from config import POSTGRES_CONF, APP_CONF

# Создание подключения к базе данных

if APP_CONF.ENV == "prod":
    _db = PostgresqlDatabase(
        POSTGRES_CONF.PG_DB,
        user=POSTGRES_CONF.PG_USER,
        password=POSTGRES_CONF.PG_PASSWD,
        host=POSTGRES_CONF.PG_HOST,
        port=POSTGRES_CONF.PG_PORT,
    )
else:
    _db = SqliteDatabase("db.sqlite")

db = _db
