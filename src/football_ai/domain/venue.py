from dataclasses import dataclass
from typing import Optional


@dataclass
class Venue:
    id: int
    name: str
    city: Optional[str]
    country: Optional[str]
    capacity: Optional[int]