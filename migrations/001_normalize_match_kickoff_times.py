import sqlite3

from football_ai.clients.football_json import FootballJsonClient
from football_ai.clients.football_json_mapper import FootballJsonMapper
from football_ai.ingestion.team_resolver import TeamResolver
from football_ai.repositories.team_repository import TeamRepository


DATABASE_PATH = "football_ai.db"
SOURCE_PATH = "2025-26/en.1-full.json"
COMPETITION_ID = 1
SEASON_ID = 1


def migrate():
    client = FootballJsonClient()
    mapper = FootballJsonMapper()
    team_resolver = TeamResolver(TeamRepository())

    data = client.get(SOURCE_PATH)

    with sqlite3.connect(DATABASE_PATH) as connection:
        source_matches = data["matches"]

        database_count = connection.execute(
            """
            SELECT COUNT(*)
            FROM matches
            WHERE competition_id = ?
              AND season_id = ?
            """,
            (COMPETITION_ID, SEASON_ID),
        ).fetchone()[0]

        print(f"Database matches: {database_count}")
        print(f"Source matches: {len(source_matches)}")

        if database_count != len(source_matches):
            raise ValueError(
                "Database and source match counts do not match"
            )

        updates = []

        for source_match in source_matches:
            home_team_id = team_resolver.resolve(source_match["team1"])
            away_team_id = team_resolver.resolve(source_match["team2"])

            existing_match = connection.execute(
                """
                SELECT id
                FROM matches
                WHERE competition_id = ?
                  AND season_id = ?
                  AND home_team_id = ?
                  AND away_team_id = ?
                """,
                (
                    COMPETITION_ID,
                    SEASON_ID,
                    home_team_id,
                    away_team_id,
                ),
            ).fetchone()

            if existing_match is None:
                raise ValueError(
                    f"Match not found: "
                    f"{source_match['team1']} vs "
                    f"{source_match['team2']}"
                )

            match = mapper.map_match(
                data=source_match,
                competition_id=COMPETITION_ID,
                season_id=SEASON_ID,
                home_team_id=home_team_id,
                away_team_id=away_team_id,
            )

            updates.append(
                (
                    match.kickoff_time.isoformat(),
                    existing_match[0],
                )
            )

        connection.executemany(
            """
            UPDATE matches
            SET kickoff_time = ?
            WHERE id = ?
            """,
            updates,
        )

        connection.commit()

        print(f"Updated kickoff times: {len(updates)}")


if __name__ == "__main__":
    migrate()