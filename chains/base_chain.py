
# chains/base_chain.py
from langchain_groq import ChatGroq
from config import Config

class BaseChain:
    def __init__(self, temperature=None):
        self.llm = ChatGroq(
            temperature=temperature or Config.TECHNICAL_TEMPERATURE,
            groq_api_key=Config.GROQ_API_KEY,
            model_name=Config.DEFAULT_MODEL
        )