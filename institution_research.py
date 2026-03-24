#!/usr/bin/env python3
"""Research what institutions are publishing using OpenAlex API.

Usage: python3 institution_research.py "Institution Name"
"""

import urllib.request
import json
import sys
import ssl


def research_institution(name: str):
    """Look up an institution and its recent publications."""
    ctx = ssl.create_default_context()
    query = name.replace(" ", "+")

    # Find institution
    url = f"https://api.openalex.org/institutions?search={query}&per_page=1&mailto=example@example.com"
    req = urllib.request.Request(url, headers={"User-Agent": "OpenAlexTools/1.0"})
    resp = urllib.request.urlopen(req, context=ctx)
    data = json.loads(resp.read())

    if not data["results"]:
        print(f"No institution found: {name}")
        return

    inst = data["results"][0]
    inst_id = inst["id"].split("/")[-1]

    print(f"\n{'='*60}")
    print(f"  {inst['display_name']}")
    print(f"{'='*60}")
    print(f"  Type:         {inst.get('type', 'N/A')}")
    print(f"  Country:      {inst.get('country_code', 'N/A')}")
    print(f"  Total works:  {inst['works_count']:,}")
    print(f"  Citations:    {inst['cited_by_count']:,}")

    # Get recent top papers
    papers_url = (
        f"https://api.openalex.org/works?"
        f"filter=authorships.institutions.id:{inst_id},publication_year:2024-2025"
        f"&sort=cited_by_count:desc&per_page=5&mailto=example@example.com"
    )
    req = urllib.request.Request(papers_url, headers={"User-Agent": "OpenAlexTools/1.0"})
    resp = urllib.request.urlopen(req, context=ctx)
    papers = json.loads(resp.read())

    print(f"\n  Top Recent Papers (2024-2025):")
    print(f"  {'-'*55}")
    for p in papers["results"]:
        title = (p["title"] or "N/A")[:50]
        print(f"  [{p['publication_year']}] {title}... ({p['cited_by_count']} citations)")

    print(f"\n  Source: OpenAlex (openalex.org)\n")


def main():
    if len(sys.argv) < 2:
        print('Usage: python3 institution_research.py "Institution Name"')
        print('Example: python3 institution_research.py "Google DeepMind"')
        sys.exit(1)

    research_institution(sys.argv[1])


if __name__ == "__main__":
    main()
