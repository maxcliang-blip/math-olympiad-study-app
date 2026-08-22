#!/usr/bin/env python3
"""
Import scraped AoPS AIME data into index.html as new practice sections.

Usage:
  python3 import_aops.py aops_2024.json aops_2023.json

Adds sections like "aops-2024-i" with problems split into 3 difficulty levels:
- Level 1 (Problems 1-5): Easy
- Level 2 (Problems 6-10): Medium  
- Level 3 (Problems 11-15): Hard

Each problem gets: num, prompt, solution, answer, hints, source, topic, difficulty
"""
import json
import re
import sys

TOPICS = ["Algebra", "Geometry", "Number Theory", "Combinatorics", "Prealgebra", "Precalculus", "Intermediate Algebra"]

def load_scraped(paths):
    data = {}
    for p in paths:
        d = json.load(open(p))
        for k, v in d.items():
            data[k] = v
    return data

def detect_topic(prompt):
    prompt_lower = prompt.lower()
    if any(kw in prompt_lower for kw in ["circle", "triangle", "angle", "polygon", "geometry", "area", "volume", "coordinate", "trig"]):
        return "Geometry"
    elif any(kw in prompt_lower for kw in ["probability", "ways", "arrange", "choose", "count", "combination", "permutation", "pigeonhole"]):
        return "Combinatorics"
    elif any(kw in prompt_lower for kw in ["prime", "divisible", "mod", "gcd", "lcm", "integer", "factor", "divisor", "remainder"]):
        return "Number Theory"
    else:
        return "Algebra"

def difficulty_from_num(num):
    """AIME problems 1-15: 1-5 Easy, 6-10 Medium, 11-15 Hard"""
    if num <= 5:
        return 1  # Easy
    elif num <= 10:
        return 2  # Medium
    else:
        return 3  # Hard

def make_sections(year_id, problems):
    """Build section objects matching the app's format, split by difficulty."""
    title = year_id.replace("_", " ")
    year = year_id.split("_")[0]
    group = f"AoPS AIME {year}"
    
    # Group problems by difficulty
    by_diff = {1: [], 2: [], 3: []}
    for p in problems:
        num = p.get("num", 0)
        diff = difficulty_from_num(num)
        
        prompt = p.get("problem", "").strip()
        solutions = p.get("solutions", [])
        solution_text = "\n\n---\n\n".join(solutions) if solutions else ""
        answer = str(p.get("answer", ""))
        topic = detect_topic(prompt)
        
        prob_entry = [num, prompt, solution_text, answer, [], f"AoPS {title}", topic]
        by_diff[diff].append(prob_entry)
    
    # Create one section per difficulty level
    sections = []
    diff_names = {1: "Level 1 (Easy)", 2: "Level 2 (Medium)", 3: "Level 3 (Hard)"}
    
    for diff in [1, 2, 3]:
        probs = by_diff[diff]
        if not probs:
            continue
            
        sec_id = f"aops-{year_id.lower().replace('_', '-')}-diff{diff}"
        sections.append({
            "id": sec_id,
            "title": f"{title} {diff_names[diff]}",
            "sub": f"AoPS Wiki {title} {diff_names[diff]} — {len(probs)} problems",
            "type": "prac",
            "group": group,
            "levels": [{"n": diff_names[diff], "probs": probs}]
        })
    
    return sections

def insert_sections(html, sections):
    arr_start = html.index("const SECTIONS = [")
    state_idx = html.index("// State")
    arr_end = html.rfind("];", arr_start, state_idx) + 2
    
    for section in sections:
        if section["id"] in html[arr_start:arr_end]:
            print(f"  Section {section['id']} already present, skipping")
            continue
        
        insert_pos = arr_end - 2
        pre = html[insert_pos-3:insert_pos]
        comma = ",\n" if not pre.rstrip().endswith(",") else "\n"
        
        section_json = json.dumps(section, ensure_ascii=False, separators=(',', ':'))
        html = html[:insert_pos] + comma + "  " + section_json + "\n" + html[insert_pos:]
        arr_end = html.rfind("];", arr_start, state_idx) + 2  # update arr_end
    
    return html

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 import_aops.py file1.json [file2.json ...]")
        return
    
    scraped = load_scraped(sys.argv[1:])
    print(f"Loaded {len(scraped)} year(s)")
    
    html = open("index.html", encoding="utf-8").read()
    
    all_sections = []
    for year_id, problems in scraped.items():
        print(f"Processing {year_id} ({len(problems)} problems)...")
        sections = make_sections(year_id, problems)
        all_sections.extend(sections)
        for s in sections:
            print(f"  {s['id']}: {len(s['levels'][0]['probs'])} problems")
    
    html = insert_sections(html, all_sections)
    
    open("index.html", "w", encoding="utf-8").write(html)
    print(f"\nDone. Added {len(all_sections)} difficulty-split sections.")

if __name__ == "__main__":
    main()