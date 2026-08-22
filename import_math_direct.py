#!/usr/bin/env python3
"""
Direct import: MATH dataset -> JS sections inserted into index.html
Writes properly escaped JavaScript directly.
"""
import json
import pandas as pd
from huggingface_hub import hf_hub_download

print("Loading MATH dataset...")
path = hf_hub_download(repo_id='qwedsacf/competition_math', repo_type='dataset', 
                       filename='data/train-00000-of-00001-7320a6f3aba8ebd2.parquet')
df = pd.read_parquet(path)
print(f"Total problems: {len(df)}")

import re

def extract_answer(solution):
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
    ptype = row['type']
    level = row['level']
    if not level or level[-1] not in '12345':
        continue
    
    key = f"{ptype.lower().replace(' ', '-').replace('&', 'and')}-level-{level[-1]}"
    if key not in sections:
        sections[key] = {
            "id": key,
            "title": f"{ptype} \u2014 Level {level[-1]}",
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
    difficulty = int(level[-1])
    
    # Store raw strings - we'll JSON-dump them when writing JS
    sections[key]["levels"][0]["probs"].append({
        "num": prob_num,
        "prompt": row['problem'],
        "solution": row['solution'],
        "answer": answer,
        "hints": [],
        "source": source,
        "difficulty": difficulty
    })

# Write JavaScript directly with proper escaping
print("\nGenerating JS sections...")
js_lines = []
for key in sorted(sections.keys()):
    sec = sections[key]
    # Cap at 50
    sec["levels"][0]["probs"] = sec["levels"][0]["probs"][:50]
    
    # Build the section object as JS using json.dumps for all strings
    probs_js = []
    for p in sec["levels"][0]["probs"]:
        prob_arr = [
            p["num"],
            p["prompt"],
            p["solution"],
            p["answer"],
            p["hints"],
            p["source"],
            p["difficulty"]
        ]
        probs_js.append("[" + ", ".join(json.dumps(x) for x in prob_arr) + "]")
    
    level_js = json.dumps({
        "n": f"Level {sec['id'][-1]}",
        "probs": json.loads("[" + ", ".join(probs_js) + "]")  # parse back to get proper nesting
    })
    
    sec_obj = {
        "id": sec["id"],
        "title": sec["title"],
        "sub": sec["sub"],
        "type": sec["type"],
        "group": sec["group"],
        "levels": [json.loads(level_js)]
    }
    
    js_lines.append("  " + json.dumps(sec_obj) + ",")

result = "\n".join(js_lines)

with open('/tmp/new_sections_direct.js', 'w') as f:
    f.write(result)

print(f"Written {len(sections)} sections to /tmp/new_sections_direct.js")
print("First 500 chars:")
print(result[:500])