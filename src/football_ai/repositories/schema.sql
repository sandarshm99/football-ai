CREATE TABLE IF NOT EXISTS competitions (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    country TEXT,
    type TEXT
);

CREATE TABLE IF NOT EXISTS seasons (
    id INTEGER PRIMARY KEY,
    competition_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    start_year INTEGER,
    end_year INTEGER,
    FOREIGN KEY (competition_id) REFERENCES competitions(id)
);

CREATE TABLE IF NOT EXISTS teams (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    short_name TEXT,
    country TEXT,
    founded INTEGER,
    venue_id INTEGER
);

CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    first_name TEXT,
    last_name TEXT,
    date_of_birth TEXT,
    nationality TEXT,
    position TEXT,
    preferred_foot TEXT,
    team_id INTEGER,
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

CREATE TABLE IF NOT EXISTS referees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    nationality TEXT
);

CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    competition_id INTEGER NOT NULL,
    season_id INTEGER NOT NULL,
    round TEXT,
    matchday INTEGER,

    home_team_id INTEGER NOT NULL,
    away_team_id INTEGER NOT NULL,

    kickoff_time TEXT NOT NULL,
    venue_id INTEGER,
    status TEXT NOT NULL,

    home_score INTEGER,
    away_score INTEGER,

    home_half_time_score INTEGER,
    away_half_time_score INTEGER,

    home_extra_time_score INTEGER,
    away_extra_time_score INTEGER,

    home_penalty_score INTEGER,
    away_penalty_score INTEGER,

    referee_id INTEGER,
    attendance INTEGER,

    source TEXT,
    source_match_id TEXT,

    FOREIGN KEY (competition_id) REFERENCES competitions(id),
    FOREIGN KEY (season_id) REFERENCES seasons(id),
    FOREIGN KEY (home_team_id) REFERENCES teams(id),
    FOREIGN KEY (away_team_id) REFERENCES teams(id),
    FOREIGN KEY (referee_id) REFERENCES referees(id)
);

CREATE TABLE IF NOT EXISTS goals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER NOT NULL,
    team_id INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    minute TEXT NOT NULL,

    FOREIGN KEY (match_id) REFERENCES matches(id),
    FOREIGN KEY (team_id) REFERENCES teams(id),
    FOREIGN KEY (player_id) REFERENCES players(id),

    UNIQUE (match_id, team_id, player_id, minute)
);

CREATE TABLE IF NOT EXISTS season_teams (
    season_id INTEGER NOT NULL,
    team_id INTEGER NOT NULL,

    PRIMARY KEY (season_id, team_id),

    FOREIGN KEY (season_id) REFERENCES seasons(id),
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_matches_unique_fixture
ON matches (
    competition_id,
    season_id,
    home_team_id,
    away_team_id,
    kickoff_time
);