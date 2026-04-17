import feedparser

def fetch_articles(feeds, max_per_feed=5):
    articles = []
    for url in feeds:
        feed = feedparser.parse(url)
        for entry in feed.entries[:max_per_feed]:
            articles.append({
                'title': entry.get('title', ''),
                'link': entry.get('link', ''),
                'summary': entry.get('summary', '')[:500],
                'source': feed.feed.get('title', url),
            })

    return articles

