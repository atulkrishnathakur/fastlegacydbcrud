## How to use existing database or table in sql alchemy without model

## create the database connection
1. create the `database/dbconnection.py`

```
from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456789@localhost:5432/sampledb1"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
metadata = MetaData()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

```
2. create the `database/session.py` file for session
```
from .dbconnection import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

```

3 create the `database/dbtables/employee.py` to load existing table of database

```
from sqlalchemy import Table, Column, Integer, String
from database.dbconnection import engine,metadata
emp_m = Table(
    "emp_m",
    metadata,
    autoload_with=engine 
)
```

## create the route `router/api/emp_route.py` file
1. reference: https://docs.sqlalchemy.org/en/20/core/connections.html
2. reference: https://docs.sqlalchemy.org/en/20/core/metadata.html 
3. reference: https://docs.sqlalchemy.org/en/20/tutorial/metadata.html
4. reference: https://docs.sqlalchemy.org/en/20/tutorial/data_select.html

```
from fastapi import APIRouter,Depends,status
from typing import Annotated
from sqlalchemy.orm import Session
from database.session import get_db
from database.dbtables import employee
from database.dbtables.employee import emp_m
from database.dbconnection import engine
from fastapi import status
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import delete
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.post("/employee-list",name="employeelist")
def getEmployee(db:Session = Depends(get_db)):
    try:
        # https://docs.sqlalchemy.org/en/20/core/metadata.html
        # https://docs.sqlalchemy.org/en/20/tutorial/metadata.html
        # https://docs.sqlalchemy.org/en/20/tutorial/data_select.html
        
        #print(emp_m)
        #print(emp_m.columns.emp_hame)
        #print(emp_m.c.emp_hame)
        #print(emp_m.c["emp_hame"])
        
        '''
        emp_id, emp_name, email = emp_m.c["id", "emp_hame", "email"]
        print(emp_name)
        '''


        '''
        for dbcolumnname in emp_m.c:
            print(dbcolumnname)
        '''

        # https://docs.sqlalchemy.org/en/20/core/connections.html
        # row._mapping is used to correct the format
        stmt = select(emp_m)
        result = db.execute(stmt)
        # results_list = [row._mapping for row in result] # without dict it also show in dictionary
        results_list = [dict(row._mapping) for row in result] # you can use dict()
        json_data = jsonable_encoder(results_list)
        return json_data

    except Exception as e:
        print(f"Exception error {e}")

```

1. in this file in get getEmployee function you can see how to select data
