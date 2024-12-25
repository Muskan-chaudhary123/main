
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from uuid import UUID
app = FastAPI()

class Book(BaseModel):
    id : UUID
    title : str = Field(min_length=1)
    author: str = Field(min_length=1,max_length=100)
    description: str = Field(min_length=1,max_length=100)
    rating: int= Field(gt=1,lt=101)

BOOKS = []


@app.get("/")
# call read api
def read_books(): # now fast api should know that this is a get request method so for that we will use get method
    return BOOKS

@app.post("/")
def create_book(book:Book):
    BOOKS.append(book)
    return book

@app.put("/{book_id}")
def update_book(book_id:UUID,book:Book):
    counter = 0

    for x in BOOKS:
        if x.id == book_id:
            BOOKS[counter-1] = book
            return BOOKS[counter-1]

    raise HTTPException(
        status_code = 404,
        detail = f"ID{book_id} : does not exist"

    )


@app.delete("/{book_id}")
def delete_book(book_id:UUID):
    counter = 0

    for x in BOOKS:
        if x.id == book_id:
            del BOOKS[counter-1]
            return f"ID : {book_id} deleted "

    raise HTTPException(
       status_code=404,
       detail=f"ID{book_id} : Does not exist"
            )


