#!/usr/bin/env python3
"""Look up researcher profiles using OpenAlex API.

Usage: python3 author_lookup.py "Author Name"

No API key needed.
"""

import urllib.request
import json
import sys
import ssl


def lookup_author(name: str) -> dict:
    """Look up an author by name and return their profile."""
    ctx = ssl.create_default_context()
    query = name.replace(" ", "+")
    url = (
        f"https://api.openalex.org/authors?"
        f"search={query}&per_page=1&mailto=example@example.com"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "OpenAlexTools/1.0"})
    response = urllib.request.urlopen(req, context=ctx)
    data = json.loads(response.read())

    if not data["results"]:
        return None

    a = data["results"][0]
    institutions = a.get("last_known_institutions", [])
    inst_name = institutions[0].get("display_name", "Unknown") if institutions else "Unknown"

    return {
        "name": a["display_name"],
        "works_count": a["works_count"],
        "cited_by_count": a["cited_by_count"],
        "h_index": a.get("summary_stats", {}).get("h_index", 0),
        "i10_index": a.get("summary_stats", {}).get("i10_index", 0),
        "institution": inst_name,
        "orcid": a.get("orcid"),
        "id": a["id"],
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 author_lookup.py \"Author Name\"")
        print("Example: python3 author_lookup.py \"Yann LeCun\"")
        sys.exit(1)

    name = sys.argv[1]
    author = lookup_author(name)

    if not author:
        print(f"No author found for: {name}")
        sys.exit(1)

    print(f"\n{'='*50}")
    print(f"  {author['name']}")
    print(f"{'='*50}")
    print(f"  Institution:  {author['institution']}")
    print(f"  Works:        {author['works_count']:,}")
    print(f"  Citations:    {author['cited_by_count']:,}")
    print(f"  h-index:      {author['h_index']}")
    print(f"  i10-index:    {author['i10_index']}")
    if author['orcid']:
        print(f"  ORCID:        {author['orcid']}")
    print(f"  OpenAlex ID:  {author['id']}")
    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
