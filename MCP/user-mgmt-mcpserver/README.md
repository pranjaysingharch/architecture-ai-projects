# User Tools MCP Server

This is a FastAPI-based MCP (Model Context Protocol) server that exposes user management operations as MCP tools.

## Setup


### 1. Install dependencies (using [uv](https://github.com/astral-sh/uv))

```bash
cd user-mgmt-mcpserver
uv sync
```

### 2. Run the MCP server

```bash
uvicorn user-tools-mcp:app --reload --port 6274
```

The MCP server will be available at `http://localhost:6274` by default.

## Features
- List all users (proxy to API)
- Register a new user (proxy to API)
- MCP tool metadata for interoperability

## Example: List Users via MCP

```python
import requests
response = requests.get("http://localhost:6274/users")
print(response.json())
```

## Example: Register User via MCP

```python
import requests
payload = {"username": "bob", "email": "bob@example.com", "password": "pw"}
response = requests.post("http://localhost:6274/users/register", params=payload)
print(response.json())
```

---

## Notes
- The MCP server proxies requests to the User Management API (default: `http://localhost:8000`).
- Ensure the API server is running before using the MCP server.
