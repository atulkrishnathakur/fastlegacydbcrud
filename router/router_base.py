from fastapi import APIRouter, FastAPI
from router.api import emp_route
from router.api import vmenu_route

api_router = APIRouter()
api_router.include_router(emp_route.router, prefix="", tags=["employees"])
api_router.include_router(vmenu_route.router, prefix="", tags=["vmenu"])