import sqlite3

def create_database():
    conn = sqlite3.connect("resumes.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            text TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_resume(name, email, text):
    conn = sqlite3.connect("resumes.db")
    c = conn.cursor()
    c.execute("INSERT INTO resumes (name, email, text) VALUES (?, ?, ?)", (name, email, text))
    conn.commit()
    conn.close()

def get_all_resumes():
    conn = sqlite3.connect("resumes.db")
    c = conn.cursor()
    c.execute("SELECT name, email, text FROM resumes")
    data = [{"name": row[0], "email": row[1], "text": row[2]} for row in c.fetchall()]
    conn.close()
    return data

create_database()  # تشغيل عند بدء التطبيق

