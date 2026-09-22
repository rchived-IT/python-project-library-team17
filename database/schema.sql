-- Library Management System Database Schema
-- SQLite
-- Matches the entity descriptions in the SRS (Section 6.2) and
-- docs/requirements_traceability.md (FR-1, FR-3, FR-4, FR-5, FR-6)

PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------
-- Users: system accounts for Administrators and Librarian/Staff (FR-1, FR-2)
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS users (
    user_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    username        TEXT NOT NULL UNIQUE,
    password_hash   TEXT NOT NULL,
    role            TEXT NOT NULL CHECK (role IN ('Administrator', 'Librarian'))
);

-- ---------------------------------------------------------------
-- Books: catalogue of all books held by the library (FR-3, FR-7)
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS books (
    book_id             INTEGER PRIMARY KEY AUTOINCREMENT,
    title               TEXT NOT NULL,
    author              TEXT NOT NULL,
    isbn                TEXT NOT NULL UNIQUE,
    genre               TEXT,
    total_copies        INTEGER NOT NULL CHECK (total_copies >= 0),
    available_copies    INTEGER NOT NULL CHECK (
        available_copies >= 0 AND available_copies <= total_copies
    )
);

-- ---------------------------------------------------------------
-- Members: registered library members eligible to borrow books (FR-4)
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS members (
    member_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    name                TEXT NOT NULL,
    contact_number      TEXT NOT NULL,
    email               TEXT,
    membership_status   TEXT NOT NULL CHECK (
        membership_status IN ('Active', 'Suspended', 'Expired')
    )
);

-- ---------------------------------------------------------------
-- Loans: links a Book, a Member, and the issue/return/due dates (FR-5, FR-6)
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS loans (
    loan_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id         INTEGER NOT NULL REFERENCES books(book_id) ON DELETE CASCADE,
    member_id       INTEGER NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    issue_date      TEXT NOT NULL,
    due_date        TEXT NOT NULL,
    return_date     TEXT,
    fine_amount     REAL NOT NULL DEFAULT 0 CHECK (fine_amount >= 0),
    CHECK (due_date > issue_date)
);

-- ---------------------------------------------------------------
-- Indexes to speed up common lookups (FR-7 search/filter, FR-8 reporting)
-- ---------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_books_title   ON books(title);
CREATE INDEX IF NOT EXISTS idx_books_author  ON books(author);
CREATE INDEX IF NOT EXISTS idx_loans_book    ON loans(book_id);
CREATE INDEX IF NOT EXISTS idx_loans_member  ON loans(member_id);
