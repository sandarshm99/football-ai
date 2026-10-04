from dataclasses import dataclass
from typing import Optional


@dataclass
class Team:
    id: int
    name: str
    short_name: Optional[str]
    country: Optional[str]
    founded: Optional[int]
    venue_id: Optional[int]