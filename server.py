from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import requests
import os

load_dotenv()

mcp = FastMCP("GitHub MCP")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


@mcp.tool()
def list_repositories():
    """
    List all repositories of the authenticated user.
    """

    response = requests.get(
        "https://api.github.com/user/repos",
        headers=HEADERS
    )

    response.raise_for_status()

    repos = response.json()

    return [
        {
            "name": repo["name"],
            "full_name": repo["full_name"],
            "private": repo["private"]
        }
        for repo in repos
    ]


@mcp.tool()
def get_repository(owner: str, repo: str):
    """
    Get details of a repository.
    """

    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers=HEADERS
    )

    response.raise_for_status()

    repo_data = response.json()

    return {
        "name": repo_data["name"],
        "description": repo_data["description"],
        "stars": repo_data["stargazers_count"],
        "forks": repo_data["forks_count"]
    }


if __name__ == "__main__":
    mcp.run()