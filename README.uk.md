[English](README.md) | [**Українська**](README.uk.md)

# PostgreSQL Tasks CRUD

Невелике домашнє завдання, що будує нормалізовану схему PostgreSQL для трекера задач (`users`, `status`, `tasks`), наповнює її синтетичними даними через `Faker` і виконує всі обов'язкові SELECT-запити.

## Стек

- Python 3.12
- `psycopg2-binary`
- `Faker`

## Схема

- `users(id, fullname, email)`
- `status(id, name)` - наприклад `new`, `in progress`, `completed`
- `tasks(id, title, description, status_id → status.id, user_id → users.id)`

## Конфігурація

Налаштування підключення читаються зі змінних середовища (див. `.env.example`):

```
POSTGRES_HOST=localhost
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=
POSTGRES_PORT=5432
```

Скопіюйте `.env.example` → `.env` і впишіть локальний пароль.

## Запуск

```bash
pip install -r requirements.txt

# 1. Створити схему
python create_tables.py

# 2. Наповнити users + tasks
python seed.py

# 3. Виконати SELECT-вправи
python selecty.py

# Видалити все (очистка)
python delete_tables.py
```
