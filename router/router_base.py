from fastapi import APIRouter, FastAPI
from router.api import emp_route

api_router = APIRouter()
api_router.include_router(emp_route.router, prefix="", tags=["employees"])