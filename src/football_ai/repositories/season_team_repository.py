from football_ai.repositories.database import get_connection


class SeasonTeamRepository:

    def save(self, season_id: int, team_id: int):
        with get_connection() as connection:
            connection.execute(
                """
                INSERT OR IGNORE INTO season_teams (
                    season_id,
                    team_id
                )
                VALUES (?, ?)
                """,
                (season_id, team_id),
            )

    def find_by_season(self, season_id: int):
        with get_connection() as connection:
            return connection.execute(
                """
                SELECT team_id
                FROM season_teams
                WHERE season_id = ?
                ORDER BY team_id
                """,
                (season_id,),
            ).fetchall()