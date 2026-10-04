from football_ai.clients.football_json import FootballJsonClient
from football_ai.domain.team import Team
from football_ai.repositories.season_team_repository import SeasonTeamRepository
from football_ai.repositories.team_repository import TeamRepository


class TeamIngestionService:

    def __init__(
        self,
        client: FootballJsonClient,
        team_repository: TeamRepository,
        season_team_repository: SeasonTeamRepository,
    ):
        self.client = client
        self.team_repository = team_repository
        self.season_team_repository = season_team_repository

    def ingest(
        self,
        path: str,
        season_id: int,
    ):
        data = self.client.get(path)

        team_names = sorted(
            set(
                [match["team1"] for match in data["matches"]]
                + [match["team2"] for match in data["matches"]]
            )
        )

        for index, team_name in enumerate(team_names, start=1):
            team = Team(
                id=index,
                name=team_name,
                short_name=None,
                country="England",
                founded=None,
                venue_id=None,
            )

            self.team_repository.save(team)
            self.season_team_repository.save(season_id, team.id)

            print(
                f"Registered team: {team_name} | "
                f"ID: {team.id} | Season: {season_id}"
            )

        print(f"Registered {len(team_names)} teams")