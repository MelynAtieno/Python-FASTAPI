from fastapi import FastAPI

app = FastAPI()

@app.get("/get-message")
async def read_msg():
    return {"Message":"Congrats! This is your first API"}