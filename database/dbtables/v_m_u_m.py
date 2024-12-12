from sqlalchemy import Table, Column, Integer, String
from database.dbconnection import engine,metadata
vmenu = Table(
    "v_m_u_m",
    metadata,
    autoload_with=engine,
    schema="public"
)