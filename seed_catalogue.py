"""
Seeds the database with sample Books and Members, so there's data to test
against for search, issue/return, and reporting features.

Usage:
  1. Place this file in the root of your repo.
  2. Make sure database/app.db already exists (run schema.sql first).
  3. Run:  python seed_catalogue.py

Safe to run more than once - it skips any ISBN or member that already exists.
"""

import sqlite3
import sys
from pathlib import Path

DB_PATH = Path("database/app.db")

# title, author, isbn, genre, total_copies, available_copies
SEED_BOOKS = [
    ("Clean Code", "Robert C. Martin", "9780132350884", "Software Engineering", 3, 3),
    ("The Pragmatic Programmer", "David Thomas & Andrew Hunt", "9780135957059", "Software Engineering", 2, 2),
    ("Introduction to Algorithms", "Cormen, Leiserson, Rivest, Stein", "9780262046305", "Computer Science", 2, 2),
    ("Python Crash Course", "Eric Matthes", "9781593279288", "Programming", 4, 4),
    ("Database System Concepts", "Silberschatz, Korth, Sudarshan", "9780078022159", "Databases", 2, 2),
    ("Fluent Python", "Luciano Ramalho", "9781492056355", "Programming", 3, 3),
    ("Design Patterns", "Gamma, Helm, Johnson, Vlissides", "9780201633610", "Software Engineering", 2, 2),
    ("Operating System Concepts", "Silberschatz, Galvin, Gagne", "9781119800361", "Computer Science", 2, 2),
]

# name, contact_number, email, membership_status
SEED_MEMBERS = [
    ("Grace Aitsi", "70012345", "grace.aitsi@example.com", "Active"),
    ("Peter Kaupa", "70023456", "peter.kaupa@example.com", "Active"),
    ("Maria Toua", "70034567", "maria.toua@example.com", "Active"),
    ("John Namaliu", "70045678", "john.namaliu@example.com", "Suspended"),
    ("Ruth Waigani", "70056789", None, "Active"),
]


def main():
    if not DB_PATH.exists():
        print(f"Could not find {DB_PATH}. Run schema.sql first to create the database.")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")

    books_added = 0
    for title, author, isbn, genre, total, available in SEED_BOOKS:
        existing = conn.execute("SELECT 1 FROM books WHERE isbn = ?", (isbn,)).fetchone()
        if existing:
            print(f"Skipped (already exists): {title}")
            continue
        conn.execute(
            """INSERT INTO books (title, author, isbn, genre, total_copies, available_copies)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (title, author, isbn, genre, total, available),
        )
        print(f"Added book: {title}")
        books_added += 1

    members_added = 0
    for name, contact, email, status in SEED_MEMBERS:
        existing = conn.execute(
            "SELECT 1 FROM members WHERE name = ? AND contact_number = ?", (name, contact)
        ).fetchone()
        if existing:
            print(f"Skipped (already exists): {name}")
            continue
        conn.execute(
            """INSERT INTO members (name, contact_number, email, membership_status)
               VALUES (?, ?, ?, ?)""",
            (name, contact, email, status),
        )
        print(f"Added member: {name}")
        members_added += 1

    conn.commit()
    conn.close()

    print(f"\nDone. Added {books_added} book(s) and {members_added} member(s).")


if __name__ == "__main__":
    main()
