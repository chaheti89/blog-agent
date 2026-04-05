from langchain_core.messages import HumanMessage

def worker_node(state, llm):
    topic = state["topic"]
    outline = "\n".join(state["outline"])
    print(f"\n✍️  Writing blog post...")

    response = llm.invoke([
        HumanMessage(content=f"""Write a detailed, engaging blog post about "{topic}" following this outline:

{outline}

Write in a friendly, professional tone. Include an introduction and conclusion. Make it at least 500 words.""")
    ])

    print("Blog post written!")
    return {**state, "blog_post": response.content}