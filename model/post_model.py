from pydantic import BaseModel

class PostResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str
