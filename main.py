from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()





class User(BaseModel):
    username: str
    userpw: str
    high_score: int

@app.post("/hs")
def root2(user: User):
    print(user.__dict__)
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM users WHERE username='{user.username}'")
    user_from_db = cur.fetchone()

    if user_from_db[2] < user.high_score:
        cur.execute(f"UPDATE users SET high_score = {user.high_score} WHERE username = '{user.username}';")
        conn.commit()



    return user.high_score

@app.post("/register")
def root(user: User):
    #global username
    #global userpw
    #global high_score
    print(user.__dict__)
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute(f"""INSERT INTO users (username, userpw, high_score) VALUES('{user.username}', '{user.userpw}', '{user.high_score}')""")
    conn.commit()





@app.post("/auth")
def root1(user: User):
    #global username
    #global userpw
    #global high_score
    print(user.__dict__)
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    for u in users:
        if user.username == u[0] and user.userpw == u[1]:
            return 200

    return 300






#@app.get("/auth")
#async def root():