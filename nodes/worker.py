from langchain_core.messages import HumanMessage
from tavily import TavilyClient
import os

def worker_node(state, llm):
    topic = state["topic"]
    outline = "\n".join(state["outline"])

    # Research phase
    print(f"\nResearching '{topic}'...")
    tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
    results = tavily.search(query=topic, max_results=3)
    context = "\n\n".join([r["content"] for r in results["results"]])
    print("Research complete!")

    print(f"\n Writing blog post...")
    response = llm.invoke([
        HumanMessage(content=f"""Write a detailed, engaging blog post about "{topic}" following this outline:

{outline}

Use the following research to make the post accurate and current:

{context}

Write in a friendly, professional tone. Include an introduction and conclusion. Make it at least 500 words.""")
    ])

    print("Blog post written!")
    return {**state, "blog_post": response.content, "research": context}