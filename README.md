# Overview
A simple tech news briefer in Korean. Based on Claude.

# Project Structure

```
tech-briefing/
├── .env
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── main.py               # Entrypoint
├── fetcher.py            # Fetch news by RSS
├── summarizer.py         # Call Claude API for summarization
└── notifier.py           # Send brief by calling Discord webhook
```

# How can I use?

1. Fork this repository.
2. [Get a Claude API key and charge.](https://platform.claude.com/dashboard)
3. Make your Discord server and get a webhook URL[Reference](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks).
4. Set a secrets on your fork repository.
    - Set Claude API key as `ANTHROPIC_API_KEY`.
    - Set Discord Webhook URL as `DISCORD_WEBHOOK_URL`.
5. Done! (for now)

# You can do more...

## Check the `fetcher.py` out.

You can change the RSS server to others.

## Check the `summarizer.py` out.

You can change the prompt to your language(currently Korean).  
Or change the format to the style that you prefer.