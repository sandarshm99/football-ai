from football_ai.repositories.database import get_connection
from football_ai.utils.player_name import normalize_player_name


class PlayerRepository:

    def find_by_name(self, name):
        normalized_name = normalize_player_name(name)

        with get_connection() as connection:
            cursor = connection.execute(
                """
                SELECT id, name, first_name, last_name, date_of_birth,
                       nationality, position, preferred_foot, team_id
                FROM players
                WHERE LOWER(name) = ?
                """,
                (normalized_name,),
            )

            return cursor.fetchone()

    def save(self, player):
        with get_connection() as connection:
            connection.execute(
                """
                INSERT INTO players (
                    name,
                    first_name,
                    last_name,
                    date_of_birth,
                    nationality,
                    position,
                    preferred_foot,
                    team_id
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    player.name,
                    player.first_name,
                    player.last_name,
                    player.date_of_birth,
                    player.nationality,
                    player.position,
                    player.preferred_foot,
                    player.team_id,
                ),
            )

            cursor = connection.execute(
                """
                SELECT id
                FROM players
                WHERE LOWER(name) = ?
                """,
                (normalize_player_name(player.name),),
            )

            return cursor.fetchone()[0]