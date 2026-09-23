# Library Management System

**Course:** IT0206 – Advanced Computer Programming
**Team:** Group 17
**Assessment:** Team Project Assessment (Capstone)

## Team Members
- Rachael Makapa — Team Lead / Lead Developer & Architect
- Dyan Koka — Database Engineer / QA & Test Lead
- Vernorah Tipi — Documentation Lead / Feature Developer

## Project Overview
A menu-driven Python application for managing a library's day-to-day operations — including book cataloguing, member registration, and borrowing/returning workflows. The system enforces authenticated, role-based access and persists all data in a relational database (SQLite), following a layered MVC architecture.

## Key Features
- Secure login with hashed passwords and at least two user roles (Administrator, Librarian/Staff)
- Full CRUD for books, members, and loan records
- Book borrowing and returning workflow with due dates and fines
- Search and filter for the book catalogue
- Summary reports (e.g. most borrowed books, overdue items)
- CSV/JSON import for bulk data
- Centralised logging and error handling

## Tech Stack
- **Language:** Python 3.11+
- **Database:** SQLite
- **Testing:** pytest
- **Libraries:** datetime, os, logging, requests, pandas, matplotlib, bcrypt

## Project Structure

    src/
    ├── main.py
    ├── models/
    ├── repositories/
    ├── controllers/
    ├── views/
    ├── services/
    ├── exceptions/
    └── utils/
    database/
    data/imports/
    tests/
    docs/
    logs/

## Setup Instructions
1. Clone the repository:

       git clone https://github.com/rchived-IT/python-project-library-team17.git

2. Create and activate a virtual environment:

       python -m venv venv
       venv\Scripts\activate   # Windows
       source venv/bin/activate  # macOS/Linux

3. Install dependencies:

       pip install -r requirements.txt

4. Run the application:

       python src/main.py

## Status
In development — Week 5 of 7 (Proposal & Planning phase)
