from ..constant.constant import Constant
class Model:
    def get_model_model(self, model_name):
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
        model = self.get_model_model(model_name)
        return model