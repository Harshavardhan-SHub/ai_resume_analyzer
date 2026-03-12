# AI Resume Analyzer - Walkthrough

## Features Implemented & Tested

- [x] **Resume Upload**: Accepts PDF files via the Streamlit interface.
- [x] **Text Extraction**: Uses `pdfplumber` to extract and clean text from the uploaded PDF.
- [x] **Skill Extraction**: Leverages `spaCy` to identify technical skills and keywords.
- [x] **Job Description Input**: Users can paste their target JD into a text area.
- [x] **Resume Scoring**: Computes a percentage Match Score using cosine similarity.
- [x] **Missing Skills Detection**: Clearly lists required skills that are absent from the resume.
- [x] **AI Suggestions**: Provides dynamic tips to improve the resume based on the score and missing keywords.

### Test Results Summary:

When evaluating the sample resume against a DevOps/AI Job Description:

- **Resume Match Score:** 17.7%
- **Extracted Skills:** API, CSS, Git, HTML, Java, JavaScript, etc.
- **Missing Skills correctly identified:** AWS, Docker, Kubernetes, Machine Learning

The application flow works perfectly and the output is presented in a clean, modular Streamlit dashboard!
