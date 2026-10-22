from sqlmodel import SQLModel , Field
from pydantic import BaseModel, Field, EmailStr
class StudentBase(SQLModel):
    name:str = Field(min_length=2,max_length=20,nullable=False)
    address:str = Field(min_length=2,max_length=50)
    gender:str = Field(min_length=2,max_length=10,nullable=False)
    age:int = Field(nullable=False)
    qualification: str = Field(min_length=2,max_length=50,nullable=False)
    email:str = EmailStr