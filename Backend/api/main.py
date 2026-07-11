from fastapi import FastAPI
from ..model import model
from ..constant import constant
from pydantic import BaseModel

class Message(BaseModel):
    message: str

app = FastAPI()
model_ref = model.Model()

@app.get("/")
async def root():
    return {"message": "Welcome to the API!"}
@app.get("/chat")
async def chat():
    response = model_ref.invoke_model(model_name=constant.Constant.OLLAMA, message="Who is PM of India")
    return {"message": response}

@app.post(path="/askMe")
async def askMe(message:Message):
    response = model_ref.invoke_model(model_name=constant.Constant.OLLAMA, message=message.message)
    return {"message": response.content}    