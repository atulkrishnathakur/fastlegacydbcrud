from fastapi import APIRouter,Depends,status
from typing import Annotated
from sqlalchemy.orm import Session
from database.session import get_db
from database.dbtables.v_m_u_m import vmenu
from database.dbconnection import engine
from fastapi import status
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import delete
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.post("/vmenu-list",name="vmenulist")
def getEmployee(db:Session = Depends(get_db)):
    try:
        # row._mapping is used to correct the format
        stmt = select(vmenu)
        result = db.execute(stmt)
        # results_list = [row._mapping for row in result] # without dict it also show in dictionary
        results_list = [dict(row._mapping) for row in result] # you can use dict()
        json_data = jsonable_encoder(results_list)
        return json_data
    except Exception as e:
        print(f"Exception error {e}")

@router.post("/vmenu-list-where",name="vmenulistwhere")
def getEmployee(db:Session = Depends(get_db)):
    try:
        # row._mapping is used to correct the format
        stmt = select(vmenu.c.id, vmenu.c.menu_name,vmenu.c.url_slug,vmenu.c.created_at,vmenu.c.updated_at)
        result = db.execute(stmt)
        # results_list = [row._mapping for row in result] # without dict it also show in dictionary
        results_list = [dict(row._mapping) for row in result] # you can use dict()
        json_data = jsonable_encoder(results_list)
        return json_data
    except Exception as e:
        print(f"Exception error {e}")

@router.post("/vmenu-list-inner-join",name="vmenulistjoin")
def getEmployee(db:Session = Depends(get_db)):
    try:
        # row._mapping is used to correct the format
        stmt = select(vmenu.c.id, vmenu.c.menu_name,vmenu.c.url_slug,vmenu.c.created_at,vmenu.c.updated_at)
        result = db.execute(stmt)
        # results_list = [row._mapping for row in result] # without dict it also show in dictionary
        results_list = [dict(row._mapping) for row in result] # you can use dict()
        json_data = jsonable_encoder(results_list)
        return json_data
    except Exception as e:
        print(f"Exception error {e}")
