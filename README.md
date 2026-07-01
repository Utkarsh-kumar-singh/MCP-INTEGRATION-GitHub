# 🚀 GitHub MCP Server

A production-ready **Model Context Protocol (MCP) Server** built with Python that enables AI assistants and MCP clients to interact with GitHub repositories through the GitHub REST API.

This project demonstrates how to build a custom MCP server capable of performing GitHub operations such as listing repositories, retrieving repository information, managing issues, and extending to pull requests, workflows, and code management.

---

## 📌 Features

### Repository Management

* List all repositories for the authenticated user
* Retrieve repository details
* Access repository metadata

### Issue Management

* List repository issues
* Create new issues
* Close existing issues *(future enhancement)*

### MCP Integration

* Built using the official MCP Python SDK
* Compatible with MCP Inspector
* JSON-RPC based communication
* Local STDIO transport support

---

## 🏗️ Architecture

```text
┌─────────────────────┐
│   MCP Client        │
│ (Inspector / AI)    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   GitHub MCP Server │
│      (Python)       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   GitHub REST API   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   GitHub Account    │
└─────────────────────┘
```

---

# 📂 Project Structure

```text
github-mcp/
│
├── server.py
├── .env
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

---

# ⚙️ Prerequisites

* Python 3.10+
* UV Package Manager
* GitHub Account
* GitHub Personal Access Token (PAT)
* Node.js (for MCP Inspector)

---

# 🔑 GitHub Token Setup

Generate a Personal Access Token from:

https://github.com/settings/tokens

Recommended permissions:

```text
Repository Access
Issues: Read & Write
Contents: Read
Pull Requests: Read & Write
```

Create a `.env` file:

```env
GITHUB_TOKEN=your_github_token_here
```

---

# 📦 Installation

Clone the repository:

```bash
git clone <repository-url>
cd github-mcp
```

Initialize project:

```bash
uv init
```

Install dependencies:

```bash
uv add mcp requests python-dotenv
```

---

# ▶️ Running the Server

Start the MCP server:

```bash
uv run server.py
```

The server will wait for MCP client connections.

---

# 🔍 Using MCP Inspector

Start MCP Inspector:

```bash
npx @modelcontextprotocol/inspector
```

Open:

```text
http://localhost:6274
```

Connection Settings:

```text
Transport : STDIO

Command:
uv

Arguments:
run server.py
```

Click **Connect**.

---

# 🛠️ Available Tools

## list_repositories

Returns all repositories accessible by the authenticated user.

### Example

```json
{}
```

### Response

```json
[
  {
    "name": "github-mcp",
    "full_name": "username/github-mcp",
    "private": false
  }
]
```

---

## get_repository

Returns details for a specific repository.

### Input

```json
{
  "owner": "username",
  "repo": "github-mcp"
}
```

### Response

```json
{
  "name": "github-mcp",
  "description": "GitHub MCP Server",
  "stars": 10,
  "forks": 2
}
```

---

# 🔄 MCP Request Flow

```text
User
 │
 ▼
MCP Client
 │
 ▼
Tool Call
 │
 ▼
GitHub MCP Server
 │
 ▼
GitHub REST API
 │
 ▼
Response Returned
```

---

# 🚧 Planned Enhancements

* Create GitHub Issues
* Close Issues
* Pull Request Management
* Branch Management
* File Operations
* GitHub Actions Integration
* Repository Search
* Code Search
* OAuth Authentication
* Remote MCP Deployment

---

# 🧠 Learning Outcomes

This project demonstrates:

* Model Context Protocol (MCP)
* MCP Tools
* JSON-RPC Communication
* GitHub REST API Integration
* Authentication using PAT
* MCP Inspector Usage
* Production MCP Architecture
* Local MCP Server Development

---

# 📄 License

MIT License

---

# 👨‍💻 Author

Built as a learning and production-ready MCP project for understanding MCP architecture, GitHub integrations, and AI tooling ecosystems.

# Test commit for pull request