import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
key = os.getenv("GENAI_API_KEY")
if not key:
    raise SystemExit("GENAI_API_KEY missing")

client = genai.Client(api_key=key)

try:
    models = client.models.list()
    print("\n=== AVAILABLE MODELS ===")
    for m in models:
        print(m.name)
except Exception as e:
    print("ERROR:", e)
