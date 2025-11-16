import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file
import pdfplumber
from google import genai
from io import BytesIO

load_dotenv()
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
        pdf_file = request.files["pdf"]
        extracted = extract_text(BytesIO(pdf_file.read()))
        summary = summarize_text(extracted)
    return render_template("index.html", summary=summary)

@app.route("/download", methods=["POST"])
def download_summary():
    summary_text = request.form.get("summary", "")
    buffer = BytesIO()
    buffer.write(summary_text.encode("utf-8"))
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="summary.txt", mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True)
