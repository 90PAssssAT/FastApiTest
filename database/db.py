
from sqlmodel import SQLModel,create_engine,Session
from contextlib import contextmanager
from typing import Annotated
from fastapi import Depends
from dotenv import load_dotenv
import os
load_dotenv()


DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "Mysql@127.0.0.1")
DB_NAME = os.getenv("DB_NAME", "fastapi_tutorial")
DB_URL = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@"
    f"{DB_HOST}:3306/{DB_NAME}"
)
# print(DB_URL)
engine = create_engine(DB_URL , echo=True)

def create_table():
    SQLModel.metadata.create_all(engine)

@contextmanager
def get_session_context():
    session = Session(engine)
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()

def get_session():
    with get_session_context() as session:
        yield session
SessionDependancy = Annotated[Session, Depends(get_session)]