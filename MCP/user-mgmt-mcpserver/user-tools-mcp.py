
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
import requests
app = FastAPI()

import traceback

@app.get("/users", operation_id="getUsers", summary="this tool will give you all users")
def list_users() -> list:
    try:
        url = "http://localhost:8000/users/"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Exception occurred:", e)
        print(traceback.format_exc())
        return {"error": str(e), "traceback": traceback.format_exc()}

@app.post("/users/register", operation_id="register_user", summary="this tool is used to register user")
def register_user(username: str, email: str, password: str) -> dict:
    try:
        """Register a new user via POST /users/register"""
        url = "http://localhost:8000/users/register"
        payload = {"username": username, "email": email, "password": password}
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Exception occurred:", e)
        print(traceback.format_exc())
        return {"error": str(e), "traceback": traceback.format_exc()}
    


mcp = FastApiMCP(app, name="User MCP", description="Simple application to do user management")
mcp.mount()
