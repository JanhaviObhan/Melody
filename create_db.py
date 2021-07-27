import sqlite3
def create_db():
    con=sqlite3.connect(database=r'melody.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT,song text,album text,artist text,year integer,genre text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS artists(name text,age text,gender text,country text)")
    con.commit()

create_db()