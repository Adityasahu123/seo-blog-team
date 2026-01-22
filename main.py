from scrape_products import get_trending
from keywords import seo_keywords
from generate_blog import generate_blog
from publish_local import save_post, update_index

def run():
    products = get_trending(limit=3, pages=3)
    entries = []

    for p in products:
        kws = seo_keywords(p["title"], k=4)
        title, html = generate_blog(p, kws, model="llama3:latest")
        slug, _ = save_post(title, html)
        entries.append((title, slug))

        print("Generated:", title)
        print("Keywords:", kws)
        print("-" * 50)

    update_index(entries)
    print("✅ Website generated in /docs (ready for GitHub Pages)")

if __name__ == "__main__":
    run()
