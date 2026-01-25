# config.py

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration"""
    
    # API Settings
    API_KEY = os.getenv("API_KEY", "sk_test_123456789")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    
    # Server Settings
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
    
    # Model Settings
    MODEL_PATH = os.getenv("MODEL_PATH", "./models/checkpoint.pth")
    MAX_AUDIO_SIZE_MB = int(os.getenv("MAX_AUDIO_SIZE_MB", 10))
    
    # Supported Languages
    SUPPORTED_LANGUAGES = ["Tamil", "English", "Hindi", "Malayalam", "Telugu"]
    
    # Audio Settings
    SAMPLE_RATE = 16000
    MAX_AUDIO_LENGTH_SECONDS = 30

# Create global config instance
config = Config()