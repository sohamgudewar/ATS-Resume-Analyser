def calculate_ats_score(similarity, resume_skills, jd_skills):

    skill_match = len(set(resume_skills) & set(jd_skills))

    if len(jd_skills) == 0:
        skill_score = 0
    else:
        skill_score = skill_match / len(jd_skills)

    final_score = (0.6 * similarity) + (0.4 * skill_score)

    return round(final_score * 100, 2)
