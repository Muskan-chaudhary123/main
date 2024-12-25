from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# A dictionary to store student data by student_id
student_db = {
    1: {
        "name": "Mom",
        "age": 19,
        "year": "year 12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return {"name": "first data"}

@app.post("/create_student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in student_db:
        raise HTTPException(status_code=400, detail="Student already exists")
    # Store student data by converting the Pydantic model to a dictionary
    student_db[student_id] = student
    return student_db[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in student_db:
        raise HTTPException(status_code=404, detail="Student does not exist")

    # Update the student data with the provided fields (partial update)
    existing_student = student_db[student_id]

    # Update only the fields that are provided (i.e., not None)
    if student.name is not None:
        existing_student["name"] = student.name
    if student.age is not None:
        existing_student["age"] = student.age
    if student.year is not None:
        existing_student["year"] = student.year

    return existing_student

@app.get("/get_student/{student_id}")
def get_student(student_id: int):
    student = student_db.get(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.delete("/delete_student/{student_id}")
def delete_student(student_id : int):
    if student_id not in student_db:
        return {"error":"student does not exist"}

    del student_db[student_id]
    return {"message":"student deleted successfully"}