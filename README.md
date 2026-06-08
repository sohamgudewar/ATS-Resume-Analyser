# ATS Resume Analyser

> Stop guessing why your resume gets ghosted.

A Python tool that compares your resume against a job description, extracts skills, calculates an ATS compatibility score, and tells you exactly what's missing — so you can fix it before the algorithm bins you.

---

## Features

- **PDF Resume Parsing** — extracts raw text from your resume
- **Skill Extraction** — identifies skills from both resume and job description
- **Similarity Scoring** — computes semantic similarity between resume content and JD
- **ATS Score** — combined score reflecting keyword match and content alignment
- **Gap Analysis** — surfaces missing skills you need to add

---

## Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| PDF Parsing | `resume_parser.py` (pdfplumber / PyMuPDF) |
| Skill Extraction | NLP-based (`skill_extractor.py`) |
| Similarity | Cosine similarity (`similarity.py`) |
| Scoring | Custom weighted logic (`ats_score.py`) |

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/sohamgudewar/ATS-Resume-Analyser.git
cd ATS-Resume-Analyser
pip install -r requirements.txt
```

### Run

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## Usage

1. Upload your resume as a **PDF**
2. Paste the **job description** into the text area
3. Hit **Analyse Resume**
4. Review:
   - Your **ATS Score** (%)
   - Skills found in your **resume**
   - Skills required by the **JD**
   - **Missing skills** you should add

---

## Project Structure

```
ATS-Resume-Analyser/
├── app.py               # Streamlit frontend
├── resume_parser.py     # PDF text extraction
├── skill_extractor.py   # NLP skill identification
├── similarity.py        # Cosine similarity computation
├── ats_score.py         # ATS scoring logic
├── requirements.txt
└── README.md
```

---

## Roadmap

- [ ] Support for DOCX resumes
- [ ] Role-specific skill taxonomy
- [ ] Exportable gap report (PDF)
- [ ] REST API endpoint for programmatic access
- [ ] Multi-JD batch analysis

---

## Author

**Soham Gudewar**  
B.Tech AI & Data Science — AISSMS IOIT, Pune  
[GitHub](https://github.com/sohamgudewar) · [LinkedIn](https://linkedin.com/in/sohamgudewar)

---

## License

MIT
