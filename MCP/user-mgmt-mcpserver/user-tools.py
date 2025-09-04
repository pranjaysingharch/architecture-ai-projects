# hello_mcp.py
from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("UserMCP")

@mcp.tool()
def register_user(username: str, email: str, password: str) -> dict:
    """Register a new user via POST /users/register"""
    url = "http://localhost:8000/users/register"
    payload = {"username": username, "email": email, "password": password}
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()

@mcp.tool()
def get_user(user_id: int) -> dict:
    """Get a user by ID via GET /users/{user_id}"""
    url = f"http://localhost:8000/users/{user_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

@mcp.tool()
def delete_user(user_id: int) -> dict:
    """Delete a user by ID via DELETE /users/{user_id}"""
    url = f"http://localhost:8000/users/{user_id}"
    response = requests.delete(url)
    response.raise_for_status()
    return response.json()

@mcp.tool()
def list_users() -> list:
    """List all users via GET /users/"""
    url = "http://localhost:8000/users/"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# ✅ expose SSE app for uvicorn
app = mcp.sse_app
