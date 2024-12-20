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
from sqlalchemy import and_, or_
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


@router.post("/vmenu-insert",name="vmenuinsert")
def insertVmenu(db:Session = Depends(get_db)):
    try:
        # https://docs.sqlalchemy.org/en/20/core/dml.html
        # https://docs.sqlalchemy.org/en/20/tutorial/data_insert.html

        stmt = insert(vmenu).values(
            course_id=10,
            vertica_menu_group_id=1,
            chapter_heading_main="Inserted By Sqlalchemy Table",
            menu_name="New menu Name",
            url_slug="new-menu-name"
            )
        db.execute(stmt)
        db.commit()
    except Exception as e:
        print(f"Exception error {e}")


@router.post("/vmenu-update",name="vmenuupdate")
def updateVmenu(db:Session = Depends(get_db)):
    try:
        # https://docs.sqlalchemy.org/en/20/core/dml.html
        # https://docs.sqlalchemy.org/en/20/tutorial/data_insert.html
        # user for operators: https://docs.sqlalchemy.org/en/20/core/sqlelement.html 

        stmt = update(vmenu).where(
            vmenu.c.id ==113 
            ).values(
            course_id=10,
            vertica_menu_group_id=1,
            chapter_heading_main="Inserted By Sqlalchemy Table updated",
            menu_name="New menu Name updated",
            url_slug="new-menu-name updatedd"
            )
        db.execute(stmt)
        db.commit()
    except Exception as e:
        print(f"Exception error {e}")


@router.post("/vmenu-update-and",name="vmenuupdateand")
def updateVmenubyand(db:Session = Depends(get_db)):
    try:
        # https://docs.sqlalchemy.org/en/20/core/dml.html
        # https://docs.sqlalchemy.org/en/20/tutorial/data_insert.html
        # user for operators: https://docs.sqlalchemy.org/en/20/core/sqlelement.html 

        stmt = update(vmenu).where(
            and_(vmenu.c.course_id ==10, vmenu.c.vertica_menu_group_id ==1)
            ).values(
            course_id=10,
            vertica_menu_group_id=1,
            chapter_heading_main="Inserted By Sqlalchemy Table updated and_ operator",
            menu_name="New menu Name updated and_ ",
            url_slug="new-menu-name updatedd and_ "
            )
        db.execute(stmt)
        db.commit()
    except Exception as e:
        print(f"Exception error {e}")


@router.post("/vmenu-update-or",name="vmenuupdateor")
def updateVmenubyor(db:Session = Depends(get_db)):
    try:
        # https://docs.sqlalchemy.org/en/20/core/dml.html
        # https://docs.sqlalchemy.org/en/20/tutorial/data_insert.html
        # user for operators: https://docs.sqlalchemy.org/en/20/core/sqlelement.html 

        stmt = update(vmenu).where(
            or_(vmenu.c.course_id ==10, vmenu.c.vertica_menu_group_id ==1)
            ).values(
            course_id=10,
            vertica_menu_group_id=1,
            chapter_heading_main="Inserted By Sqlalchemy Table updated or_ operator",
            menu_name="New menu Name updated or_ ",
            url_slug="new-menu-name updatedd or_ "
            )
        db.execute(stmt)
        db.commit()
    except Exception as e:
        print(f"Exception error {e}")


@router.post("/vmenu-delete",name="vmenudelete")
def updateVmenubyor(db:Session = Depends(get_db)):
    try:
        # https://docs.sqlalchemy.org/en/20/core/dml.html
        # https://docs.sqlalchemy.org/en/20/tutorial/data_insert.html
        # user for operators: https://docs.sqlalchemy.org/en/20/core/sqlelement.html 

        stmt = delete(vmenu).where(vmenu.c.id == 113)
        db.execute(stmt)
        db.commit()
    except Exception as e:
        print(f"Exception error {e}")