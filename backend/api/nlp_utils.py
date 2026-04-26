import spacy
import PyPDF2
import docx
import re
from .role_mappings import ROLE_REQUIREMENTS, PREDEFINED_SKILLS

# Load the spacy English model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_obj):
    text = ""
    try:
        reader = PyPDF2.PdfReader(file_obj)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    except Exception as e:
        print(f"Error extracting PDF: {e}")
    return text

def extract_text_from_docx(file_obj):
    text = ""
    try:
        doc = docx.Document(file_obj)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        print(f"Error extracting DOCX: {e}")
    return text

def extract_text(file_obj, filename):
    if filename.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_obj)
    elif filename.lower().endswith('.docx') or filename.lower().endswith('.doc'):
        return extract_text_from_docx(file_obj)
    return ""

def get_extracted_skills(text):
    text_lower = text.lower()
    found_skills = set()
    
    # We use both simple string matching and token matching to extract skills
    # Simple matching (good for multi-word skills like "machine learning")
    for skill in PREDEFINED_SKILLS:
        # Use regex for word boundaries to avoid partial matches
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.add(skill)
            
    return list(found_skills)

def match_all_roles(extracted_skills):
    results = []
    extracted_set = set(extracted_skills)
    
    for role, required_skills in ROLE_REQUIREMENTS.items():
        matched_skills = list(required_skills.intersection(extracted_set))
        missing_skills = list(required_skills.difference(extracted_set))
        
        if not required_skills:
            match_percentage = 0
        else:
            match_percentage = int((len(matched_skills) / len(required_skills)) * 100)
            
        suggestions = []
        if match_percentage < 50:
            suggestions.append(f"Consider taking foundational courses in {role} methodologies.")
        if missing_skills:
            suggestions.append(f"Try to add projects using the following missing skills: {', '.join(missing_skills[:3])}.")
        if match_percentage >= 80:
            suggestions.append("Your resume is a strong match for this role! Tailor your experience section to highlight these skills.")
            
        results.append({
            "role": role,
            "match_percentage": match_percentage,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "suggestions": suggestions
        })
        
    # Sort by match percentage descending
    results.sort(key=lambda x: x["match_percentage"], reverse=True)
    
    # Return top 3
    return results[:3]
