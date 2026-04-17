import requests
import os

def send_to_discord(content, env_path):
    webhook_url = os.getenv(env_path)

    # Discord messages have maximum length as 2000. So get chunking.
    chunks = [content[i:i+1900] for i in range(0, len(content), 1900)]

    for chunk in chunks:
        payload = {'content': chunk}
        response = requests.post(webhook_url, json=payload)
        if response.status_code != 204:
            print(f"디스코드 전송 실패: {response.status_code}")
