
from response_model.StudentResponse import StudentResponse
from request_model.StudentRequest import StudentRequest
from sqlmodel import select
from models.Student import Student
from database.db import SessionDependancy
from fastapi import Depends, HTTPException, Query , status , Path , APIRouter

router = APIRouter(
    prefix="/student",
    tags=["Student"]
)
# Get Method
@router.get("/all",response_model=list[StudentResponse])
async def get_all(session:SessionDependancy):
    query = select(Student)
    result = session.exec(query).all()
    return result

# Post Method
@router.post("/create",response_model=StudentResponse,status_code= status.HTTP_201_CREATED)
async def create_student(studReq:StudentRequest,session:SessionDependancy):
    student_data = studReq.model_dump()
    print(student_data)
    stud_data = Student.model_validate(student_data)
    print(stud_data)
    session.add(stud_data)
    session.commit()
    session.refresh(stud_data)
    return stud_data

# Update Method
@router.put("/update/{id}", response_model=Student)
def update_student(studReq: StudentRequest,session: SessionDependancy,id: int = Path(ge=1)):
    student = session.get(Student, id)
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    student.name = studReq.name
    student.address = studReq.address
    student.gender = studReq.gender
    student.age = studReq.age
    student.qualification = studReq.qualification
    student.email = studReq.email

    session.add(student)
    session.commit()
    session.refresh(student)
    return student

# Delete Method
@router.delete("/delete/{id}",response_model=dict)
async def delete_student(session: SessionDependancy,id: int = Path(ge=1)):
    student = session.get(Student, id)
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    session.delete(student)
    session.commit()
    return {"message": f"Student with id {id} deleted successfully"}
    
