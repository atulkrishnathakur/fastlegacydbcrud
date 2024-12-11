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


        '''
        # Session ka use karke query ko execute karte hain aur results ko correct format mein fetch karte hain (row._mapping ka use karke).
        #stmt = select(emp_m.c.id,emp_m.c.menu_name)
        stmt = select(emp_m)
        result = db.execute(stmt)
        results_list = [dict(row._mapping) for row in result] 
        json_data = jsonable_encoder(results_list)
        return json_data
        '''
        stmt = select(emp_m)
        result = db.execute(stmt)
        results_list = [dict(row._mapping) for row in result] 
        json_data = jsonable_encoder(results_list)
        return json_data

    except Exception as e:
        print(f"Exception error {e}")
