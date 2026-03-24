#!/usr/bin/env python3
"""Search the most-cited papers on any topic using OpenAlex API.

Usage: python3 search_papers.py "large language models" [limit]

No API key needed. No pip install. Uses Python stdlib only.
"""

import urllib.request
import json
import sys
import ssl


def search_papers(topic: str, limit: int = 10) -> list:
    """Search for most-cited papers on a topic."""
    ctx = ssl.create_default_context()
    query = topic.replace(" ", "+")
    url = (
        f"https://api.openalex.org/works?"
        f"search={query}&sort=cited_by_count:desc&per_page={limit}"
        f"&mailto=example@example.com"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "OpenAlexTools/1.0"})
    response = urllib.request.urlopen(req, context=ctx)
    data = json.loads(response.read())

    results = []
    for work in data["results"]:
        results.append({
            "title": work["title"],
            "year": work["publication_year"],
            "citations": work["cited_by_count"],
            "doi": work.get("doi"),
            "type": work.get("type"),
            "open_access": work.get("open_access", {}).get("is_oa", False),
        })
    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 search_papers.py \"topic\" [limit]")
        print("Example: python3 search_papers.py \"large language models\" 10")
        sys.exit(1)

    topic = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    print(f"\nTop {limit} most-cited papers on: {topic}\n")
    print(f"{'#':>3} {'Year':>5} {'Citations':>10}  {'Title'}")
    print("-" * 80)

    papers = search_papers(topic, limit)
    for i, p in enumerate(papers, 1):
        oa = "🔓" if p["open_access"] else "🔒"
        title = p["title"][:55] if p["title"] else "N/A"
        print(f"{i:>3} {p['year']:>5} {p['citations']:>10,}  {oa} {title}")

    print(f"\nTotal results shown: {len(papers)}")
    print(f"Source: OpenAlex (openalex.org) — free, no API key needed")


if __name__ == "__main__":
    main()
