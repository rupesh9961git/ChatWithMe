from langchain.tools import tool

@tool
def find_wheather(location: str) -> str:
    """Simulate a weather lookup for the given location."""
    return f"The current weather in {location} is sunny with a temperature of 25°C."