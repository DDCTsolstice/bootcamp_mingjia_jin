# src/config.py
from dotenv import load_dotenv
import os

def load_env():
    """
    Load environment variables from .env file
    """
    load_dotenv()

def get_key(key: str):
    """
    Get a value from environment variables by key
    """
    return os.getenv(key)

