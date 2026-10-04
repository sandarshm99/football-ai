from dataclasses import dataclass


@dataclass
class Goal:
    id: int
    match_id: int
    team_id: int
    player_id: int
    minute: str
