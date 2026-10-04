from dataclasses import dataclass
from typing import Optional


@dataclass
class Competition:
    id: int
    name: str
    country: Optional[str]
    type: Optional[str]