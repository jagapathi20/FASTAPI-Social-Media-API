# FastAPI Social Media API

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.121.0-009688.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-336791.svg)](https://www.postgresql.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://github.com/<your-username>/fastapi-social-media/actions/workflows/tests.yml/badge.svg)](https://github.com/<your-username>/fastapi-social-media/actions)

A full-featured **social media backend API** built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT authentication**.  
It demonstrates clean architecture, modular routing, Alembic migrations, password hashing, and robust testing using Pytest.

---

## Project Preview

> _Add your API demo screenshot or OpenAPI docs preview here._

![FastAPI Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

---

## Features

**User Authentication**
- JWT-based login system  
- Password hashing with `passlib`  
- Token verification & protected routes  

**Post Management**
- Create, Read, Update, Delete (CRUD) operations  
- Ownership checks (only authors can modify/delete)  
- Pagination & search support  

**Voting System**
- Upvote / downvote functionality  
- Prevents duplicate votes  

**Database & ORM**
- PostgreSQL + SQLAlchemy ORM  
- Alembic for migrations  
- Pydantic models for validation  

**Testing**
- Pytest with isolated test database  
- Fixtures for posts, users, and auth  
- CI-ready test configuration  

---

## Project Structure

```
app/
│
├── __init__.py
├── main.py                # FastAPI entry point
├── models.py              # SQLAlchemy models
├── schemas.py             # Pydantic schemas
├── utils.py               # Password hashing utilities
├── oauth2.py              # JWT creation & validation
├── config.py              # Environment configuration
├── database.py            # SQLAlchemy engine & session
│
├── routers/               # API routes
│   ├── post.py
│   ├── user.py
│   ├── auth.py
│   └── vote.py
│
├── tests/                 # Pytest suite
│   ├── conftest.py
│   ├── test_users.py
│   ├── test_posts.py
│   ├── test_votes.py
│   └── ...
│
├── alembic/               # Migration scripts
├── alembic.ini            # Alembic config
├── requirements.txt
└── README.md
```

---

## Installation

### Clone the repository
```bash
git clone https://github.com/<your-username>/fastapi-social-media.git
cd fastapi-social-media
```

### Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate     # Linux / macOS
venv\Scripts\activate        # Windows
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Set up environment variables  
Create a `.env` file in the project root:

```env
database_host_name=localhost
database_port=5432
database_password=yourpassword
database_name=fastapi
database_username=postgres
secret_key=your_secret_key
algorithm=HS256
access_token_expire_minutes=30
```

### Run Alembic migrations
```bash
alembic upgrade head
```

### Start the development server
```bash
uvicorn app.main:app --reload
```

Server runs at **http://127.0.0.1:8000**

Swagger docs at **http://127.0.0.1:8000/docs**

---

## Running Tests

```bash
pytest -v
```

---

## API Endpoints Overview

### Authentication
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/login` | User login, returns access token |

###  Users
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/users/` | Create a new user |
| GET | `/users/{id}` | Retrieve a user by ID |

### Posts
| Method | Endpoint | Description |
|--------|-----------|-------------|
| GET | `/posts/` | List all posts |
| GET | `/posts/{id}` | Retrieve a single post |
| POST | `/posts/` | Create a new post |
| PUT | `/posts/{id}` | Update an existing post |
| DELETE | `/posts/{id}` | Delete a post |

### Votes
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/vote/` | Cast or remove a vote on a post |

---

## Docker (Optional)

### Development mode
```bash
docker compose -f docker-compose-dev.yml up --build
```

### Production mode
```bash
docker compose -f docker-compose-prod.yml up --build -d
```

---

## Tech Stack

| Layer | Technology |
|-------|-------------|
| **Framework** | FastAPI |
| **Database** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **Migrations** | Alembic |
| **Authentication** | JWT via `python-jose` |
| **Testing** | Pytest |
| **Containerization** | Docker, Docker Compose |

---