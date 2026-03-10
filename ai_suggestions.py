def generate_suggestions(missing_skills, match_score):
    """
    Generate actionable suggestions based on missing skills and the overall match score.
    """
    suggestions = []
    
    if match_score < 40:
        suggestions.append("Your resume match score is quite low. Strongly consider tailoring your resume to the specific job description.")
        suggestions.append("Ensure you are using the exact keywords mentioned in the job posting.")
    elif match_score < 75:
        suggestions.append("Good start! But you can improve your match score by incorporating more relevant keywords.")
    else:
        suggestions.append("Excellent match! Your resume is very well-tailored to this job description.")
        
    if missing_skills:
        missing_str = ", ".join(missing_skills).title()
        suggestions.append(f"Consider adding the following missing skills if you possess them: **{missing_str}**")
        suggestions.append(f"Include measurable achievements demonstrating your experience with those missing skills.")
    
    suggestions.append("Improve formatting for ATS systems by using standard section headers (e.g., Experience, Education, Skills).")
    suggestions.append("Use strong action verbs (e.g., Developed, Managed, Achieved) to start your bullet points.")
    suggestions.append("Add measurable achievements (e.g., 'Improved performance by 20%') where possible.")
    
    return suggestions
