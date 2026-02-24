# Endpoint Test Report

**Generated:** 2026-02-23 18:07:30

## Summary

- **Total Endpoints Tested:** 142
- **Successful (2xx):** 139 (97.9%)
- **Failed:** 3 (2.1%)
- **Invalid response (non-JSON or parse error):** 0

### Performance Metrics

- **Average Response Time:** 595.48 ms
- **Minimum Response Time:** 102.54 ms
- **Maximum Response Time:** 6520.94 ms

---

## Validation issues

- **Get Planning Context** `GET https://satisfactory-api-yfw1.onrender.com/planning-context`
  - HTTP 404
- **Get Planning Context with progression** `GET https://satisfactory-api-yfw1.onrender.com/planning-context?include_progression=true`
  - HTTP 404
- **Get Planning Context tier 3** `GET https://satisfactory-api-yfw1.onrender.com/planning-context?tier=3`
  - HTTP 404

---

## Detailed Results

### Root

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/`
- **Status Code:** 200
- **Response Time:** 179.93 ms
- **Response Size:** 99 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Meta

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/meta`
- **Status Code:** 200
- **Response Time:** 161.85 ms
- **Response Size:** 103 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Planning Context

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/planning-context`
- **Status Code:** 404
- **Response Time:** 171.43 ms
- **Response Size:** 22 bytes
- **Success:** False
- **Valid JSON:** N/A

### Get Planning Context with progression

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/planning-context?include_progression=true`
- **Status Code:** 404
- **Response Time:** 159.72 ms
- **Response Size:** 22 bytes
- **Success:** False
- **Valid JSON:** N/A

### Get Planning Context tier 3

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/planning-context?tier=3`
- **Status Code:** 404
- **Response Time:** 166.59 ms
- **Response Size:** 22 bytes
- **Success:** False
- **Valid JSON:** N/A

### Get All Miners

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/miners`
- **Status Code:** 200
- **Response Time:** 132.48 ms
- **Response Size:** 1365 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Miner Mk1

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/miners/1`
- **Status Code:** 200
- **Response Time:** 136.85 ms
- **Response Size:** 452 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Miner Mk2

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/miners/2`
- **Status Code:** 200
- **Response Time:** 5156.16 ms
- **Response Size:** 454 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Miner Mk3

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/miners/3`
- **Status Code:** 200
- **Response Time:** 125.79 ms
- **Response Size:** 455 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Belts

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts`
- **Status Code:** 200
- **Response Time:** 141.83 ms
- **Response Size:** 1203 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Belt Mk1

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/1`
- **Status Code:** 200
- **Response Time:** 118.95 ms
- **Response Size:** 198 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Belt Mk2

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/2`
- **Status Code:** 200
- **Response Time:** 163.04 ms
- **Response Size:** 199 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Belt Mk3

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/3`
- **Status Code:** 200
- **Response Time:** 153.10 ms
- **Response Size:** 199 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Belt Mk4

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/4`
- **Status Code:** 200
- **Response Time:** 1703.21 ms
- **Response Size:** 199 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Belt Mk5

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/5`
- **Status Code:** 200
- **Response Time:** 121.38 ms
- **Response Size:** 200 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Belt Mk6

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/6`
- **Status Code:** 200
- **Response Time:** 128.50 ms
- **Response Size:** 201 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Recipes

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes`
- **Status Code:** 200
- **Response Time:** 185.78 ms
- **Response Size:** 584740 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipes - Alternate Only

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes?alternate_only=true`
- **Status Code:** 200
- **Response Time:** 229.44 ms
- **Response Size:** 84295 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipes - By Building (Constructor)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes?building=Constructor`
- **Status Code:** 200
- **Response Time:** 160.91 ms
- **Response Size:** 25967 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipes - Combined Filters

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes?alternate_only=true&building=Assembler`
- **Status Code:** 200
- **Response Time:** 197.83 ms
- **Response Size:** 22936 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipes - By Product (Iron Plate)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes?produces=Iron Plate`
- **Status Code:** 200
- **Response Time:** 333.15 ms
- **Response Size:** 584740 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipes - Unlocked by Tier

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes?unlocked_by_tier=1`
- **Status Code:** 200
- **Response Time:** 934.01 ms
- **Response Size:** 584740 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipe by Name (Class Name)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes/Recipe_IronRod_C`
- **Status Code:** 200
- **Response Time:** 757.32 ms
- **Response Size:** 517 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipe by Name (Display Name)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes/Iron%20Rod`
- **Status Code:** 200
- **Response Time:** 156.92 ms
- **Response Size:** 517 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipe by Name (Alternate)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes/Alternate:%20Pure%20Iron%20Ingot`
- **Status Code:** 200
- **Response Time:** 197.03 ms
- **Response Size:** 696 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Buildings

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings`
- **Status Code:** 200
- **Response Time:** 293.75 ms
- **Response Size:** 3077 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Buildings - By Type (Constructor)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings?building_type=Constructor`
- **Status Code:** 200
- **Response Time:** 294.28 ms
- **Response Size:** 447 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Buildings - Unlocked by Tier

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings?unlocked_by_tier=1`
- **Status Code:** 200
- **Response Time:** 220.13 ms
- **Response Size:** 3077 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Building by Type (Constructor)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings/Constructor`
- **Status Code:** 200
- **Response Time:** 209.67 ms
- **Response Size:** 445 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Building by Type (Assembler)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings/Assembler`
- **Status Code:** 200
- **Response Time:** 307.10 ms
- **Response Size:** 441 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Building by Type (Manufacturer)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings/Manufacturer`
- **Status Code:** 200
- **Response Time:** 374.71 ms
- **Response Size:** 456 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Items

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items`
- **Status Code:** 200
- **Response Time:** 294.55 ms
- **Response Size:** 45120 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Items - By Type (Component)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items?item_type=component`
- **Status Code:** 200
- **Response Time:** 121.13 ms
- **Response Size:** 42420 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Items - By Type (Raw Resource)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items?item_type=raw_resource`
- **Status Code:** 200
- **Response Time:** 122.89 ms
- **Response Size:** 2701 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Items - Unlocked by Tier

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items?unlocked_by_tier=1`
- **Status Code:** 200
- **Response Time:** 148.11 ms
- **Response Size:** 45120 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Item by Name (Class Name)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items/Desc_IronPlate_C`
- **Status Code:** 200
- **Response Time:** 120.49 ms
- **Response Size:** 170 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Item by Name (Display Name)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items/Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 105.85 ms
- **Response Size:** 170 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Item by Name (Iron Ore)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items/Iron%20Ore`
- **Status Code:** 200
- **Response Time:** 115.61 ms
- **Response Size:** 178 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Resource Nodes

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/resource-nodes`
- **Status Code:** 200
- **Response Time:** 118.41 ms
- **Response Size:** 3404 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Raw Resources

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/raw-resources`
- **Status Code:** 200
- **Response Time:** 126.04 ms
- **Response Size:** 2393 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Wiki Reference

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/wiki/Iron%20Ore`
- **Status Code:** 200
- **Response Time:** 116.60 ms
- **Response Size:** 78 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Pipelines

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipelines`
- **Status Code:** 200
- **Response Time:** 124.58 ms
- **Response Size:** 462 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Pipeline Mk1

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipelines/1`
- **Status Code:** 200
- **Response Time:** 125.25 ms
- **Response Size:** 228 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Pipeline Mk2

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipelines/2`
- **Status Code:** 200
- **Response Time:** 116.40 ms
- **Response Size:** 231 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Pipeline Pumps

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipeline-pumps`
- **Status Code:** 200
- **Response Time:** 113.22 ms
- **Response Size:** 880 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Pipeline Pump Mk1

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipeline-pumps/1`
- **Status Code:** 200
- **Response Time:** 144.62 ms
- **Response Size:** 438 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Pipeline Pump Mk2

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipeline-pumps/2`
- **Status Code:** 200
- **Response Time:** 127.42 ms
- **Response Size:** 439 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Locomotives

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/locomotives`
- **Status Code:** 200
- **Response Time:** 140.99 ms
- **Response Size:** 380 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Freight Cars

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/freight-cars`
- **Status Code:** 200
- **Response Time:** 129.70 ms
- **Response Size:** 406 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Train Stations

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations`
- **Status Code:** 200
- **Response Time:** 121.54 ms
- **Response Size:** 1362 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Stations - Solid Type

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations?station_type=solid`
- **Status Code:** 200
- **Response Time:** 130.34 ms
- **Response Size:** 762 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Stations - Liquid Type

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations?station_type=liquid`
- **Status Code:** 200
- **Response Time:** 121.29 ms
- **Response Size:** 411 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Stations - Empty Type

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations?station_type=empty`
- **Status Code:** 200
- **Response Time:** 120.59 ms
- **Response Size:** 191 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Locomotive by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/locomotives/Electric%20Locomotive`
- **Status Code:** 200
- **Response Time:** 139.20 ms
- **Response Size:** 378 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Freight Car by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/freight-cars/Freight%20Car`
- **Status Code:** 200
- **Response Time:** 135.64 ms
- **Response Size:** 404 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Train Signals

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/signals`
- **Status Code:** 200
- **Response Time:** 111.19 ms
- **Response Size:** 417 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Signals - Block Signal

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/signals?signal_type=Block%20Signal`
- **Status Code:** 200
- **Response Time:** 109.97 ms
- **Response Size:** 143 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Signal - Block Signal

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/signals/Block%20Signal`
- **Status Code:** 200
- **Response Time:** 112.85 ms
- **Response Size:** 141 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Signal - Path Signal

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/signals/Path%20Signal`
- **Status Code:** 200
- **Response Time:** 141.44 ms
- **Response Size:** 139 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Signal - End Stop

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/signals/End%20Stop`
- **Status Code:** 200
- **Response Time:** 108.68 ms
- **Response Size:** 133 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Station by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations/Train%20Station`
- **Status Code:** 200
- **Response Time:** 107.21 ms
- **Response Size:** 363 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Station by Name - Fluid Freight Platform

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations/Fluid%20Freight%20Platform`
- **Status Code:** 200
- **Response Time:** 116.38 ms
- **Response Size:** 409 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Railway Tracks

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/railway-tracks`
- **Status Code:** 200
- **Response Time:** 112.36 ms
- **Response Size:** 248 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Trucks

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/vehicles/trucks`
- **Status Code:** 200
- **Response Time:** 105.42 ms
- **Response Size:** 860 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Truck

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/vehicles/trucks/truck`
- **Status Code:** 200
- **Response Time:** 111.75 ms
- **Response Size:** 410 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Tractor

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/vehicles/trucks/tractor`
- **Status Code:** 200
- **Response Time:** 117.73 ms
- **Response Size:** 447 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Truck Stations

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/truck-stations`
- **Status Code:** 200
- **Response Time:** 102.54 ms
- **Response Size:** 350 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Drones

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/drones`
- **Status Code:** 200
- **Response Time:** 117.26 ms
- **Response Size:** 454 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Drone Stations

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/drone-stations`
- **Status Code:** 200
- **Response Time:** 114.65 ms
- **Response Size:** 481 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Drone by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/drones/Drone`
- **Status Code:** 200
- **Response Time:** 104.63 ms
- **Response Size:** 452 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Freight Platforms

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/freight-platforms`
- **Status Code:** 200
- **Response Time:** 115.56 ms
- **Response Size:** 832 bytes
- **Success:** True
- **Valid JSON:** Yes

### Production Rate

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/production-rate?recipe=Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 120.99 ms
- **Response Size:** 586 bytes
- **Success:** True
- **Valid JSON:** Yes

### Production Rate with Overclock

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/production-rate?recipe=Recipe_IronPlate_C&overclock=150`
- **Status Code:** 200
- **Response Time:** 108.46 ms
- **Response Size:** 588 bytes
- **Success:** True
- **Valid JSON:** Yes

### Buildings Needed

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/buildings-needed?recipe=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 113.63 ms
- **Response Size:** 245 bytes
- **Success:** True
- **Valid JSON:** Yes

### Buildings Needed with Overclock

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/buildings-needed?recipe=Iron%20Plate&target_rate=120&overclock=200`
- **Status Code:** 200
- **Response Time:** 123.28 ms
- **Response Size:** 247 bytes
- **Success:** True
- **Valid JSON:** Yes

### Production Chain

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/production-chain?item=Heavy%20Modular%20Frame&target_rate=10`
- **Status Code:** 200
- **Response Time:** 271.95 ms
- **Response Size:** 14973 bytes
- **Success:** True
- **Valid JSON:** Yes

### Production Chain - No Alternates

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/production-chain?item=Iron%20Plate&target_rate=60&include_alternates=false`
- **Status Code:** 200
- **Response Time:** 189.91 ms
- **Response Size:** 1233 bytes
- **Success:** True
- **Valid JSON:** Yes

### Production Chain - Preferred Recipe

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/production-chain?item=Computer&target_rate=5&preferred_recipe=Alternate:%20Caterium%20Computer`
- **Status Code:** 200
- **Response Time:** 363.59 ms
- **Response Size:** 12381 bytes
- **Success:** True
- **Valid JSON:** Yes

### Compare Recipes

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/compare-recipes?item=Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 205.55 ms
- **Response Size:** 3815 bytes
- **Success:** True
- **Valid JSON:** Yes

### Miner Output

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/miner-output?resource=Iron%20Ore&miner_mk=3&purity=pure&overclock=200`
- **Status Code:** 200
- **Response Time:** 199.38 ms
- **Response Size:** 240 bytes
- **Success:** True
- **Valid JSON:** Yes

### Miner Output - Normal Purity

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/miner-output?resource=Coal&miner_mk=2&purity=normal`
- **Status Code:** 200
- **Response Time:** 130.93 ms
- **Response Size:** 236 bytes
- **Success:** True
- **Valid JSON:** Yes

### Belt Requirements

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/belt-requirements?throughput=540`
- **Status Code:** 200
- **Response Time:** 137.76 ms
- **Response Size:** 671 bytes
- **Success:** True
- **Valid JSON:** Yes

### Belt Requirements - High Throughput

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/belt-requirements?throughput=1200`
- **Status Code:** 200
- **Response Time:** 130.54 ms
- **Response Size:** 440 bytes
- **Success:** True
- **Valid JSON:** Yes

### Perfect Ratios

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/perfect-ratios?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 155.71 ms
- **Response Size:** 1636 bytes
- **Success:** True
- **Valid JSON:** Yes

### Perfect Ratios - With Overclock

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/perfect-ratios?item=Heavy%20Modular%20Frame&target_rate=10&allow_overclock=true`
- **Status Code:** 200
- **Response Time:** 272.08 ms
- **Response Size:** 16653 bytes
- **Success:** True
- **Valid JSON:** Yes

### Optimize 100 Percent

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/optimize-100-percent?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 146.50 ms
- **Response Size:** 2352 bytes
- **Success:** True
- **Valid JSON:** Yes

### Optimize 100 Percent - With Overclock

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/optimize-100-percent?item=Computer&target_rate=5&allow_overclock=true`
- **Status Code:** 200
- **Response Time:** 718.51 ms
- **Response Size:** 19371 bytes
- **Success:** True
- **Valid JSON:** Yes

### Factory Efficiency

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/factory-efficiency?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 210.95 ms
- **Response Size:** 2144 bytes
- **Success:** True
- **Valid JSON:** Yes

### Factory Efficiency - Heavy Modular Frame

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/factory-efficiency?item=Heavy%20Modular%20Frame&target_rate=10`
- **Status Code:** 200
- **Response Time:** 417.69 ms
- **Response Size:** 20866 bytes
- **Success:** True
- **Valid JSON:** Yes

### Building Utilization

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/building-utilization?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 591.70 ms
- **Response Size:** 1355 bytes
- **Success:** True
- **Valid JSON:** Yes

### Building Utilization - Computer

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/building-utilization?item=Computer&target_rate=5`
- **Status Code:** 200
- **Response Time:** 801.53 ms
- **Response Size:** 12637 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Generators

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators`
- **Status Code:** 200
- **Response Time:** 589.61 ms
- **Response Size:** 3046 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Generators - By Type (Coal)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators?generator_type=Coal`
- **Status Code:** 200
- **Response Time:** 500.09 ms
- **Response Size:** 940 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Generator by Type (Coal)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators/Coal`
- **Status Code:** 200
- **Response Time:** 497.45 ms
- **Response Size:** 938 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Generator by Type (Nuclear)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators/Nuclear`
- **Status Code:** 200
- **Response Time:** 395.43 ms
- **Response Size:** 960 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Generator by Name - Coal Generator

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators/name/Coal%20Generator`
- **Status Code:** 200
- **Response Time:** 395.18 ms
- **Response Size:** 306 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Generator by Name - Biomass

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators/name/Biomass`
- **Status Code:** 200
- **Response Time:** 300.51 ms
- **Response Size:** 1144 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Generators by Tier

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators/tier/3`
- **Status Code:** 200
- **Response Time:** 301.02 ms
- **Response Size:** 940 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Power Storage

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/storage`
- **Status Code:** 200
- **Response Time:** 301.02 ms
- **Response Size:** 460 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Power Storage by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/storage/Power%20Storage`
- **Status Code:** 200
- **Response Time:** 204.18 ms
- **Response Size:** 458 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Power Poles

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/poles`
- **Status Code:** 200
- **Response Time:** 195.55 ms
- **Response Size:** 1053 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Power Pole Mk1

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/poles/1`
- **Status Code:** 200
- **Response Time:** 195.53 ms
- **Response Size:** 349 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Power Pole Mk2

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/poles/2`
- **Status Code:** 200
- **Response Time:** 106.50 ms
- **Response Size:** 349 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Power Pole Mk3

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/poles/3`
- **Status Code:** 200
- **Response Time:** 152.86 ms
- **Response Size:** 351 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Power Pole by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/poles/name/Power%20Pole%20Mk.1`
- **Status Code:** 200
- **Response Time:** 147.29 ms
- **Response Size:** 349 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Splitters

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/splitters`
- **Status Code:** 200
- **Response Time:** 305.60 ms
- **Response Size:** 1021 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Splitters - By Type (Smart)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/splitters?splitter_type=Smart`
- **Status Code:** 200
- **Response Time:** 201.91 ms
- **Response Size:** 331 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Splitter by Name - Conveyor Splitter

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/splitters/Conveyor%20Splitter`
- **Status Code:** 200
- **Response Time:** 261.33 ms
- **Response Size:** 330 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Splitter by Name - Smart

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/splitters/Smart`
- **Status Code:** 200
- **Response Time:** 454.78 ms
- **Response Size:** 329 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Mergers

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/mergers`
- **Status Code:** 200
- **Response Time:** 394.19 ms
- **Response Size:** 220 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Merger by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/mergers/Conveyor%20Merger`
- **Status Code:** 200
- **Response Time:** 393.60 ms
- **Response Size:** 218 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Storage Containers

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/storage`
- **Status Code:** 200
- **Response Time:** 385.00 ms
- **Response Size:** 360 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Storage Containers - By Type (Industrial)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/storage?container_type=Industrial`
- **Status Code:** 200
- **Response Time:** 1286.17 ms
- **Response Size:** 360 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Storage Container by Name - Storage Container

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/storage/Storage%20Container`
- **Status Code:** 200
- **Response Time:** 1189.91 ms
- **Response Size:** 242 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Storage Container by Name - Industrial

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/storage/Industrial`
- **Status Code:** 200
- **Response Time:** 129.63 ms
- **Response Size:** 358 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Fluid Buffers

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/fluid-buffers`
- **Status Code:** 200
- **Response Time:** 119.41 ms
- **Response Size:** 498 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Valves

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/valves`
- **Status Code:** 200
- **Response Time:** 169.52 ms
- **Response Size:** 264 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Valves - By Type (Inverted)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/valves?valve_type=Inverted`
- **Status Code:** 200
- **Response Time:** 115.77 ms
- **Response Size:** 2 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Valve by Name - Valve

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/valves/Valve`
- **Status Code:** 200
- **Response Time:** 118.05 ms
- **Response Size:** 262 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Valve by Name - Inverted

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/valves/Inverted`
- **Status Code:** 200
- **Response Time:** 166.56 ms
- **Response Size:** 215 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Water Extractors

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/extractors/water-extractors`
- **Status Code:** 200
- **Response Time:** 135.94 ms
- **Response Size:** 452 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Water Extractor by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/extractors/water-extractors/Water%20Extractor`
- **Status Code:** 200
- **Response Time:** 116.19 ms
- **Response Size:** 450 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Resource Well Extractors

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/extractors/resource-well-extractors`
- **Status Code:** 200
- **Response Time:** 115.10 ms
- **Response Size:** 403 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Resource Well Extractors - By Type (Oil)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/extractors/resource-well-extractors?resource_type=Oil`
- **Status Code:** 200
- **Response Time:** 110.73 ms
- **Response Size:** 403 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Milestones

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones`
- **Status Code:** 200
- **Response Time:** 103.14 ms
- **Response Size:** 27106 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Milestones - By Tier

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones?tier=3`
- **Status Code:** 200
- **Response Time:** 133.29 ms
- **Response Size:** 2453 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Milestones - By Phase

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones?phase=2`
- **Status Code:** 200
- **Response Time:** 105.31 ms
- **Response Size:** 3081 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Milestones by Tier (Path Parameter)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones/3`
- **Status Code:** 200
- **Response Time:** 123.22 ms
- **Response Size:** 2453 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Milestone by Name - Coal Power

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones/name/Coal%20Power`
- **Status Code:** 200
- **Response Time:** 127.55 ms
- **Response Size:** 543 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Milestone by Name - Quantum Encoding

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones/name/Quantum%20Encoding`
- **Status Code:** 200
- **Response Time:** 215.57 ms
- **Response Size:** 733 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Unlocks

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks`
- **Status Code:** 200
- **Response Time:** 1525.22 ms
- **Response Size:** 175039 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlocks - By Type (Building)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks?unlock_type=building`
- **Status Code:** 200
- **Response Time:** 4009.37 ms
- **Response Size:** 2 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlocks - By Tier

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks?tier=4`
- **Status Code:** 200
- **Response Time:** 3915.05 ms
- **Response Size:** 5689 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlocks - By Milestone

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks?milestone=Coal%20Power`
- **Status Code:** 200
- **Response Time:** 6520.94 ms
- **Response Size:** 1030 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlock by Name - Constructor

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks/Constructor`
- **Status Code:** 200
- **Response Time:** 5167.82 ms
- **Response Size:** 148 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlock by Name - Iron Plate

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks/Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 5296.24 ms
- **Response Size:** 148 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlocks by Type - Building

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks/type/building`
- **Status Code:** 200
- **Response Time:** 5296.26 ms
- **Response Size:** 2 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlocks by Type - Recipe

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks/type/recipe`
- **Status Code:** 200
- **Response Time:** 4228.47 ms
- **Response Size:** 161570 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlocks by Type - Schematic

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks/type/schematic`
- **Status Code:** 200
- **Response Time:** 5689.13 ms
- **Response Size:** 13470 bytes
- **Success:** True
- **Valid JSON:** Yes

### Swagger UI

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/docs`
- **Status Code:** 200
- **Response Time:** 3002.25 ms
- **Response Size:** 950 bytes
- **Success:** True
- **Valid JSON:** N/A

### ReDoc

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/redoc`
- **Status Code:** 200
- **Response Time:** 2999.80 ms
- **Response Size:** 910 bytes
- **Success:** True
- **Valid JSON:** N/A

### OpenAPI JSON

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/openapi.json`
- **Status Code:** 200
- **Response Time:** 1474.14 ms
- **Response Size:** 77217 bytes
- **Success:** True
- **Valid JSON:** Yes

