from fastapi import Body, FastAPI

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


@app.get("/books")
async def get_books():
        return BOOKS

@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)