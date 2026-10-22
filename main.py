from fastapi import FastAPI
from database.db import create_table
from routers.student import router as student_router

app = FastAPI(
    version="1.1.1",
    title="FastAPI Test",
    description="Create Api"
)

app.include_router(student_router) 

@app.on_event("startup")
def on_startup():
    create_table()