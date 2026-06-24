from flask import Flask, request, jsonify, send_file, render_template
from flask_cors import CORS

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

import os
import tempfile

from parser import parse_resume
from matcher import match_resume_job, get_missing_skills
from question_gen import generate_questions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():

    pdf_file = request.files['resume']

    job_description = request.form['job_description']

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix='.pdf'
    ) as tmp:

        pdf_file.save(tmp.name)

        tmp_path = tmp.name

    parsed = parse_resume(tmp_path)

    match = match_resume_job(
        parsed['raw_text'],
        job_description,
        parsed['skills']
    )

    missing = get_missing_skills(
        parsed['skills'],
        job_description
    )

    questions = generate_questions(
        parsed['raw_text'],
        job_description
    )

    tips = generate_tips(
        missing,
        match['match_score']
    )

    breakdown = get_score_breakdown(parsed)

    os.remove(tmp_path)

    print("ROLE =", suggest_role(parsed['skills']))
    
    return jsonify({

        "name":
        parsed['name'],

        "email":
        parsed['email'],

        "phone":
        parsed['phone'],

        "skills":
        parsed['skills'],

        "education":
        parsed.get('education', []),

        "experience":
        parsed.get('experience', []),

        "match_score":
        match['match_score'],

        "verdict":
        match['verdict'],

        "missing":
        missing,

        "questions":
        questions,

        "tips":
        tips,
        
        "recommended_role":
        suggest_role(parsed['skills']),
        
        "resume_category":
        get_resume_category(parsed['skills']),
         
        "resume_strength":
        get_resume_strength(parsed['skills']),
        
        "job_readiness":
        calculate_readiness(
        match['match_score'],
        missing
        ),
         
        "breakdown":
        breakdown,
        
        "roadmap":
        generate_roadmap(missing)
    })
    
def suggest_role(skills):

    if "python" in skills and "sql" in skills:
        return "Data Analyst"

    elif "html" in skills and "css" in skills:
        return "Frontend Developer"

    elif "machine learning" in skills:
        return "Machine Learning Engineer"

    else:
        return "Software Developer"
    
def get_resume_category(skills):

    if "python" in skills and "sql" in skills:
        return "Data Science / Analytics"

    elif "html" in skills and "css" in skills:
        return "Web Development"

    elif "machine learning" in skills:
        return "Artificial Intelligence"

    else:
        return "Software Development"
    
def get_resume_strength(skills):

    count = len(skills)

    if count >= 9:
        return "Advanced"

    elif count >= 5:
        return "Intermediate"

    else:
        return "Beginner"
    
def get_score_breakdown(parsed):

    return {
        "skills_score":
        min(len(parsed['skills']) * 10, 100),

        "education_score":
        60 if parsed.get('education') else 20,

        "experience_score":
        40
    }
    
def calculate_readiness(score, missing_skills):

    readiness = score

    readiness += 30

    readiness -= len(missing_skills) * 5

    readiness = max(0, min(100, readiness))

    return readiness

def generate_roadmap(missing_skills):

    roadmap = []

    for skill in missing_skills:
        roadmap.append(f"Learn {skill}")

    return roadmap

def generate_tips(missing_skills, score):

    tips = []

    if score < 50:

        tips.append(
            "Your resume needs more relevant keywords."
        )

    if missing_skills:

        tips.append(
            f"Add these skills to boost score: "
            f"{', '.join(missing_skills[:3])}"
        )

    if score >= 75:

        tips.append(
            "Great match! Apply confidently."
        )

    if not tips:

        tips.append(
            "Add more project details to improve score."
        )

    return tips


@app.route('/download-report', methods=['POST'])

def download_report():

    data = request.json

    filename = "resume_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(

        Paragraph(
            "AI Resume Screener Report",
            styles['Title']
        )
    )

    elements.append(Spacer(1, 12))

    fields = [

        ("Name", data.get("name")),

        ("Email", data.get("email")),

        ("Phone", data.get("phone")),

        ("Match Score",
         str(data.get("match_score")) + "%"),

        ("Verdict", data.get("verdict")),

        ("Skills",
         ", ".join(data.get("skills", []))),

        ("Missing Skills",
         ", ".join(data.get("missing", []))),

        ("Tips",
         ", ".join(data.get("tips", [])))
    ]

    for label, value in fields:

        elements.append(

            Paragraph(
                f"<b>{label}:</b> {value}",
                styles['BodyText']
            )
        )

        elements.append(Spacer(1, 10))

    elements.append(

        Paragraph(
            "<b>Interview Questions:</b>",
            styles['Heading2']
        )
    )

    questions = data.get("questions", "")

    for q in questions.split("\n"):

        if q.strip():

            elements.append(

                Paragraph(
                    q,
                    styles['BodyText']
                )
            )

    doc.build(elements)

    return send_file(
        filename,
        as_attachment=True
    )


if __name__ == '__main__':

    app.run(debug=True)