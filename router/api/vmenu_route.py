from fastapi import APIRouter,Depends,status
from typing import Annotated
from sqlalchemy.orm import Session
from database.session import get_db
from database.dbtables.v_m_u_m import vmenu
from database.dbtables.cs_m import coursem
from database.dbconnection import engine
from fastapi import status
from sqlalchemy import select
from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy import join
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.post("/vmenu-list",name="vmenulist")
def getVmenu(db:Session = Depends(get_db)):
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
def getVmenuWhere(db:Session = Depends(get_db)):
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

@router.post("/vmenu-select-join",name="select_from_multiple_tables")
def getVmenuSelectFrom(db:Session = Depends(get_db)):
    try:
        # https://docs.sqlalchemy.org/en/20/tutorial/data_select.html
        # row._mapping is used to correct the format
        # stmt = select(vmenu.c.id, vmenu.c.menu_name,vmenu.c.url_slug,vmenu.c.created_at,coursem.c.course_name,coursem.c.course_code) # give warnning because here we are not use join here. 
        # stmt = select(vmenu.c.id, vmenu.c.menu_name,vmenu.c.url_slug,vmenu.c.created_at,coursem.c.course_name,coursem.c.course_code).join_from(vmenu,coursem) # If you are not used foreign key in database tables then it will give error.
        # stmt = select(vmenu.c.id, vmenu.c.menu_name,vmenu.c.url_slug,vmenu.c.created_at,coursem.c.course_name,coursem.c.course_code).join(coursem) # It is giving error because we are not using ON clause
        # stmt = select(vmenu.c.id, vmenu.c.menu_name,vmenu.c.url_slug,vmenu.c.created_at,coursem.c.course_name,coursem.c.course_code).join(coursem, vmenu.c.course_id == coursem.c.id )

        # https://docs.sqlalchemy.org/en/20/core/selectable.html
        j = join(vmenu,coursem, vmenu.c.course_id == coursem.c.id )
        stmt = select(vmenu.c.id, vmenu.c.menu_name,vmenu.c.url_slug,vmenu.c.created_at,coursem.c.course_name,coursem.c.course_code).select_from(j) # select_from used to write complex queries
        result = db.execute(stmt)

        # results_list = [row._mapping for row in result] # without dict it also show in dictionary
        results_list = [dict(row._mapping) for row in result] # you can use dict()
        json_data = jsonable_encoder(results_list)
        return json_data
    except Exception as e:
        print(f"Exception error {e}")
