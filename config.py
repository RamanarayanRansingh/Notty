# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "your-default-key")
    
    # Model Settings
    DEFAULT_MODEL = "llama-3.1-70b-versatile"
    TECHNICAL_TEMPERATURE = 0.3
    CREATIVE_TEMPERATURE = 0.7
    
    # App Settings
    MAX_CODE_LENGTH = 5000
    SUPPORTED_LANGUAGES = [
        "python", "javascript", "java", "cpp", "rust",
        "go", "ruby", "php", "swift", "kotlin"
    ]
    
    # File Export Settings
    EXPORT_FORMATS = ["markdown", "pdf", "html", "docx"]
