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
        return f"""# {self.title}
ID: {self.id}

## Context
{self.context}

## Decision
{self.decision}

## Alternatives Considered
{', '.join(self.alternatives_considered)}

## Consequences
{self.consequences}
"""
