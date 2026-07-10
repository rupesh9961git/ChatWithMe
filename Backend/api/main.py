from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the API!"}
@app.get("/chat")
async def chat():

    
    return {"message": "Hello, World!"}