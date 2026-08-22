#!/usr/bin/env python3
"""
Import MATH dataset (hendrycks/competition_math) into amc10tooly format.
Outputs new SECTIONS entries that can be inserted into index.html.
"""
import json
import pandas as pd
from huggingface_hub import hf_hub_download

# Load dataset
print("Loading MATH dataset...")
path = hf_hub_download(repo_id='qwedsacf/competition_math', repo_type='dataset', 
                       filename='data/train-00000-of-00001-7320a6f3aba8ebd2.parquet')
df = pd.read_parquet(path)
print(f"Total problems: {len(df)}")
print("Types:", df['type'].value_counts().to_dict())
print("Levels:", df['level'].value_counts().to_dict())

# Problem schema in app: [num, prompt, solution, answer, hints[], source, difficulty]
# MATH has: problem, solution, type, level
# Answer is in the solution (boxed). We'll extract it.
import re

def extract_answer(solution):
    """Extract boxed answer from solution."""
    for pattern in [
        r"\\boxed\{([^}]+)\}",
        r"Answer\s*[:=]\s*([^\n.]+)",
        r"The answer is\s+([^\n.]+)",
    ]:
        m = re.search(pattern, solution, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return ""

# Build sections by type + level
sections = {}
for _, row in df.iterrows():
    ptype = row['type']  # Algebra, Geometry, Number Theory, Counting & Statistics, etc.
    level = row['level']  # Level 1-5
    if not level or level[-1] not in '12345':
        continue  # Skip unclassified
    
    key = f"{ptype.lower().replace(' ', '-').replace('&', 'and')}-level-{level[-1]}"
    if key not in sections:
        sections[key] = {
            "id": key,
            "title": f"{ptype} — Level {level[-1]}",
            "sub": f"MATH dataset {ptype} Level {level[-1]} problems",
            "type": "prac",
            "group": ptype,
            "levels": [{
                "n": f"Level {level[-1]}",
                "probs": []
            }]
        }
    
    prob_num = len(sections[key]["levels"][0]["probs"]) + 1
    answer = extract_answer(row['solution'])
    source = f"MATH dataset {ptype} Level {level[-1]}"
    difficulty = int(level[-1])  # 1-5
    
    sections[key]["levels"][0]["probs"].append([
        prob_num,
        row['problem'],
        row['solution'],
        answer,
        [],  # hints
        source,
        difficulty
    ])

# Output as JavaScript
print("\n// Generated sections for index.html")
for key in sorted(sections.keys()):
    sec = sections[key]
    sec["levels"][0]["probs"] = sec["levels"][0]["probs"][:50]  # Cap at 50 per section
    print(f"  // {sec['id']}: {len(sec['levels'][0]['probs'])} problems")
    
# Write full JSON for inspection
with open('/tmp/math_sections.json', 'w') as f:
    json.dump(sections, f, indent=2)
print("\nFull JSON written to /tmp/math_sections.json")