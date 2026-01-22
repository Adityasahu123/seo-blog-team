import re
import time
from pytrends.request import TrendReq

STOPWORDS = {
    "the","a","an","and","or","of","to","for","with","in","on","at","by",
    "is","are","this","that","these","those","from","as","it","its"
}

def _clean_seed(seed: str) -> str:
    seed = (seed or "").strip()
    seed = re.sub(r"\s+", " ", seed)
    return seed[:90] if seed else "product"

def _offline_keywords(seed: str, k: int = 4):
    # Remove punctuation, keep words
    words = re.findall(r"[A-Za-z0-9]+", seed.lower())
    words = [w for w in words if w not in STOPWORDS]

    # Build a short core phrase (max 5 words)
    core = " ".join(words[:5]).strip()
    if not core:
        core = "best product"

    candidates = [
        core,
        f"{core} review",
        f"best {core}",
        f"{core} price",
        f"buy {core} online",
        f"{core} features",
    ]

    # Unique + take k
    uniq = []
    for x in candidates:
        x = x.strip()
        if x and x.lower() not in [u.lower() for u in uniq]:
            uniq.append(x)
    return uniq[:k]

def seo_keywords(seed: str, k: int = 4):
    seed = _clean_seed(seed)

    # Try pytrends with a couple retries
    try:
        pytrends = TrendReq(hl="en-US", tz=330, retries=2, backoff_factor=0.5, timeout=(10, 25))
        pytrends.build_payload([seed], timeframe="today 12-m")

        rq = pytrends.related_queries()
        out = []

        top = rq.get(seed, {}).get("top")
        if top is not None and not top.empty:
            out = [q for q in top["query"].tolist() if str(q).strip()]

        if len(out) >= k:
            # unique + first k
            uniq = []
            for x in out:
                if x.lower() not in [u.lower() for u in uniq]:
                    uniq.append(x)
            return uniq[:k]

    except Exception as e:
        # 429 or any other error -> fallback
        # (optional) tiny delay so repeated runs don't hammer Google
        time.sleep(1)

    # Fallback: offline keyword generation
    return _offline_keywords(seed, k=k)
