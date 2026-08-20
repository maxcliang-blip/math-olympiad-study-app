#!/usr/bin/env python3
"""
AoPS AIME Scraper - Robust version with proper rate limiting.
Resumes from existing data, handles 429 errors with exponential backoff.
"""
import json
import os
import re
import time
import random
from curl_cffi import requests
from bs4 import BeautifulSoup

BASE = "https://artofproblemsolving.com"
IMPERSONATE = "chrome124"
DATA_FILE = "aops_all.json"

# Rate limiting config
MIN_DELAY = 2.5      # seconds between requests
MAX_DELAY = 4.0      # max delay
JITTER = 0.5         # random jitter
MAX_RETRIES = 5      # retries on 429

def get_soup(url, retries=MAX_RETRIES):
    for attempt in range(retries):
        delay = random.uniform(MIN_DELAY, MAX_DELAY)
        time.sleep(delay)
        
        r = requests.get(url, impersonate=IMPERSONATE, timeout=30)
        if r.status_code == 200:
            return BeautifulSoup(r.text, "html.parser")
        elif r.status_code == 429:
            wait = (2 ** attempt) * 2 + random.uniform(0, 1)
            print(f"  [429] Rate limited, waiting {wait:.1f}s (attempt {attempt+1}/{retries})")
            time.sleep(wait)
        else:
            print(f"  HTTP {r.status_code} for {url}")
            return None
    return None

def content_div(soup):
    return soup.find("div", {"id": "mw-content-text"}) or soup.find("div", class_="mw-parser-output")

def img_to_latex(tag):
    for img in tag.find_all("img", alt=True):
        alt = img.get("alt", "")
        if alt.startswith("$") and alt.endswith("$"):
            latex = alt[1:-1]
            img.replace_with(soup_new_latex(latex, img))
    return tag

def soup_new_latex(latex, orig_img):
    from bs4 import NavigableString
    return NavigableString(f"${latex}$")

def get_year_links():
    url = f"{BASE}/wiki/index.php/AIME_Problems_and_Solutions"
    soup = get_soup(url)
    if not soup:
        return []
    content = content_div(soup)
    years = []
    if content:
        for table in content.find_all("table"):
            for link in table.find_all("a", href=True):
                m = re.search(r"title=(\d{4}_AIME_[IV]+)", link["href"])
                if m:
                    yr = m.group(1)
                    if yr not in [y["id"] for y in years]:
                        years.append({"id": yr, "url": f"{BASE}/wiki/index.php/{yr}"})
    return years

def get_problem_links(year_url):
    soup = get_soup(year_url)
    if not soup:
        return []
    content = content_div(soup)
    probs = []
    if content:
        for link in content.find_all("a", href=True):
            href = link["href"]
            text = link.get_text(strip=True)
            if "Problems/Problem_" in href:
                m = re.search(r"Problem (\d+)", text)
                if m:
                    probs.append({"num": int(m.group(1)), "url": f"{BASE}{href}"})
    return sorted(probs, key=lambda x: x["num"])

def get_answer_key(year_id):
    url = f"{BASE}/wiki/index.php/{year_id}_Answer_Key"
    soup = get_soup(url)
    if not soup:
        return []
    content = content_div(soup)
    answers = []
    if content:
        for line in content.get_text().split("\n"):
            line = line.strip()
            if re.match(r"^\d{1,4}$", line):
                answers.append(int(line))
    return answers

def get_problem(prob_url):
    soup = get_soup(prob_url)
    if not soup:
        return {}
    content = content_div(soup)
    if not content:
        return {}
    
    headings = content.find_all(["h1", "h2", "h3", "h4"])
    problem_text = ""
    solutions = []
    for h in headings:
        htext = h.get_text(strip=True).lower()
        if htext == "problem":
            parts = []
            for sib in h.find_next_siblings():
                if sib.name in ["h1", "h2", "h3", "h4"]:
                    break
                if sib.name == "p":
                    parts.append(str(sib))
            if parts:
                p_soup = BeautifulSoup("".join(parts), "html.parser")
                img_to_latex(p_soup)
                problem_text = p_soup.get_text().strip()
        elif htext.startswith("solution"):
            sol_parts = []
            for sib in h.find_next_siblings():
                if sib.name in ["h1", "h2", "h3", "h4"]:
                    break
                if sib.name == "p":
                    sol_parts.append(str(sib))
            if sol_parts:
                s_soup = BeautifulSoup("".join(sol_parts), "html.parser")
                img_to_latex(s_soup)
                solutions.append(s_soup.get_text().strip())
    return {"problem": problem_text, "solutions": solutions}

def load_existing():
    if os.path.exists(DATA_FILE):
        return json.load(open(DATA_FILE))
    return {}

def save_data(data):
    json.dump(data, open(DATA_FILE, "w"), indent=2)

def scrape_year(year):
    yid = year["id"]
    print(f"  Scraping {yid}...")
    
    probs = get_problem_links(year["url"])
    answers = get_answer_key(yid)
    print(f"    {len(probs)} problems, {len(answers)} answers")
    
    result = []
    for p in probs:
        data = get_problem(p["url"])
        data["num"] = p["num"]
        if p["num"] - 1 < len(answers):
            data["answer"] = answers[p["num"] - 1]
        result.append(data)
        ok = "OK" if data.get("problem") else "EMPTY"
        print(f"    Problem {p['num']}: {ok}")
    
    return result

def main():
    print("=== AoPS AIME Scraper (Robust) ===")
    
    # Load existing
    all_data = load_existing()
    print(f"Loaded {len(all_data)} years from {DATA_FILE}")
    
    # Get all year links
    years = get_year_links()
    print(f"Found {len(years)} year pages on AoPS")
    
    # Find incomplete/empty years
    incomplete = []
    for y in years:
        yid = y["id"]
        existing = all_data.get(yid, [])
        if not existing:
            incomplete.append((y, "empty"))
        else:
            ok = sum(1 for p in existing if p.get("problem"))
            if ok < len(existing):
                incomplete.append((y, f"partial ({ok}/{len(existing)})"))
    
    print(f"Years to scrape: {len(incomplete)}")
    for y, status in incomplete:
        print(f"  {y['id']}: {status}")
    
    if not incomplete:
        print("All years complete!")
        return
    
    # Scrape each incomplete year
    for i, (year, status) in enumerate(incomplete):
        print(f"\n[{i+1}/{len(incomplete)}] {year['id']} ({status})")
        result = scrape_year(year)
        all_data[year["id"]] = result
        save_data(all_data)
        print(f"  Saved. Total years in file: {len(all_data)}")
    
    # Final stats
    save_data(all_data)
    total_probs = sum(len(v) for v in all_data.values())
    filled = sum(1 for v in all_data.values() for p in v if p.get("problem"))
    print(f"\n=== DONE ===")
    print(f"Total years: {len(all_data)}")
    print(f"Total problems: {total_probs}")
    print(f"Problems with text: {filled}")
    for k, v in sorted(all_data.items()):
        ok = sum(1 for p in v if p.get("problem"))
        print(f"  {k}: {ok}/{len(v)}")

if __name__ == "__main__":
    main()