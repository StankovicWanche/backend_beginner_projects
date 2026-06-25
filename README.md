# Backend Beginner Projects

A structured repository containing my journey into backend engineering with Python, FastAPI, and SQLAlchemy.

## 📁 Project 01: Live Status Logger API

A database-driven web application component that manages data tracking logs using local persistent storage. This project demonstrates foundational CRUD operations over an isolated multi-file software architecture.

### 🛠️ Tech Stack & Concepts Demonstrated
- **Framework:** FastAPI (Python Async Web Server Engine)
- **Database Architecture:** SQLAlchemy ORM (Object-Relational Mapping Framework)
- **Storage Engine:** SQLite (Local persistent file database architecture)
- **Patterns:** Separation of Concerns (Split into `main.py`, `models.py`, and `database.py`)

### 🚀 Core Endpoint Gateways
- `POST /logs` - **Create:** Submits and commits a new text record row into the database warehouse.
- `GET /history` - **Read:** Retrieves and lists every single stored record entry from the system.
- `PUT /logs/{log_id}` - **Update:** Performs live object modification on specific rows via unique ID trackers.
- `DELETE /logs/{log_id}` - **Destroy:** Permanently removes data crates entirely out of storage memory grids.
-