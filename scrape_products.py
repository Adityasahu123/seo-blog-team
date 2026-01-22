import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE = "https://books.toscrape.com/"
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

def scrape_page(page_no: int):
    url = f"{BASE}catalogue/page-{page_no}.html"
    html = requests.get(url, timeout=30).text
    soup = BeautifulSoup(html, "html.parser")

    items = []
    for pod in soup.select("article.product_pod"):
        title = pod.h3.a["title"].strip()
        price = pod.select_one(".price_color").get_text(strip=True)
        rel = pod.h3.a["href"]
        link = urljoin(BASE, "catalogue/" + rel)

        rating_class = pod.select_one("p.star-rating")["class"]
        rating_word = [c for c in rating_class if c != "star-rating"][0]
        rating = RATING_MAP.get(rating_word, 0)

        items.append({"title": title, "price": price, "rating": rating, "url": link})
    return items

def get_trending(limit=3, pages=3):
    all_items = []
    for p in range(1, pages + 1):
        all_items.extend(scrape_page(p))

    # "Trending" proxy: highest ratings first
    all_items.sort(key=lambda x: x["rating"], reverse=True)
    return all_items[:limit]

if __name__ == "__main__":
    print(get_trending())
