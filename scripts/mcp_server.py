"""
MCP server that exposes the Satisfactory Game Data API as tools.
Run with: uv run --with mcp python scripts/mcp_server.py
Or after pip install -e ".[mcp]": python -m scripts.mcp_server

Cursor: add an MCP server with command "uv" and args ["run", "--with", "mcp", "python", "scripts/mcp_server.py"]
(or point to the repo path). Uses stdio transport by default.
"""
from __future__ import annotations

import json
import os

import httpx

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    raise SystemExit("Install MCP SDK: pip install mcp  or  uv add mcp")

BASE_URL = os.environ.get(
    "SATISFACTORY_API_BASE_URL",
    "https://satisfactory-api-yfw1.onrender.com",
).rstrip("/")

mcp = FastMCP(
    "Satisfactory API",
    json_response=True,
)


@mcp.tool()
def get_planning_context(
    tier: int | None = None,
    milestone: str | None = None,
    include_progression: bool = False,
) -> dict:
    """
    Fetch the full planning-context payload from the Satisfactory API: items, recipes,
    buildings, belts, miners, resource-nodes, raw-resources, overclock, and optionally
    progression (milestones and unlocks). Use this to bootstrap a factory planner in one call.
    Optional tier (integer) or milestone (display name) filters data to that tier/milestone.
    """
    params: dict[str, str | int | bool] = {}
    if tier is not None:
        params["tier"] = tier
    if milestone is not None:
        params["milestone"] = milestone
    if include_progression:
        params["include_progression"] = "true"
    with httpx.Client(timeout=60.0) as client:
        r = client.get(f"{BASE_URL}/planning-context", params=params)
        r.raise_for_status()
        return r.json()


@mcp.tool()
def satisfactory_get(path: str, query_params: str | None = None) -> dict | list:
    """
    Call any GET endpoint on the Satisfactory Game Data API. path is the path without
    leading slash (e.g. 'recipes', 'items/Iron Ingot', 'calculate/buildings-needed').
    query_params is an optional JSON object of query parameters (e.g. {"recipe_name": "Iron Plate", "target_per_min": "60"}).
    Returns the JSON response.
    """
    path = path.lstrip("/")
    params = json.loads(query_params) if query_params else None
    with httpx.Client(timeout=30.0) as client:
        r = client.get(f"{BASE_URL}/{path}", params=params or {})
        r.raise_for_status()
        return r.json()


if __name__ == "__main__":
    mcp.run(transport="stdio")
