# AI Resume Analyzer - Walkthrough

## Features Implemented & Tested

- [x] **Resume Upload**: Accepts PDF files via the Streamlit interface.
- [x] **Text Extraction**: Uses `pdfplumber` to extract and clean text from the uploaded PDF.
- [x] **Skill Extraction**: Leverages `spaCy` to identify technical skills and keywords.
- [x] **Job Description Input**: Users can paste their target JD into a text area.
- [x] **Resume Scoring**: Computes a percentage Match Score using cosine similarity.
- [x] **Missing Skills Detection**: Clearly lists required skills that are absent from the resume.
- [x] **AI Suggestions**: Provides dynamic tips to improve the resume based on the score and missing keywords.

## Application Demo

Here is a complete recording of the browser subagent testing the application end-to-end (uploading a test resume, pasting a job description, and viewing the results):

![Application Test Demo](C:/Users/HARSHA/.gemini/antigravity/brain/26fb104d-522f-445c-a480-f0740e5db787/resume_analyzer_test_1773124952526.webp)

### Test Results Summary:

When evaluating the sample resume against a DevOps/AI Job Description:

- **Resume Match Score:** 17.7%
- **Extracted Skills:** API, CSS, Git, HTML, Java, JavaScript, etc.
- **Missing Skills correctly identified:** AWS, Docker, Kubernetes, Machine Learning

The application flow works perfectly and the output is presented in a clean, modular Streamlit dashboard!
