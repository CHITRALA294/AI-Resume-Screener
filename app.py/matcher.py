def match_resume_job(resume_text,
                     job_description,
                     resume_skills=None):

    common_skills = [
        "python", "flask", "django",
        "machine learning", "sql",
        "react", "docker", "aws",
        "html", "css", "javascript",
        "pandas", "numpy"
    ]

    job_lower = job_description.lower()

    required_skills = [
        s for s in common_skills
        if s in job_lower
    ]

    matched = [
        s for s in required_skills
        if s in (resume_skills or [])
    ]

    if required_skills:

        score = (
            len(matched)
            / len(required_skills)
        ) * 100

    else:

        score = 50

    score = round(score)

    return {

        "match_score": score,

        "verdict": get_verdict(score)
    }

def get_verdict(score):

    if score >= 75:
        return "Strong Match"

    elif score >= 50:
        return "Moderate Match"

    else:
        return "Weak Match"

def get_missing_skills(resume_skills,
                       job_description):

    job_lower = job_description.lower()

    missing = []

    common_skills = [
        "python", "flask", "django",
        "machine learning", "sql",
        "react", "docker", "aws",
        "html", "css", "javascript",
        "pandas", "numpy"
    ]

    for skill in common_skills:

        if (
            skill in job_lower
            and
            skill not in resume_skills
        ):

            missing.append(skill)

    return missing