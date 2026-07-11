from ..constant.constant import Constant
from langchain_ollama import ChatOllama
import os
from dotenv import load_dotenv

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
            }
        )

     raise ValueError(f"Unknown model: {model_name}")
       
    def invoke_model(self, model_name, message):
        model = self.get_model(model_name)
        response = model.invoke(message)
        return response
       