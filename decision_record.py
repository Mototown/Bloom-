from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
class DecisionRecord(BaseModel):
    id: str
    title: str
    context: str
    decision: str
    alternatives_considered: List[str] = []
    consequences: str = ""
    created_at: datetime = datetime.utcnow()
    author: Optional[str] = None
    related_model: Optional[str] = None
    def to_markdown(self):
        return f"# {self.title}\n{self.decision}\n"
