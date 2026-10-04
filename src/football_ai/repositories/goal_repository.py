from football_ai.repositories.database import get_connection


class GoalRepository:

    def save(self, goal):
        with get_connection() as connection:
            connection.execute(
                """
                INSERT OR IGNORE INTO goals (
                    match_id,
                    team_id,
                    player_id,
                    minute
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    goal.match_id,
                    goal.team_id,
                    goal.player_id,
                    goal.minute,
                ),
            )

            cursor = connection.execute(
                """
                SELECT id
                FROM goals
                WHERE match_id = ?
                  AND team_id = ?
                  AND player_id = ?
                  AND minute = ?
                """,
                (
                    goal.match_id,
                    goal.team_id,
                    goal.player_id,
                    goal.minute,
                ),
            )

            return cursor.fetchone()[0]

    def find_by_id(self, goal_id: int):
        with get_connection() as connection:
            return connection.execute(
                """
                SELECT
                    id,
                    match_id,
                    team_id,
                    player_id,
                    minute
                FROM goals
                WHERE id = ?
                """,
                (goal_id,),
            ).fetchone()