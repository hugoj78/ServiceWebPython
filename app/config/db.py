from sqlalchemy import create_engine, MetaData
import os

DB_URI = os.environ['DB_URI']
engine = create_engine(DB_URI)

meta = MetaData()
conn = engine.connect()