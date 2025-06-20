from fastapi import FastAPI, HTTPException
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

@app.get("/books/{book_id}")
async def get_book_id(book_id: int):
    global book_catalog
    if book_id < 0 or book_id >= len(book_catalog):
        raise HTTPException(status_code=404, detail="Book ID does not exist")
    else:
        results = {"Book ID": book_id, "Book Requested": book_catalog[book_id]}
        return results

@app.post("/books")
async def add_book(book: Books):
    global book_catalog
    book_catalog.append(book.dict())
    return {"Message":"Book added successfully!", "Book Added":book}


        

@app.put("/books/{book_id}")
async def edit_book(book_id: int, book: Books):
    global book_catalog
    if book_id < 0 or book_id >= len(book_catalog):
        raise HTTPException(status_code=404, detail="Book ID does not exist")
    else:
        book_catalog[book_id] = book
        results = {"Message":"Book updated successfully!", "Book ID": book_id, "Book": book}
        return results

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    global book_catalog
    if book_id < 0 or book_id >= len(book_catalog):
        raise HTTPException(status_code=404, detail="Book ID does not exist")
    else:
        book_catalog.pop(book_id)
        return {"Message": "Book deleted successfully!", "Books Available": book_catalog}


