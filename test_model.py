# test_model.py
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

resp = client.models.generate_content(
    model="models/gemini-1.5-flash",
    contents=[{"role":"user","parts":[{"text":"Say hello"}]}]
)
print("API call succeeded. Response:", resp.text)
