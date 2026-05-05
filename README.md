# PostgreSQL Tasks CRUD

A small homework that builds a normalized PostgreSQL schema for a task tracker (`users`, `status`, `tasks`), seeds it with synthetic data via `Faker`, and exercises every required SELECT query.

## Stack

- Python 3.12
- `psycopg2-binary`
- `Faker`

## Schema

- `users(id, fullname, email)`
- `status(id, name)` — e.g. `new`, `in progress`, `completed`
- `tasks(id, title, description, status_id → status.id, user_id → users.id)`

## Configuration

The connection settings are read from environment variables (see `.env.example`):

```
POSTGRES_HOST=localhost
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=
POSTGRES_PORT=5432
```

Copy `.env.example` → `.env` and fill in your local password.

## Run

```bash
pip install -r requirements.txt

# 1. Create the schema
python create_tables.py

# 2. Seed users + tasks
python seed.py

# 3. Run the SELECT exercises
python selecty.py

# Drop everything (cleanup)
python delete_tables.py
```
