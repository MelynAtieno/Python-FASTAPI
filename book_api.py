from fastapi import FastAPI

app = FastAPI()

# books(id, title: str, author: str){
#         [
#             1, "Rules of Life", "John Doe",
#             1, "Rules of Life", "John Doe",
#             1, "Rules of Life", "John Doe",
#             1, "Rules of Life", "John Doe",
#             1, "Rules of Life", "John Doe"

#         ]
# }

@app.get("/books")
async def get_books():
    return {"Message":"Success!", "Books": books}

@app.post("/books")
async def post_book(id: int, name: str, author: str):
    global books
    books += id,name,author
    return {"Message": "Book added successfully!", "Books": books}

@app.get("/books/{id}")
async def get_book_id():
    return {"Message":"Success", "Book": {id}}

@app.put("/books/{id}")
async def edit_book():
    global books
    books[id] = 
    return {"Message": "Book edited successfully!", "Books": books}

@app.delete("/books/{id}")
async def delete_book():
    global books
    books[id] = ""
    return {"Message": "Book deleted successfully!", "Books": books}


