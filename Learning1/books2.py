from fastapi import Body, FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    category: str
    description: str
    rating: float

    def __init__(self, id, title,author, category, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.description = description 
        self.rating = rating

BOOKS = [
    Book(1, 'Title One', 'Henry','science', 'A fascinating look at the science of everyday life.', 4.5),
    Book(2, 'Title Two', 'Adam', 'science', 'An exploration of the latest developments in scientific research.', 4.0),
    Book(3, 'Title Three', 'william', 'history', 'A comprehensive overview of historical events and their impact.', 3.5),
    Book(4, 'Title Four', 'Arthur', 'math', 'A guide to understanding mathematical concepts and their applications.', 4.2),
    Book(5, 'Title Five', 'Charles', 'math', 'A detailed analysis of advanced mathematical theories.', 4.8),
]

class BookModel(BaseModel):
    id: Optional[int]= Field(description="The unique identifier for the book", default=None)
    title: str = Field(min_length=5, max_length=8)
    author: str
    category: str
    description: str = Field(min_length=10, max_length=50)
    rating: float = Field(gt=-1, lt=5)

    model_config = {
        "json_schema_extra":{
            "example": {
                "title": "Title Six",
                "author": "John",
                "category": "science",
                "description": "A captivating exploration of scientific discoveries.",
                "rating": 4.3
            }
        }
    }


@app.get("/books")
async def get_books():
        return BOOKS

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return {"message": "Book added successfully", "book": new_book}

@app.put("/books/update_book")
async def update_book(book_author: str = Body(), rating: float = Body()):
     for book in BOOKS:
          if book.author.casefold() == book_author.casefold():
                book.rating = rating
                return {"message": "Book rating updated successfully", "book": book}

@app.post("/books/create_a_book")
async def create_a_book(new_book: BookModel):
     modify_book=Book(**new_book.model_dump())
     BOOKS.append(unique_book_id(modify_book))


def unique_book_id(book: Book):
    if len(BOOKS)>0:
         book.id=BOOKS[-1].id + 1
    else:
         book.id = 1
    return book