
from dotenv import load_dotenv
from tavily import TavilyClient
import os

load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

results = tavily.search(
    query="MS Dhoni biography career achievements",
    max_results=5
)

for item in results["results"]:
    print("\nTITLE:", item.get("title"))
    print("URL:", item.get("url"))
    print("SNIPPET:", item.get("content", "")[:200])
    print("-" * 50)

