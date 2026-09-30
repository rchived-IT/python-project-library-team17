# Library Management System

**Course:** IT0206 – Advanced Computer Programming
**Team:** Group 17 (Team Project Assessment)
**Repository:** github.com/rchived-IT/python-project-library-team17

## Team Members

| Name | Student ID |
|---|---|
| Rachael Makapa | ST250068 |
| Dyan Koka | ST250073 |
| Vernorah Tipi | ST250467 |

## Project Overview

A menu-driven Python application for the day-to-day work of a small library: cataloguing books, registering members, lending and returning books with fines, searching, reporting, bulk data import/export and database backup. Users log in with a username and password and have one of two roles (Administrator or Librarian). Data is stored in SQLite through a layered, MVC-style design (models, repositories, services, controllers, views).

## Quick Start

Run every command from the project root. Python 3.11 or newer is required.

1. **Create and activate a virtual environment**

   ```text
   python -m venv venv
   venv\Scripts\activate          # Windows
   source venv/bin/activate       # macOS / Linux
   ```

2. **Install dependencies**

   ```text
   pip install -r requirements.txt
   ```

3. **Create the database from the schema** (skip if `data/database/app.db` already exists)

   ```text
   python -c "import sqlite3; sqlite3.connect('data/database/app.db').executescript(open('data/database/schema.sql').read())"
   ```

4. **Create the starter accounts and, optionally, sample data**

   ```text
   python seed_users.py
   python seed_catalogue.py
   ```

   `seed_users.py` prints the demonstration usernames and passwords when it runs. They are for testing only: change or delete them before real use.

5. **Start the application**

   ```text
   python -m src.main
   ```

6. **Run the automated tests**

   ```text
   python -m pytest -q
   ```

## Features

- Login with bcrypt-hashed passwords; Administrator and Librarian roles (only Administrators can manage user accounts)
- Create, view, update and delete books, members and loans
- Borrowing and returning with due dates, availability tracking and fines (default 1.00 per overdue day)
- Search books (title, author, ISBN, genre), members (name, contact, email) and loans (IDs)
- Reports: library summary, book availability, member status, loan summary, most-borrowed books and overdue loans
- pandas analytics export (`loan_analytics.csv`) and a matplotlib loan-status chart
- CSV and JSON import, CSV/JSON export and SQLite database backup
- Central logging to `logs/app.log` and custom exceptions
- Open Library catalogue lookup over HTTP (`requests`); this is a service method (`BookService.search_online_books`) and is not yet available from a menu

## Main Menu

```text
1. Manage Books        5. Reports
2. Manage Members      6. Logout
3. Manage Loans        7. Administration (Administrators only)
4. Search              8. Data Import / Backup
```

## Technology

| Area | Choice |
|---|---|
| Language | Python 3.11+ |
| Database | SQLite (`sqlite3`) |
| Libraries | bcrypt, requests, pandas, matplotlib, pytest |
| Standard library | sqlite3, csv, json, pathlib, logging, datetime, dataclasses, abc |

## Project Structure

```text
src/
├── main.py             entry point and main menu
├── models/             Book, Member, Loan, User
├── repositories/       parameterised SQLite access
├── services/           business rules, import/export, backup
├── controllers/        authentication and administration
├── views/              console menus and reports
├── reports/            abstract and concrete report renderers
├── exceptions/         custom exception classes
└── utils/              logging
data/
├── database/           schema.sql and app.db
├── imports/            sample CSV / JSON files
└── exports/            exports, backups, analytics and chart output
tests/                  pytest suite
docs/                   documentation
logs/                   application log
```

The layout follows the IT0206 handbook, with the differences explained in the Technical Documentation.

## Testing

Run `python -m pytest -q`. The team recorded **49 passing tests** (Windows, Python 3.14).

To measure coverage, install `pytest-cov` and run `python -m pytest --cov=src`.

Functional test cases, the UAT record and the defect log are in `docs/test_report.md` and `docs/uat_record.md`.

## Documentation

| File | Contents |
|---|---|
| `docs/installation_guide.md` | Environment and dependency set-up |
| `docs/user_manual.md` | End-user walkthrough |
| `docs/technical_documentation.md` | Architecture, class and ER diagrams, module reference |
| `docs/test_report.md` | Test plan, results, functional cases, defect log |
| `docs/uat_record.md` | UAT scenarios and sign-off |
| `docs/requirements_traceability.md` | Requirements mapped to code and tests |
| `docs/submission_checklist.md` | Submission checklist |

The Proposal, SRS, Database Design, User Manual, Technical Documentation and Test Report are also submitted together as one PDF.

## Data Privacy

- The system stores members' names, contact numbers and optional emails, and staff usernames with password hashes.
- Passwords are stored only as bcrypt hashes and are never logged.
- Data is visible only after login; user-account management is Administrator-only.
- Exports and backups contain member details in plain form, so store them securely.
- `.gitignore` excludes `*.db` and log files so the live database and logs are not published.
- Sample members are fictitious.

## AI Usage Disclosure

The first drafts of the six project documents were generated with Claude (Anthropic) from the project repository, and was reviewed and rewritten by the team. Any other AI use is described in the Technical Documentation, Section 15.

## Known Issues

- `seed_catalogue.py` sets its database path to `data/data/database/app.db` instead of `data/database/app.db`, so it may not find the database. Correct the path in the script before running it.

## Version Control

The code is developed in Git and hosted on GitHub. The commit history is in the repository.

## Acknowledgements

Third-party libraries (bcrypt, requests, pandas, matplotlib, pytest) are used under their own open-source licences.
