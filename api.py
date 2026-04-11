from fastapi import FastAPI
from pydantic import BaseModel
from main import graph

app = FastAPI(title="Blog Agent API")

class BlogRequest(BaseModel):
    topic: str

@app.post("/generate")
async def generate_blog(req: BlogRequest):
    result = graph.invoke({
        "topic": req.topic,
        "outline": None,
        "blog_post": None,
        "research": None,
        "revision_count": 0
    })
    return {
        "topic": req.topic,
        "outline": result["outline"],
        "blog_post": result["blog_post"],
        "research": result.get("research"),
    }

@app.get("/health")
def health():
    return {"status": "ok"}