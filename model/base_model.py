from typing import List, Optional
from pydantic import BaseModel, HttpUrl

class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: Optional[HttpUrl]


class Support(BaseModel):
    url: Optional[HttpUrl]
    text: str

class Response(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[User]
    support: Support
