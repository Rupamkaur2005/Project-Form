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
        village TEXT,
        district TEXT,
        occupation TEXT,
        address TEXT
    )
    """)

    conn.commit()
    conn.close()
create_table() 
def insert_data(name, age, gender, village, district, occupation, address):
    conn = sqlite3.connect("personal_info.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO personal_info
        (name, age, gender, village, district, occupation, address)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, age, gender, village, district, occupation, address))

    conn.commit()
    conn.close()   