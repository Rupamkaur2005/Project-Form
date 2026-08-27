import sqlite3
def create_table():
    conn = sqlite3.connect("personal_info.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS personal_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            color TEXT,
            fav_food TEXT,
            fav_subject TEXT,
            hobby TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_data(name, age, gender, color, fav_food, fav_subject, hobby):
    conn = sqlite3.connect("personal_info.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO personal_info
        (name, age, gender, color, fav_food, fav_subject, hobby)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, age, gender, color, fav_food, fav_subject, hobby))

    conn.commit()
    conn.close()