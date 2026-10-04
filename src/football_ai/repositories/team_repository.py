from football_ai.repositories.database import get_connection
from football_ai.utils.team_name import normalize_team_name


class TeamRepository:

    def find_by_normalized_name(self, name: str):
        normalized_name = normalize_team_name(name)

        with get_connection() as connection:
            rows = connection.execute(
                """
                SELECT id, name, short_name, country, founded, venue_id
                FROM teams
                """
            ).fetchall()

        for row in rows:
            if normalize_team_name(row[1]) == normalized_name:
                return row

        return None

    def save(self, team):
        with get_connection() as connection:
            connection.execute(
                """
                INSERT OR IGNORE INTO teams (
                    id, name, short_name, country, founded, venue_id
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    team.id,
                    team.name,
                    team.short_name,
                    team.country,
                    team.founded,
                    team.venue_id,
                ),
            )