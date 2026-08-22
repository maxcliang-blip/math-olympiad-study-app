#!/usr/bin/env python3
"""
MATH dataset importer - FINAL VERSION with comprehensive answer extraction.
"""
import re
import json
import pandas as pd
from huggingface_hub import hf_hub_download

print("Loading MATH dataset...")
path = hf_hub_download(repo_id='qwedsacf/competition_math', repo_type='dataset',
                       filename='data/train-00000-of-00001-7320a6f3aba8ebd2.parquet')
df = pd.read_parquet(path)
print(f"Total problems: {len(df)}")


def extract_answer(solution):
    """Extract final answer from solution text - comprehensive patterns."""
    if not isinstance(solution, str):
        return ""
    for pattern in [
        r"\\boxed\{([^}]+)\}",
        r"Answer\s*[:=]\s*([^\n.]+)",
        r"The answer is\s+([^\n.]+)",
        r"= \$\s*([^$]+)\s*\$",
        r"=\s*([^.\n]+)\.",
    ]:
        m = re.search(pattern, solution, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    # Fallback: last boxed-like or numeric expression
    m = re.search(r"(\d+(?:\.\d+)?(?:/\d+)?(?:\\pi|\\sqrt\{\d+\})?)\s*[.\n]", solution)
    if m:
        return m.group(1).strip()
    return ""


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

    problem = [prob_num, row['problem'], row['solution'], answer, [], source, difficulty]
    sections[key]["levels"][0]["probs"].append(problem)

# Generate JS using json.dumps (proper escaping)
print("\nGenerating JS sections...")
js_lines = []
for key in sorted(sections.keys()):
    sec = sections[key]
    sec["levels"][0]["probs"] = sec["levels"][0]["probs"][:50]

    probs_js = []
    for p in sec["levels"][0]["probs"]:
        probs_js.append("[" + ", ".join(json.dumps(x) for x in p) + "]")

    level_obj = {
        "n": f"Level {sec['id'][-1]}",
        "probs": json.loads("[" + ", ".join(probs_js) + "]")
    }

    sec_obj = {
        "id": sec["id"],
        "title": sec["title"],
        "sub": sec["sub"],
        "type": sec["type"],
        "group": sec["group"],
        "levels": [level_obj]
    }

    js_lines.append("  " + json.dumps(sec_obj) + ",")

result = "\n".join(js_lines)
with open('/tmp/new_sections_final.js', 'w') as f:
    f.write(result)

print(f"Written {len(sections)} sections to /tmp/new_sections_final.js")

# Validate
test = "[" + result.rstrip(',\n').rstrip() + "]"
obj = json.loads(test)
print(f"Validation: {len(obj)} sections, all parse as JSON")
total = sum(len(s['levels'][0]['probs']) for s in obj)
print(f"Total problems: {total}")
empty = sum(1 for s in obj for p in s['levels'][0]['probs'] if not p[3] or p[3].strip() == '')
print(f"Empty answers: {empty} ({100*empty/total:.1f}%)")
print(f"Non-empty: {total-empty} ({100*(total-empty)/total:.1f}%)")

# Sample with asy
for s in obj:
    for p in s['levels'][0]['probs']:
        if '[asy]' in p[1]:
            print(f"Sample with asy: {p[0]} answer={repr(p[3])}")
            break
    else:
        continue
    break