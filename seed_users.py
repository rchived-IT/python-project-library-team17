"""
Seeds the database with initial user accounts so you can test login.

Usage:
  1. Place this file in the root of your repo (same level as schema.sql's
     parent folder, database/).
  2. Make sure database/app.db already exists (run schema.sql first).
  3. Run:  python seed_users.py
  4. Log in with the printed username/password.

Safe to run more than once — it skips any username that already exists.
"""

import sqlite3
import sys
from pathlib import Path

try:
    import bcrypt
except ImportError:
    print("bcrypt is not installed. Run: pip install bcrypt")
    sys.exit(1)

DB_PATH = Path("database/app.db")

# username, plain-text password (only ever used here, never stored), role
SEED_USERS = [
    ("admin", "Admin123!", "Administrator"),
    ("librarian1", "Staff123!", "Librarian"),
]


def hash_password(plain_password: str) -> str:
    return bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def main():
    if not DB_PATH.exists():
        print(f"Could not find {DB_PATH}. Run schema.sql first to create the database.")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    for username, plain_password, role in SEED_USERS:
        existing = conn.execute(
            "SELECT 1 FROM users WHERE username = ?", (username,)
        ).fetchone()
        if existing:
            print(f"Skipped (already exists): {username}")
            continue

        conn.execute(
            "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
            (username, hash_password(plain_password), role),
        )
        print(f"Created: {username} / {plain_password}  (role: {role})")

    conn.commit()
    conn.close()

    print("\nDone. You can now log in with the credentials printed above.")
    print("Change or remove these before final submission — don't leave demo passwords in place.")


if __name__ == "__main__":
    main()
