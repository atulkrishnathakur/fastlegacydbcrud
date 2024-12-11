from sqlalchemy import Table, Column, Integer, String
from database.dbconnection import engine,metadata
emp_m = Table(
    "emp_m",
    metadata,
    autoload_with=engine 
)