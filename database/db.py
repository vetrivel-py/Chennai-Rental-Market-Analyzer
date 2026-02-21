import sqlite3
from pathlib import Path


DB_PATH = Path("data/rentals.db")


def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
       CREATE TABLE IF NOT EXISTS rentals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    price INTEGER,
    location TEXT,
    bhk TEXT,
    bathroom TEXT,
    furnishing TEXT
)
    """)

    cursor.execute("DELETE FROM rentals")  # clear old data

    conn.commit()
    conn.close()


def insert_data(data: list[dict]):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for item in data:
        cursor.execute(
            "INSERT INTO rentals (title, price, location, bhk, bathroom, furnishing) VALUES (?, ?, ?, ?, ?, ?)",
            (item["title"], item["price"], item["location"], item.get("bhk", None), item.get("bathroom", None), item.get("furnishing", None))
        )

    conn.commit()
    conn.close()