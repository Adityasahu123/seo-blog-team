import re
import requests

def _word_count(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))

def generate_blog(product: dict, keywords: list, model="llama3:latest"):
    kw = ", ".join(keywords[:4])

    prompt = f"""
Write an SEO-friendly blog post of 150–200 words in simple HTML using only <p> tags.

Product:
- Title: {product['title']}
- Price: {product.get('price','')}
- Link: {product.get('url','')}

SEO keywords (MUST include each naturally at least once): {kw}

Rules:
- Friendly, helpful tone
- No keyword stuffing
- End with one short CTA sentence (e.g., "Check it out here...")
- Output ONLY the HTML (no explanations)
"""

    r = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False, "options": {"temperature": 0.6}},
        timeout=180
    )
    r.raise_for_status()
    html = r.json().get("response", "").strip()

    wc = _word_count(html)
    if wc < 150 or wc > 200:
        fix_prompt = f"""
Rewrite the following HTML to be 150–200 words total.
Keep ONLY <p> tags. Keep all keywords included naturally at least once: {kw}.
End with a short CTA.

HTML:
{html}
"""
        r2 = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": fix_prompt, "stream": False},
            timeout=180
        )
        r2.raise_for_status()
        html = r2.json().get("response", "").strip()

    title = f"{product['title']} – Quick Review"
    return title, html
