from dataclasses import dataclass
from typing import Optional


@dataclass
class Referee:
    id: int
    name: str
    nationality: Optional[str]