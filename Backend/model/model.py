from Backend.tools.tool import find_wheather

from ..constant.constant import Constant
from langchain_ollama import ChatOllama
import os
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

API_KEY = os.getenv("OLLAMA_API_KEY")
BASE_URL = os.getenv("OLLAMA_BASE_URL", "https://api.ollama.com")
class Model:
    def get_model_name(self, model_name):
        if model_name == "latest":
            return Constant.CLAUDE_OPUS_LATEST
        elif model_name == Constant.CLAUDE_OPUS_LATEST:
            return Constant.CLAUDE_OPUS_LATEST
        elif model_name == Constant.CLAUDE_SONNET_LATEST:
            return Constant.CLAUDE_SONNET_LATEST
        elif model_name == Constant.CLAUDE_HAIKU_LATEST:
            return Constant.CLAUDE_HAIKU_LATEST
        elif model_name == Constant.OLLAMA:
            return Constant.OLLAMA
        else:
            raise ValueError(f"Unknown model name: {model_name}")
        
    def get_model(self, model_name):
     if model_name in (
        "latest",
        Constant.CLAUDE_OPUS_LATEST,
        Constant.CLAUDE_HAIKU_LATEST,
        Constant.CLAUDE_SONNET_LATEST,
    ):
        raise NotImplementedError("Claude models are not supported yet")

     elif model_name == Constant.OLLAMA:
        return ChatOllama(
            model=Constant.OLLAMA,
            base_url=os.getenv("OLLAMA_BASE_URL"),
            headers={
                "Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"
            },
            max_tokens=100,
            temperature=1,
            max_retries=3,
            timeout=120
        )

     raise ValueError(f"Unknown model: {model_name}")
       
    def invoke_model_with_single_message(self, model_name, message):
        model = self.get_model(model_name)
        response = model.invoke(message)
        return response
       
    def invoke_model_with_conversation(self, model_name, messages):
        conversation = [{"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": messages},
                        {"role": "assistant", "content": "How can I assist you today?"}]
        model = self.get_model(model_name)
        response = model.invoke(conversation)
        return response   
    def invoke_model_with_langchain_messages(self, model_name, messages):
        conversation = [SystemMessage("You are a helpful assistant."), HumanMessage(messages)]
        model = self.get_model(model_name)
        response = model.invoke(conversation)
        return response.content
    
    def stream_model(self, model_name, messages):
        conversation = [SystemMessage("You are a helpful assistant."), HumanMessage(messages)]
        model = self.get_model(model_name)
        response = model.stream(conversation)
        return response
    
    def batch_model(self, model_name):
        model = self.get_model(model_name)
        response = model.batch(["Who is PM of India", "What is the capital of France?", "What is the largest ocean on Earth?"])
        return response    
    
    def call_model_with_tools(self, model_name, messages):
        conversation = [SystemMessage("You are a helpful assistant."), HumanMessage(messages)]
        model = self.get_model(model_name).bind_tools([find_wheather])
        response_ai = model.invoke(conversation)
        conversation.append(response_ai)
        for tool_call in response_ai.tool_calls:
            response_tool = find_wheather.invoke(tool_call)
            conversation.append(response_tool)

        response = model.invoke(conversation)    
        return response.content   