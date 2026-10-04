from datetime import datetime, timezone
from typing import Optional

from football_ai.domain.match import Match
from football_ai.domain.goal import Goal
from football_ai.domain.match_status import MatchStatus


class FootballJsonMapper:

    @staticmethod
    def map_match(
        data: dict,
        competition_id: int,
        season_id: int,
        home_team_id: int,
        away_team_id: int,
    ) -> Match:

        score = data.get("score")

        full_time_score: Optional[list] = None
        half_time_score: Optional[list] = None

        if isinstance(score, dict):
            full_time_score = score.get("ft")
            half_time_score = score.get("ht")

        elif isinstance(score, list):
            full_time_score = score

        home_score = None
        away_score = None

        if full_time_score:
            home_score = full_time_score[0]
            away_score = full_time_score[1]

        home_half_time_score = None
        away_half_time_score = None

        if half_time_score:
            home_half_time_score = half_time_score[0]
            away_half_time_score = half_time_score[1]

        time = data["time"]
        time = time.replace("UTC+0", "+00:00")
        time = time.replace("UTC+1", "+01:00")

        kickoff_time = datetime.fromisoformat(
            f"{data['date']}T{time}"
        ).astimezone(timezone.utc)

        return Match(
            id=0,
            competition_id=competition_id,
            season_id=season_id,
            round=data.get("round"),
            matchday=None,
            home_team_id=home_team_id,
            away_team_id=away_team_id,
            kickoff_time=kickoff_time,
            venue_id=None,
            status=MatchStatus.FINISHED if full_time_score else MatchStatus.SCHEDULED,
            home_score=home_score,
            away_score=away_score,
            home_half_time_score=home_half_time_score,
            away_half_time_score=away_half_time_score,
            home_extra_time_score=None,
            away_extra_time_score=None,
            home_penalty_score=None,
            away_penalty_score=None,
            referee_id=None,
            attendance=data.get("attendance"),
            source="openfootball",
            source_match_id=None,
        )

    @staticmethod
    def map_goals(
        data: dict,
        match_id: int,
        home_team_id: int,
        away_team_id: int,
        player_ids: dict[str, int],
    ) -> list[Goal]:

        goals = []

        for goal_data in data.get("goals1", []):
            goals.append(
                Goal(
                    id=0,
                    match_id=match_id,
                    team_id=home_team_id,
                    player_id=player_ids[goal_data["name"]],
                    minute=goal_data["minute"],
                )
            )

        for goal_data in data.get("goals2", []):
            goals.append(
                Goal(
                    id=0,
                    match_id=match_id,
                    team_id=away_team_id,
                    player_id=player_ids[goal_data["name"]],
                    minute=goal_data["minute"],
                )
            )

        return goals
