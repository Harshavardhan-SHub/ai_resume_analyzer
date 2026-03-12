from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.utils import load_spacy_model

# A predefined list of common tech and soft skills for matching
COMMON_SKILLS = {
    "python", "java", "c++", "c#", "javascript", "typescript", "react", "angular", "vue", 
    "node.js", "sql", "nosql", "mysql", "postgresql", "mongodb", "docker", "kubernetes", 
    "aws", "gcp", "azure", "machine learning", "deep learning", "data science", 
    "artificial intelligence", "nlp", "html", "css", "git", "github", "linux", "unix", 
    "agile", "scrum", "tensorflow", "keras", "pytorch", "pandas", "numpy", 
    "scikit-learn", "api", "rest", "graphql", "django", "flask", "fastapi", "ci/cd"
}

def extract_skills(text):
    """
    Extract skills from text using spaCy and keyword matching.
    """
    nlp = load_spacy_model()
    doc = nlp(text.lower())
    
    extracted_skills = set()
    
    # Extract noun chunks assuming some skills might be compound nouns
    for chunk in doc.noun_chunks:
        chunk_text = chunk.text.strip()
        if chunk_text in COMMON_SKILLS:
            extracted_skills.add(chunk_text)
            
    # Direct token match
    for token in doc:
        if token.text in COMMON_SKILLS:
            extracted_skills.add(token.text)
            
    # Substring match for multi-word skills like "machine learning"
    for skill in COMMON_SKILLS:
        if skill in text.lower():
            extracted_skills.add(skill)
            
    return sorted(list(extracted_skills))

def calculate_similarity(resume_text, jd_text):
    """
    Calculates cosine similarity between the resume and the job description.
    """
    if not resume_text or not jd_text:
        return 0.0
        
    # Use CountVectorizer to convert text into a matrix of token counts, ignoring common stop words
    vectorizer = CountVectorizer(stop_words='english')
    try:
        feature_matrix = vectorizer.fit_transform([resume_text, jd_text])
    except ValueError:
        # Happens if text only contains stop words
        return 0.0
        
    vectors = feature_matrix.toarray()
    
    # Cosine similarity between the two vectors
    csim = cosine_similarity(vectors)
    match_score = csim[0][1] * 100
    
    return round(match_score, 2)

def find_missing_skills(resume_skills, jd_text):
    """
    Finds skills that are present in the JD but not in the resume.
    """
    jd_skills = extract_skills(jd_text)
    
    missing_skills = [skill for skill in jd_skills if skill not in resume_skills]
    return missing_skills
