# Satisfactory Game Data API

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

A simple REST API that provides game data from Satisfactory in an easy-to-use format. Perfect for building factory planning tools, calculators, and automation scripts.

## What is This?

This API reads game data files from your Satisfactory installation and makes all the information available through simple HTTP requests. Instead of digging through game files yourself, you can just ask the API for:

- How fast belts move
- What recipes exist and how they work
- Building specifications and requirements
- Resource extraction rates
- Transportation system details
- And much more!

## Quick Start

**1. Install dependencies:**
```bash
pip install -r requirements.txt
```

Or install as a package (editable):
```bash
pip install -e .
```

**2. Make sure you have the game data file:**
- Place `en-US.json` from your Satisfactory installation into the `Docs/` directory
- This file contains all the game data the API needs
- Without it, the server still starts but `GET /ready` returns 503 and data endpoints may fail

**3. Start the server:**
```bash
uvicorn src.api.main:app --reload
```

Or run the installed entry point: `satisfactory-api` (uses `PORT` from the environment or 8000).

**4. Visit the interactive documentation:**
- Open your browser to `http://localhost:8000/docs`
- This gives you a visual interface to try all the endpoints

Alternatively, run `./run.sh` (uses `PORT` from the environment or 8000).

That's it! Your API is running and ready to use.

## Live API

A deployed instance is available at `https://satisfactory-api-yfw1.onrender.com` (no auth). Use `/docs` there for interactive docs. Full endpoint list and test status: see `docs/endpoints.md`. You can try the API without any local setup by using this base URL in your scripts or with `curl`.

## Use in your project

You can depend on this API in two ways:

**Option A: Call the live API**  
Use the base URL `https://satisfactory-api-yfw1.onrender.com` in your app. No installation or game data required. Example with `httpx`:

```bash
pip install httpx
```

```python
import httpx
base = "https://satisfactory-api-yfw1.onrender.com"
r = httpx.get(f"{base}/recipes", params={"alternate_only": True, "limit": 10})
recipes = r.json()
```

**Option B: Run your own instance**  
Clone this repo, add `Docs/en-US.json` from your game install, then run the server. Use `http://localhost:8000` (or your deployed URL) as the base URL in your code. See [Deploying the API](#deploying-the-api) for hosting options.

**Generate a client from the API**  
The API exposes an OpenAPI 3.0 spec at `GET /openapi.json`. Use it with [OpenAPI Generator](https://openapi-generator.tech/), [Swagger Codegen](https://swagger.io/tools/swagger-codegen/), or your IDE to generate a type-safe client in Python, TypeScript, or other languages. Example (replace with your base URL if self-hosting):

```bash
curl -o openapi.json https://satisfactory-api-yfw1.onrender.com/openapi.json
openapi-generator generate -i openapi.json -g python -o ./satisfactory-client
```

## API stability

This project follows [Semantic Versioning](https://semver.org/) for the API. Patch releases (e.g. 1.0.x) keep response shapes and query parameters compatible. Breaking changes will be documented in [CHANGELOG.md](CHANGELOG.md) and released as a new major version.

## What Can I Do With This API?

### Get Game Data
Access information about miners, belts, recipes, buildings, items, and transportation systems through simple HTTP requests.

### Build Tools
Create factory calculators, production planners, or automation scripts that need real game data.

### Filter and Search
Query recipes by building type, find alternate recipes, filter items by category, and more.

### Calculate Production
Use the calculation endpoints to figure out building requirements, production chains, and resource needs.

### Use cases

Use this API to build:

- Factory calculators and production planners
- Bots or scripts that need up-to-date recipe and building data
- Web or mobile apps that display Satisfactory data (belts, miners, power, logistics)
- Tools that compare recipes or compute full production chains

If you build something with this API, consider sharing it so we can link it here.

## Available Endpoints

Full reference with request/response details: `docs/endpoints.md`. Summary by group:

### Health and readiness
- `GET /health` - Liveness; returns 200 when the app is running
- `GET /ready` - Readiness; returns 200 when the app and game descriptor are loadable (503 otherwise)

### Miners
- `GET /miners` - All miners (Mk1, Mk2, Mk3)
- `GET /miners/{mk}` - Specific miner details

### Conveyor Belts
- `GET /belts` - All belt types (Mk1 through Mk6)
- `GET /belts/{mk}` - Specific belt speed and details

### Recipes
- `GET /recipes` - All recipes in the game
  - Add `?alternate_only=true` to see only alternate recipes
  - Add `?building=Constructor` to filter by building type
  - Optional `?limit=` and `?offset=` for pagination (see docs/endpoints.md)
- `GET /recipes/{recipe_name}` - Get a specific recipe

### Buildings
- `GET /buildings` - All production buildings
  - Add `?building_type=Assembler` to filter
- `GET /buildings/{building_type}` - Specific building details

### Items
- `GET /items` - All items (resources, components, equipment)
  - Add `?item_type=component` to filter by type
  - Optional `?limit=` and `?offset=` for pagination (see docs/endpoints.md)
- `GET /items/{item_name}` - Specific item information

### Transportation
Get information about all transportation methods:

**Pipelines**
- `GET /transportation/pipelines` - All pipeline types
- `GET /transportation/pipelines/{mk}` - Specific pipeline

**Pipeline Pumps**
- `GET /transportation/pipeline-pumps` - All pump types
- `GET /transportation/pipeline-pumps/{mk}` - Specific pump

**Trains**
- `GET /transportation/train-stations` - All station types
  - Add `?station_type=solid` to filter
- `GET /transportation/trains/locomotives` - Locomotive specs
- `GET /transportation/trains/freight-cars` - Freight car specs

**Vehicles**
- `GET /transportation/vehicles/trucks` - All vehicles (Truck, Tractor)
- `GET /transportation/vehicles/trucks/{vehicle_type}` - Specific vehicle

**Drones**
- `GET /transportation/drone-stations` - Drone station info
- `GET /transportation/drones` - Drone specifications

**Truck Stations**
- `GET /transportation/truck-stations` - Truck station details

### Resources
- `GET /resource-nodes` - All resource node types with purity levels
- `GET /raw-resources` - All raw resource definitions
- `GET /wiki/{item}` - Get wiki link for any item

### Calculations
- `GET /calculate/production-rate` - Production rate for a recipe
- `GET /calculate/buildings-needed` - Buildings needed for a target rate
- `GET /calculate/production-chain` - Full production chain
- `GET /calculate/compare-recipes` - Compare recipes
- `GET /calculate/miner-output` - Miner output by node and purity
- `GET /calculate/belt-requirements` - Belt requirements for a rate
- Additional calculation endpoints: see `docs/endpoints.md`

### Power
- `GET /power/generators` - Power generator specs
- `GET /power/storage` - Power storage (e.g. batteries)
- `GET /power/poles` - Power pole types

### Logistics
- `GET /logistics/splitters` - Conveyor splitters
- `GET /logistics/mergers` - Conveyor mergers
- `GET /logistics/storage` - Storage containers
- `GET /logistics/fluid-buffers` - Fluid buffers
- `GET /logistics/valves` - Valves

### Extractors
- `GET /extractors/water-extractors` - Water extractors
- `GET /extractors/resource-well-extractors` - Resource well extractors

### Progression
- `GET /progression/milestones` - Milestones (optional `?limit=` and `?offset=` for pagination; see docs/endpoints.md)
- `GET /progression/unlocks` - Unlocks (optional `?limit=` and `?offset=` for pagination; see docs/endpoints.md)

### More you can do (summary)

The above lists the main endpoints. The API also supports many lookups and filters not shown in full here:

- **Transportation:** Freight platforms (`/transportation/freight-platforms`), railway tracks (`/transportation/railway-tracks`), train signals (`/transportation/trains/signals`, plus by type). Get a single item by name: locomotives, freight cars, drones, train stations.
- **Progression:** Milestones by tier (`/progression/milestones/{tier}`) or by name (`/progression/milestones/name/{milestone_name}`). Unlocks by name or by type (`/progression/unlocks/type/{unlock_type}`).
- **Power:** Generators by name or by tier; storage by name; poles by name.
- **Logistics:** Splitters, mergers, storage containers, and valves by name (e.g. `/logistics/splitters/{splitter_name}`).
- **Extractors:** Water extractors and resource well extractors by name.

For the complete list of paths, query parameters, and response shapes, see `docs/endpoints.md`.

## Example Usage

Examples below use the live API. Replace the base URL with `http://localhost:8000` when running the API locally.

**Get all recipes:**
```bash
curl https://satisfactory-api-yfw1.onrender.com/recipes
```

**Get only alternate recipes:**
```bash
curl "https://satisfactory-api-yfw1.onrender.com/recipes?alternate_only=true"
```

**Get a specific item:**
```bash
curl "https://satisfactory-api-yfw1.onrender.com/items/Iron%20Ingot"
```

**Get all Mk3 belts:**
```bash
curl https://satisfactory-api-yfw1.onrender.com/belts/3
```

**Run the example script** (fetches recipes and runs a buildings-needed calculation):
```bash
python3 examples/fetch_and_calculate.py
python3 examples/fetch_and_calculate.py --base-url http://localhost:8000
```

## Interactive Documentation

When the API is running, you can use the built-in documentation:

- **Swagger UI**: `http://localhost:8000/docs` - Visual interface to test endpoints
- **ReDoc**: `http://localhost:8000/redoc` - Clean, readable API documentation

Both are automatically generated and always up-to-date with the API.

## Testing

Run the Postman-based endpoint tests (requires the server to be running, or use the live API):

```bash
python3 scripts/run_postman_collection_tests.py
python3 scripts/run_postman_collection_tests.py --base-url https://satisfactory-api-yfw1.onrender.com
```

The collection is in `docs/postman_collection.json`. Results are written to `docs/endpoint_test_report.md` and `docs/endpoint_test_report.json`.

## MCP (Model Context Protocol) server

The API can be exposed as an MCP server so AI assistants (e.g. Cursor) can call it as tools. Two tools are provided:

- **get_planning_context** – Returns the full planning-context payload (items, recipes, buildings, belts, miners, resource-nodes, raw-resources, overclock; optional progression). Optional args: `tier`, `milestone`, `include_progression`.
- **satisfactory_get** – Generic GET: pass a path (e.g. `recipes`, `items/Iron Ingot`, `calculate/buildings-needed`) and optional `query_params` as JSON to call any endpoint.

Install the MCP SDK, then run the server with stdio (for Cursor):

```bash
pip install mcp
python scripts/mcp_server.py
```

Or with uv (no install): `uv run --with mcp python scripts/mcp_server.py`

Base URL is taken from `SATISFACTORY_API_BASE_URL` (default: the live deployment). To use your local API, set `SATISFACTORY_API_BASE_URL=http://localhost:8000`.

**Cursor:** In Settings > Features > MCP, add a new server. Choose **stdio**. Set the command to `python` (or `python3`) and args to the full path to `scripts/mcp_server.py` in your repo. Ensure the MCP package is installed in that environment (`pip install mcp` or `uv add mcp`). Alternatively use command `uv` with args `run`, `--with`, `mcp`, `python`, `<full-path>/scripts/mcp_server.py`.

## Project Structure

```
satisfactory-api/
├── src/
│   ├── api/
│   │   ├── main.py
│   │   └── routers/
│   ├── parsers/
│   ├── models/
│   └── utils/
├── Docs/
│   └── en-US.json
├── docs/
│   ├── endpoints.md
│   ├── postman_collection.json
│   └── endpoint_test_report.md
├── examples/
│   └── fetch_and_calculate.py
├── scripts/
│   ├── sync_game_data.py
│   ├── verify_data.py
│   ├── run_postman_collection_tests.py
│   └── mcp_server.py
├── run.sh
├── Dockerfile
├── pyproject.toml
├── requirements.txt
├── CONTRIBUTING.md
├── CHANGELOG.md
└── LICENSE
```

## Updating After Game Updates

When Satisfactory releases an update:

1. Copy the new `en-US.json` file to the `Docs/` directory
   - Or run the sync script to pull from your game install:
     ```bash
     python3 scripts/sync_game_data.py "C:\Program Files (x86)\Steam\steamapps\common\Satisfactory\CommunityResources"
     ```
     If the descriptor JSON files live in a `Docs` subfolder under that path, they are copied into project `Docs/`. You can set `SATISFACTORY_SOURCE` instead of passing the path, or use the WSL path from Linux.
2. Run the verification script: `python3 scripts/verify_data.py`
3. Restart the API server

The API automatically reads from the data files, so no code changes are needed.

## Data Source

The API reads from game descriptor files that come with your Satisfactory installation. These JSON files contain all the game data in a structured format. The API simply makes this data accessible through HTTP endpoints.

## Deploying the API

You can run the API on the web so others can call it. The app uses the `PORT` environment variable when set (default 8000), which most hosting platforms provide automatically.

**Configuration (environment variables):**

- `PORT` – Port to bind (default 8000). Set by most PaaS providers.
- `BASE_URL` – Optional. If set, the root response `GET /` includes a `base_url` field with this value (e.g. `https://your-app.onrender.com`). Useful for clients that discover the API URL from the root.
- `SATISFACTORY_SOURCE` – Optional. Default source path for `scripts/sync_game_data.py` when no path argument is given.

**Health and readiness:** For load balancers and orchestration, use `GET /health` (returns 200 when the app is up) and `GET /ready` (returns 200 when the app and the game descriptor file are loadable; returns 503 if the descriptor is missing or invalid). See `docs/endpoints.md` for details.

### Docker

Build and run locally or on any host that supports Docker:

```bash
docker build -t satisfactory-api .
docker run -p 8000:8000 satisfactory-api
```

To use a different port: `docker run -p 3000:3000 -e PORT=3000 satisfactory-api`

### Railway

1. Push the repo to GitHub and sign in at [railway.app](https://railway.app).
2. New Project -> Deploy from GitHub repo -> select this repo.
3. Railway will detect the Dockerfile and deploy. If you do not use Docker, set the start command to: `uvicorn src.api.main:app --host 0.0.0.0 --port $PORT`
4. Open the generated URL (e.g. `https://your-app.up.railway.app`). Docs: `https://your-app.up.railway.app/docs`

### Render

1. Push to GitHub and sign in at [render.com](https://render.com).
2. New -> Web Service -> connect the repo.
3. Environment: Python 3. Set start command: `uvicorn src.api.main:app --host 0.0.0.0 --port $PORT`
4. Deploy. Your API will be at `https://your-service.onrender.com`

### Fly.io

1. Install [flyctl](https://fly.io/docs/hands-on/install-flyctl/) and sign in.
2. From the project root: `fly launch` (accept defaults or name the app).
3. Deploy: `fly deploy`. The API will be at `https://your-app.fly.dev`

After deploying, share the base URL (e.g. `https://your-app.fly.dev`) so others can call endpoints like `GET /recipes` or use `/docs` for the interactive API docs.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for the full text. The project is for educational and community use with Satisfactory game data.

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to run tests, add endpoints, and update data after game updates.
