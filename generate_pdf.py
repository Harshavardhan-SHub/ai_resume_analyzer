from reportlab.pdfgen import canvas

def create_resume():
    c = canvas.Canvas("test_resume.pdf")
    textobject = c.beginText()
    textobject.setTextOrigin(50, 800)
    textobject.setFont("Helvetica", 14)
    
    resume_text = """
    John Doe
    Software Engineer
    
    Skills:
    Python, Javascript, React, SQL, AWS, Machine Learning, Docker
    
    Experience:
    ABC Corp - developed scalable web applications using Python and React.
    Implemented machine learning models for data analysis.
    
    Education:
    B.S. Computer Science
    """
    
    for line in resume_text.split('\n'):
        textobject.textLine(line)
        
    c.drawText(textobject)
    c.save()

if __name__ == "__main__":
    create_resume()
