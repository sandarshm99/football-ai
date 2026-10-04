from football_ai.repositories.database import get_connection


class CompetitionRepository:

    def save(self, competition):
        with get_connection() as connection:
            connection.execute(
                """
                INSERT OR IGNORE INTO competitions (
                    id, name, country, type
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    competition.id,
                    competition.name,
                    competition.country,
                    competition.type,
                ),
            )

    def find_by_id(self, competition_id: int):
        with get_connection() as connection:
            return connection.execute(
                """
                SELECT id, name, country, type
                FROM competitions
                WHERE id = ?
                """,
                (competition_id,),
            ).fetchone()