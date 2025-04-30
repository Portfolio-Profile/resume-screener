from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

sbert = SentenceTransformer('all-MiniLM-L6-v2')

# modules/matcher.py

def compute_relevance(parsed_resume: dict, job_description: str) -> dict:
    """
    Simple exact‐match scoring:
      - final_score = (matched_count / total_jd_keywords) * 100
      - keyword_score == final_score
      - semantic_score = 0.0 (not used)
    """
    # 1. Lowercase all skills
    resume_skills = [s.lower() for s in parsed_resume.get("skills", [])]
    # 2. Split JD on commas and lowercase
    jd_keywords   = [kw.strip().lower() for kw in job_description.split(",") if kw.strip()]

    # 3. Compute matched skills
    matched_skills = list(set(resume_skills) & set(jd_keywords))

    # 4. Calculate ratio
    ratio = len(matched_skills) / len(jd_keywords) if jd_keywords else 0.0

    # 5. Final score out of 100
    final_score   = round(ratio * 100, 2)
    keyword_score = final_score
    semantic_score = 0.0

    return {
        "matched_skills": matched_skills,
        "keyword_score": keyword_score,
        "semantic_score": semantic_score,
        "final_score": final_score,
    }

def semantic_score(resume_text, jd_text):
    emb = sbert.encode([resume_text, jd_text])
    return cosine_similarity([emb[0]], [emb[1]])[0, 0]
