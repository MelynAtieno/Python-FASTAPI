from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Books(BaseModel):
    name: str
    author: str

book_catalog = [{"name":"Rules of Life", "author": "John Doe"},{"name":"Happy Life", "author":"James Bennett"}]
        
           
    

@app.get("/books")
async def get_books():
    global book_catalog
    return {"Books": book_catalog}

@app.post("/books")
async def add_book(book: Books):
    global book_catalog
    book_catalog.append(book)
    return book

@app.get("/books/{book_id}")
async def get_book_id(book_id: int):
    global book_catalog
    results = {"book_id": book_id, "book": book_catalog[book_id]}
    return results

@app.put("/books/{book_id}")
async def edit_book(book_id: int, books: Books):
    results = {"book_id": book_id, "books": book_catalog}
    return results

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    global book_catalog
    book_catalog.pop(book_id)
    return {"Message": "Book deleted successfully!", "Books": book_catalog}


