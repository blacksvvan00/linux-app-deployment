from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "app"),
        user=os.getenv("DB_USER", "app"),
        password=os.getenv("DB_PASSWORD", "password")
    )


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/users")
def users():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT id, name FROM users ORDER BY id")

    result = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {
            "id": user[0],
            "name": user[1]
        }
        for user in result
    ]


@app.post("/users")
def create_user(name: str):
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users(name) VALUES(%s) RETURNING id",
        (name,)
    )

    user_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return {
        "id": user_id,
        "name": name
    }


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM users WHERE id=%s RETURNING id, name",
        (user_id,)
    )

    deleted = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": deleted[0],
        "name": deleted[1],
        "status": "deleted"
    }
