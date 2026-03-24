#!/usr/bin/env python3
"""Track research publication trends over time using OpenAlex API.

Usage: python3 trend_tracker.py "topic" [start_year] [end_year]

No API key needed. No pip install.
"""

import urllib.request
import json
import sys
import ssl


def get_yearly_count(topic: str, year: int) -> int:
    """Get number of papers published on a topic in a given year."""
    ctx = ssl.create_default_context()
    query = topic.replace(" ", "+")
    url = (
        f"https://api.openalex.org/works?"
        f"search={query}&filter=publication_year:{year}&per_page=1"
        f"&mailto=example@example.com"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "OpenAlexTools/1.0"})
    response = urllib.request.urlopen(req, context=ctx)
    data = json.loads(response.read())
    return data["meta"]["count"]


def track_trend(topic: str, start: int = 2018, end: int = 2025):
    """Track publication trend for a topic across years."""
    print(f"\nPublication trend: \"{topic}\" ({start}-{end})\n")
    print(f"{'Year':>5} | {'Papers':>10} | {'Growth':>8} | {'Chart'}")
    print("-" * 60)

    prev_count = None
    max_count = 0
    results = []

    for year in range(start, end + 1):
        count = get_yearly_count(topic, year)
        results.append((year, count))
        if count > max_count:
            max_count = count

    for year, count in results:
        bar_len = int(count / max(max_count, 1) * 30)
        bar = "█" * bar_len

        if prev_count and prev_count > 0:
            growth = ((count - prev_count) / prev_count) * 100
            growth_str = f"+{growth:.0f}%" if growth > 0 else f"{growth:.0f}%"
        else:
            growth_str = "baseline"

        print(f"{year:>5} | {count:>10,} | {growth_str:>8} | {bar}")
        prev_count = count

    print(f"\nSource: OpenAlex (openalex.org)")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 trend_tracker.py \"topic\" [start_year] [end_year]")
        print("Example: python3 trend_tracker.py \"large language models\" 2018 2025")
        sys.exit(1)

    topic = sys.argv[1]
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 2018
    end = int(sys.argv[3]) if len(sys.argv) > 3 else 2025

    track_trend(topic, start, end)


if __name__ == "__main__":
    main()
