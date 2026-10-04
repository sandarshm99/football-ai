import sqlite3

from football_ai.repositories.match_repository import MatchRepository


def test_save_same_match_is_idempotent():
    repository = MatchRepository()

    match = type("Match", (), {
        "competition_id": 1,
        "season_id": 1,
        "round": "1",
        "matchday": 1,
        "home_team_id": 1,
        "away_team_id": 2,
        "kickoff_time": __import__("datetime").datetime.fromisoformat(
            "2025-08-15T19:00:00+00:00"
        ),
        "venue_id": None,
        "status": type("Status", (), {"value": "FINISHED"})(),
        "home_score": 2,
        "away_score": 1,
        "home_half_time_score": 1,
        "away_half_time_score": 0,
        "home_extra_time_score": None,
        "away_extra_time_score": None,
        "home_penalty_score": None,
        "away_penalty_score": None,
        "referee_id": None,
        "attendance": None,
        "source": "test",
        "source_match_id": None,
    })()

    first_id = repository.save(match)
    second_id = repository.save(match)

    assert first_id == second_id

    with sqlite3.connect("football_ai.db") as connection:
        count = connection.execute(
            """
            SELECT COUNT(*)
            FROM matches
            WHERE competition_id = 1
              AND season_id = 1
              AND home_team_id = 1
              AND away_team_id = 2
              AND kickoff_time = ?
            """,
            (match.kickoff_time.isoformat(),),
        ).fetchone()[0]

    assert count == 1