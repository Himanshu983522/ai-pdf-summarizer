# AI PDF Summarizer

AI PDF Summarizer is a web application that allows users to upload a PDF and get concise AI-generated summaries in bullet points. It uses Google’s Generative AI API for text summarization.

---

## Features

- Upload any PDF file and get a summarized version of the content.
- Download the summary as a `.txt` file.
- Light/Dark mode toggle for better user experience.
- Built using Flask, PDFPlumber, and Google Generative AI.

---

## Demo

You can access the live demo (if deployed) here:  
`https://your-app-name.onrender.com`  *(replace with your deployed link)*

---

## Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **PDF Processing:** pdfplumber
- **AI Integration:** Google Generative AI (`google-generativeai` / `google-ai-generativelanguage`)
- **Environment Management:** python-dotenv

---

## Installation

Follow these steps to run the project locally:

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/ai-pdf-summarizer.git
cd ai-pdf-summarizer

2. Create and activate a virtual environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Set up environment variables
Create a .env file in the project root with the following content:

GENAI_API_KEY=your_google_generative_ai_api_key

5. Run the application
python app.py

6. Open the app in your browser

Go to: http://127.0.0.1:5000

Usage:-

Upload a PDF file.

Click Summarize PDF.

View the summary in bullet points.

Download the summary as a .txt file.
