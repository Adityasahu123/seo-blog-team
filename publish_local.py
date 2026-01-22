import os
from slugify import slugify

def save_post(title: str, html: str):
    os.makedirs("docs", exist_ok=True)
    slug = slugify(title)[:60]
    path = f"docs/{slug}.html"

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"<html><body><h2>{title}</h2>{html}</body></html>")

    return slug, path

def update_index(entries):
    links = "\n".join([f'<li><a href="{slug}.html">{title}</a></li>' for title, slug in entries])
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(f"<html><body><h1>SEO Blogs</h1><ul>{links}</ul></body></html>")
