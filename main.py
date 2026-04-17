from dotenv import load_dotenv
from fetcher import fetch_articles
from notifier import send_to_discord
from summarizer import summarize_articles

load_dotenv()

FEEDS_TECH = [
    "https://feeds.geeknews.kr/rss/news",
    "https://hnrss.org/best",
    "https://feeds.arstechnica.com/arstechnica/technology-lab",
    "https://www.technologyreview.com/feed/",
    "https://www.phoronix.com/rss.php"
]

FEEDS_AI = [
    "https://rss.arxiv.org/rss/cs.AI",
    "https://rss.arxiv.org/rss/cs.LG",
    "https://rss.arxiv.org/rss/cs.CV",
    "https://rss.arxiv.org/rss/cs.CL",
    "https://papers.takara.ai/api/feed",
    "https://huggingface.co/blog/feed.xml",
    "https://openai.com/news/rss.xml",
    " https://blog.google/technology/ai/rss/",
    "https://www.marktechpost.com/feed/",
]

ENVS = [
    'TECH_WEBHOOK',
    'AI_WEBHOOK'
]

def main():
    print("기사 수집 중...")
    tech_articles = fetch_articles(FEEDS_TECH, max_per_feed=5)
    print(f"{len(tech_articles)}개 기사 수집 완료")
    ai_articles = fetch_articles(FEEDS_AI, max_per_feed=5)
    print(f"{len(ai_articles)}개 기사 수집 완료")

    try:
        print("요약 생성 중...")
        tech_briefing = summarize_articles(tech_articles)
        ai_briefing = summarize_articles(ai_articles)
        print("요약 완료")

        print("디스코드 전송 중...")
        send_to_discord(tech_briefing, ENVS[0])
        send_to_discord(ai_briefing, ENVS[1])
        print("전송 완료!")
    except Exception as e:
        print("디스코드 전송 중...")
        send_to_discord('[Error occured]: ' + str(e), ENVS[0])
        print("전송 완료!")

    

if __name__ == '__main__':
    main()