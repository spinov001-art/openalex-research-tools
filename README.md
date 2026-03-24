# OpenAlex Research Tools 🔬

> Search 250M+ research papers for free using the OpenAlex API. No API key needed.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![No API Key](https://img.shields.io/badge/API%20Key-Not%20Required-green.svg)](https://openalex.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## What Is OpenAlex?

[OpenAlex](https://openalex.org) is a free, open index of the global research system:
- **250M+ works** (papers, books, datasets)
- **100M+ authors** with citation metrics
- **100K+ institutions** worldwide
- **50K+ journals and conferences**

Free alternative to Scopus ($10K/yr) and Web of Science ($50K/yr).

## Quick Start

```bash
# No installation needed — uses Python stdlib only
python3 search_papers.py "large language models"
python3 trend_tracker.py "quantum computing" 2020 2025
python3 author_lookup.py "Yann LeCun"
python3 institution_research.py "Google DeepMind"
```

## Tools Included

| Script | What it does |
|--------|-------------|
| `search_papers.py` | Find most-cited papers on any topic |
| `trend_tracker.py` | Track publication trends over years |
| `author_lookup.py` | Get author h-index, citations, works |
| `institution_research.py` | Research what companies are publishing |
| `research_dashboard.py` | Compare multiple topics side by side |

## Example Output

```
$ python3 trend_tracker.py "large language models" 2020 2025

Year  | Papers  | Growth
2020  |   1,204 | baseline
2021  |   2,891 | +140%
2022  |   8,445 | +192%
2023  |  28,102 | +233%  ← explosion
2024  |  61,334 | +118%
2025  |  45,209 | (partial)
```

## API Endpoints

| Endpoint | Returns | Example |
|----------|---------|---------|
| `/works` | Papers, books | `?search=topic&sort=cited_by_count:desc` |
| `/authors` | Researchers | `?search=name` |
| `/institutions` | Universities, labs | `?search=MIT` |
| `/topics` | Research areas | `?search=machine+learning` |
| `/sources` | Journals | `?search=Nature` |

## Tutorial

📖 **Full tutorial with explanations:** [OpenAlex API: Search 250M+ Research Papers for Free](https://dev.to/0012303/openalex-api-search-250m-research-papers-for-free-no-api-key-needed-2jj3-temp-slug-1035286)

## Related Projects

- [awesome-web-scraping-2026](https://github.com/spinov001-art/awesome-web-scraping-2026) — 77+ data collection tools
- [ai-market-research-reports](https://github.com/spinov001-art/ai-market-research-reports) — Market research without hallucinations
- [pypi-package-analyzer](https://github.com/spinov001-art/pypi-package-analyzer) — Analyze Python packages via API
- [free-apis-list](https://github.com/spinov001-art/free-apis-list) — 100+ free APIs for developers

## License

MIT
