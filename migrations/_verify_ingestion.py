import sqlite3


connection = sqlite3.connect("football_ai.db")

rows = connection.execute(
    """
    SELECT
        g.id,
        h.name,
        a.name,
        p.name,
        g.minute
    FROM goals g
    JOIN matches m ON m.id = g.match_id
    JOIN teams h ON h.id = m.home_team_id
    JOIN teams a ON a.id = m.away_team_id
    JOIN players p ON p.id = g.player_id
    WHERE g.match_id = ?
    ORDER BY g.id
    """,
    (1,),
).fetchall()

print("Goals:", len(rows))

for row in rows:
    print(row)

connection.close()