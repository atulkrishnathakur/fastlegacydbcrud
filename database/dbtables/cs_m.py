from sqlalchemy import Table, Column, Integer, String
from database.dbconnection import engine,metadata
coursem = Table(
    "cs_m",
    metadata,
    autoload_with=engine,
    schema="public"
)