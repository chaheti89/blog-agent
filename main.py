import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from state import BlogState
from nodes.planner import planner_node
from nodes.worker import worker_node
from nodes.reducer import should_continue
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0,
    google_api_key=os.environ["GOOGLE_API_KEY"]
)

# Build the graph
builder = StateGraph(BlogState)
builder.add_node("planner", lambda state: planner_node(state, llm))
builder.add_node("worker", lambda state: worker_node(state, llm))

builder.add_edge(START, "planner")
builder.add_conditional_edges("planner", should_continue, {"worker": "worker", "end": END})
builder.add_edge("worker", END)

graph = builder.compile()

# Run it
if __name__ == "__main__":
    topic = input("Enter a blog topic: ")
    result = graph.invoke({"topic": topic, "outline": None, "blog_post": None})
    
    print("\n" + "="*60)
    print("FINAL BLOG POST")
    print("="*60)
    print(result["blog_post"])
    
    # Save to file
    with open("blog_output.txt", "w") as f:
        f.write(result["blog_post"])
    print("\n Blog saved to blog_output.txt")