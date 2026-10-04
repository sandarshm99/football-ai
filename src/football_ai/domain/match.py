from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from football_ai.domain.match_status import MatchStatus


@dataclass
class Match:
    id: int

    competition_id: int
    season_id: int
    round: Optional[str]
    matchday: Optional[int]

    home_team_id: int
    away_team_id: int

    kickoff_time: datetime
    venue_id: Optional[int]
    status: MatchStatus

    home_score: Optional[int]
    away_score: Optional[int]

    home_half_time_score: Optional[int]
    away_half_time_score: Optional[int]

    home_extra_time_score: Optional[int]
    away_extra_time_score: Optional[int]

    home_penalty_score: Optional[int]
    away_penalty_score: Optional[int]

    referee_id: Optional[int]
    attendance: Optional[int]

    source: Optional[str]
    source_match_id: Optional[str]