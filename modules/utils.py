# modules/utils.py
import re
from datetime import datetime


def clean_text(text: str) -> str:
    """
    Lowercase, collapse whitespace, strip.
    """
    text = text.lower()
    return re.sub(r"\s+", " ", text).strip()


def compute_years_experience(experience_str: str) -> float:
    """
    Parses strings like '3 years', '2.5 years' and returns float.
    """
    try:
        num = float(experience_str.split()[0])
        return num
    except:
        return 0.0