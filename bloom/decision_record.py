from __future__ import annotations

from datetime import datetime, timezone
from typing import List, Optional

from pydantic import BaseModel, Field


class DecisionRecord(BaseModel):
    """Architecture Decision Record that travels with every generated model."""

    id: str
    title: str
    context: str
    decision: str
    alternatives_considered: List[str] = Field(default_factory=list)
    consequences: str = ""
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    author: Optional[str] = None
    related_model: Optional[str] = None

    def to_markdown(self) -> str:
        alts = "\n".join(f"- {a}" for a in self.alternatives_considered) or "- (none recorded)"
        author_line = f"**Author:** {self.author}\n" if self.author else ""
        model_line = f"**Related model:** `{self.related_model}`\n" if self.related_model else ""

        return f"""# {self.title}

**ID:** `{self.id}`  
**Date:** {self.created_at.strftime("%Y-%m-%d %H:%M UTC")}  
{author_line}{model_line}
## Context

{self.context}

## Decision

{self.decision}

## Alternatives Considered

{alts}

## Consequences

{self.consequences or "(not recorded)"}
"""