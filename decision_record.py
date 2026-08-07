from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class DecisionRecord(BaseModel):
    id: str
    title: str
    context: str
    decision: str
    alternatives_considered: List[str] = []
    consequences: str = ""
    created_at: datetime = Field(default_factory=datetime.utcnow)
    author: Optional[str] = None
    related_model: Optional[str] = None

    def to_markdown(self) -> str:
        alts = "\n".join(f"- {a}" for a in self.alternatives_considered)
        return f"""# {self.title}
**ID:** {self.id}
**Date:** {self.created_at.date()}
**Model:** {self.related_model or 'N/A'}

## Context
{self.context}

## Decision
{self.decision}

## Alternatives Considered
{alts}

## Consequences
{self.consequences}
"""
