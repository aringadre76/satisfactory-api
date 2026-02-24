# Contributing to Satisfactory Game Data API

Thanks for your interest in contributing. This document explains how to run the project, run tests, and update data after game updates.

## Development setup

1. Clone the repo and install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Or install the package in editable mode:

   ```bash
   pip install -e .
   ```

2. Place the game descriptor file `en-US.json` in the `Docs/` directory. Without it, the server starts but `GET /ready` returns 503 and data endpoints may fail. Get `en-US.json` from your Satisfactory installation (e.g. under `CommunityResources/Docs/`).

3. Start the server:

   ```bash
   uvicorn src.api.main:app --reload
   ```

   Or: `./run.sh` (uses `PORT` from the environment or 8000).

4. Open `http://localhost:8000/docs` for interactive API docs.

## Running tests

Endpoint tests use the Postman collection and can run against a local server or the live API:

```bash
python3 scripts/run_postman_collection_tests.py
python3 scripts/run_postman_collection_tests.py --base-url https://satisfactory-api-yfw1.onrender.com
```

Results are written to `docs/endpoint_test_report.md` and `docs/endpoint_test_report.json`. The collection is in `docs/postman_collection.json`.

## Adding or changing endpoints

- Routers live under `src/api/routers/`. Add or edit a router and include it in `src/api/main.py`.
- Pydantic models for request/response live in `src/models/`.
- Game data is parsed in `src/parsers/game_descriptor_parser.py`. Use it to expose new fields or entities.
- After adding endpoints, update `docs/endpoints.md` and the Postman collection (`docs/postman_collection.json`) so docs and tests stay in sync.

## Updating after a game update

When Satisfactory releases an update:

1. Copy the new `en-US.json` into `Docs/`, or run the sync script from your game install path:

   ```bash
   python3 scripts/sync_game_data.py "C:\Program Files (x86)\Steam\steamapps\common\Satisfactory\CommunityResources"
   ```

   You can set `SATISFACTORY_SOURCE` instead of passing the path.

2. Run the verification script:

   ```bash
   python3 scripts/verify_data.py
   ```

3. Restart the API server.

If the game’s descriptor format changes, parser updates may be needed in `src/parsers/game_descriptor_parser.py`.

## Pull requests

- Keep changes focused. Use a short, clear branch name.
- Ensure the Postman-based tests pass (run the script above).
- Update `docs/endpoints.md` and the Postman collection when you add or change endpoints.

Contributions are welcome.
