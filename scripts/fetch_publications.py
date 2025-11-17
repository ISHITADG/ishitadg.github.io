#!/usr/bin/env python3
"""
Google Scholar Publications Fetcher
Fetches publications from Google Scholar and generates Jekyll-compatible markdown files.
"""

import requests
from bs4 import BeautifulSoup
import json
import os
import re
from datetime import datetime, timedelta
from pathlib import Path
import time
import sys

# Configuration
SCHOLAR_ID = "okBrMn8AAAAJ"
SCHOLAR_URL = f"https://scholar.google.com/citations?hl=en&user={SCHOLAR_ID}&view_op=list_works&sortby=pubdate"
OUTPUT_DIR = Path(__file__).parent.parent / "_publications"
RECENT_MONTHS = 3  # For filtering recent publications

# Headers to mimic a browser request
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}


def parse_publication_date(date_str):
    """Parse publication date from various formats."""
    if not date_str:
        return None
    
    # Try to extract year
    year_match = re.search(r'\d{4}', date_str)
    if year_match:
        year = int(year_match.group())
        # Assume recent publications are from current year or last year
        current_year = datetime.now().year
        if year == current_year or year == current_year - 1:
            # For recent publications, try to parse month if available
            month_keywords = {
                'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
            }
            date_lower = date_str.lower()
            for month_name, month_num in month_keywords.items():
                if month_name in date_lower:
                    try:
                        return datetime(year, month_num, 1)
                    except:
                        pass
            # If no month found, assume beginning of year
            return datetime(year, 1, 1)
        return datetime(year, 1, 1)
    return None


def is_recent_publication(pub_date, months=RECENT_MONTHS):
    """Check if publication is within the last N months."""
    if not pub_date:
        return False
    cutoff_date = datetime.now() - timedelta(days=months * 30)
    return pub_date >= cutoff_date


def fetch_publications():
    """Fetch publications from Google Scholar."""
    print(f"Fetching publications from Google Scholar (ID: {SCHOLAR_ID})...")
    
    try:
        response = requests.get(SCHOLAR_URL, headers=HEADERS, timeout=30)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching Google Scholar page: {e}")
        print("Note: Google Scholar may block automated requests. Consider using SerpAPI or manual updates.")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    publications = []
    
    # Find all publication entries
    pub_entries = soup.find_all('tr', class_='gsc_a_tr')
    
    if not pub_entries:
        print("No publications found. Google Scholar may have changed its structure.")
        print("Consider using SerpAPI (https://serpapi.com/google-scholar-api) for more reliable access.")
        return []
    
    print(f"Found {len(pub_entries)} publications")
    
    for entry in pub_entries:
        try:
            # Extract title
            title_elem = entry.find('a', class_='gsc_a_at')
            if not title_elem:
                continue
            
            title = title_elem.get_text(strip=True)
            pub_link = f"https://scholar.google.com{title_elem.get('href', '')}"
            
            # Extract authors and venue
            author_venue_elem = entry.find('div', class_='gs_gray')
            if author_venue_elem:
                author_venue_text = author_venue_elem.get_text(strip=True)
                # Try to split authors and venue (usually separated by " - ")
                parts = author_venue_text.split(' - ', 1)
                authors = parts[0] if parts else ""
                venue = parts[1] if len(parts) > 1 else ""
            else:
                authors = ""
                venue = ""
            
            # Extract year
            year_elem = entry.find('span', class_='gsc_a_y')
            year = None
            if year_elem:
                year_text = year_elem.get_text(strip=True)
                year_match = re.search(r'\d{4}', year_text)
                if year_match:
                    year = int(year_match.group())
            
            # Extract citations
            citations_elem = entry.find('a', class_='gsc_a_c')
            citations = 0
            if citations_elem:
                citations_text = citations_elem.get_text(strip=True)
                citations_match = re.search(r'\d+', citations_text)
                if citations_match:
                    citations = int(citations_match.group())
            
            # Try to parse publication date
            pub_date = None
            if year:
                pub_date = datetime(year, 1, 1)  # Default to beginning of year
            
            publications.append({
                'title': title,
                'authors': authors,
                'venue': venue,
                'year': year,
                'citations': citations,
                'link': pub_link,
                'date': pub_date
            })
            
        except Exception as e:
            print(f"Error parsing publication entry: {e}")
            continue
    
    return publications


def generate_markdown(pub, index):
    """Generate Jekyll markdown file for a publication."""
    # Create a safe filename from title
    safe_title = re.sub(r'[^\w\s-]', '', pub['title']).strip()
    safe_title = re.sub(r'[-\s]+', '-', safe_title)
    filename = f"{pub['year'] or 'unknown'}-{safe_title[:50]}.md"
    filename = filename.lower()
    
    # Format authors (highlight if "Ishita Dasgupta" or "Dasgupta" is in authors)
    authors = pub['authors']
    if 'Dasgupta' in authors or 'Ishita' in authors:
        # Bold the author name
        authors = re.sub(r'(\bIshita\s+Dasgupta\b|\bDasgupta,?\s+I\b)', r'**\1**', authors, flags=re.IGNORECASE)
    
    # Generate markdown content
    # Use a default date if none available (Jekyll requires valid dates)
    if pub['date']:
        date_str = pub['date'].strftime('%Y-%m-%d')
    elif pub['year']:
        date_str = f"{pub['year']}-01-01"
    else:
        date_str = "2024-01-01"  # Default fallback
    
    content = f"""---
layout: publication
title: "{pub['title']}"
authors: "{authors}"
venue: "{pub['venue']}"
year: {pub['year'] or 'null'}
citations: {pub['citations']}
link: "{pub['link']}"
date: {date_str}
---

## Abstract

[Abstract will be added manually or fetched from another source]

## Links

- [Google Scholar]({pub['link']})
"""
    
    return filename, content


def save_publications(publications):
    """Save publications as markdown files."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Clear existing publications (optional - comment out if you want to keep manual edits)
    # for file in OUTPUT_DIR.glob("*.md"):
    #     file.unlink()
    
    recent_pubs = []
    saved_count = 0
    
    for i, pub in enumerate(publications):
        try:
            filename, content = generate_markdown(pub, i)
            filepath = OUTPUT_DIR / filename
            
            # Write file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            saved_count += 1
            
            # Check if recent
            if is_recent_publication(pub['date']):
                recent_pubs.append(pub)
                
        except Exception as e:
            print(f"Error saving publication '{pub['title']}': {e}")
            continue
    
    print(f"Saved {saved_count} publications to {OUTPUT_DIR}")
    print(f"Found {len(recent_pubs)} publications from the last {RECENT_MONTHS} months")
    
    # Save recent publications list as JSON for easy access
    recent_file = Path(__file__).parent.parent / "_data" / "recent_publications.json"
    recent_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(recent_file, 'w', encoding='utf-8') as f:
        json.dump(recent_pubs, f, indent=2, default=str)
    
    return recent_pubs


def main():
    """Main function."""
    print("=" * 60)
    print("Google Scholar Publications Fetcher")
    print("=" * 60)
    
    publications = fetch_publications()
    
    if not publications:
        print("\nNo publications found. Exiting.")
        sys.exit(1)
    
    recent_pubs = save_publications(publications)
    
    print("\n" + "=" * 60)
    print("Summary:")
    print(f"  Total publications: {len(publications)}")
    print(f"  Recent publications (last {RECENT_MONTHS} months): {len(recent_pubs)}")
    print("=" * 60)
    
    if recent_pubs:
        print("\nRecent publications:")
        for pub in recent_pubs[:5]:  # Show first 5
            print(f"  - {pub['title']} ({pub['year']})")


if __name__ == "__main__":
    main()

