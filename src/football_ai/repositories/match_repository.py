from football_ai.repositories.database import get_connection


class MatchRepository:

    def save(self, match):
        with get_connection() as connection:
            connection.execute(
                """
                INSERT INTO matches (
                    competition_id,
                    season_id,
                    round,
                    matchday,
                    home_team_id,
                    away_team_id,
                    kickoff_time,
                    venue_id,
                    status,
                    home_score,
                    away_score,
                    home_half_time_score,
                    away_half_time_score,
                    home_extra_time_score,
                    away_extra_time_score,
                    home_penalty_score,
                    away_penalty_score,
                    referee_id,
                    attendance,
                    source,
                    source_match_id
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT (
                    competition_id,
                    season_id,
                    home_team_id,
                    away_team_id,
                    kickoff_time
                ) DO NOTHING
                """,
                (
                    match.competition_id,
                    match.season_id,
                    match.round,
                    match.matchday,
                    match.home_team_id,
                    match.away_team_id,
                    match.kickoff_time.isoformat(),
                    match.venue_id,
                    match.status.value,
                    match.home_score,
                    match.away_score,
                    match.home_half_time_score,
                    match.away_half_time_score,
                    match.home_extra_time_score,
                    match.away_extra_time_score,
                    match.home_penalty_score,
                    match.away_penalty_score,
                    match.referee_id,
                    match.attendance,
                    match.source,
                    match.source_match_id,
                ),
            )

            cursor = connection.execute(
                """
                SELECT id
                FROM matches
                WHERE competition_id = ?
                  AND season_id = ?
                  AND home_team_id = ?
                  AND away_team_id = ?
                  AND kickoff_time = ?
                """,
                (
                    match.competition_id,
                    match.season_id,
                    match.home_team_id,
                    match.away_team_id,
                    match.kickoff_time.isoformat(),
                ),
            )

            return cursor.fetchone()[0]
    
    def find_by_id(self, match_id: int):
        with get_connection() as connection:
            return connection.execute(
                """
                SELECT
                    id,
                    competition_id,
                    season_id,
                    round,
                    matchday,
                    home_team_id,
                    away_team_id,
                    kickoff_time,
                    venue_id,
                    status,
                    home_score,
                    away_score,
                    home_half_time_score,
                    away_half_time_score,
                    home_extra_time_score,
                    away_extra_time_score,
                    home_penalty_score,
                    away_penalty_score,
                    referee_id,
                    attendance,
                    source,
                    source_match_id
                FROM matches
                WHERE id = ?
                """,
                (match_id,),
            ).fetchone()