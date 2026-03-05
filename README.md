# FastAPI Todo Backend

A simple backend API for a Todo application built using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.
It provides basic CRUD operations for managing tasks.

---

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Uvicorn

---

## Project Structure

```
.
├── main.py      # API routes
├── models.py    # Database models
├── schemas.py   # Data validation schemas
├── crud.py      # Database operations
├── db.py        # Database connection
```

---

## Setup

### 1. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```

### 3. Configure database

Update the connection string in `db.py`:

```
postgresql://username:password@localhost:5432/todolist
```

Make sure PostgreSQL is running and the database exists.

### 4. Run the server

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

to test the API.

---

## API Endpoints

| Method | Endpoint      | Description        |
| ------ | ------------- | ------------------ |
| POST   | `/todos/`     | Create a todo      |
| GET    | `/todos/`     | Get all todos      |
| PUT    | `/todos/{id}` | Update todo status |
| DELETE | `/todos/{id}` | Delete a todo      |

---

## Example Request

```json
{
  "Title": "Learn FastAPI",
  "desc": "Build a todo backend"
}
```

---

A simple backend project for learning FastAPI and PostgreSQL.
