from football_ai.repositories.database import get_connection


class SeasonRepository:

    def save(self, season):
        with get_connection() as connection:
            connection.execute(
                """
                INSERT OR IGNORE INTO seasons (
                    id, competition_id, name, start_year, end_year
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    season.id,
                    season.competition_id,
                    season.name,
                    season.start_year,
                    season.end_year,
                ),
            )

    def find_by_id(self, season_id: int):
        with get_connection() as connection:
            return connection.execute(
                """
                SELECT id, competition_id, name, start_year, end_year
                FROM seasons
                WHERE id = ?
                """,
                (season_id,),
            ).fetchone()