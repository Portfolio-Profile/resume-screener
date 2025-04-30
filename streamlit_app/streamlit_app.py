import os, sys

# Tell Python where to find our modules folder
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import streamlit as st
import tempfile
import os
import pandas as pd
import plotly.express as px
from modules.parser import parse_resume
from modules.matcher import compute_relevance
from modules.experience_analyzer import calculate_total_experience_months

st.set_page_config(page_title="🚀 AI Resume Screener Pro", layout="wide")
st.title("🚀 Intelligent Resume Screener Pro")

uploaded_files = st.file_uploader("Upload Resume(s)", type=["pdf", "docx"], accept_multiple_files=True)
job_desc = st.text_area("Paste Job Description Keywords (e.g. python, machine learning)", height=150)

if st.button("Run Screening"):
    results = []
    all_skills = []
    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        parsed = parse_resume(tmp_path)
        matching = compute_relevance(parsed, job_desc or "")
        combined = {**parsed, **matching}
        results.append(combined)
        all_skills.extend(parsed.get('skills', []))

    if results:
        results = sorted(results, key=lambda x: x['final_score'], reverse=True)

        st.subheader("🎯 Top Matching Resumes")

        for idx, r in enumerate(results[:5]):
            st.markdown(f"### {idx+1}. {r.get('name', 'Resume')}")
            st.progress(int(r.get('final_score', 0)))
            st.markdown(f"**Matched Skills:** {', '.join(r.get('matched_skills', []))}")
            st.markdown(f"**Final Score:** {r.get('final_score', 0)}%")
            st.markdown(f"**All Extracted Skills:** {', '.join(r.get('skills', []))}")
            st.markdown(f"**Education:** {', '.join(r.get('education', []))}")

            # ✅ Only show Working Experience
            st.subheader("🛠️ Working Experience")
            total_months = calculate_total_experience_months(r.get('experience', []))
            total_years = round(total_months / 12, 2)
            st.markdown(f"**Total Working Experience:** {total_years} years ({total_months} months)")

            st.divider()

        # 📊 Skill Match Graph
        st.subheader("📊 Skill Match Percentage")
        df = pd.DataFrame({
            "Resume": [r.get('name', f"Resume {i+1}") for i, r in enumerate(results)],
            "Score": [round(r.get('final_score', 0) * 100, 1) for r in results]
        })
        fig = px.bar(df, x="Resume", y="Score", color="Score", text_auto=True, height=400)
        st.plotly_chart(fig)

        # 📈 All Skills Pie Chart
        st.subheader("📈 Skills Distribution Across Resumes")
        skill_counts = pd.Series(all_skills).value_counts().reset_index()
        skill_counts.columns = ['Skill', 'Count']
        pie_fig = px.pie(skill_counts, names='Skill', values='Count', height=500)
        st.plotly_chart(pie_fig)

    else:
        st.warning("❗ No resumes matched the Job Description skills.")
