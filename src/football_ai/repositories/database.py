import sqlite3
from pathlib import Path


DATABASE_PATH = "football_ai.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    schema_path = Path(__file__).with_name("schema.sql")

    with get_connection() as connection:
        schema = schema_path.read_text()
        connection.executescript(schema)