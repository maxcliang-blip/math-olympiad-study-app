#!/usr/bin/env python3
"""
Scrape AoPS Wiki contest problem pages.
Target: pages like https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions
which have tables linking to individual year/problem pages.
"""
import re
import json
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

SESSION = requests.Session()
SESSION.headers.update({
    "User-Agent": "Mozilla/5.0 (compatible; MathAppScraper/1.0; +https://hub.laxmiang.work.gd/math/)"
})

def fetch(url):
    r = SESSION.get(url, timeout=20)
    r.raise_for_status()
    return r.text

def parse_aime_index(url):
    """Parse the main AIME index page for year links."""
    html = fetch(url)
    soup = BeautifulSoup(html, "lxml")
    years = []
    # AoPS wiki tables: look for links to AIME year pages
    for a in soup.find_all("a", href=True):
        href = a["href"]
        text = a.get_text(strip=True)
        if "/wiki/index.php/" in href and re.search(r"AIME_\d{4}", href):
            full = urljoin(url, href)
            year_match = re.search(r"AIME_(\d{4})", href)
            if year_match:
                years.append({"year": int(year_match.group(1)), "url": full, "label": text})
    return years

def parse_aime_year_page(url):
    """Parse a single AIME year page for problem links."""
    html = fetch(url)
    soup = BeautifulSoup(html, "lxml")
    problems = []
    # Problem links typically look like /wiki/index.php/2023_AIME_I_Problems/Problem_1
    for a in soup.find_all("a", href=True):
        href = a["href"]
        text = a.get_text(strip=True)
        m = re.search(r"/wiki/index\.php/(\d{4})_AIME_[I|II]_Problems/Problem_(\d+)", href)
        if m:
            year = int(m.group(1))
            prob_num = int(m.group(2))
            full = urljoin(url, href)
            problems.append({"year": year, "num": prob_num, "url": full, "label": text})
    return problems

def parse_problem_page(url):
    """Extract problem statement, answer, and solution from a problem page."""
    html = fetch(url)
    soup = BeautifulSoup(html, "lxml")
    
    # AoPS problem pages: problem in <div class="mw-parser-output">, first few paragraphs
    # Answer often in a box or explicit "Answer: X"
    content = soup.find("div", class_="mw-parser-output")
    if not content:
        return None
    
    text = content.get_text("\n", strip=True)
    
    # Try to find answer
    answer = None
    for pattern in [
        r"Answer\s*[:=]\s*([^\n.]+)",
        r"\\boxed\{([^}]+)\}",
        r"The answer is\s+([^\n.]+)",
    ]:
        m = re.search(pattern, text, re.IGNORECASE)
        if m:
            answer = m.group(1).strip()
            break
    
    # The problem statement is usually the first substantial paragraph(s)
    # Split by double newline, take first non-trivial chunk
    paragraphs = [p.strip() for p in text.split("\n\n") if len(p.strip()) > 50]
    problem_text = paragraphs[0] if paragraphs else text[:1000]
    
    return {
        "problem": problem_text,
        "answer": answer,
        "source_url": url
    }

def main():
    # Demo: AIME index
    index_url = "https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions"
    print(f"Fetching index: {index_url}")
    years = parse_aime_index(index_url)
    print(f"Found {len(years)} AIME years")
    for y in years[:3]:
        print(f"  {y['year']}: {y['url']}")
    
    if years:
        # Demo: first year page
        year_url = years[0]["url"]
        print(f"\nFetching year page: {year_url}")
        probs = parse_aime_year_page(year_url)
        print(f"Found {len(probs)} problems")
        for p in probs[:3]:
            print(f"  Problem {p['num']}: {p['url']}")
        
        # Demo: first problem
        if probs:
            prob_url = probs[0]["url"]
            print(f"\nFetching problem: {prob_url}")
            data = parse_problem_page(prob_url)
            print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()