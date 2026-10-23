# Multi-Agent AI Research Assistant

## Project Overview

An AI-powered research assistant built using Python, LangChain, Groq, and Tavily. It searches the web, extracts webpage content, generates research reports, and evaluates those reports using an AI critic.

## Key Features

### 1. Webpage Scraping
I added a `User-Agent` header to identify my HTTP request as a browser-associated client, which can improve compatibility with websites that handle automated requests differently.

Python does not become Chrome; it only sets a request header. This does not guarantee website access or bypass anti-bot protections.

### 2. Research Report Generation
The Writer Chain generates a structured research report using the topic and information gathered by the research workflow.

### 3. AI Critic
The Critic Chain asks the AI to evaluate the generated report, identify its strengths and weaknesses, and provide a score and feedback.

## Tech Stack

- Python
- LangChain
- Groq
- Tavily
- Requests
- BeautifulSoup
- python-dotenv

## How to Run

1. Install the dependencies from `requirements.txt`.
2. Configure your Groq and Tavily API keys in a `.env` file.
3. Run the application:

```bash
python pipeline.py
```

4. Enter a research topic to generate a report and receive critic feedback.

## Security

Keep API keys private. Never upload your `.env` file or actual API credentials to GitHub.


