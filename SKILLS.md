# Satisfactory Game Data API – Skill for AI Assistants

Use this file so your AI assistant (Cursor, Cloud Code, Codex, etc.) knows the Satisfactory API: base URL, all endpoints, and where to find full details. Add this file to your project or point your tool at it.

## Base URL and auth

- **Base URL (live):** `https://satisfactory-api-yfw1.onrender.com`
- **Base URL (local):** `http://localhost:8000`
- **Authentication:** None. All endpoints are public.

Interactive docs: `{base}/docs`. OpenAPI spec: `{base}/openapi.json`.

## Pagination

Only these list endpoints support optional `limit` and `offset` query parameters (1–1000 and ≥0): `GET /recipes`, `GET /items`, `GET /progression/milestones`, `GET /progression/unlocks`. All other list endpoints return the full list with no pagination.

## All endpoints (method, path, purpose)

### Root and health

| Method | Path | Purpose |
|--------|------|--------|
| GET | `/` | API info (message, version, links to /docs and /openapi.json) |
| GET | `/health` | Liveness (200 if process is running) |
| GET | `/ready` | Readiness (200 if game data is loaded, 503 if not) |
| GET | `/meta` | API version, game data timestamp, overclock min/max/presets |
| GET | `/version` | Same as /meta |

### Planning bootstrap

| Method | Path | Purpose |
|--------|------|--------|
| GET | `/planning-context` | Single payload: items, recipes, buildings, belts, miners, resource-nodes, raw-resources, overclock; optional tier/milestone filter and include_progression (milestones + unlocks) |

### Core data

| Method | Path | Purpose |
|--------|------|--------|
| GET | `/miners` | All miners (Mk1–Mk3) |
| GET | `/miners/{mk}` | One miner by mark (1–3) |
| GET | `/belts` | All belts (Mk1–Mk6); speed in items/min |
| GET | `/belts/{mk}` | One belt by mark (1–6) |
| GET | `/recipes` | All recipes; filters: alternate_only, building, search, produces, unlocked_by_tier, unlocked_by_milestone, limit, offset |
| GET | `/recipes/{recipe_name}` | One recipe by name or class name |
| GET | `/buildings` | All production buildings; filters: building_type, unlocked_by_tier, unlocked_by_milestone |
| GET | `/buildings/{building_type}` | One building type |
| GET | `/items` | All items; filters: item_type, tier, phase, unlocked_by_tier, unlocked_by_milestone, limit, offset |
| GET | `/items/{item_name}` | One item by name or class name |
| GET | `/resource-nodes` | All resource node types |
| GET | `/raw-resources` | All raw resources |

### Calculations

| Method | Path | Purpose |
|--------|------|--------|
| GET | `/calculate/production-rate` | Items/min for a recipe (query: recipe, building?, overclock?) |
| GET | `/calculate/buildings-needed` | Building count for target rate (recipe, target_rate, building?, overclock?) |
| GET | `/calculate/production-chain` | Full chain for an item at target rate (item, target_rate, include_alternates?, preferred_recipe?, byproduct_recycling?, max_belt_mk?, input_belt_limit?, output_belt_limit?) |
| GET | `/calculate/compare-recipes` | Compare all recipes that produce an item (item) |
| GET | `/calculate/miner-output` | Miner output rate (miner_mk, overclock?, purity?) |
| GET | `/calculate/belt-requirements` | Belt mk and count for a throughput (throughput_per_minute) |
| GET | `/calculate/perfect-ratios` | Perfect building ratios for 100% efficiency (item, target_rate, include_alternates?, preferred_recipe?, allow_overclock?) |
| GET | `/calculate/optimize-100-percent` | Optimize chain for 100% efficiency (item, target_rate, include_alternates?, preferred_recipe?, allow_overclock?) |
| GET | `/calculate/factory-efficiency` | Factory efficiency metrics (item, target_rate, include_alternates?, preferred_recipe?, allow_overclock?) |
| GET | `/calculate/building-utilization` | Per-building utilization (item, target_rate, include_alternates?, preferred_recipe?) |

### Power

| Method | Path | Purpose |
|--------|------|--------|
| GET | `/power/generators` | All generators; filter: generator_type |
| GET | `/power/generators/{generator_type}` | One generator type |
| GET | `/power/generators/name/{generator_name}` | Generator by name |
| GET | `/power/generators/tier/{tier}` | Generators by tier |
| GET | `/power/storage` | All power storage |
| GET | `/power/storage/{storage_name}` | One storage by name |
| GET | `/power/poles` | All power poles |
| GET | `/power/poles/{mk}` | Pole by mk |
| GET | `/power/poles/name/{pole_name}` | Pole by name |

### Logistics

| Method | Path | Purpose |
|--------|------|--------|
| GET | `/logistics/splitters` | All splitters |
| GET | `/logistics/splitters/{splitter_name}` | One splitter |
| GET | `/logistics/mergers` | All mergers |
| GET | `/logistics/mergers/{merger_name}` | One merger |
| GET | `/logistics/storage` | All storage containers |
| GET | `/logistics/storage/{container_name}` | One container |
| GET | `/logistics/fluid-buffers` | All fluid buffers |
| GET | `/logistics/valves` | All valves |
| GET | `/logistics/valves/{valve_name}` | One valve |

### Extractors

| Method | Path | Purpose |
|--------|------|--------|
| GET | `/extractors/water-extractors` | All water extractors |
| GET | `/extractors/water-extractors/{extractor_name}` | One water extractor |
| GET | `/extractors/resource-well-extractors` | All resource well extractors |

### Transportation

| Method | Path | Purpose |
|--------|------|--------|
| GET | `/transportation/trains/locomotives` | All locomotives |
| GET | `/transportation/trains/freight-cars` | All freight cars |
| GET | `/transportation/trains/locomotives/{locomotive_name}` | One locomotive |
| GET | `/transportation/trains/freight-cars/{car_name}` | One freight car |
| GET | `/transportation/trains/signals` | All train signals |
| GET | `/transportation/trains/signals/{signal_type}` | One signal type |
| GET | `/transportation/railway-tracks` | Railway track types |
| GET | `/transportation/train-stations/{station_name}` | Train station by name |
| GET | `/transportation/vehicles/trucks` | All trucks |
| GET | `/transportation/vehicles/trucks/{vehicle_type}` | One truck type |
| GET | `/transportation/drones` | All drones |
| GET | `/transportation/drones/{drone_name}` | One drone |
| GET | `/transportation/freight-platforms` | All freight platforms |

### Progression

| Method | Path | Purpose |
|--------|------|--------|
| GET | `/progression/milestones` | All milestones; filters: tier, phase, limit, offset |
| GET | `/progression/milestones/{tier}` | Milestones by tier |
| GET | `/progression/milestones/name/{milestone_name}` | One milestone by name |
| GET | `/progression/unlocks` | All unlocks; filters: unlock_type, limit, offset |
| GET | `/progression/unlocks/{unlock_name}` | One unlock by name |
| GET | `/progression/unlocks/type/{unlock_type}` | Unlocks by type |

### Wiki and docs

| Method | Path | Purpose |
|--------|------|--------|
| GET | `/wiki/{item}` | Wiki info for an item |
| GET | `/docs` | Swagger UI |
| GET | `/redoc` | ReDoc |
| GET | `/openapi.json` | OpenAPI 3.0 spec |

## Full reference

For request/response shapes, all query parameters, and examples: use the API’s interactive docs at `{base}/docs`, or the OpenAPI spec at `{base}/openapi.json`. If you have the repo, see `docs/endpoints.md`.

## How to add this skill

- **Cursor:** Put this file in your project and reference it in project instructions, or add a skill under `.cursor/skills/` whose SKILL.md says to read the project’s `SKILLS.md` (or copy this file into that skill).
- **Cloud Code / Codex / other tools:** Configure the tool to include this file as project context or a pinned doc (path: `SKILLS.md` in the repo root, or copy it into your app repo).

---

## For repo contributors (this project only)

- Run API: `uvicorn src.api.main:app --reload` or `satisfactory-api`. Sync game data: `python3 scripts/sync_game_data.py`. Run Postman tests: `python3 scripts/run_postman_collection_tests.py`. Verify data: `python3 scripts/verify_data.py`.
- Prefer `python3`, no comments in code or terminal commands, no em dashes. Do not git commit until the user asks.
- Full endpoint docs and examples live in `docs/endpoints.md`; keep that file in sync when changing the API.
