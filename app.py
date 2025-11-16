import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file
import pdfplumber
import google.generativeai as genai
from io import BytesIO

# Load .env locally; Render will use environment variables
load_dotenv()

# Initialize GenAI client with API key from environment variable
client = genai.Client(api_key=os.getenv("GENAI_API_KEY"))

app = Flask(__name__)

def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            txt = page.extract_text()
            if txt:
                text += txt + "\n"
    return text

def summarize_text(text):
    response = client.models.generate_content(
        model="models/gemini-2.0-flash",
        contents=f"Summarize this into 10–12 bullet points:\n\n{text}"
    )
    return response.text

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None
    if request.method == "POST":
        pdf
