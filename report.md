# Report – SEO Blog Post Creation Tool

## Objective
Build an AI-based SEO blog tool that scrapes products, researches keywords, generates a 150–200 word SEO blog post, and publishes it online.

## Pipeline Implemented

### 1) Product Scraping
- Source: BooksToScrape (public demo e-commerce site)
- Extracted: title, price, rating, product link
- Trending logic (prototype): top-rated products from multiple pages

### 2) SEO Keyword Research (3–4 keywords)
- Primary: Google Trends related queries using pytrends
- Issue: Google can rate-limit automated requests (HTTP 429)
- Solution: fallback keyword generation using product title:
  - "<product> review", "best <product>", "<product> price", "buy <product> online"
- Output: 3–4 keywords per product

### 3) Blog Generation (AI)
- Local LLM: Ollama (`llama3:latest`)
- Prompt constraints:
  - 150–200 words
  - include all keywords naturally
  - friendly tone + CTA
  - HTML output in <p> tags
- Added rewrite pass if blog is outside word limit.

### 4) Publishing
- Generated static HTML posts in `docs/`
- Hosted using GitHub Pages from `/docs`

## How to Run
```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
