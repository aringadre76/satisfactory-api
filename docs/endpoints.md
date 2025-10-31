# Satisfactory Game Data API - Endpoints Documentation

## Base URL
```
http://localhost:8000
```

## Authentication
No authentication required.

---

## Endpoints

### Root

#### `GET /`
Get API information.

**Response:**
```json
{
  "message": "Satisfactory Game Data API",
  "version": "1.0.0",
  "docs": "/docs"
}
```

---

### Miners

#### `GET /miners`
Get all miners (Mk1, Mk2, Mk3).

**Response:** `List[Miner]`

**Example:**
```bash
GET /miners
```

**Response Model:**
```json
[
  {
    "mk": 1,
    "className": "Build_MinerMk1_C",
    "displayName": "Miner Mk.1",
    "description": "Extracts solid resources...",
    "extractCycleTime": 1.0,
    "itemsPerCycle": 1,
    "powerConsumption": 5.0,
    "powerConsumptionExponent": 1.321929,
    "extractStartupTime": 15.0
  }
]
```

#### `GET /miners/{mk}`
Get specific miner by mark version.

**Parameters:**
- `mk` (path, integer): Miner mark version (1, 2, or 3)

**Response:** `Miner`

**Example:**
```bash
GET /miners/1
```

**Error Responses:**
- `404`: Miner Mk.{mk} not found. Valid values are 1, 2, or 3
- `500`: Game descriptor data not available

---

### Belts

#### `GET /belts`
Get all conveyor belts (Mk1 through Mk6).

**Response:** `List[Belt]`

**Example:**
```bash
GET /belts
```

**Response Model:**
```json
[
  {
    "mk": 1,
    "className": "Build_ConveyorBeltMk1_C",
    "displayName": "Conveyor Belt Mk.1",
    "description": "Transports up to 60 resources per minute...",
    "speed": 120.0
  }
]
```

#### `GET /belts/{mk}`
Get specific belt by mark version.

**Parameters:**
- `mk` (path, integer): Belt mark version (1-6)

**Response:** `Belt`

**Example:**
```bash
GET /belts/3
```

**Error Responses:**
- `404`: Belt Mk.{mk} not found. Valid values are 1 through 6
- `500`: Game descriptor data not available

---

### Recipes

#### `GET /recipes`
Get all recipes including alternate recipes.

**Query Parameters:**
- `alternate_only` (optional, boolean): Filter to only alternate recipes
- `building` (optional, string): Filter by building type (e.g., "Constructor", "Assembler", "Manufacturer")

**Response:** `List[Recipe]`

**Examples:**
```bash
GET /recipes
GET /recipes?alternate_only=true
GET /recipes?building=Constructor
GET /recipes?alternate_only=false&building=Assembler
```

**Response Model:**
```json
[
  {
    "className": "Recipe_IronRod_C",
    "displayName": "Iron Rod",
    "isAlternate": false,
    "ingredients": [
      {
        "itemClass": "/Script/Engine.BlueprintGeneratedClass'/Game/FactoryGame/Resource/Parts/IronIngot/Desc_IronIngot.Desc_IronIngot_C'",
        "amount": 1
      }
    ],
    "products": [
      {
        "itemClass": "/Script/Engine.BlueprintGeneratedClass'/Game/FactoryGame/Resource/Parts/IronRod/Desc_IronRod.Desc_IronRod_C'",
        "amount": 1
      }
    ],
    "manufacturingDuration": 4.0,
    "producedIn": ["Constructor"],
    "variablePowerConsumptionConstant": null,
    "variablePowerConsumptionFactor": null
  }
]
```

#### `GET /recipes/{recipe_name}`
Get specific recipe by class name or display name.

**Parameters:**
- `recipe_name` (path, string): Recipe class name or display name (case-insensitive)

**Response:** `Recipe`

**Examples:**
```bash
GET /recipes/Recipe_IronRod_C
GET /recipes/Iron%20Rod
GET /recipes/Alternate:%20Pure%20Iron%20Ingot
```

**Error Responses:**
- `404`: Recipe '{recipe_name}' not found
- `500`: Game descriptor data not available

---

### Buildings

#### `GET /buildings`
Get all production buildings.

**Query Parameters:**
- `building_type` (optional, string): Filter by building type (e.g., "Constructor", "Assembler", "Manufacturer", "Smelter", "Foundry", "Refinery", "Blender", "ParticleAccelerator", "Packager")

**Response:** `List[Building]`

**Examples:**
```bash
GET /buildings
GET /buildings?building_type=Constructor
```

**Response Model:**
```json
[
  {
    "className": "Build_ConstructorMk1_C",
    "displayName": "Constructor",
    "description": "Basic constructor for automated production...",
    "buildingType": "Constructor",
    "powerConsumption": 4.0,
    "powerConsumptionExponent": 1.321929,
    "tierUnlocked": 1,
    "milestone": "Tier 1 - Parts"
  }
]
```

#### `GET /buildings/{building_type}`
Get specific building by type.

**Parameters:**
- `building_type` (path, string): Building type (case-insensitive)

**Response:** `Building`

**Examples:**
```bash
GET /buildings/Constructor
GET /buildings/assembler
GET /buildings/Manufacturer
```

**Error Responses:**
- `404`: Building type '{building_type}' not found
- `500`: Game descriptor data not available

---

### Items

#### `GET /items`
Get all items (raw resources, components, products, equipment, building parts).

**Query Parameters:**
- `item_type` (optional, string): Filter by item type
  - `raw_resource`: Raw resources (Iron Ore, Copper Ore, Coal, etc.)
  - `component`: Components (Iron Plate, Iron Rod, Wire, etc.)
  - `equipment`: Equipment items
  - `building_part`: Building parts

**Response:** `List[Item]`

**Examples:**
```bash
GET /items
GET /items?item_type=component
GET /items?item_type=raw_resource
```

**Response Model:**
```json
[
  {
    "className": "Desc_IronPlate_C",
    "displayName": "Iron Plate",
    "description": "A basic iron component...",
    "itemType": "component",
    "stackSize": "SS_MEDIUM"
  }
]
```

#### `GET /items/{item_name}`
Get specific item by class name or display name.

**Parameters:**
- `item_name` (path, string): Item class name or display name (case-insensitive)

**Response:** `Item`

**Examples:**
```bash
GET /items/Desc_IronPlate_C
GET /items/Iron%20Plate
GET /items/Iron%20Ore
```

**Error Responses:**
- `404`: Item '{item_name}' not found
- `500`: Game descriptor data not available

---

### Resource Nodes

#### `GET /resource-nodes`
Get all resource node types with purity levels and multipliers.

**Response:** `List[ResourceNode]`

**Example:**
```bash
GET /resource-nodes
```

**Response Model:**
```json
[
  {
    "resourceType": "Iron Ore",
    "purity": "normal",
    "multiplier": 1.0,
    "displayName": "Iron Ore"
  },
  {
    "resourceType": "Iron Ore",
    "purity": "pure",
    "multiplier": 2.0,
    "displayName": "Iron Ore"
  }
]
```

**Purity Levels:**
- `impure`: 0.5x extraction multiplier
- `normal`: 1.0x extraction multiplier
- `pure`: 2.0x extraction multiplier

---

### Raw Resources

#### `GET /raw-resources`
Get all raw resource definitions.

**Response:** `List[RawResource]`

**Example:**
```bash
GET /raw-resources
```

**Response Model:**
```json
[
  {
    "className": "Desc_OreIron_C",
    "displayName": "Iron Ore",
    "description": "A common resource found throughout the world...",
    "resourceType": "Ore Iron"
  }
]
```

---

### Transportation

The API provides comprehensive transportation method data including pipelines, trains, trucks, and drones.

#### Pipelines

##### `GET /transportation/pipelines`
Get all pipelines (Mk1, Mk2).

**Response:** `List[Pipeline]`

**Example:**
```bash
GET /transportation/pipelines
```

**Response Model:**
```json
[
  {
    "mk": 1,
    "className": "Build_Pipeline_C",
    "displayName": "Pipeline Mk.1",
    "description": "Transports fluids. Capacity: 300 m³ of fluid per minute.",
    "flowRate": 300.0
  },
  {
    "mk": 2,
    "className": "Build_PipelineMK2_C",
    "displayName": "Pipeline Mk.2",
    "description": "Transports fluids. Capacity: 600 m³ of fluid per minute.",
    "flowRate": 600.0
  }
]
```

##### `GET /transportation/pipelines/{mk}`
Get specific pipeline by mark version.

**Parameters:**
- `mk` (path, integer): Pipeline mark version (1 or 2)

**Response:** `Pipeline`

**Example:**
```bash
GET /transportation/pipelines/1
```

**Error Responses:**
- `404`: Pipeline Mk.{mk} not found. Valid values are 1 or 2
- `500`: Game descriptor data not available

---

#### Pipeline Pumps

##### `GET /transportation/pipeline-pumps`
Get all pipeline pumps (Mk1, Mk2).

**Response:** `List[PipelinePump]`

**Example:**
```bash
GET /transportation/pipeline-pumps
```

**Response Model:**
```json
[
  {
    "mk": 1,
    "className": "Build_PipelinePump_C",
    "displayName": "Pipeline Pump Mk.1",
    "description": "Maximum Head Lift: 20 m",
    "powerConsumption": 4.0,
    "headLift": 20.0,
    "flowRate": null
  },
  {
    "mk": 2,
    "className": "Build_PipelinePumpMk2_C",
    "displayName": "Pipeline Pump Mk.2",
    "description": "Maximum Head Lift: 50 m",
    "powerConsumption": 8.0,
    "headLift": 50.0,
    "flowRate": null
  }
]
```

##### `GET /transportation/pipeline-pumps/{mk}`
Get specific pipeline pump by mark version.

**Parameters:**
- `mk` (path, integer): Pump mark version (1 or 2)

**Response:** `PipelinePump`

**Example:**
```bash
GET /transportation/pipeline-pumps/2
```

---

#### Trains

##### `GET /transportation/trains/locomotives`
Get electric locomotive specifications.

**Response:** `List[TrainLocomotive]`

**Example:**
```bash
GET /transportation/trains/locomotives
```

**Response Model:**
```json
[
  {
    "className": "Desc_Locomotive_C",
    "displayName": "Electric Locomotive",
    "description": "Moves Freight Cars from station to station. Requires between 25-110 MW of power to move.",
    "powerConsumption": 110.0,
    "powerConsumptionMin": 25.0,
    "powerConsumptionMax": 110.0,
    "maxSpeed": null
  }
]
```

##### `GET /transportation/trains/freight-cars`
Get freight car specifications.

**Response:** `List[TrainFreightCar]`

**Example:**
```bash
GET /transportation/trains/freight-cars
```

**Response Model:**
```json
[
  {
    "className": "Desc_FreightWagon_C",
    "displayName": "Freight Car",
    "description": "Has a 1600 m³ or 32-slot capacity, depending on whether resources are liquid or solid.",
    "storageSlots": 32,
    "fluidCapacityM3": 1600.0,
    "throughputRate": null
  }
]
```

##### `GET /transportation/train-stations`
Get all train stations (solid, liquid, empty platforms).

**Query Parameters:**
- `station_type` (optional, string): Filter by station type
  - `solid`: Solid freight platforms
  - `liquid`: Liquid freight platforms
  - `empty`: Empty platforms

**Response:** `List[TrainStation]`

**Examples:**
```bash
GET /transportation/train-stations
GET /transportation/train-stations?station_type=solid
GET /transportation/train-stations?station_type=liquid
```

**Response Model:**
```json
[
  {
    "className": "Build_TrainStation_C",
    "displayName": "Train Station",
    "description": "Serves as a hub for Locomotives...",
    "powerConsumption": 100.0,
    "platformCount": 2,
    "stationType": "solid"
  },
  {
    "className": "Build_TrainDockingStationLiquid_C",
    "displayName": "Fluid Freight Platform",
    "description": "Loads and unloads Freight Cars that stop at the Freight Platform.",
    "powerConsumption": 100.0,
    "platformCount": 2,
    "stationType": "liquid"
  }
]
```

---

#### Vehicles (Trucks & Tractors)

##### `GET /transportation/vehicles/trucks`
Get all vehicle types (Truck, Tractor).

**Response:** `List[TruckVehicle]`

**Example:**
```bash
GET /transportation/vehicles/trucks
```

**Response Model:**
```json
[
  {
    "className": "Desc_Truck_C",
    "displayName": "Truck",
    "description": "Picks up and delivers resources at Truck Stations. Has 48 inventory slots.",
    "vehicleType": "Truck",
    "storageSlots": 48,
    "fuelConsumptionRate": 75.0,
    "maxSpeed": null,
    "tierUnlocked": null
  },
  {
    "className": "Desc_Tractor_C",
    "displayName": "Tractor",
    "description": "Picks up and delivers resources at Truck Stations. Has 25 inventory slots.",
    "vehicleType": "Tractor",
    "storageSlots": 25,
    "fuelConsumptionRate": 55.0,
    "maxSpeed": null,
    "tierUnlocked": null
  }
]
```

##### `GET /transportation/vehicles/trucks/{vehicle_type}`
Get specific vehicle by type.

**Parameters:**
- `vehicle_type` (path, string): Vehicle type (`truck` or `tractor`, case-insensitive)

**Response:** `TruckVehicle`

**Examples:**
```bash
GET /transportation/vehicles/trucks/truck
GET /transportation/vehicles/trucks/tractor
```

**Error Responses:**
- `404`: Vehicle type '{vehicle_type}' not found. Valid values are: truck, tractor

---

##### `GET /transportation/truck-stations`
Get truck station specifications.

**Response:** `List[TruckStation]`

**Example:**
```bash
GET /transportation/truck-stations
```

**Response Model:**
```json
[
  {
    "className": "Build_TruckStation_C",
    "displayName": "Truck Station",
    "description": "Loads and unloads Trucks and Tractors...",
    "powerConsumption": 50.0,
    "inputOutputRate": null
  }
]
```

---

#### Drones

##### `GET /transportation/drones`
Get drone specifications.

**Response:** `List[Drone]`

**Example:**
```bash
GET /transportation/drones
```

**Response Model:**
```json
[
  {
    "className": "Desc_DroneTransport_C",
    "displayName": "Drone",
    "description": "Transports available input back and forth between its home Port and destination Ports. Has 9 inventory slots.",
    "cargoSlots": 9,
    "batteryCapacity": null,
    "maxSpeed": null,
    "rangeLimit": null
  }
]
```

##### `GET /transportation/drone-stations`
Get drone station specifications.

**Response:** `List[DroneStation]`

**Example:**
```bash
GET /transportation/drone-stations
```

**Response Model:**
```json
[
  {
    "className": "Build_DroneStation_C",
    "displayName": "Drone Port",
    "description": "Manages Drones for automated transport...",
    "powerConsumption": 100.0,
    "droneCapacity": 1,
    "chargingRate": null,
    "throughputRate": null
  }
]
```

---

### Wiki

#### `GET /wiki/{item}`
Get Satisfactory Wiki reference URL for an item.

**Parameters:**
- `item` (path, string): Item name (automatically formatted for wiki URL)

**Response:**
```json
{
  "item": "Iron Ore",
  "wiki_url": "https://satisfactory.fandom.com/wiki/Iron_Ore"
}
```

**Example:**
```bash
GET /wiki/Iron%20Ore
```

---

### Documentation Endpoints

The API automatically provides interactive documentation via FastAPI:

#### `GET /docs`
Swagger UI interactive API documentation (browser interface).

#### `GET /redoc`
ReDoc interactive API documentation (alternative browser interface).

#### `GET /openapi.json`
OpenAPI 3.0 specification in JSON format.

---

## Response Format

All endpoints return JSON. Error responses follow this format:

```json
{
  "detail": "Error message here"
}
```

## HTTP Status Codes

- `200 OK`: Request successful
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error (usually data parsing issue)

## Common Query Parameters

### Filtering
Most list endpoints support filtering via query parameters:
- Boolean filters: Use `true` or `false` as values
- String filters: Case-insensitive matching

### Pagination
Currently, all endpoints return complete datasets. For large result sets (like recipes with 800+ items), consider filtering using query parameters.

## Examples

### Get all alternate recipes for Constructors
```bash
GET /recipes?alternate_only=true&building=Constructor
```

### Get all components
```bash
GET /items?item_type=component
```

### Calculate production chain
1. Get recipe: `GET /recipes/Iron%20Plate`
2. Get building: `GET /buildings/Constructor`
3. Calculate: Production rate = (60 seconds / manufacturingDuration) * product amount per cycle

### Find belt speed for a production rate
1. Get recipe: `GET /recipes/Iron%20Rod`
2. Calculate required throughput
3. Find matching belt: `GET /belts` (filter by speed >= required throughput)

---

## Calculation Endpoints

The API provides comprehensive calculation endpoints for factory planning, including support for alternate recipes and overclocking.

### Production Rate

#### `GET /calculate/production-rate`
Calculate production rate (items/minute) for a recipe.

**Query Parameters:**
- `recipe` (required, string): Recipe name or class name
- `building` (optional, string): Building type (defaults to first available building)
- `overclock` (optional, float): Overclock percentage (1.0-250.0, default: 100.0)

**Response:**
```json
{
  "recipe": "Iron Plate",
  "building": "Constructor",
  "overclock_percentage": 100.0,
  "production_duration": 6.0,
  "effective_duration": 6.0,
  "products": [
    {
      "item_class": "/Script/Engine.BlueprintGeneratedClass'/Game/FactoryGame/Resource/Parts/IronPlate/Desc_IronPlate.Desc_IronPlate_C'",
      "amount_per_cycle": 1,
      "items_per_minute": 10.0,
      "items_per_hour": 600.0
    }
  ],
  "ingredients": [
    {
      "item_class": "...",
      "amount_per_cycle": 3,
      "items_per_minute": 30.0,
      "items_per_hour": 1800.0
    }
  ],
  "power_consumption_mw": 4.0
}
```

**Example:**
```bash
GET /calculate/production-rate?recipe=Iron%20Plate
GET /calculate/production-rate?recipe=Recipe_IronPlate_C&overclock=150
```

---

### Buildings Needed

#### `GET /calculate/buildings-needed`
Calculate how many buildings are needed for a target production rate.

**Query Parameters:**
- `recipe` (required, string): Recipe name or class name
- `target_rate` (required, float): Target production rate (items per minute)
- `building` (optional, string): Building type
- `overclock` (optional, float): Overclock percentage (default: 100.0)

**Response:**
```json
{
  "recipe": "Iron Plate",
  "building": "Constructor",
  "target_production_rate": 60.0,
  "production_rate_per_building": 10.0,
  "buildings_needed": 6.0,
  "buildings_needed_rounded": 6,
  "power_per_building_mw": 4.0,
  "total_power_mw": 24.0,
  "overclock_percentage": 100.0
}
```

**Example:**
```bash
GET /calculate/buildings-needed?recipe=Iron%20Plate&target_rate=60
GET /calculate/buildings-needed?recipe=Iron%20Plate&target_rate=120&overclock=200
```

---

### Production Chain

#### `GET /calculate/production-chain`
Calculate the complete production chain for an item, recursively following all dependencies.

**Query Parameters:**
- `item` (required, string): Item name or class name
- `target_rate` (required, float): Target production rate (items per minute)
- `include_alternates` (optional, boolean): Include alternate recipes (default: true)
- `preferred_recipe` (optional, string): Use specific recipe (for forcing a particular alternate)

**Response:**
```json
{
  "target_item": "Heavy Modular Frame",
  "target_rate": 10.0,
  "total_power_mw": 284.5,
  "buildings": [
    {
      "building": "Constructor",
      "count": 4,
      "power_mw": 16.0
    },
    {
      "building": "Assembler",
      "count": 3,
      "power_mw": 45.0
    }
  ],
  "raw_resources": {
    "Iron Ore": 450.0,
    "Coal": 120.0,
    "Limestone": 30.0
  },
  "steps": [
    {
      "item": "Iron Plate",
      "recipe": "Iron Plate",
      "is_alternate": false,
      "building": "Constructor",
      "buildings_needed": 6.0,
      "buildings_needed_rounded": 6,
      "production_rate_per_building": 10.0,
      "target_production_rate": 60.0,
      "power_per_building_mw": 4.0,
      "total_power_mw": 24.0,
      "ingredients": [...]
    }
  ]
}
```

**Example:**
```bash
GET /calculate/production-chain?item=Heavy%20Modular%20Frame&target_rate=10
GET /calculate/production-chain?item=Iron%20Plate&target_rate=60&include_alternates=false
GET /calculate/production-chain?item=Computer&target_rate=5&preferred_recipe=Alternate:%20Caterium%20Computer
```

---

### Compare Recipes

#### `GET /calculate/compare-recipes`
Compare all recipes (including alternates) that produce a specific item.

**Query Parameters:**
- `item` (required, string): Item name or class name

**Response:**
```json
{
  "item": "Iron Plate",
  "recipes_count": 3,
  "recipes": [
    {
      "recipe_name": "Iron Plate",
      "is_alternate": false,
      "building": "Constructor",
      "items_per_minute_per_building": 10.0,
      "production_duration_seconds": 6.0,
      "ingredients": [...],
      "product_amount": 1,
      "resource_efficiency": 0.333,
      "power_per_building_mw": 4.0,
      "power_per_item_mw": 0.4
    },
    {
      "recipe_name": "Alternate: Coated Iron Plate",
      "is_alternate": true,
      "building": "Assembler",
      "items_per_minute_per_building": 7.5,
      "production_duration_seconds": 8.0,
      "ingredients": [...],
      "product_amount": 1,
      "resource_efficiency": 0.25,
      "power_per_building_mw": 15.0,
      "power_per_item_mw": 2.0
    }
  ]
}
```

**Example:**
```bash
GET /calculate/compare-recipes?item=Iron%20Plate
GET /calculate/compare-recipes?item=Computer
```

**Use Cases:**
- Compare resource efficiency between recipes
- Find most power-efficient recipe
- Compare alternate recipes for optimization
- See all production options for an item

---

### Miner Output

#### `GET /calculate/miner-output`
Calculate miner extraction output with purity and overclocking.

**Query Parameters:**
- `resource` (required, string): Resource name (e.g., "Iron Ore", "Coal")
- `miner_mk` (required, integer): Miner mark (1, 2, or 3)
- `purity` (optional, string): Purity level - "impure", "normal", or "pure" (default: "normal")
- `overclock` (optional, float): Overclock percentage (default: 100.0)

**Response:**
```json
{
  "resource": "Iron Ore",
  "miner_mk": 3,
  "purity": "pure",
  "overclock_percentage": 250.0,
  "base_extraction_rate_per_minute": 60.0,
  "effective_extraction_rate_per_minute": 300.0,
  "effective_extraction_rate_per_hour": 18000.0,
  "power_consumption_mw": 75.0
}
```

**Example:**
```bash
GET /calculate/miner-output?resource=Iron%20Ore&miner_mk=3&purity=pure&overclock=200
GET /calculate/miner-output?resource=Coal&miner_mk=2&purity=normal
```

**Purity Multipliers:**
- `impure`: 0.5x (50% extraction rate)
- `normal`: 1.0x (100% extraction rate)
- `pure`: 2.0x (200% extraction rate)

---

### Belt Requirements

#### `GET /calculate/belt-requirements`
Find suitable conveyor belts for a required throughput.

**Query Parameters:**
- `throughput` (required, float): Required throughput (items per minute)

**Response:**
```json
{
  "required_throughput_per_minute": 540.0,
  "recommended_belt": {
    "mk": 3,
    "display_name": "Conveyor Belt Mk.3",
    "speed_per_minute": 540.0,
    "utilization_percentage": 100.0,
    "headroom": 0.0
  },
  "all_suitable_belts": [
    {
      "mk": 3,
      "display_name": "Conveyor Belt Mk.3",
      "speed_per_minute": 540.0,
      "utilization_percentage": 100.0,
      "headroom": 0.0
    },
    {
      "mk": 4,
      "display_name": "Conveyor Belt Mk.4",
      "speed_per_minute": 960.0,
      "utilization_percentage": 56.25,
      "headroom": 420.0
    }
  ]
}
```

**Example:**
```bash
GET /calculate/belt-requirements?throughput=540
GET /calculate/belt-requirements?throughput=1200
```

---

## Calculation Examples

### Full Factory Planning Workflow

**1. Compare recipes for an item:**
```bash
GET /calculate/compare-recipes?item=Heavy%20Modular%20Frame
```
Choose the best recipe based on resource efficiency or power consumption.

**2. Calculate production chain:**
```bash
GET /calculate/production-chain?item=Heavy%20Modular%20Frame&target_rate=10&preferred_recipe=Alternate:%20Heavy%20Encased%20Frame
```
Get full breakdown of all dependencies, buildings needed, and raw resources.

**3. Calculate miner requirements:**
```bash
GET /calculate/miner-output?resource=Iron%20Ore&miner_mk=3&purity=pure&overclock=250
```
Determine if you have enough raw resource extraction.

**4. Calculate belt requirements:**
```bash
GET /calculate/belt-requirements?throughput=450
```
Find the right belt for your production line.

**5. Calculate power requirements:**
The production chain endpoint includes total power consumption for the entire factory.

### Alternate Recipe Optimization

Compare standard vs alternate recipes:
```bash
GET /calculate/compare-recipes?item=Iron%20Rod
```

Then use preferred recipe in chain calculation:
```bash
GET /calculate/production-chain?item=Iron%20Rod&target_rate=60&preferred_recipe=Alternate:%20Steel%20Rod
```

### Overclocking Calculations

All production endpoints support overclocking:
```bash
GET /calculate/production-rate?recipe=Iron%20Plate&overclock=150
GET /calculate/buildings-needed?recipe=Iron%20Plate&target_rate=60&overclock=200
```

Power consumption scales with overclock percentage using the building's power consumption exponent.

---

## 100% Efficiency Calculation Endpoints

The API provides comprehensive endpoints for optimizing factory designs to achieve 100% efficiency with perfect ratios and minimal waste.

### Perfect Ratios

#### `GET /calculate/perfect-ratios`
Calculate perfect building ratios for 100% efficiency using exact decimal building counts and optional overclocking.

**Query Parameters:**
- `item` (required, string): Item name or class name
- `target_rate` (required, float): Target production rate (items per minute)
- `include_alternates` (optional, boolean): Include alternate recipes (default: true)
- `preferred_recipe` (optional, string): Preferred recipe name
- `allow_overclock` (optional, boolean): Allow overclocking to achieve perfect ratios (default: true)

**Response:**
```json
{
  "target_item": "Iron Plate",
  "target_rate": 60.0,
  "allow_overclock": true,
  "total_power_mw": 24.5,
  "overall_efficiency_percentage": 100.0,
  "buildings": [
    {
      "building": "Constructor",
      "exact_count": 6.0,
      "rounded_count": 6,
      "overclock_percentage": 100.0,
      "total_power_mw": 24.0,
      "production_rate_per_building": 10.0
    }
  ],
  "steps": [
    {
      "item": "Iron Plate",
      "recipe": "Iron Plate",
      "is_alternate": false,
      "building": "Constructor",
      "exact_buildings_needed": 6.0,
      "optimal_overclock_percentage": 100.0,
      "production_rate_per_building": 10.0,
      "target_production_rate": 60.0,
      "actual_production_rate": 60.0,
      "efficiency_percentage": 100.0,
      "power_per_building_mw": 4.0,
      "total_power_mw": 24.0,
      "ingredients": [...]
    }
  ],
  "raw_resources": {
    "Iron Ore": 180.0
  }
}
```

**Example:**
```bash
GET /calculate/perfect-ratios?item=Iron%20Plate&target_rate=60
GET /calculate/perfect-ratios?item=Heavy%20Modular%20Frame&target_rate=10&allow_overclock=true
```

---

### Optimize for 100% Efficiency

#### `GET /calculate/optimize-100-percent`
Optimize production chain for 100% efficiency with perfect ratios, optimal overclocking, and efficiency analysis.

**Query Parameters:**
- `item` (required, string): Item name or class name
- `target_rate` (required, float): Target production rate (items per minute)
- `include_alternates` (optional, boolean): Include alternate recipes (default: true)
- `preferred_recipe` (optional, string): Preferred recipe name
- `allow_overclock` (optional, boolean): Allow overclocking (default: true)

**Response:**
```json
{
  "target_item": "Iron Plate",
  "target_rate": 60.0,
  "allow_overclock": true,
  "total_power_mw": 24.0,
  "overall_efficiency_percentage": 100.0,
  "is_100_percent_efficient": true,
  "buildings": [...],
  "steps": [...],
  "raw_resources": {...},
  "efficiency_analysis": {
    "overall_efficiency_percentage": 100.0,
    "building_efficiency": [
      {
        "building": "Constructor",
        "item": "Iron Plate",
        "efficiency_percentage": 100.0,
        "utilization_percentage": 100.0,
        "is_bottleneck": false,
        "production_rate": 60.0,
        "target_rate": 60.0
      }
    ],
    "bottlenecks": [],
    "optimization_recommendations": [
      "All buildings operating at 100% efficiency"
    ],
    "waste_analysis": {
      "has_waste": false,
      "wasted_resources": []
    }
  }
}
```

**Example:**
```bash
GET /calculate/optimize-100-percent?item=Iron%20Plate&target_rate=60
GET /calculate/optimize-100-percent?item=Computer&target_rate=5&allow_overclock=true
```

**Use Cases:**
- Optimize factory designs for perfect efficiency
- Eliminate idle time and resource waste
- Find optimal building counts with overclocking
- Identify and resolve bottlenecks

---

### Factory Efficiency Analysis

#### `GET /calculate/factory-efficiency`
Calculate comprehensive factory efficiency metrics including building utilization, belt utilization, bottlenecks, and waste analysis.

**Query Parameters:**
- `item` (required, string): Item name or class name
- `target_rate` (required, float): Target production rate (items per minute)
- `include_alternates` (optional, boolean): Include alternate recipes (default: true)
- `preferred_recipe` (optional, string): Preferred recipe name
- `allow_overclock` (optional, boolean): Allow overclocking (default: true)

**Response:**
```json
{
  "target_item": "Iron Plate",
  "target_rate": 60.0,
  "overall_efficiency_percentage": 100.0,
  "average_building_efficiency": 100.0,
  "average_belt_efficiency": 100.0,
  "is_100_percent_efficient": true,
  "total_power_mw": 24.0,
  "building_utilization": {
    "Constructor": {
      "exact_count": 6.0,
      "rounded_count": 6,
      "utilization_efficiency": 100.0
    }
  },
  "belt_utilization": [
    {
      "step": "Iron Plate",
      "throughput_per_minute": 60.0,
      "recommended_belt_mk": 1,
      "belt_speed": 120.0,
      "utilization_percentage": 50.0,
      "is_optimal": false
    }
  ],
  "bottlenecks": [],
  "waste_analysis": {
    "has_waste": false,
    "wasted_resources": []
  },
  "optimization_recommendations": [
    "All buildings operating at 100% efficiency"
  ],
  "detailed_steps": [...]
}
```

**Example:**
```bash
GET /calculate/factory-efficiency?item=Iron%20Plate&target_rate=60
GET /calculate/factory-efficiency?item=Heavy%20Modular%20Frame&target_rate=10
```

**Use Cases:**
- Analyze overall factory efficiency
- Identify bottlenecks and inefficiencies
- Optimize belt utilization
- Track building utilization percentages
- Detect resource waste

---

### Building Utilization Analysis

#### `GET /calculate/building-utilization`
Calculate per-building utilization percentages and identify under-utilized, over-utilized, and optimally-utilized buildings.

**Query Parameters:**
- `item` (required, string): Item name or class name
- `target_rate` (required, float): Target production rate (items per minute)
- `include_alternates` (optional, boolean): Include alternate recipes (default: true)
- `preferred_recipe` (optional, string): Preferred recipe name

**Response:**
```json
{
  "target_item": "Iron Plate",
  "target_rate": 60.0,
  "buildings": {
    "Constructor": [
      {
        "building": "Constructor",
        "item": "Iron Plate",
        "recipe": "Iron Plate",
        "exact_buildings_needed": 6.0,
        "rounded_buildings_used": 6,
        "utilization_percentage": 100.0,
        "production_rate_per_building": 10.0,
        "target_rate": 60.0,
        "actual_rate": 60.0,
        "efficiency_gap": 0.0
      }
    ]
  },
  "under_utilized": [],
  "over_utilized": [],
  "optimally_utilized": [
    {
      "building": "Constructor",
      "item": "Iron Plate",
      "recipe": "Iron Plate",
      "exact_buildings_needed": 6.0,
      "rounded_buildings_used": 6,
      "utilization_percentage": 100.0,
      "production_rate_per_building": 10.0,
      "target_rate": 60.0,
      "actual_rate": 60.0,
      "efficiency_gap": 0.0
    }
  ]
}
```

**Example:**
```bash
GET /calculate/building-utilization?item=Iron%20Plate&target_rate=60
GET /calculate/building-utilization?item=Computer&target_rate=5
```

**Use Cases:**
- Identify under-utilized buildings (<90% utilization)
- Identify over-utilized buildings (>100% utilization)
- Find buildings operating at optimal efficiency (90-100%)
- Calculate exact building needs vs. rounded counts
- Measure efficiency gaps

---

## Efficiency Calculation Examples

### Achieving 100% Efficiency

**1. Optimize a production chain for 100% efficiency:**
```bash
GET /calculate/optimize-100-percent?item=Iron%20Plate&target_rate=60
```
Returns configuration with perfect ratios, optimal overclocking, and efficiency analysis.

**2. Calculate factory-wide efficiency metrics:**
```bash
GET /calculate/factory-efficiency?item=Heavy%20Modular%20Frame&target_rate=10
```
Analyze overall efficiency, building utilization, belt utilization, and identify bottlenecks.

**3. Analyze building utilization:**
```bash
GET /calculate/building-utilization?item=Computer&target_rate=5
```
Identify which buildings are under-utilized, over-utilized, or optimal.

**4. Get perfect ratios without overclocking:**
```bash
GET /calculate/perfect-ratios?item=Iron%20Rod&target_rate=60&allow_overclock=false
```
Calculate exact building counts needed, showing decimals for perfect ratios.

### Efficiency Workflow

1. **Compare recipes:**
   ```bash
   GET /calculate/compare-recipes?item=Heavy%20Modular%20Frame
   ```
   Find the most efficient recipe.

2. **Optimize for 100% efficiency:**
   ```bash
   GET /calculate/optimize-100-percent?item=Heavy%20Modular%20Frame&target_rate=10&preferred_recipe=Alternate:%20Heavy%20Encased%20Frame
   ```
   Get perfect ratios with optimal overclocking.

3. **Analyze factory efficiency:**
   ```bash
   GET /calculate/factory-efficiency?item=Heavy%20Modular%20Frame&target_rate=10
   ```
   Verify 100% efficiency and check for bottlenecks.

4. **Check building utilization:**
   ```bash
   GET /calculate/building-utilization?item=Heavy%20Modular%20Frame&target_rate=10
   ```
   Identify any under-utilized buildings that could be optimized.

---

## Power

### Power Generators

#### `GET /power/generators`
Get all power generators (Biomass, Coal, Fuel, Geothermal, Nuclear).

**Query Parameters:**
- `generator_type` (optional, string): Filter by generator type (Biomass, Coal, Fuel, Geothermal, Nuclear)

**Response:** `List[PowerGenerator]`

**Examples:**
```bash
GET /power/generators
GET /power/generators?generator_type=Coal
```

**Response Model:**
```json
[
  {
    "className": "Build_GeneratorBiomass_Automated_C",
    "displayName": "Biomass Burner",
    "description": "Burns biomass to generate power...",
    "generatorType": "Biomass",
    "powerOutput": 30.0,
    "powerConsumption": 0.0,
    "fuelTypes": ["Desc_Biomass_C"],
    "fuelConsumptionRate": 4.0,
    "waterConsumptionRate": null,
    "tierUnlocked": 0,
    "milestone": null
  },
  {
    "className": "Build_GeneratorCoal_C",
    "displayName": "Coal Generator",
    "description": "Burns coal to generate power...",
    "generatorType": "Coal",
    "powerOutput": 75.0,
    "powerConsumption": 0.0,
    "fuelTypes": ["Desc_Coal_C"],
    "fuelConsumptionRate": 15.0,
    "waterConsumptionRate": 45.0,
    "tierUnlocked": 3,
    "milestone": "Coal Power"
  },
  {
    "className": "Build_FuelGenerator_C",
    "displayName": "Fuel Generator",
    "description": "Burns fuel to generate power...",
    "generatorType": "Fuel",
    "powerOutput": 150.0,
    "powerConsumption": 0.0,
    "fuelTypes": ["Desc_Fuel_C"],
    "fuelConsumptionRate": 12.0,
    "waterConsumptionRate": null,
    "tierUnlocked": 5,
    "milestone": "Oil Processing"
  },
  {
    "className": "Build_GeothermalGenerator_C",
    "displayName": "Geothermal Generator",
    "description": "Generates power from geothermal vents...",
    "generatorType": "Geothermal",
    "powerOutput": 200.0,
    "powerConsumption": 0.0,
    "fuelTypes": null,
    "fuelConsumptionRate": null,
    "waterConsumptionRate": null,
    "tierUnlocked": 6,
    "milestone": "Advanced Oil Processing"
  },
  {
    "className": "Build_GeneratorNuclear_C",
    "displayName": "Nuclear Power Plant",
    "description": "Generates power from nuclear fuel...",
    "generatorType": "Nuclear",
    "powerOutput": 2500.0,
    "powerConsumption": 0.0,
    "fuelTypes": ["Desc_NuclearFuelRod_C"],
    "fuelConsumptionRate": 0.2,
    "waterConsumptionRate": 300.0,
    "tierUnlocked": 8,
    "milestone": "Nuclear Power"
  }
]
```

#### `GET /power/generators/{generator_type}`
Get specific power generator by type.

**Parameters:**
- `generator_type` (path, string): Generator type (case-insensitive)

**Response:** `PowerGenerator`

**Examples:**
```bash
GET /power/generators/Coal
GET /power/generators/Nuclear
```

**Error Responses:**
- `404`: Power generator type '{generator_type}' not found
- `500`: Game descriptor data not available

#### `GET /power/generators/name/{generator_name}`
Get specific power generator by display name.

**Parameters:**
- `generator_name` (path, string): Generator display name or type (case-insensitive)

**Response:** `PowerGenerator`

**Examples:**
```bash
GET /power/generators/name/Coal%20Generator
GET /power/generators/name/Biomass
```

**Error Responses:**
- `404`: Power generator '{generator_name}' not found
- `500`: Game descriptor data not available

#### `GET /power/generators/tier/{tier}`
Get all power generators unlocked at a specific tier.

**Parameters:**
- `tier` (path, integer): Tier number

**Response:** `List[PowerGenerator]`

**Example:**
```bash
GET /power/generators/tier/3
```

**Error Responses:**
- `404`: No power generators found for tier {tier}
- `500`: Game descriptor data not available

---

### Power Storage

#### `GET /power/storage`
Get power storage information.

**Response:** `List[PowerStorage]`

**Example:**
```bash
GET /power/storage
```

**Response Model:**
```json
[
  {
    "className": "Build_PowerStorage_C",
    "displayName": "Power Storage",
    "description": "Stores excess power...",
    "capacity": 100.0,
    "chargeRate": 100.0,
    "dischargeRate": 100.0,
    "efficiency": 1.0,
    "tierUnlocked": 5,
    "milestone": "Expanded Power Infrastructure"
  }
]
```

#### `GET /power/storage/{storage_name}`
Get specific power storage by name.

**Parameters:**
- `storage_name` (path, string): Power storage display name (case-insensitive)

**Response:** `PowerStorage`

**Example:**
```bash
GET /power/storage/Power%20Storage
```

**Error Responses:**
- `404`: Power storage '{storage_name}' not found
- `500`: Game descriptor data not available

---

### Power Poles

#### `GET /power/poles`
Get all power poles (Mk1, Mk2, Mk3).

**Response:** `List[PowerPole]`

**Example:**
```bash
GET /power/poles
```

**Response Model:**
```json
[
  {
    "mk": 1,
    "className": "Build_PowerPoleMk1_C",
    "displayName": "Power Pole Mk.1",
    "description": "Basic power distribution...",
    "connectionLimit": 4,
    "powerTransmission": null
  }
]
```

#### `GET /power/poles/{mk}`
Get specific power pole by mark version.

**Parameters:**
- `mk` (path, integer): Power pole mark version (1, 2, or 3)

**Response:** `PowerPole`

**Example:**
```bash
GET /power/poles/2
```

**Error Responses:**
- `404`: Power Pole Mk.{mk} not found. Valid values are 1, 2, or 3
- `500`: Game descriptor data not available

#### `GET /power/poles/name/{pole_name}`
Get specific power pole by display name.

**Parameters:**
- `pole_name` (path, string): Power pole display name (case-insensitive)

**Response:** `PowerPole`

**Example:**
```bash
GET /power/poles/name/Power%20Pole%20Mk.1
```

**Error Responses:**
- `404`: Power pole '{pole_name}' not found
- `500`: Game descriptor data not available

---

## Logistics

### Conveyor Splitters

#### `GET /logistics/splitters`
Get all conveyor splitters (Regular, Smart, Programmable).

**Query Parameters:**
- `splitter_type` (optional, string): Filter by splitter type (Regular, Smart, Programmable)

**Response:** `List[ConveyorSplitter]`

**Examples:**
```bash
GET /logistics/splitters
GET /logistics/splitters?splitter_type=Smart
```

**Response Model:**
```json
[
  {
    "className": "Build_ConveyorSplitter_C",
    "displayName": "Conveyor Splitter",
    "description": "Splits items from one input to three outputs...",
    "splitterType": "Regular",
    "outputCount": 3,
    "throughputCapacity": null,
    "tierUnlocked": 1,
    "milestone": "Tier 1 - Parts"
  },
  {
    "className": "Build_ConveyorSplitterSmart_C",
    "displayName": "Smart Splitter",
    "description": "Smart splitter with filtering capabilities...",
    "splitterType": "Smart",
    "outputCount": 3,
    "throughputCapacity": null,
    "tierUnlocked": 4,
    "milestone": "Conveyor Splitters"
  },
  {
    "className": "Build_ConveyorSplitterProgrammable_C",
    "displayName": "Programmable Splitter",
    "description": "Programmable splitter with advanced filtering...",
    "splitterType": "Programmable",
    "outputCount": 3,
    "throughputCapacity": null,
    "tierUnlocked": 6,
    "milestone": "Advanced Logistics"
  }
]
```

#### `GET /logistics/splitters/{splitter_name}`
Get specific splitter by display name or type.

**Parameters:**
- `splitter_name` (path, string): Splitter display name or type (case-insensitive)

**Response:** `ConveyorSplitter`

**Examples:**
```bash
GET /logistics/splitters/Conveyor%20Splitter
GET /logistics/splitters/Smart
```

**Error Responses:**
- `404`: Splitter '{splitter_name}' not found
- `500`: Game descriptor data not available

---

### Conveyor Mergers

#### `GET /logistics/mergers`
Get conveyor merger information.

**Response:** `List[ConveyorMerger]`

**Example:**
```bash
GET /logistics/mergers
```

**Response Model:**
```json
[
  {
    "className": "Build_ConveyorMerger_C",
    "displayName": "Conveyor Merger",
    "description": "Merges items from three inputs to one output...",
    "inputCount": 3,
    "throughputCapacity": null,
    "tierUnlocked": 1,
    "milestone": "Tier 1 - Parts"
  }
]
```

#### `GET /logistics/mergers/{merger_name}`
Get specific merger by display name.

**Parameters:**
- `merger_name` (path, string): Merger display name (case-insensitive)

**Response:** `ConveyorMerger`

**Example:**
```bash
GET /logistics/mergers/Conveyor%20Merger
```

**Error Responses:**
- `404`: Merger '{merger_name}' not found
- `500`: Game descriptor data not available

---

### Storage Containers

#### `GET /logistics/storage`
Get all storage containers (Storage, Industrial, Buffer).

**Query Parameters:**
- `container_type` (optional, string): Filter by container type (Storage, Industrial, Buffer)

**Response:** `List[StorageContainer]`

**Examples:**
```bash
GET /logistics/storage
GET /logistics/storage?container_type=Industrial
```

**Response Model:**
```json
[
  {
    "className": "Build_StorageContainer_C",
    "displayName": "Storage Container",
    "description": "Basic storage container...",
    "containerType": "Storage",
    "storageSlots": 48,
    "inputRate": null,
    "outputRate": null,
    "tierUnlocked": 1,
    "milestone": "Tier 1 - Parts"
  },
  {
    "className": "Build_StorageContainerMk2_C",
    "displayName": "Industrial Storage Container",
    "description": "Industrial storage container...",
    "containerType": "Industrial",
    "storageSlots": 48,
    "inputRate": null,
    "outputRate": null,
    "tierUnlocked": 4,
    "milestone": "Expanded Power Infrastructure"
  },
  {
    "className": "Build_IndustrialStorageBuffer_C",
    "displayName": "Industrial Storage Buffer",
    "description": "Large industrial storage buffer...",
    "containerType": "Buffer",
    "storageSlots": 48,
    "inputRate": null,
    "outputRate": null,
    "tierUnlocked": 7,
    "milestone": "Nuclear Power"
  }
]
```

#### `GET /logistics/storage/{container_name}`
Get specific storage container by display name or type.

**Parameters:**
- `container_name` (path, string): Container display name or type (case-insensitive)

**Response:** `StorageContainer`

**Examples:**
```bash
GET /logistics/storage/Storage%20Container
GET /logistics/storage/Industrial
```

**Error Responses:**
- `404`: Storage container '{container_name}' not found
- `500`: Game descriptor data not available

---

### Fluid Buffers

#### `GET /logistics/fluid-buffers`
Get all fluid buffer types.

**Response:** `List[FluidBuffer]`

**Example:**
```bash
GET /logistics/fluid-buffers
```

**Response Model:**
```json
[
  {
    "className": "Build_FluidBuffer_C",
    "displayName": "Fluid Buffer",
    "description": "Stores fluid resources...",
    "capacity": 50.0,
    "inputRate": null,
    "outputRate": null,
    "tierUnlocked": 3,
    "milestone": "Coal Power"
  },
  {
    "className": "Build_IndustrialFluidBuffer_C",
    "displayName": "Industrial Fluid Buffer",
    "description": "Large industrial fluid buffer...",
    "capacity": 200.0,
    "inputRate": null,
    "outputRate": null,
    "tierUnlocked": 5,
    "milestone": "Oil Processing"
  }
]
```

---

### Valves

#### `GET /logistics/valves`
Get all valve types (Regular, Inverted).

**Query Parameters:**
- `valve_type` (optional, string): Filter by valve type (Regular, Inverted)

**Response:** `List[Valve]`

**Examples:**
```bash
GET /logistics/valves
GET /logistics/valves?valve_type=Inverted
```

**Response Model:**
```json
[
  {
    "className": "Build_Valve_C",
    "displayName": "Valve",
    "description": "Controls fluid flow...",
    "valveType": "Regular",
    "maxFlowRate": null,
    "tierUnlocked": 5,
    "milestone": "Oil Processing"
  },
  {
    "className": "Build_ValveInverted_C",
    "displayName": "Inverted Valve",
    "description": "Inverted valve for reverse flow control...",
    "valveType": "Inverted",
    "maxFlowRate": null,
    "tierUnlocked": 5,
    "milestone": "Oil Processing"
  }
]
```

#### `GET /logistics/valves/{valve_name}`
Get specific valve by display name or type.

**Parameters:**
- `valve_name` (path, string): Valve display name or type (case-insensitive)

**Response:** `Valve`

**Examples:**
```bash
GET /logistics/valves/Valve
GET /logistics/valves/Inverted
```

**Error Responses:**
- `404`: Valve '{valve_name}' not found
- `500`: Game descriptor data not available

---

## Extractors

### Water Extractors

#### `GET /extractors/water-extractors`
Get water extractor information.

**Response:** `List[WaterExtractor]`

**Example:**
```bash
GET /extractors/water-extractors
```

**Response Model:**
```json
[
  {
    "className": "Build_WaterPump_C",
    "displayName": "Water Extractor",
    "description": "Extracts water from bodies of water...",
    "extractionRate": 120.0,
    "powerConsumption": 20.0,
    "powerConsumptionExponent": 1.321929
  }
]
```

#### `GET /extractors/water-extractors/{extractor_name}`
Get specific water extractor by display name.

**Parameters:**
- `extractor_name` (path, string): Water extractor display name (case-insensitive)

**Response:** `WaterExtractor`

**Example:**
```bash
GET /extractors/water-extractors/Water%20Extractor
```

**Error Responses:**
- `404`: Water extractor '{extractor_name}' not found
- `500`: Game descriptor data not available

---

### Resource Well Extractors

#### `GET /extractors/resource-well-extractors`
Get resource well extractors (Oil, Nitrogen, etc.).

**Query Parameters:**
- `resource_type` (optional, string): Filter by resource type (Oil, Nitrogen, Generic)

**Response:** `List[ResourceWellExtractor]`

**Examples:**
```bash
GET /extractors/resource-well-extractors
GET /extractors/resource-well-extractors?resource_type=Oil
```

**Response Model:**
```json
[
  {
    "className": "Build_OilPump_C",
    "displayName": "Oil Pump",
    "description": "Extracts crude oil from resource wells...",
    "resourceType": "Oil",
    "extractionRate": null,
    "powerConsumption": 40.0,
    "pressureRequirement": null
  }
]
```

---

## Transportation

### Trains

#### `GET /transportation/trains/locomotives`
Get train locomotive information.

**Response:** `List[TrainLocomotive]`

**Example:**
```bash
GET /transportation/trains/locomotives
```

**Response Model:**
```json
[
  {
    "className": "Desc_Locomotive_C",
    "displayName": "Electric Locomotive",
    "description": "Electric train locomotive...",
    "powerConsumption": 110.0,
    "maxSpeed": null
  }
]
```

#### `GET /transportation/trains/freight-cars`
Get train freight car information.

**Response:** `List[TrainFreightCar]`

**Example:**
```bash
GET /transportation/trains/freight-cars
```

**Response Model:**
```json
[
  {
    "className": "Desc_FreightWagon_C",
    "displayName": "Freight Car",
    "description": "Train car for transporting goods...",
    "storageSlots": 32,
    "throughputRate": null
  }
]
```

#### `GET /transportation/trains/locomotives/{locomotive_name}`
Get specific locomotive by name.

**Parameters:**
- `locomotive_name` (path, string): Locomotive display name (case-insensitive)

**Response:** `TrainLocomotive`

**Example:**
```bash
GET /transportation/trains/locomotives/Electric%20Locomotive
```

**Error Responses:**
- `404`: Locomotive '{locomotive_name}' not found
- `500`: Game descriptor data not available

#### `GET /transportation/trains/freight-cars/{car_name}`
Get specific freight car by name.

**Parameters:**
- `car_name` (path, string): Freight car display name (case-insensitive)

**Response:** `TrainFreightCar`

**Example:**
```bash
GET /transportation/trains/freight-cars/Freight%20Car
```

**Error Responses:**
- `404`: Freight car '{car_name}' not found
- `500`: Game descriptor data not available

#### `GET /transportation/trains/signals`
Get all train signals (Block Signal, Path Signal, End Stop).

**Query Parameters:**
- `signal_type` (optional, string): Filter by signal type (Block Signal, Path Signal, End Stop)

**Response:** `List[TrainSignal]`

**Examples:**
```bash
GET /transportation/trains/signals
GET /transportation/trains/signals?signal_type=Block%20Signal
```

**Response Model:**
```json
[
  {
    "className": "Desc_RailroadBlockSignal_C",
    "displayName": "Block Signal",
    "description": "Directs the movement of trains to avoid collisions...",
    "signalType": "Block Signal",
    "powerConsumption": null,
    "range": null
  },
  {
    "className": "Desc_RailroadPathSignal_C",
    "displayName": "Path Signal",
    "description": "Advanced signals for bi-directional railways...",
    "signalType": "Path Signal",
    "powerConsumption": null,
    "range": null
  }
]
```

#### `GET /transportation/trains/signals/{signal_type}`
Get specific train signal by type.

**Parameters:**
- `signal_type` (path, string): Signal type (Block Signal, Path Signal, or End Stop, case-insensitive)

**Response:** `TrainSignal`

**Examples:**
```bash
GET /transportation/trains/signals/Block%20Signal
GET /transportation/trains/signals/Path%20Signal
GET /transportation/trains/signals/End%20Stop
```

**Error Responses:**
- `404`: Signal type '{signal_type}' not found. Valid values are: Block Signal, Path Signal, End Stop
- `500`: Game descriptor data not available

#### `GET /transportation/railway-tracks`
Get railway track information.

**Response:** `List[RailwayTrack]`

**Example:**
```bash
GET /transportation/railway-tracks
```

**Response Model:**
```json
[
  {
    "className": "Build_RailroadTrack_C",
    "displayName": "Railway",
    "description": "Carries trains reliably and quickly...",
    "meshLength": 1200.0,
    "powerTransmission": null,
    "connectionLimit": null
  }
]
```

#### `GET /transportation/train-stations/{station_name}`
Get specific train station by name.

**Parameters:**
- `station_name` (path, string): Train station display name (case-insensitive)

**Response:** `TrainStation`

**Examples:**
```bash
GET /transportation/train-stations/Train%20Station
GET /transportation/train-stations/Fluid%20Freight%20Platform
```

**Error Responses:**
- `404`: Train station '{station_name}' not found
- `500`: Game descriptor data not available

---

### Vehicles

#### `GET /transportation/vehicles/trucks`
Get all vehicle types (Truck, Tractor).

**Response:** `List[TruckVehicle]`

**Example:**
```bash
GET /transportation/vehicles/trucks
```

**Response Model:**
```json
[
  {
    "className": "Desc_Truck_C",
    "displayName": "Truck",
    "description": "Large automated vehicle...",
    "vehicleType": "Truck",
    "storageSlots": 48,
    "fuelConsumptionRate": 3.0,
    "maxSpeed": null,
    "tierUnlocked": null
  }
]
```

#### `GET /transportation/vehicles/trucks/{vehicle_type}`
Get specific vehicle by type.

**Parameters:**
- `vehicle_type` (path, string): Vehicle type (Truck or Tractor, case-insensitive)

**Response:** `TruckVehicle`

**Examples:**
```bash
GET /transportation/vehicles/trucks/Truck
GET /transportation/vehicles/trucks/Tractor
```

**Error Responses:**
- `404`: Vehicle type '{vehicle_type}' not found. Valid values are: truck, tractor
- `500`: Game descriptor data not available

---

### Drones

#### `GET /transportation/drones`
Get drone information.

**Response:** `List[Drone]`

**Example:**
```bash
GET /transportation/drones
```

**Response Model:**
```json
[
  {
    "className": "Desc_DroneTransport_C",
    "displayName": "Drone",
    "description": "Automated flying transport...",
    "cargoSlots": 9,
    "batteryCapacity": null,
    "maxSpeed": null,
    "rangeLimit": null
  }
]
```

#### `GET /transportation/drones/{drone_name}`
Get specific drone by name.

**Parameters:**
- `drone_name` (path, string): Drone display name (case-insensitive)

**Response:** `Drone`

**Example:**
```bash
GET /transportation/drones/Drone
```

**Error Responses:**
- `404`: Drone '{drone_name}' not found
- `500`: Game descriptor data not available

---

### Freight Platforms

#### `GET /transportation/freight-platforms`
Get freight platform information for trains.

**Response:** `List[FreightPlatform]`

**Example:**
```bash
GET /transportation/freight-platforms
```

**Response Model:**
```json
[
  {
    "className": "Build_FreightPlatform_C",
    "displayName": "Freight Platform",
    "description": "Platform for loading/unloading freight cars...",
    "powerConsumption": 0.0,
    "storageSlots": 32,
    "inputRate": null,
    "outputRate": null
  }
]
```

---

## Progression

### Milestones

#### `GET /progression/milestones`
Get milestone information for tier progression.

**Query Parameters:**
- `tier` (optional, integer): Filter by tier number

**Response:** `List[Milestone]`

**Examples:**
```bash
GET /progression/milestones
GET /progression/milestones?tier=3
```

**Response Model:**
```json
[
  {
    "className": "Schematic_3-1_C",
    "displayName": "Coal Power",
    "description": "",
    "tier": 3,
    "phase": 3,
    "cost": [
      {
        "item_class": "/Script/Engine.BlueprintGeneratedClass'/Game/FactoryGame/Resource/Parts/IronPlateReinforced/Desc_IronPlateReinforced.Desc_IronPlateReinforced_C'",
        "amount": 150
      },
      {
        "item_class": "/Script/Engine.BlueprintGeneratedClass'/Game/FactoryGame/Resource/Parts/Rotor/Desc_Rotor.Desc_Rotor_C'",
        "amount": 50
      }
    ]
  }
]
```

#### `GET /progression/milestones/{tier}`
Get all milestones for a specific tier.

**Parameters:**
- `tier` (path, integer): Tier number

**Response:** `List[Milestone]`

**Example:**
```bash
GET /progression/milestones/3
```

**Error Responses:**
- `404`: No milestones found for tier {tier}
- `500`: Game descriptor data not available

#### `GET /progression/milestones/name/{milestone_name}`
Get specific milestone by display name.

**Parameters:**
- `milestone_name` (path, string): Milestone display name (case-insensitive)

**Response:** `Milestone`

**Examples:**
```bash
GET /progression/milestones/name/Coal%20Power
GET /progression/milestones/name/Quantum%20Encoding
```

**Error Responses:**
- `404`: Milestone '{milestone_name}' not found
- `500`: Game descriptor data not available

---

### Unlocks

#### `GET /progression/unlocks`
Get all unlock information (buildings, recipes, schematics).

**Query Parameters:**
- `unlock_type` (optional, string): Filter by unlock type (building, recipe, schematic)
- `tier` (optional, integer): Filter by tier number
- `milestone` (optional, string): Filter by milestone name (case-insensitive)

**Response:** `List[Unlock]`

**Examples:**
```bash
GET /progression/unlocks
GET /progression/unlocks?unlock_type=building
GET /progression/unlocks?tier=3
GET /progression/unlocks?milestone=Coal%20Power
```

**Response Model:**
```json
[
  {
    "className": "Build_ConstructorMk1_C",
    "displayName": "Constructor",
    "unlockType": "building",
    "tier": 1,
    "milestone": "Tier 1 - Parts",
    "mamResearch": null
  },
  {
    "className": "Recipe_IronPlate_C",
    "displayName": "Iron Plate",
    "unlockType": "recipe",
    "tier": 1,
    "milestone": "Tier 1 - Parts",
    "mamResearch": null
  }
]
```

#### `GET /progression/unlocks/{unlock_name}`
Get specific unlock by display name or class name.

**Parameters:**
- `unlock_name` (path, string): Unlock display name or class name (case-insensitive)

**Response:** `Unlock`

**Examples:**
```bash
GET /progression/unlocks/Constructor
GET /progression/unlocks/Build_AssemblerMk1_C
GET /progression/unlocks/Iron%20Plate
```

**Error Responses:**
- `404`: Unlock '{unlock_name}' not found
- `500`: Game descriptor data not available

#### `GET /progression/unlocks/type/{unlock_type}`
Get all unlocks of a specific type.

**Parameters:**
- `unlock_type` (path, string): Unlock type (building, recipe, or schematic, case-insensitive)

**Response:** `List[Unlock]`

**Examples:**
```bash
GET /progression/unlocks/type/building
GET /progression/unlocks/type/recipe
GET /progression/unlocks/type/schematic
```

**Error Responses:**
- `404`: Unlock type '{unlock_type}' not found. Valid values are: building, recipe, schematic
- `500`: Game descriptor data not available

If no unlocks exist for the given type, the endpoint returns an empty list with `200 OK`.

---

