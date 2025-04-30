# Resume Screening Bot

## Overview

The **Resume Screening Bot** is an AI-based tool designed to parse resumes, extract key information, and match candidates' skills, experience, and education to job descriptions. It uses natural language processing (NLP) and machine learning techniques to assist in resume screening.

## Features

- Extracts candidate name, position, skills, experience, and education from resumes.
- Allows filtering resumes based on job description keywords (e.g., Python, Machine Learning, etc.).
- Matches resumes with job descriptions and ranks them based on relevance.
- Provides detailed insights on candidate skills, experience, and education.

## Technologies Used

- **Programming Language:** Python
- **Libraries:** 
  - `pyresparser` for resume parsing.
  - `Streamlit` for UI.
- **Artificial Intelligence (AI):** NLP (Natural Language Processing) for extracting text from resumes.
- **ATS (Applicant Tracking System):** The bot matches resumes against job descriptions for better candidate screening.
 
## Installation

## 📦 Required Libraries

Make sure you have Python **3.10** or higher installed. Use the following to install the dependencies:

pip install -r requirements.txt
pip install streamlit pyresparser pandas python-docx nltk
python -m nltk.downloader all

## Project Structure

ResumeScreeningBot/
│
├── env/                          # Virtual environment (excluded via .gitignore)
├── .gitignore
├── README.md                     # Project guide
├── requirements.txt              # Python dependencies
│
├── main.py                       # (Optional entry point, can be used for CLI tests)
│
├── modules/                      # Backend logic
│   ├── __init__.py
│   ├── parser.py                 # PDF parsing logic
│   ├── matcher.py                # Filtering logic
│   ├── experience_analyzer.py    # Experience extraction logic
│   └── utils.py                  # Helper functions
│
└── streamlit_app/
    └── streamlit_app.py          # Streamlit UI

## ▶️ How to Run
streamlit run streamlit_app/streamlit_app.py

Follow these steps to run the Resume Screening Bot on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/Portfolio-Profile/resume-screener.git

