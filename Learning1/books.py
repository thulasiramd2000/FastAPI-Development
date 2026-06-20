from fastapi import FastAPI;

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

@app.get("/books/{book_id}")
async def read_book(book_id: str):
    for book in BOOKS:
        if book["title"] == book_id:
            return book
    return {"error": "Book not found"}

@app.get("/books/")
async def read_books_by_category(category: str):
    matches = [book for book in BOOKS if book.get("category", "").casefold() == category.casefold()]
    if matches:
        return matches
    return [{"error": "No books found in this category"}]


@app.get("/books/{book_author}/")
async def read_by_author_and_category(book_author: str, category: str):
    books_results = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_results.append(book)
    return books_results