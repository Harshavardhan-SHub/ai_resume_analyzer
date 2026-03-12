import streamlit as st
from src.resume_parser import extract_text_from_pdf, clean_text
from src.skill_matcher import extract_skills, calculate_similarity, find_missing_skills
from ai_suggestions import generate_suggestions

# Page Configuration
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

def main():
    st.title("📄 AI Resume Analyzer")
    st.markdown("Upload your **PDF Resume** and paste a **Job Description** to see how well they match!")
    
    # Layout using columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Upload Resume")
        uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])
        
    with col2:
        st.subheader("2. Job Description")
        job_description = st.text_area("Paste the target job description here", height=150)
        
    # Actions
    if st.button("Analyze Resume", use_container_width=True):
        if uploaded_file is not None and job_description.strip():
            with st.spinner("Analyzing your resume... This might take a moment."):
                
                # 1. Parse and clean resume
                raw_resume = extract_text_from_pdf(uploaded_file)
                if raw_resume is None:
                    st.error("Failed to extract text from the uploaded PDF. Please upload a valid, text-based PDF.")
                    return
                    
                cleaned_resume = clean_text(raw_resume)
                cleaned_jd = clean_text(job_description)
                
                if not cleaned_resume:
                    st.warning("The uploaded PDF appears to be empty or unreadable (perhaps it's an image-based PDF).")
                    return
                
                # 2. Extract Skills
                resume_skills = extract_skills(cleaned_resume)
                
                # 3. Compute Similarity Score
                match_score = calculate_similarity(cleaned_resume, cleaned_jd)
                
                # 4. Find Missing Skills
                missing_skills = find_missing_skills(resume_skills, cleaned_jd)
                
                # 5. Get AI Suggestions
                suggestions = generate_suggestions(missing_skills, match_score)
                
                # --- Display Results ---
                st.markdown("---")
                st.header("🎯 Analysis Results")
                
                # Display Score with conditional coloring
                score_color = "normal"
                if match_score >= 80:
                    st.success(f"### Resume Match Score: {match_score}%")
                elif match_score >= 50:
                    st.warning(f"### Resume Match Score: {match_score}%")
                else:
                    st.error(f"### Resume Match Score: {match_score}%")
                    
                st.progress(match_score / 100)
                
                st.markdown("---")
                
                # Skills Display
                res_col1, res_col2 = st.columns(2)
                
                with res_col1:
                    st.subheader("✅ Extracted Skills")
                    if resume_skills:
                        for skill in resume_skills:
                            st.write(f"- {skill.title()}")
                    else:
                        st.info("No specific technical skills detected.")
                        
                with res_col2:
                    st.subheader("⚠️ Missing Skills")
                    if missing_skills:
                        for skill in missing_skills:
                            st.write(f"- {skill.title()}")
                    else:
                        st.success("Great! No major keywords/skills missing from the job description.")
                
                st.markdown("---")
                
                # Suggestions Display
                st.subheader("💡 AI Improvement Suggestions")
                for item in suggestions:
                    st.markdown(f"- {item}")
                    
        else:
            st.warning("Please both upload a resume PDF AND paste a job description to proceed.")

if __name__ == "__main__":
    main()
