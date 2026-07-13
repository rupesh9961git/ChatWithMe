from fastapi import FastAPI
from ..model import model
from ..constant import constant
from pydantic import BaseModel
from Backend.tools.tool import find_wheather
from langsmith import traceable

class Message(BaseModel):
    message: str

app = FastAPI()
model_ref = model.Model()

@app.get("/")
async def root():
    return {"message": "Welcome to the API!"}
@app.get("/chat")
async def chat():
    response = model_ref.invoke_model_with_single_message(model_name=constant.Constant.OLLAMA, message="Who is PM of India")
    return {"message": response}

@app.post(path="/askMe")
@traceable(name="askMe")
async def askme(message:Message):
    response = model_ref.invoke_model_with_langchain_messages(model_name=constant.Constant.OLLAMA, messages=message.message)
    return {"message": response}

@app.post(path="/stream")
async def stream(message:Message):
    response = model_ref.stream_model(model_name=constant.Constant.OLLAMA, messages=message.message)
    return {"message": response}

@app.post(path="/batch")
async def batch(message:Message):
    response = model_ref.batch_model(model_name=constant.Constant.OLLAMA)
    return {"message": response}

@app.post(path="/tool")
async def tool(message:Message):
    response = model_ref.call_model_with_tools(model_name=constant.Constant.OLLAMA, messages=message.message)
    return {"message": response}