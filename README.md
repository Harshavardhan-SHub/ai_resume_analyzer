# AI Resume Analyzer

An AI-powered web application built with Python and Streamlit that analyzes a PDF resume against a job description. It extracts text, detects technical skills using spaCy NLP, calculates a match score using cosine similarity via scikit-learn, and provides actionable improvement suggestions.

## Features

- **Resume Upload:** Upload PDF resumes directly via the browser.
- **Text Extraction:** Uses `pdfplumber` to accurately scrape text from PDFs and handle errors gracefully.
- **Skill Extraction:** Uses `spaCy` NLP to detect technical keywords and standard skills.
- **Resume Scoring:** Compares resume text with the job description using TF-IDF and Cosine Similarity to find keyword overlap.
- **Missing Skills Detection:** Identifies skills required by the job description but missing in the resume.
- **AI Suggestions:** Provides automated feedback and tips to improve the resume formatting and content.

## Project Structure

```text
ai_resume_analyzer/
├── app.py               # Main Streamlit dashboard application
├── resume_parser.py     # PDF parsing and text cleaning logic
├── skill_matcher.py     # NLP logic for skill extraction and cosine similarity
├── ai_suggestions.py    # Logic to generate qualitative feedback
├── utils.py             # Helper functions (e.g. downloading spaCy models)
├── requirements.txt     # Python dependencies
└── README.md            # This documentation file
```

## Setup Instructions

1. **Navigate to the project directory** (e.g., in VS Code):

   ```bash
   cd ai_resume_analyzer
   ```

2. **Create a virtual environment** (recommended to keep dependencies clean):

   ```bash
   python -m venv venv

   # Activate on Windows:
   venv\Scripts\activate

   # Activate on macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

_Note: The application will automatically attempt to download the `en_core_web_sm` spaCy model upon first run and cache it for future uses._

## Usage

1. Upload your resume (in PDF format).
2. Paste the target Job Description in the provided text area.
3. Click **Analyze Resume** to view your match score, found skills, missing skills, and actionable improvement suggestions.

## Application Demo & Walkthrough

**Features Tested:**

- **Resume Upload**: Accepts PDF files via the Streamlit interface.
- **Text Extraction**: Uses `pdfplumber` to extract and clean text from the uploaded PDF.
- **Skill Extraction**: Leverages `spaCy` to identify technical skills and keywords.
- **Job Description Input**: Users can paste their target JD into a text area.
- **Resume Scoring**: Computes a percentage Match Score using cosine similarity.
- **Missing Skills Detection**: Clearly lists required skills that are absent from the resume.
- **AI Suggestions**: Provides dynamic tips to improve the resume based on the score and missing keywords.

Here is a recording of the application in action. The recording file is saved locally in the `screenshots/` directory.

![Application Test Demo](screenshots/demo.webp)

### Test Results Summary:

When evaluating the sample resume against a DevOps/AI Job Description:

- **Resume Match Score:** 17.7%
- **Extracted Skills:** API, CSS, Git, HTML, Java, JavaScript, etc.
- **Missing Skills correctly identified:** AWS, Docker, Kubernetes, Machine Learning

The application flow works perfectly and the output is presented in a clean, modular Streamlit dashboard!
