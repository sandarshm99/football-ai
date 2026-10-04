class MatchValidator:

    def validate(self, match):
        if match.home_team_id is None:
            raise ValueError("Home team ID is required")

        if match.away_team_id is None:
            raise ValueError("Away team ID is required")

        if match.home_team_id == match.away_team_id:
            raise ValueError("Home team and away team cannot be the same")

        if match.competition_id is None:
            raise ValueError("Competition ID is required")

        if match.season_id is None:
            raise ValueError("Season ID is required")

        if match.kickoff_time is None:
            raise ValueError("Kickoff time is required")

        if match.status is None:
            raise ValueError("Match status is required")

        return True