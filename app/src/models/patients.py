from sqlalchemy import Column, Table, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text
from config.db import meta, engine

patients = Table(
    "patient",
    meta,
    Column("id", Integer, primary_key=True),
    Column("id_pro", Text),
    Column("id_patient", Text),
)

meta.create_all(engine)