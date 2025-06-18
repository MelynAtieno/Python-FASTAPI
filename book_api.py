from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Books(BaseModel):
    name: str
    author: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name" : "Rules of Life",
                    "author" : "John Doe"
                },
                {
                    "name" : "Happy life",
                    "author" : "James Bennett"
                }
            ]
        }
    }
        
           
    

@app.get("/books")
async def get_books():
    return {"Message":"Success!", "Books": books}

@app.post("/books")
async def post_book(id: int, name: str, author: str):
    global books
    books += id,name,author
    return {"Message": "Book added successfully!", "Books": books}

@app.get("/books/{id}")
async def get_book_id(id: int):
    return {"Message":"Success", "Book": id}

@app.put("/books/{book_id}")
async def edit_book(book_id: int, books: Books):
    global books
    return {"Message": "Book edited successfully!", "Books": books}

@app.delete("/books/{id}")
async def delete_book(id: int):
    global books
    books[id] = ""
    return {"Message": "Book deleted successfully!", "Books": books}


