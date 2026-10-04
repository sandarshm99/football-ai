from football_ai.clients.football_json import FootballJsonClient
from football_ai.clients.football_json_mapper import FootballJsonMapper
from football_ai.ingestion.team_resolver import TeamResolver
from football_ai.ingestion.player_resolver import PlayerResolver
from football_ai.repositories.match_repository import MatchRepository
from football_ai.repositories.goal_repository import GoalRepository
from football_ai.ingestion.match_validator import MatchValidator


class MatchIngestionService:

    def __init__(
        self,
        client: FootballJsonClient,
        mapper: FootballJsonMapper,
        team_resolver: TeamResolver,
        player_resolver: PlayerResolver,
        match_repository: MatchRepository,
        goal_repository: GoalRepository,
        validator: MatchValidator,
    ):
        self.client = client
        self.mapper = mapper
        self.team_resolver = team_resolver
        self.player_resolver = player_resolver
        self.match_repository = match_repository
        self.goal_repository = goal_repository
        self.validator = validator

    def ingest(
        self,
        path: str,
        competition_id: int,
        season_id: int,
    ):
        data = self.client.get(path)

        matches = data["matches"]

        print(f"Found {len(matches)} matches")

        for match_data in matches:
            home_team_name = match_data["team1"]
            away_team_name = match_data["team2"]

            home_team_id = self.team_resolver.resolve(home_team_name)
            away_team_id = self.team_resolver.resolve(away_team_name)

            match = self.mapper.map_match(
                data=match_data,
                competition_id=competition_id,
                season_id=season_id,
                home_team_id=home_team_id,
                away_team_id=away_team_id,
            )

            self.validator.validate(match)

            match_id = self.match_repository.save(match)

            player_ids = {}

            for goal_data in match_data.get("goals1", []):
                player_name = goal_data["name"]

                if player_name not in player_ids:
                    player_ids[player_name] = self.player_resolver.resolve(
                        player_name,
                        home_team_id,
                    )

            for goal_data in match_data.get("goals2", []):
                player_name = goal_data["name"]

                if player_name not in player_ids:
                    player_ids[player_name] = self.player_resolver.resolve(
                        player_name,
                        away_team_id,
                    )

            goals = self.mapper.map_goals(
                data=match_data,
                match_id=match_id,
                home_team_id=home_team_id,
                away_team_id=away_team_id,
                player_ids=player_ids,
            )

            for goal in goals:
                self.goal_repository.save(goal)

            print(
                f"Ingested match: {home_team_name} vs "
                f"{away_team_name} | ID: {match_id} | "
                f"Goals: {len(goals)}"
            )