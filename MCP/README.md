# MCP Layer Overview

This repository demonstrates a modular architecture for user management using the Model Context Protocol (MCP) for interoperability and automation.

## What is MCP?
MCP (Model Context Protocol) is an open protocol that standardizes how tools, models, and services expose their capabilities for discovery and invocation by clients, agents, or other services. MCP enables seamless integration and automation across different systems and languages.

## Project Structure

- `API/user_management/` — FastAPI-based user management API
- `user-mgmt-mcpserver/` — FastAPI MCP server exposing user management as MCP tools

## How It Works

- The User Management API provides core user operations (register, list, get, delete).
- The MCP server proxies these operations and exposes them as MCP tools, making them discoverable and callable by any MCP-compatible client.

## Running the System

1. **Start the User Management API**
   ```bash
   cd API/user_management
   uv sync
   uvicorn main:app --reload
   ```
2. **Start the MCP Server**
   ```bash
   cd user-mgmt-mcpserver
   uv sync
   uvicorn user-tools-mcp:app --reload --port 6274
   ```

## VS Code Configuration to Call MCP Server

To enable VS Code (with MCP-compatible extensions) to call the MCP server, add the following configuration to your `.vscode/mcp.json` file:

```json
{
  "servers": {
    "User MCP": {
      "url": "http://localhost:6274/mcp",
      "type": "http"
    }
  }
}
```

- Place this file in your workspace's `.vscode/` directory.
- Ensure the MCP server is running at the specified URL and port.

## References
- [MCP Protocol Documentation](https://github.com/modelcontext/protocol)
- [uv: Fast Python package installer](https://github.com/astral-sh/uv)

---

For more details, see the individual `README.md` files in each subdirectory.
