import requests 
import os 
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Set up API URL and Token
API_URL = "https://api-inference.huggingface.co/models/mrm8488/bert-tiny-finetuned-sms-spam-detection"
API_TOKEN = os.getenv("HF_API_TOKEN")  # Securely read token from .env

# Set authorization headers
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def check_ai_text(text):
    """
    Sends email text to Hugging Face Inference API to classify as spam/ham.

    Args:
        text (str): Combined email subject and body.

    Returns:
        tuple: (label: str, confidence: float)
    """
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    response.raise_for_status()
    result = response.json()[0]
    label = result["label"].lower()
    score = result["score"]
    return label, score