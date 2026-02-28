from dotenv import load_dotenv
from fetcher import fetch_articles
from notifier import send_to_discord
from summarizer import summarize_articles

load_dotenv()

def main():
    print("기사 수집 중...")
    articles = fetch_articles(max_per_feed=5)
    print(f"{len(articles)}개 기사 수집 완료")

    print("요약 생성 중...")
    briefing = summarize_articles(articles)
    print("요약 완료")

    print("디스코드 전송 중...")
    send_to_discord(briefing)
    print("전송 완료!")

if __name__ == '__main__':
    main()