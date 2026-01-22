# SEO Blog Post Creation Tool (Free + Local LLM)

This project is a **free prototype** that automates an SEO blog creation pipeline:

1. **Scrape products** from an e-commerce site (demo store)  
2. **Generate 3–4 SEO keywords** automatically  
3. **Generate a 150–200 word SEO blog post** that naturally includes the keywords  
4. **Publish the posts online** as a static site (GitHub Pages via `/docs`)

---

## Tech Stack
- **Python**
- **BeautifulSoup4** – product scraping  
- **Keyword Research**
  - Primary: `pytrends` (Google Trends)
  - Fallback: offline keyword expansion (handles Google 429 rate-limits)
- **Content Generation:** **Ollama** local LLM (`llama3:latest`)
- **Publishing:** Static HTML in `/docs` (GitHub Pages ready)

---

## Project Structure
seo-blog-team/
main.py
scrape_products.py
keywords.py
generate_blog.py
publish_local.py
requirements.txt
docs/
index.html
*.html


---

## Setup (Windows)

### 1) Create & activate virtual environment
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
2) Install dependencies
pip install -r requirements.txt
3) Ensure Ollama is running
Check models:

ollama list
This project uses:

llama3:latest

Test Ollama API:

$body = @{ model="llama3:latest"; prompt="Reply with ONLY: OK"; stream=$false } | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:11434/api/generate" -Method Post -ContentType "application/json" -Body $body
Run the Pipeline
python main.py
Output
After running, the generated blog site will be created in:

docs/index.html

docs/*.html (individual blog pages)

Open locally:

Go to docs/ and double-click index.html

Publish on GitHub Pages (Free Hosting)
Push repo to GitHub

Go to: Repo → Settings → Pages

Select:

Source: Deploy from branch

Branch: main

Folder: /docs

Save

Your site will be available at:

https://<github-username>.github.io/<repo-name>/
Notes (Keyword Research)
The tool attempts keyword research using Google Trends (pytrends).

If Google rate-limits requests (HTTP 429), it automatically falls back to offline keyword expansion:

<product> review, best <product>, <product> price, etc.

This keeps the pipeline fully automated and 100% free.

Author
Aditya Sahu

