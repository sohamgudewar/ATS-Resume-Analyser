import streamlit as st

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from similarity import calculate_similarity
from ats_score import calculate_ats_score


st.title("ATS Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)")
# uploaded_file = "sohamresume.pdf"


job_description = st.text_area("Paste Job Description")
# job_description = """Job Description
# We are looking for a Machine Learning Engineer / Software Engineer to join our AI team. The candidate will be responsible for building scalable machine learning systems, developing data pipelines, and deploying AI models into production.
# Responsibilities
# Develop and deploy machine learning models
# Work with large datasets for training and evaluation
# Build REST APIs for model serving
# Collaborate with cross-functional teams to integrate AI solutions
# Optimize model performance and scalability
# Write clean, maintainable, and well-documented code
# Required Skills
# Python
# Machine Learning
# Deep Learning
# TensorFlow or PyTorc
# Scikit-learn
# Data Structures & Algorithms
# SQL
# Git
# REST APIs"""

if st.button("Analyze Resume"):

    resume_text = extract_resume_text(uploaded_file)

    resume_skills = extract_skills(resume_text)

    jd_skills = extract_skills(job_description)

    similarity = calculate_similarity(resume_text, job_description)

    ats_score = calculate_ats_score(similarity, resume_skills, jd_skills)

    st.subheader("Results")

    st.write("ATS Score:", ats_score, "%")

    st.write("Resume Skills:", resume_skills)

    st.write("Job Description Skills:", jd_skills)

    missing_skills = list(set(jd_skills) - set(resume_skills))

    st.write("Missing Skills:", missing_skills)
