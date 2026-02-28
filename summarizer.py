import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def summarize_articles(articles):
    articles_text = ''
    for i, a in enumerate(articles, 1):
        articles_text += f"{i}. [{a['source']}] {a['title']}\n{a['summary']}\n\n"
        
    prompt = f"""다음은 오늘의 테크뉴스 기사 목록이야.

{articles_text}

아래 형식으로 브리핑을 작성해줘:

1. 각 기사마다:
   - 제목 (원문 영어 그대로)
   - 세 줄 한국어 요약 (사실만, 해석/의견 추가 금지)
   - 출처 링크

2. 마지막에 오늘의 주요 테마 2~3줄 요약

원문의 사실만 전달하고, 네 의견이나 해석은 절대 추가하지 마."""
    
    message = client.messages.create(
        model='claude-haiku-4-5-20251001',
        max_tokens=2000,
        messages=[{'role': 'user', 'content': prompt}]
    )
    return message.content[0].text

