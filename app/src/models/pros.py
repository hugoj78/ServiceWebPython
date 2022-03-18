from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text
from config.db import meta, engine

pros = Table(
    "pro",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(45)),
    Column("city", Text),
    Column("speciality", Text),
)

meta.create_all(engine)