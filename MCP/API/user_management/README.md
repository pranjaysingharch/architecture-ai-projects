# User Management API

A FastAPI-based User Management API supporting user registration, profile retrieval, listing, and deletion.

## Features

- Register new users
- Retrieve user profile by ID
- List all users
- Delete users

## Setup

1. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

2. Run the API server:

   ```powershell
   uvicorn main:app --reload
   ```

## Endpoints

- `POST /users/register` - Register a new user
- `GET /users/{user_id}` - Get user by ID
- `GET /users/` - List all users
- `DELETE /users/{user_id}` - Delete user
