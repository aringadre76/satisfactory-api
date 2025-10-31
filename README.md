# Satisfactory Game Data API

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

**2. Make sure you have the game data file:**
- Place `en-US.json` from your Satisfactory installation into the `Docs/` directory
- This file contains all the game data the API needs

**3. Start the server:**
```bash
uvicorn src.api.main:app --reload
```

**4. Visit the interactive documentation:**
- Open your browser to `http://localhost:8000/docs`
- This gives you a visual interface to try all the endpoints

That's it! Your API is running and ready to use.

## What Can I Do With This API?

### Get Game Data
Access information about miners, belts, recipes, buildings, items, and transportation systems through simple HTTP requests.

### Build Tools
Create factory calculators, production planners, or automation scripts that need real game data.

### Filter and Search
Query recipes by building type, find alternate recipes, filter items by category, and more.

### Calculate Production
Use the calculation endpoints to figure out building requirements, production chains, and resource needs.

## Available Endpoints

The API is organized into logical groups:

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
- `GET /recipes/{recipe_name}` - Get a specific recipe

### Buildings
- `GET /buildings` - All production buildings
  - Add `?building_type=Assembler` to filter
- `GET /buildings/{building_type}` - Specific building details

### Items
- `GET /items` - All items (resources, components, equipment)
  - Add `?item_type=component` to filter by type
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

## Example Usage

**Get all recipes:**
```bash
curl http://localhost:8000/recipes
```

**Get only alternate recipes:**
```bash
curl http://localhost:8000/recipes?alternate_only=true
```

**Get a specific item:**
```bash
curl http://localhost:8000/items/Iron%20Ingot
```

**Get all Mk3 belts:**
```bash
curl http://localhost:8000/belts/3
```

## Interactive Documentation

When the API is running, you can use the built-in documentation:

- **Swagger UI**: `http://localhost:8000/docs` - Visual interface to test endpoints
- **ReDoc**: `http://localhost:8000/redoc` - Clean, readable API documentation

Both are automatically generated and always up-to-date with the API.

## Project Structure

```
satisfactory-api/
├── src/
│   ├── api/
│   │   ├── main.py              # FastAPI application entry point
│   │   └── routers/              # All API route handlers
│   ├── parsers/
│   │   └── game_descriptor_parser.py  # Parses game data files
│   ├── models/                   # Data structure definitions
│   └── utils/                    # Helper functions
├── Docs/                         # Game data files go here
│   └── en-US.json               # Main game descriptor file
├── docs/                         # Documentation files
├── scripts/                      # Utility scripts
└── requirements.txt             # Python dependencies
```

## Updating After Game Updates

When Satisfactory releases an update:

1. Copy the new `en-US.json` file to the `Docs/` directory
2. Run the verification script: `python3 scripts/verify_data.py`
3. Restart the API server

The API automatically reads from the data files, so no code changes are needed.

## Data Source

The API reads from game descriptor files that come with your Satisfactory installation. These JSON files contain all the game data in a structured format. The API simply makes this data accessible through HTTP endpoints.

## License

This project is for educational and community use with Satisfactory game data.
