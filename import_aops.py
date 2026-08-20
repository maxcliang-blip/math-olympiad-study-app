#!/usr/bin/env python3
"""
Import scraped AoPS AIME data into index.html as new practice sections.

Usage:
  python3 import_aops.py aops_2024.json           # import one file
  python3 import_aops.py aops_2024.json aops_2023.json  # import multiple

Adds sections like "aops-2024-i" and "aops-2024-ii" with all 15 problems.
"""
import json
import re
import sys

TOPICS = ["Algebra", "Geometry", "Number Theory", "Combinatorics", "Prealgebra", "Precalculus", "Intermediate Algebra"]

def load_scraped(paths):
    """Load scraped JSON files, returning {year_id: [problems]}."""
    data = {}
    for p in paths:
        d = json.load(open(p))
        for k, v in d.items():
            data[k] = v
    return data

def make_section(year_id, problems):
    """Build a section object matching the app's format."""
    # year_id like "2024_AIME_I" -> title "2024 AIME I"
    title = year_id.replace("_", " ")
    sec_id = "aops-" + year_id.lower().replace("_", "-")
    # Group by year
    year = year_id.split("_")[0]
    group = f"AoPS AIME {year}"
    
    # Build problems array: [[num, prompt, solution, answer, hints, source, topic]]
    probs = []
    for p in problems:
        num = p.get("num", 0)
        prompt = p.get("problem", "").strip()
        solutions = p.get("solutions", [])
        solution_text = "\n\n---\n\n".join(solutions) if solutions else ""
        answer = str(p.get("answer", ""))
        # Topic detection (simple heuristic)
        topic = "Algebra"
        if any(kw in prompt.lower() for kw in ["circle", "triangle", "angle", "polygon", "geometry", "area", "volume"]):
            topic = "Geometry"
        elif any(kw in prompt.lower() for kw in ["probability", "ways", "arrange", "choose", "count"]):
            topic = "Combinatorics"
        elif any(kw in prompt.lower() for kw in ["prime", "divisible", "mod", "gcd", "lcm", "integer"]):
            topic = "Number Theory"
        
        probs.append([num, prompt, solution_text, answer, [], f"AoPS {title}", topic])
    
    return {
        "id": sec_id,
        "title": title,
        "sub": f"AoPS Wiki {title} — {len(probs)} problems",
        "type": "prac",
        "group": group,
        "levels": [{"n": f"{title}", "probs": probs}]
    }

def insert_section(html, section):
    """Insert section into SECTIONS array before '];' near // State."""
    arr_start = html.index("const SECTIONS = [")
    state_idx = html.index("// State")
    arr_end = html.rfind("];", arr_start, state_idx) + 2
    arr = html[arr_start:arr_end]
    
    # Check if already inserted
    if section["id"] in arr:
        print(f"  Section {section['id']} already present, skipping")
        return html
    
    # Find the last section object end (before the final ];)
    # Insert before the last '];' that closes the array
    insert_pos = arr_end - 2  # before '];'
    # Ensure we have a comma if needed
    pre = html[insert_pos-3:insert_pos]
    comma = ",\n" if not pre.rstrip().endswith(",") else "\n"
    
    section_json = json.dumps(section, ensure_ascii=False, indent=2)
    # Convert to JS object literal (JSON is valid JS)
    html = html[:insert_pos] + comma + "  " + section_json + "\n" + html[insert_pos:]
    return html

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 import_aops.py file1.json [file2.json ...]")
        return
    
    scraped = load_scraped(sys.argv[1:])
    print(f"Loaded {len(scraped)} year(s)")
    
    html = open("index.html", encoding="utf-8").read()
    
    for year_id, problems in scraped.items():
        print(f"Adding {year_id} ({len(problems)} problems)...")
        section = make_section(year_id, problems)
        html = insert_section(html, section)
    
    open("index.html", "w", encoding="utf-8").write(html)
    print("Done. index.html updated.")

if __name__ == "__main__":
    main()
