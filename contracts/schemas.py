import json
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class ResearchRequest:
    topic: str
    max_sources: int = 5

@dataclass
class SourceData:
    title: str
    source: str
    url: str
    content: str
    date: Optional[str] = None
    claims: List[str] = field(default_factory=list)

@dataclass
class ResearchReport:
    topic: str
    sources: List[SourceData]
    agreements: List[str]
    conflicts: List[Dict[str, str]]
    markdown: str
