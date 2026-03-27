from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel


#  schemas specify type of data API accepts and returns


class StoryOptionsSchema(BaseModel):
    text: str
    node_id: Optional[int] = None


# base classes are parent, created to be inherited from
class StoryNodeBase(BaseModel):
    content: str
    is_ending: bool = False
    is_winning_ending: bool = False


# reponse classes are what is returned from api call
class CompleteStoryNodeResponse(StoryNodeBase):
    id: int
    options: List[StoryOptionsSchema] = []

    class Config:
        from_attributes = True


class StoryBase(BaseModel):
    title: str
    session_id: Optional[str] = None

    class Config:
        from_attributes = True


# request classes are sent from front to backend
class CreateStoryRequest(BaseModel):
    theme: str


class CompleteStoryResponse(StoryBase):
    id: int
    created_at: datetime
    root_node: CompleteStoryNodeResponse
    all_nodes: Dict[int, CompleteStoryNodeResponse]

    class Config:
        from_attributes = True
