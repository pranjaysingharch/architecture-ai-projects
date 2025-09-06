# User Management API

A FastAPI-based User Management API supporting user registration, profile retrieval, listing, and deletion.

# User Management API

This is a FastAPI-based user management API for registering, listing, retrieving, and deleting users.

## Setup


### 1. Install dependencies (using [uv](https://github.com/astral-sh/uv))

```bash
cd API/user_management
uv sync
```

### 2. Run the API server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000` by default.

## Endpoints

- `POST /users/register` — Register a new user
- `GET /users/{user_id}` — Get user by ID
- `GET /users/` — List all users
- `DELETE /users/{user_id}` — Delete user

## Example: Register a User

```http
POST /users/register
Content-Type: application/json

{
   "username": "alice",
   "email": "alice@example.com",
   "password": "securepassword"
}
```

## Example: List Users

```http
GET /users/
```

---

## Notes
- This demo uses in-memory storage. All data will be lost on server restart.
- For production, add authentication and persistent storage.
