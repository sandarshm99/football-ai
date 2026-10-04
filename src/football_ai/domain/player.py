from dataclasses import dataclass
from typing import Optional


@dataclass
class Player:
    id: int
    name: str
    first_name: Optional[str]
    last_name: Optional[str]
    date_of_birth: Optional[str]
    nationality: Optional[str]
    position: Optional[str]
    preferred_foot: Optional[str]
    team_id: Optional[int]