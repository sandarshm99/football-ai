from football_ai.clients.football_json import FootballJsonClient
from football_ai.clients.football_json_mapper import FootballJsonMapper
from football_ai.ingestion.match_ingestion import MatchIngestionService
from football_ai.ingestion.match_validator import MatchValidator
from football_ai.ingestion.player_resolver import PlayerResolver
from football_ai.ingestion.team_resolver import TeamResolver
from football_ai.repositories.goal_repository import GoalRepository
from football_ai.repositories.match_repository import MatchRepository
from football_ai.repositories.player_repository import PlayerRepository
from football_ai.repositories.team_repository import TeamRepository


def create_match_ingestion_service():
    client = FootballJsonClient()
    mapper = FootballJsonMapper()

    team_repository = TeamRepository()
    team_resolver = TeamResolver(team_repository)

    player_repository = PlayerRepository()
    player_resolver = PlayerResolver(player_repository)

    match_repository = MatchRepository()
    goal_repository = GoalRepository()

    validator = MatchValidator()

    return MatchIngestionService(
        client=client,
        mapper=mapper,
        team_resolver=team_resolver,
        player_resolver=player_resolver,
        match_repository=match_repository,
        goal_repository=goal_repository,
        validator=validator,
    )