# Overview
A simple tech news briefer. Based on Claude.

# Project Structure
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
