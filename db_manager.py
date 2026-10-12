"""Optional SQLite helper for local experiments.

The included API currently reads the bundled CSV. Render's ephemeral filesystem
is not suitable for permanent database storage; use a hosted database or a
properly configured persistent disk if you need stored records online.
"""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "commerce.db"

def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id TEXT NOT NULL,
                customer_id TEXT NOT NULL,
                order_date TEXT NOT NULL,
                sales REAL NOT NULL
            )
        """)
        connection.commit()
