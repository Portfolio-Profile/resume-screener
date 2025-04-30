# Resume Screening Bot

## Overview

The **Resume Screening Bot** is an AI-assisted resume filtering tool built using Python and NLP techniques. It parses resumes, extracts important information, and allows filtering based on user-selected keywords (skills, education, or experience). It simplifies and speeds up the shortlisting process during hiring.

## Features

- Extracts candidate **name**, **position**, **skills**, **experience**, and **education** from resumes (PDF format).
- Upload and screen **multiple resumes** at once.
- Filter candidates by custom **keywords** under categories like skills, education, or experience.
- Clear message displayed if no candidate matches.
- Displays an overview of candidate experience and skills if no filter is applied.

> **Note:** Matching against full job descriptions (ATS logic) is not implemented yet, but keyword-based filtering is available.

## Technologies Used

- **Programming Language:** Python 3.10
- **Libraries:**
  - `pyresparser` – NLP-based resume parsing
  - `pandas` – Data manipulation
  - `python-docx` – Handles DOCX formats if needed
  - `nltk` – Natural Language Toolkit used internally by pyresparser
  - `Streamlit` – Web UI framework
- **AI/NLP:** Used via pyresparser for structured data extraction
- **Filtering:** Based on keyword matching for skills, education, or experience

## 📦 Installation

Make sure Python **3.10+** is installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/Portfolio-Profile/resume-screener.git
   cd resume-screener
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv env
   env\Scripts\activate  # On Windows
   # OR
   source env/bin/activate  # On Mac/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m nltk.downloader all
   ```

## 📁 Project Structure

```
ResumeScreeningBot/
│
├── env/                          # Virtual environment (excluded via .gitignore)
├── .gitignore                    # Ignore rules
├── README.md                     # Project guide
├── requirements.txt              # Python dependencies
│
├── main.py                       # (Optional) CLI entry point
│
├── modules/                      # Backend logic
│   ├── __init__.py
│   ├── parser.py                 # Resume parsing logic
│   ├── matcher.py                # Filtering logic
│   ├── experience_analyzer.py    # Experience analyzer
│   └── utils.py                  # Utility functions
│
└── streamlit_app/
    └── streamlit_app.py          # Streamlit user interface
```

## ▶️ How to Run

Run the Streamlit app:
```bash
streamlit run streamlit_app/streamlit_app.py
```

The UI will open in your default browser. You can now upload resumes and apply filters.

## 🔗 Repository

GitHub Repo: [https://github.com/Portfolio-Profile/resume-screener](https://github.com/Portfolio-Profile/resume-screener)

