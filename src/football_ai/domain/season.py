from dataclasses import dataclass
from typing import Optional


@dataclass
class Season:
    id: int
    competition_id: int
    name: str
    start_year: Optional[int]
    end_year: Optional[int]