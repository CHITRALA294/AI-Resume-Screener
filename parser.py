import fitz
import re

skills_list = [
    "python",
    "java",
    "sql",
    "power bi",
    "excel",
    "machine learning",
    "data analysis",
    "flask",
    "html",
    "css",
    "javascript",
    "react",
    "pandas",
    "numpy"
]

def extract_email(text):

    email = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", text)

    return email[0] if email else "Not Found"

def extract_phone(text):

    phone = re.findall(r"\+?\d[\d -]{8,12}\d", text)

    return phone[0] if phone else "Not Found"

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill in text:
            found_skills.append(skill)

    return found_skills

def parse_resume(pdf_path):

    doc = fitz.open(pdf_path)

    raw_text = ""

    for page in doc:
        raw_text += page.get_text()

    return {
        "name": raw_text.split('\n')[0],
        "email": extract_email(raw_text),
        "phone": extract_phone(raw_text),
        "skills": extract_skills(raw_text),
        "raw_text": raw_text
    }