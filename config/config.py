from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    HF_TOKEN = os.getenv("HF_TOKEN")
