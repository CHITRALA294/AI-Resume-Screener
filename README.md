# AI Resume Screener

## Overview

AI Resume Screener is a Flask-based web application that analyzes resumes against a given job description. The system provides ATS-style scoring, missing skill detection, interview question generation, and resume improvement suggestions.

The goal of the project is to help job seekers understand how well their resume matches a target role and identify areas for improvement.

---

## Features

### Resume Analysis

* Upload PDF resumes
* Extract candidate information
* Parse skills from resumes
* Detect education details
* Recommend suitable job roles
* Assess resume strength level
* Generate career roadmap
* Calculate job readiness score
* Provide score breakdown analysis

### ATS Match Score

* Compare resume skills with job requirements
* Generate a match percentage score
* Provide match verdicts (Strong, Moderate, Weak)

### Missing Skill Detection

* Identify skills required by the job description but missing from the resume
* Highlight improvement opportunities

### Interview Preparation

* Generate role-based interview questions
* Help candidates prepare for technical interviews

### Resume Improvement Tips

* Provide suggestions based on ATS score
* Recommend missing skills to improve employability

### PDF Report Generation

* Download resume analysis results as a PDF report

---
### Additional Features

* Dark Mode / Light Mode support
* Career guidance dashboard
* Resume score breakdown
  
## Tech Stack

* Python
* Flask
* Flask-CORS
* PyMuPDF (fitz)
* ReportLab
* HTML
* CSS
* JavaScript

---

## Project Structure

```text
AI_Resume_Screener/
│
├── app.py
├── main.py
├── parser.py
├── matcher.py
├── question_gen.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│
└── resumes/
```

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/CHITRALA294/AI-Resume-Screener.git
cd AI-Resume-Screener
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## Sample Workflow

1. Upload Resume PDF
2. Paste Job Description
3. Click Analyze Resume
4. View:
ATS Score
Candidate Information
Recommended Role
Resume Strength
Job Readiness Score
Career Roadmap
Score Breakdown
Skills Detected
Missing Skills
Interview Questions
Resume Tips
5. Download PDF Report

---

## Future Enhancements

* AI Career Recommendation Agent
* Resume Improvement Agent
* Multi-Agent Architecture
* Advanced Resume Parsing
* Cloud Deployment
* Real-Time Job Matching

---

## Author

**Chitrala Akshitha**

B.Tech Graduate | Data Analytics Enthusiast | AI & Machine Learning Learner
