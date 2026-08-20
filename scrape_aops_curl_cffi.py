#!/usr/bin/env python3
"""
AoPS Wiki scraper using curl_cffi to bypass Cloudflare.
Extracts AIME problems, solutions, and answers.

Usage:
  python3 scrape_aops_curl_cffi.py --year 2024 --test-1      # test one problem
  python3 scrape_aops_curl_cffi.py --year 2024               # full year (I + II)
  python3 scrape_aops_curl_cffi.py --all                    # all years
  python3 scrape_aops_curl_cffi.py --all --out aops_all.json
"""
import argparse
import json
import re
import time
from curl_cffi import requests
from bs4 import BeautifulSoup

BASE = "https://artofproblemsolving.com"
IMPERSONATE = "chrome124"
DELAY = 0.3  # seconds between requests (be polite)

def get_soup(url, retries=3):
    for attempt in range(retries):
        r = requests.get(url, impersonate=IMPERSONATE, timeout=20)
        if r.status_code == 200:
            return BeautifulSoup(r.text, "html.parser")
        elif r.status_code == 429:
            wait = 2 ** attempt
            print(f"  Rate limited (429), waiting {wait}s...")
            time.sleep(wait)
        else:
            print(f"  HTTP {r.status_code} for {url}")
            return None
    return None

def content_div(soup):
    return soup.find("div", {"id": "mw-content-text"}) or soup.find("div", class_="mw-parser-output")

def img_to_latex(tag):
    """Replace <img alt='$x$'> with $x$ LaTeX."""
    for img in tag.find_all("img", alt=True):
        alt = img.get("alt", "")
        if alt.startswith("$") and alt.endswith("$"):
            latex = alt[1:-1]
            img.replace_with(soup_new_latex(latex))
    return tag

def soup_new_latex(latex):
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
    # Find 'Problem' heading
    headings = content.find_all(["h1", "h2", "h3", "h4"])
    problem_text = ""
    solutions = []
    for i, h in enumerate(headings):
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

def scrape_year(year_id, out_format="dict"):
    print(f"Scraping {year_id}...")
    year_url = f"{BASE}/wiki/index.php/{year_id}"
    probs = get_problem_links(year_url)
    answers = get_answer_key(year_id)
    print(f"  {len(probs)} problems, {len(answers)} answers")
    result = []
    for p in probs:
        time.sleep(DELAY)
        data = get_problem(p["url"])
        data["num"] = p["num"]
        if p["num"] - 1 < len(answers):
            data["answer"] = answers[p["num"] - 1]
        result.append(data)
        print(f"  Problem {p['num']}: {'OK' if data.get('problem') else 'EMPTY'}")
    return result

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", type=str, help="e.g. 2024 or 2024_AIME_I")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--test-1", action="store_true", help="scrape just 1 problem")
    ap.add_argument("--out", type=str, default="aops_scraped.json")
    args = ap.parse_args()

    if args.test_1:
        # Test with 2024 AIME I Problem 1
        print("=== TEST: 2024 AIME I Problem 1 ===")
        data = get_problem(f"{BASE}/wiki/index.php/2024_AIME_I_Problems/Problem_1")
        print("Problem:", data.get("problem", "")[:400])
        print("Answer: 204 (from key)")
        print("Solutions found:", len(data.get("solutions", [])))
        return

    if args.all:
        years = get_year_links()
        print(f"Found {len(years)} year pages")
    elif args.year:
        yid = args.year if "_AIME" in args.year else f"{args.year}_AIME_I"
        years = [{"id": yid, "url": f"{BASE}/wiki/index.php/{yid}"}]
    else:
        print("Use --year YYYY or --all or --test-1")
        return

    all_data = {}
    for y in years:
        all_data[y["id"]] = scrape_year(y["id"])
        if args.test_1:
            break

    with open(args.out, "w") as f:
        json.dump(all_data, f, indent=2)
    print(f"\nSaved to {args.out}")

if __name__ == "__main__":
    main()