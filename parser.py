# modules/parser.py
import pdfplumber
import docx
import re
from datetime import datetime

def load_text(file_path: str) -> str:
    """
    Read PDF or DOCX and return all text as one string.
    """
    text = ""
    if file_path.lower().endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
    elif file_path.lower().endswith(".docx"):
        doc = docx.Document(file_path)
        for p in doc.paragraphs:
            if p.text:
                text += p.text + " "
    return text

def extract_name(text: str) -> str:
    """
    Naively extract the first non-empty line as the candidate's name.
    """
    for line in text.splitlines():
        clean = line.strip()
        if clean:
            return clean
    return "Unknown"

def extract_skills(text: str) -> list:
    """
    Extract skills by keyword matching from a predefined skill list.
    """
    skill_keywords = [
        "python", "php", "java", "javascript", "html", "css", "sql",
        "flutter", "keras", "tensorflow", "opencv", "nlp",
        "scikit-learn", "pandas", "numpy", "django", "flask", "laravel",
        "react", "node.js", "docker", "kubernetes", "git"
    ]
    lower = text.lower()
    found = [skill for skill in skill_keywords if skill in lower]
    return list(set(found))

def extract_education(text: str) -> list:
    """
    Extract common education keywords.
    """
    edu_keys = ["bachelor", "master", "phd", "diploma"]
    lower = text.lower()
    return [k for k in edu_keys if k in lower]

def extract_experience_entries(text: str, skills: list) -> list:
    """
    Find all date ranges (e.g. 'Oct 2024 - Apr 2025') in text,
    associate each entry with the resume's skill list.
    """
    # Matches 'Jan 2020 - Dec 2021' or 'Jan 2020 – Dec 2021' or 'Jan 2020 - Present'
    pattern = r'(\b[A-Za-z]{3,9}\s\d{4})\s*[-–]\s*(\b(?:Present|[A-Za-z]{3,9}\s\d{4}))'
    matches = re.findall(pattern, text)
    entries = []
    for start, end in matches:
        entries.append({
            'start_date': start,
            'end_date': end,
            'skills': skills
        })
    return entries

def parse_resume(file_path: str) -> dict:
    """
    Main parser entrypoint.
    Returns a dict with:
      - name
      - skills
      - education
      - experience (list of date-entry dicts)
      - raw_text
    """
    text = load_text(file_path)
    name = extract_name(text)
    skills = extract_skills(text)
    education = extract_education(text)
    experience = extract_experience_entries(text, skills)

    return {
        'name': name,
        'skills': skills,
        'education': education,
        'experience': experience,
        'raw_text': text
    }
