from football_ai.repositories.team_repository import TeamRepository


class TeamResolver:

    def __init__(self, team_repository: TeamRepository):
        self.team_repository = team_repository

    def resolve(self, external_name: str) -> int:
        team = self.team_repository.find_by_normalized_name(external_name)

        if team is None:
            raise ValueError(
                f"Team not found for external name: {external_name}"
            )

        return team[0]