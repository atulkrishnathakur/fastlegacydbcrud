from fastapi import FastAPI
from fastapi import FastAPI,Depends, HTTPException, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from router.router_base import api_router
from sqlalchemy import create_engine

def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(DEBUG=True)
    include_router(app)
    return app

app = start_application()
