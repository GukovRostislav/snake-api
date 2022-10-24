import sqlite3
conn = sqlite3.connect('data.db')
cur = conn.cursor()
cur.execute("UPDATE users SET high_score = 228 WHERE username = 'aa';")
conn.commit()
