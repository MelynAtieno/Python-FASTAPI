from fastapi import FastAPI

app = FastAPI()

@app.get("/get-message")
async def read_root():
    return {"Message":"Congrats! This is your first API"}

@app.get("/pass-name")
def hello(name: str):
    return {"Message": "My name is " + name}

initial_string = "Never Give Up"

@app.post("/add")
async def add_text(text: str):
    global initial_string
    initial_string += text
    return {"Message":"Text added","current_string": initial_string}

@app.put("/change")
async def change_text(new_text: str):
    global initial_string
    initial_string = new_text
    return {"Message": "Text changed","current_string": initial_string}

