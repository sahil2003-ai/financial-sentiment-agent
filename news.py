import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

def fetch_news():
    if not API_KEY:
        return ["Add NEWS_API_KEY in .env to fetch live news"]

    url = f"https://newsapi.org/v2/top-headlines?category=business&apiKey={API_KEY}"
    response = requests.get(url).json()

    articles = response.get("articles", [])[:3]
    return [a.get("title", "No title") for a in articles]