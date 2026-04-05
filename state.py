from typing import TypedDict, List, Optional

class BlogState(TypedDict):
    topic: str
    outline: Optional[List[str]]
    blog_post: Optional[str]