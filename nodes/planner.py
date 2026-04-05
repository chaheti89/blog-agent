from langchain_core.messages import HumanMessage

def planner_node(state, llm):
    topic = state["topic"]
    print(f"\n📋 Planning blog outline for: {topic}")
    
    response = llm.invoke([
        HumanMessage(content=f"""Create a detailed blog post outline for the topic: "{topic}"
        
Return ONLY a numbered list of section headings, one per line. Example:
1. Introduction
2. Section Title
3. Section Title
...
10. Conclusion""")
    ])
    
    outline = [line.strip() for line in response.content.strip().split("\n") if line.strip()]
    print(f"Outline created with {len(outline)} sections")
    return {**state, "outline": outline}