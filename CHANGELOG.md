# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) for the API; patch releases keep response shapes compatible.

## [1.0.0] - 2026-02-23

### Added

- Initial REST API for Satisfactory game data (miners, belts, recipes, buildings, items, transportation, power, logistics, extractors, progression).
- Calculation endpoints (production rate, buildings needed, production chain, compare recipes, miner output, belt requirements).
- Health and readiness endpoints (`/health`, `/ready`) for load balancers and orchestration.
- Interactive docs (Swagger UI at `/docs`, ReDoc at `/redoc`) and OpenAPI spec at `/openapi.json`.
- Optional pagination (`limit`, `offset`) on recipes, items, milestones, and unlocks.
- Postman collection and script for endpoint tests.
- Dockerfile and deployment notes for Railway, Render, Fly.io.
- MIT license, pyproject.toml for pip-installable package, CONTRIBUTING.md, and example integration script.

[1.0.0]: https://github.com/your-org/satisfactory-api/releases/tag/v1.0.0
