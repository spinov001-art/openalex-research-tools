#!/usr/bin/env python3
"""Compare research output across multiple topics.

Usage: python3 research_dashboard.py "topic1" "topic2" "topic3"
"""

import urllib.request
import json
import sys
import ssl


def get_topic_stats(topic: str) -> dict:
    """Get 2025 publication count for a topic."""
    ctx = ssl.create_default_context()
    query = topic.replace(" ", "+")
    url = (
        f"https://api.openalex.org/works?"
        f"search={query}&filter=publication_year:2025&per_page=1"
        f"&mailto=example@example.com"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "OpenAlexTools/1.0"})
    resp = urllib.request.urlopen(req, context=ctx)
    data = json.loads(resp.read())
    return {"topic": topic, "papers_2025": data["meta"]["count"]}


def main():
    if len(sys.argv) < 2:
        topics = [
            "large language models",
            "computer vision",
            "reinforcement learning",
            "quantum computing",
            "web scraping",
            "RAG retrieval augmented generation",
        ]
    else:
        topics = sys.argv[1:]

    print(f"\n{'='*55}")
    print(f"  RESEARCH TREND DASHBOARD — 2025")
    print(f"{'='*55}")
    print(f"  {'Topic':<35} | {'Papers 2025':>12}")
    print(f"  {'-'*35}-+-{'-'*12}")

    max_count = 0
    results = []
    for topic in topics:
        stats = get_topic_stats(topic)
        results.append(stats)
        if stats["papers_2025"] > max_count:
            max_count = stats["papers_2025"]

    for r in sorted(results, key=lambda x: x["papers_2025"], reverse=True):
        bar = "█" * int(r["papers_2025"] / max(max_count, 1) * 15)
        print(f"  {r['topic']:<35} | {r['papers_2025']:>10,}  {bar}")

    print(f"\n  Source: OpenAlex — openalex.org")
    print(f"  No API key needed. Data updated daily.\n")


if __name__ == "__main__":
    main()
