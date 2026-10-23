
from agents import (
    build_reader_agent,
    build_search_agent,
    writer_chain,
    critic_chain,
)


def run_research_pipeline(topic: str) -> dict:
    state = {}

    # Step 1: Search
    print("Searching the web...")

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [
            (
                "user",
                f"Find recent, reliable information about: {topic}. "
                "Use the web_search tool and return relevant titles, "
                "URLs, and snippets."
            )
        ]
    })

    state["search_results"] = search_result["messages"][-1].content

    if not state["search_results"].strip():
        raise ValueError("Search returned empty results.")

    # Step 2: Read a webpage
    print("Reading a relevant webpage...")

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [
            (
                "user",
                f"Research topic: {topic}\n\n"
                f"Search results:\n{state['search_results'][:4000]}\n\n"
                "Choose a relevant, reliable URL. Prefer authoritative "
                "sources and avoid Scribd or document-sharing sites. "
                "Use the scrape_url tool and summarize the content "
                "actually retrieved. If scraping fails, try another URL."
            )
        ]
    })

    state["scraped_content"] = reader_result["messages"][-1].content

    # Step 3: Write the report
    print("Writing the research report...")

    combined_research = (
        f"Search results:\n{state['search_results']}\n\n"
        f"Scraped content:\n{state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": combined_research,
    })

    # Step 4: Critic review
    print("Reviewing the report...")

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print("\nResearch Report:\n")
    print(state["report"])

    print("\nCritic Feedback:\n")
    print(state["feedback"])

    return state


if __name__ == "__main__":
    topic = input("Research topic: ").strip()

    if topic:
        try:
            run_research_pipeline(topic)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Please enter a research topic.")
