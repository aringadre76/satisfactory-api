# Endpoint Test Report

**Generated:** 2026-02-23 18:22:34

## Summary

- **Total Endpoints Tested:** 145
- **Successful (2xx):** 145 (100.0%)
- **Failed:** 0 (0.0%)
- **Invalid response (non-JSON or parse error):** 0

### Performance Metrics

- **Average Response Time:** 790.30 ms
- **Minimum Response Time:** 107.24 ms
- **Maximum Response Time:** 5760.14 ms

---

## Validation issues

None.

---

## Detailed Results

### Root

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/`
- **Status Code:** 200
- **Response Time:** 162.00 ms
- **Response Size:** 99 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Meta

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/meta`
- **Status Code:** 200
- **Response Time:** 768.53 ms
- **Response Size:** 167 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Health

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/health`
- **Status Code:** 200
- **Response Time:** 157.71 ms
- **Response Size:** 15 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Ready

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/ready`
- **Status Code:** 200
- **Response Time:** 764.38 ms
- **Response Size:** 18 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Version

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/version`
- **Status Code:** 200
- **Response Time:** 609.50 ms
- **Response Size:** 167 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Planning Context

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/planning-context`
- **Status Code:** 200
- **Response Time:** 1152.20 ms
- **Response Size:** 641454 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Planning Context with progression

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/planning-context?include_progression=true`
- **Status Code:** 200
- **Response Time:** 2160.62 ms
- **Response Size:** 843640 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Planning Context tier 3

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/planning-context?tier=3`
- **Status Code:** 200
- **Response Time:** 2889.69 ms
- **Response Size:** 82167 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Miners

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/miners`
- **Status Code:** 200
- **Response Time:** 2099.65 ms
- **Response Size:** 1365 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Miner Mk1

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/miners/1`
- **Status Code:** 200
- **Response Time:** 2336.76 ms
- **Response Size:** 452 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Miner Mk2

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/miners/2`
- **Status Code:** 200
- **Response Time:** 789.79 ms
- **Response Size:** 454 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Miner Mk3

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/miners/3`
- **Status Code:** 200
- **Response Time:** 728.97 ms
- **Response Size:** 455 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Belts

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts`
- **Status Code:** 200
- **Response Time:** 209.92 ms
- **Response Size:** 1203 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Belt Mk1

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/1`
- **Status Code:** 200
- **Response Time:** 157.49 ms
- **Response Size:** 198 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Belt Mk2

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/2`
- **Status Code:** 200
- **Response Time:** 146.44 ms
- **Response Size:** 199 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Belt Mk3

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/3`
- **Status Code:** 200
- **Response Time:** 150.92 ms
- **Response Size:** 199 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Belt Mk4

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/4`
- **Status Code:** 200
- **Response Time:** 160.58 ms
- **Response Size:** 199 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Belt Mk5

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/5`
- **Status Code:** 200
- **Response Time:** 148.13 ms
- **Response Size:** 200 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Belt Mk6

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/6`
- **Status Code:** 200
- **Response Time:** 155.27 ms
- **Response Size:** 201 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Recipes

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes`
- **Status Code:** 200
- **Response Time:** 415.66 ms
- **Response Size:** 584740 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipes - Alternate Only

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes?alternate_only=true`
- **Status Code:** 200
- **Response Time:** 402.46 ms
- **Response Size:** 84295 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipes - By Building (Constructor)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes?building=Constructor`
- **Status Code:** 200
- **Response Time:** 692.25 ms
- **Response Size:** 25967 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipes - Combined Filters

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes?alternate_only=true&building=Assembler`
- **Status Code:** 200
- **Response Time:** 486.45 ms
- **Response Size:** 22936 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipes - By Product (Iron Plate)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes?produces=Iron Plate`
- **Status Code:** 200
- **Response Time:** 375.90 ms
- **Response Size:** 4840 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipes - Unlocked by Tier

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes?unlocked_by_tier=1`
- **Status Code:** 200
- **Response Time:** 406.25 ms
- **Response Size:** 228400 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipe by Name (Class Name)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes/Recipe_IronRod_C`
- **Status Code:** 200
- **Response Time:** 404.83 ms
- **Response Size:** 517 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipe by Name (Display Name)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes/Iron%20Rod`
- **Status Code:** 200
- **Response Time:** 397.54 ms
- **Response Size:** 517 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Recipe by Name (Alternate)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes/Alternate:%20Pure%20Iron%20Ingot`
- **Status Code:** 200
- **Response Time:** 402.80 ms
- **Response Size:** 696 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Buildings

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings`
- **Status Code:** 200
- **Response Time:** 387.18 ms
- **Response Size:** 3077 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Buildings - By Type (Constructor)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings?building_type=Constructor`
- **Status Code:** 200
- **Response Time:** 396.47 ms
- **Response Size:** 447 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Buildings - Unlocked by Tier

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings?unlocked_by_tier=1`
- **Status Code:** 200
- **Response Time:** 402.88 ms
- **Response Size:** 2 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Building by Type (Constructor)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings/Constructor`
- **Status Code:** 200
- **Response Time:** 397.87 ms
- **Response Size:** 445 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Building by Type (Assembler)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings/Assembler`
- **Status Code:** 200
- **Response Time:** 398.40 ms
- **Response Size:** 441 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Building by Type (Manufacturer)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings/Manufacturer`
- **Status Code:** 200
- **Response Time:** 307.73 ms
- **Response Size:** 456 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Items

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items`
- **Status Code:** 200
- **Response Time:** 199.88 ms
- **Response Size:** 45120 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Items - By Type (Component)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items?item_type=component`
- **Status Code:** 200
- **Response Time:** 200.62 ms
- **Response Size:** 42420 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Items - By Type (Raw Resource)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items?item_type=raw_resource`
- **Status Code:** 200
- **Response Time:** 203.05 ms
- **Response Size:** 2701 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Items - Unlocked by Tier

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items?unlocked_by_tier=1`
- **Status Code:** 200
- **Response Time:** 187.51 ms
- **Response Size:** 2 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Item by Name (Class Name)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items/Desc_IronPlate_C`
- **Status Code:** 200
- **Response Time:** 127.40 ms
- **Response Size:** 170 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Item by Name (Display Name)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items/Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 119.66 ms
- **Response Size:** 170 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Item by Name (Iron Ore)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items/Iron%20Ore`
- **Status Code:** 200
- **Response Time:** 136.71 ms
- **Response Size:** 178 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Resource Nodes

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/resource-nodes`
- **Status Code:** 200
- **Response Time:** 130.71 ms
- **Response Size:** 3404 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Raw Resources

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/raw-resources`
- **Status Code:** 200
- **Response Time:** 172.58 ms
- **Response Size:** 2393 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Wiki Reference

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/wiki/Iron%20Ore`
- **Status Code:** 200
- **Response Time:** 168.40 ms
- **Response Size:** 78 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Pipelines

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipelines`
- **Status Code:** 200
- **Response Time:** 121.96 ms
- **Response Size:** 462 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Pipeline Mk1

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipelines/1`
- **Status Code:** 200
- **Response Time:** 117.42 ms
- **Response Size:** 228 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Pipeline Mk2

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipelines/2`
- **Status Code:** 200
- **Response Time:** 148.62 ms
- **Response Size:** 231 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Pipeline Pumps

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipeline-pumps`
- **Status Code:** 200
- **Response Time:** 121.60 ms
- **Response Size:** 880 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Pipeline Pump Mk1

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipeline-pumps/1`
- **Status Code:** 200
- **Response Time:** 122.03 ms
- **Response Size:** 438 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Pipeline Pump Mk2

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipeline-pumps/2`
- **Status Code:** 200
- **Response Time:** 115.74 ms
- **Response Size:** 439 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Locomotives

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/locomotives`
- **Status Code:** 200
- **Response Time:** 107.24 ms
- **Response Size:** 380 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Freight Cars

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/freight-cars`
- **Status Code:** 200
- **Response Time:** 3462.28 ms
- **Response Size:** 406 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Train Stations

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations`
- **Status Code:** 200
- **Response Time:** 121.03 ms
- **Response Size:** 1362 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Stations - Solid Type

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations?station_type=solid`
- **Status Code:** 200
- **Response Time:** 120.49 ms
- **Response Size:** 762 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Stations - Liquid Type

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations?station_type=liquid`
- **Status Code:** 200
- **Response Time:** 110.55 ms
- **Response Size:** 411 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Stations - Empty Type

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations?station_type=empty`
- **Status Code:** 200
- **Response Time:** 121.95 ms
- **Response Size:** 191 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Locomotive by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/locomotives/Electric%20Locomotive`
- **Status Code:** 200
- **Response Time:** 127.55 ms
- **Response Size:** 378 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Freight Car by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/freight-cars/Freight%20Car`
- **Status Code:** 200
- **Response Time:** 110.25 ms
- **Response Size:** 404 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Train Signals

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/signals`
- **Status Code:** 200
- **Response Time:** 108.34 ms
- **Response Size:** 417 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Signals - Block Signal

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/signals?signal_type=Block%20Signal`
- **Status Code:** 200
- **Response Time:** 111.56 ms
- **Response Size:** 143 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Signal - Block Signal

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/signals/Block%20Signal`
- **Status Code:** 200
- **Response Time:** 112.61 ms
- **Response Size:** 141 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Signal - Path Signal

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/signals/Path%20Signal`
- **Status Code:** 200
- **Response Time:** 108.30 ms
- **Response Size:** 139 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Signal - End Stop

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/signals/End%20Stop`
- **Status Code:** 200
- **Response Time:** 117.27 ms
- **Response Size:** 133 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Station by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations/Train%20Station`
- **Status Code:** 200
- **Response Time:** 112.04 ms
- **Response Size:** 363 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Train Station by Name - Fluid Freight Platform

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations/Fluid%20Freight%20Platform`
- **Status Code:** 200
- **Response Time:** 117.17 ms
- **Response Size:** 409 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Railway Tracks

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/railway-tracks`
- **Status Code:** 200
- **Response Time:** 149.11 ms
- **Response Size:** 248 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Trucks

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/vehicles/trucks`
- **Status Code:** 200
- **Response Time:** 107.65 ms
- **Response Size:** 860 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Truck

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/vehicles/trucks/truck`
- **Status Code:** 200
- **Response Time:** 113.01 ms
- **Response Size:** 410 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Tractor

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/vehicles/trucks/tractor`
- **Status Code:** 200
- **Response Time:** 130.16 ms
- **Response Size:** 447 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Truck Stations

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/truck-stations`
- **Status Code:** 200
- **Response Time:** 110.12 ms
- **Response Size:** 350 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Drones

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/drones`
- **Status Code:** 200
- **Response Time:** 116.65 ms
- **Response Size:** 454 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Drone Stations

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/drone-stations`
- **Status Code:** 200
- **Response Time:** 136.52 ms
- **Response Size:** 481 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Drone by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/drones/Drone`
- **Status Code:** 200
- **Response Time:** 118.61 ms
- **Response Size:** 452 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Freight Platforms

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/freight-platforms`
- **Status Code:** 200
- **Response Time:** 110.64 ms
- **Response Size:** 832 bytes
- **Success:** True
- **Valid JSON:** Yes

### Production Rate

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/production-rate?recipe=Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 113.29 ms
- **Response Size:** 586 bytes
- **Success:** True
- **Valid JSON:** Yes

### Production Rate with Overclock

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/production-rate?recipe=Recipe_IronPlate_C&overclock=150`
- **Status Code:** 200
- **Response Time:** 116.04 ms
- **Response Size:** 588 bytes
- **Success:** True
- **Valid JSON:** Yes

### Buildings Needed

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/buildings-needed?recipe=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 121.11 ms
- **Response Size:** 245 bytes
- **Success:** True
- **Valid JSON:** Yes

### Buildings Needed with Overclock

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/buildings-needed?recipe=Iron%20Plate&target_rate=120&overclock=200`
- **Status Code:** 200
- **Response Time:** 117.12 ms
- **Response Size:** 247 bytes
- **Success:** True
- **Valid JSON:** Yes

### Production Chain

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/production-chain?item=Heavy%20Modular%20Frame&target_rate=10`
- **Status Code:** 200
- **Response Time:** 2342.28 ms
- **Response Size:** 64530 bytes
- **Success:** True
- **Valid JSON:** Yes

### Production Chain - No Alternates

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/production-chain?item=Iron%20Plate&target_rate=60&include_alternates=false`
- **Status Code:** 200
- **Response Time:** 2392.42 ms
- **Response Size:** 2177 bytes
- **Success:** True
- **Valid JSON:** Yes

### Production Chain - Preferred Recipe

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/production-chain?item=Computer&target_rate=5&preferred_recipe=Alternate:%20Caterium%20Computer`
- **Status Code:** 200
- **Response Time:** 4636.17 ms
- **Response Size:** 60337 bytes
- **Success:** True
- **Valid JSON:** Yes

### Compare Recipes

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/compare-recipes?item=Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 2397.34 ms
- **Response Size:** 3815 bytes
- **Success:** True
- **Valid JSON:** Yes

### Miner Output

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/miner-output?resource=Iron%20Ore&miner_mk=3&purity=pure&overclock=200`
- **Status Code:** 200
- **Response Time:** 2304.52 ms
- **Response Size:** 240 bytes
- **Success:** True
- **Valid JSON:** Yes

### Miner Output - Normal Purity

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/miner-output?resource=Coal&miner_mk=2&purity=normal`
- **Status Code:** 200
- **Response Time:** 2298.94 ms
- **Response Size:** 236 bytes
- **Success:** True
- **Valid JSON:** Yes

### Belt Requirements

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/belt-requirements?throughput=540`
- **Status Code:** 200
- **Response Time:** 411.67 ms
- **Response Size:** 671 bytes
- **Success:** True
- **Valid JSON:** Yes

### Belt Requirements - High Throughput

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/belt-requirements?throughput=1200`
- **Status Code:** 200
- **Response Time:** 393.51 ms
- **Response Size:** 440 bytes
- **Success:** True
- **Valid JSON:** Yes

### Perfect Ratios

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/perfect-ratios?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 401.90 ms
- **Response Size:** 1636 bytes
- **Success:** True
- **Valid JSON:** Yes

### Perfect Ratios - With Overclock

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/perfect-ratios?item=Heavy%20Modular%20Frame&target_rate=10&allow_overclock=true`
- **Status Code:** 200
- **Response Time:** 387.86 ms
- **Response Size:** 16653 bytes
- **Success:** True
- **Valid JSON:** Yes

### Optimize 100 Percent

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/optimize-100-percent?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 3508.49 ms
- **Response Size:** 2352 bytes
- **Success:** True
- **Valid JSON:** Yes

### Optimize 100 Percent - With Overclock

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/optimize-100-percent?item=Computer&target_rate=5&allow_overclock=true`
- **Status Code:** 200
- **Response Time:** 304.96 ms
- **Response Size:** 19371 bytes
- **Success:** True
- **Valid JSON:** Yes

### Factory Efficiency

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/factory-efficiency?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 147.88 ms
- **Response Size:** 2144 bytes
- **Success:** True
- **Valid JSON:** Yes

### Factory Efficiency - Heavy Modular Frame

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/factory-efficiency?item=Heavy%20Modular%20Frame&target_rate=10`
- **Status Code:** 200
- **Response Time:** 693.30 ms
- **Response Size:** 20866 bytes
- **Success:** True
- **Valid JSON:** Yes

### Building Utilization

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/building-utilization?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 544.16 ms
- **Response Size:** 1355 bytes
- **Success:** True
- **Valid JSON:** Yes

### Building Utilization - Computer

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/building-utilization?item=Computer&target_rate=5`
- **Status Code:** 200
- **Response Time:** 3206.87 ms
- **Response Size:** 33535 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Generators

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators`
- **Status Code:** 200
- **Response Time:** 3394.86 ms
- **Response Size:** 3046 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Generators - By Type (Coal)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators?generator_type=Coal`
- **Status Code:** 200
- **Response Time:** 3389.47 ms
- **Response Size:** 940 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Generator by Type (Coal)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators/Coal`
- **Status Code:** 200
- **Response Time:** 698.08 ms
- **Response Size:** 938 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Generator by Type (Nuclear)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators/Nuclear`
- **Status Code:** 200
- **Response Time:** 691.63 ms
- **Response Size:** 960 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Generator by Name - Coal Generator

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators/name/Coal%20Generator`
- **Status Code:** 200
- **Response Time:** 300.90 ms
- **Response Size:** 306 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Generator by Name - Biomass

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators/name/Biomass`
- **Status Code:** 200
- **Response Time:** 204.54 ms
- **Response Size:** 1144 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Generators by Tier

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators/tier/3`
- **Status Code:** 200
- **Response Time:** 304.56 ms
- **Response Size:** 940 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Power Storage

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/storage`
- **Status Code:** 200
- **Response Time:** 202.17 ms
- **Response Size:** 460 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Power Storage by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/storage/Power%20Storage`
- **Status Code:** 200
- **Response Time:** 217.72 ms
- **Response Size:** 458 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Power Poles

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/poles`
- **Status Code:** 200
- **Response Time:** 202.67 ms
- **Response Size:** 1053 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Power Pole Mk1

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/poles/1`
- **Status Code:** 200
- **Response Time:** 188.78 ms
- **Response Size:** 349 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Power Pole Mk2

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/poles/2`
- **Status Code:** 200
- **Response Time:** 111.97 ms
- **Response Size:** 349 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Power Pole Mk3

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/poles/3`
- **Status Code:** 200
- **Response Time:** 112.78 ms
- **Response Size:** 351 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Power Pole by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/poles/name/Power%20Pole%20Mk.1`
- **Status Code:** 200
- **Response Time:** 146.05 ms
- **Response Size:** 349 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Splitters

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/splitters`
- **Status Code:** 200
- **Response Time:** 144.64 ms
- **Response Size:** 1021 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Splitters - By Type (Smart)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/splitters?splitter_type=Smart`
- **Status Code:** 200
- **Response Time:** 187.37 ms
- **Response Size:** 331 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Splitter by Name - Conveyor Splitter

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/splitters/Conveyor%20Splitter`
- **Status Code:** 200
- **Response Time:** 269.87 ms
- **Response Size:** 330 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Splitter by Name - Smart

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/splitters/Smart`
- **Status Code:** 200
- **Response Time:** 456.19 ms
- **Response Size:** 329 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Mergers

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/mergers`
- **Status Code:** 200
- **Response Time:** 262.12 ms
- **Response Size:** 220 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Merger by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/mergers/Conveyor%20Merger`
- **Status Code:** 200
- **Response Time:** 388.94 ms
- **Response Size:** 218 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Storage Containers

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/storage`
- **Status Code:** 200
- **Response Time:** 302.56 ms
- **Response Size:** 360 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Storage Containers - By Type (Industrial)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/storage?container_type=Industrial`
- **Status Code:** 200
- **Response Time:** 295.99 ms
- **Response Size:** 360 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Storage Container by Name - Storage Container

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/storage/Storage%20Container`
- **Status Code:** 200
- **Response Time:** 201.14 ms
- **Response Size:** 242 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Storage Container by Name - Industrial

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/storage/Industrial`
- **Status Code:** 200
- **Response Time:** 295.20 ms
- **Response Size:** 358 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Fluid Buffers

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/fluid-buffers`
- **Status Code:** 200
- **Response Time:** 396.75 ms
- **Response Size:** 498 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Valves

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/valves`
- **Status Code:** 200
- **Response Time:** 298.10 ms
- **Response Size:** 264 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Valves - By Type (Inverted)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/valves?valve_type=Inverted`
- **Status Code:** 200
- **Response Time:** 295.83 ms
- **Response Size:** 2 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Valve by Name - Valve

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/valves/Valve`
- **Status Code:** 200
- **Response Time:** 209.24 ms
- **Response Size:** 262 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Valve by Name - Inverted

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/valves/Inverted`
- **Status Code:** 200
- **Response Time:** 201.16 ms
- **Response Size:** 215 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Water Extractors

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/extractors/water-extractors`
- **Status Code:** 200
- **Response Time:** 130.01 ms
- **Response Size:** 452 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Water Extractor by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/extractors/water-extractors/Water%20Extractor`
- **Status Code:** 200
- **Response Time:** 111.20 ms
- **Response Size:** 450 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Resource Well Extractors

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/extractors/resource-well-extractors`
- **Status Code:** 200
- **Response Time:** 115.01 ms
- **Response Size:** 403 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Resource Well Extractors - By Type (Oil)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/extractors/resource-well-extractors?resource_type=Oil`
- **Status Code:** 200
- **Response Time:** 160.37 ms
- **Response Size:** 403 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Milestones

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones`
- **Status Code:** 200
- **Response Time:** 125.16 ms
- **Response Size:** 27106 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Milestones - By Tier

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones?tier=3`
- **Status Code:** 200
- **Response Time:** 119.83 ms
- **Response Size:** 2453 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Milestones - By Phase

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones?phase=2`
- **Status Code:** 200
- **Response Time:** 126.33 ms
- **Response Size:** 3081 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Milestones by Tier (Path Parameter)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones/3`
- **Status Code:** 200
- **Response Time:** 111.60 ms
- **Response Size:** 2453 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Milestone by Name - Coal Power

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones/name/Coal%20Power`
- **Status Code:** 200
- **Response Time:** 120.01 ms
- **Response Size:** 543 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Milestone by Name - Quantum Encoding

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones/name/Quantum%20Encoding`
- **Status Code:** 200
- **Response Time:** 1170.73 ms
- **Response Size:** 733 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get All Unlocks

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks`
- **Status Code:** 200
- **Response Time:** 1175.83 ms
- **Response Size:** 175039 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlocks - By Type (Building)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks?unlock_type=building`
- **Status Code:** 200
- **Response Time:** 2292.61 ms
- **Response Size:** 2 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlocks - By Tier

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks?tier=4`
- **Status Code:** 200
- **Response Time:** 5760.14 ms
- **Response Size:** 5689 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlocks - By Milestone

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks?milestone=Coal%20Power`
- **Status Code:** 200
- **Response Time:** 4706.26 ms
- **Response Size:** 1030 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlock by Name - Constructor

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks/Constructor`
- **Status Code:** 200
- **Response Time:** 4681.21 ms
- **Response Size:** 148 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlock by Name - Iron Plate

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks/Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 4602.38 ms
- **Response Size:** 148 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlocks by Type - Building

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks/type/building`
- **Status Code:** 200
- **Response Time:** 4597.14 ms
- **Response Size:** 2 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlocks by Type - Recipe

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks/type/recipe`
- **Status Code:** 200
- **Response Time:** 3325.12 ms
- **Response Size:** 161570 bytes
- **Success:** True
- **Valid JSON:** Yes

### Get Unlocks by Type - Schematic

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks/type/schematic`
- **Status Code:** 200
- **Response Time:** 3302.31 ms
- **Response Size:** 13470 bytes
- **Success:** True
- **Valid JSON:** Yes

### Swagger UI

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/docs`
- **Status Code:** 200
- **Response Time:** 3499.79 ms
- **Response Size:** 950 bytes
- **Success:** True
- **Valid JSON:** N/A

### ReDoc

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/redoc`
- **Status Code:** 200
- **Response Time:** 1292.12 ms
- **Response Size:** 910 bytes
- **Success:** True
- **Valid JSON:** N/A

### OpenAPI JSON

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/openapi.json`
- **Status Code:** 200
- **Response Time:** 1279.15 ms
- **Response Size:** 82238 bytes
- **Success:** True
- **Valid JSON:** Yes

