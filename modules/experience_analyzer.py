from datetime import datetime
from dateutil import parser

def parse_date(date_str):
    try:
        return parser.parse(date_str)
    except:
        return None

def calculate_total_experience_months(experience_list):
    total_months = 0
    for exp in experience_list:
        start = parse_date(exp.get("start_date", ""))
        end = parse_date(exp.get("end_date", ""))

        if start and end:
            months = (end.year - start.year) * 12 + (end.month - start.month)
            total_months += max(months, 0)
    return total_months
