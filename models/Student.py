from datetime import datetime, timezone
from sqlmodel import Field
from models.StudentBase import StudentBase

class Student(StudentBase, table=True):
    id:int | None = Field(primary_key=True,default=None)   
    is_active: bool = Field(default=True, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc),nullable=False)