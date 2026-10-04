from football_ai.domain.player import Player
from football_ai.repositories.player_repository import PlayerRepository
from football_ai.utils.player_name import normalize_player_name


class PlayerResolver:

    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    def resolve(self, external_name: str, team_id: int | None = None) -> int:
        normalized_name = normalize_player_name(external_name)

        player = self.player_repository.find_by_name(normalized_name)

        if player is not None:
            return player[0]

        player = Player(
            id=0,
            name=normalized_name,
            first_name=None,
            last_name=None,
            date_of_birth=None,
            nationality=None,
            position=None,
            preferred_foot=None,
            team_id=team_id,
        )

        return self.player_repository.save(player)