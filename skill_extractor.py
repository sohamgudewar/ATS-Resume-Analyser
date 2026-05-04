SKILLS_DB = ["python", "machine learning", "deep learning", "sql", "docker", "kubernetes", "tensorflow", "pytorch", "nlp", "data analysis", "pandas", "numpy", "scikit-learn", "aws"]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return found_skills
