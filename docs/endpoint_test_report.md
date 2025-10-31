# Endpoint Test Report

**Generated:** 2025-10-30 19:01:45

## Summary

- **Total Endpoints Tested:** 134
- **Successful:** 134 (100.0%)
- **Failed:** 0 (0.0%)

### Performance Metrics

- **Average Response Time:** 67.40 ms
- **Minimum Response Time:** 5.42 ms
- **Maximum Response Time:** 780.39 ms

---

## Detailed Results

### Root

- **URL:** `GET http://localhost:8000/`
- **Status Code:** 200
- **Response Time:** 8.70 ms
- **Response Size:** 73 bytes
- **Success:** True

### Get All Miners

- **URL:** `GET http://localhost:8000/miners`
- **Status Code:** 200
- **Response Time:** 7.46 ms
- **Response Size:** 1365 bytes
- **Success:** True

### Get Miner Mk1

- **URL:** `GET http://localhost:8000/miners/1`
- **Status Code:** 200
- **Response Time:** 12.97 ms
- **Response Size:** 452 bytes
- **Success:** True

### Get Miner Mk2

- **URL:** `GET http://localhost:8000/miners/2`
- **Status Code:** 200
- **Response Time:** 9.12 ms
- **Response Size:** 454 bytes
- **Success:** True

### Get Miner Mk3

- **URL:** `GET http://localhost:8000/miners/3`
- **Status Code:** 200
- **Response Time:** 10.89 ms
- **Response Size:** 455 bytes
- **Success:** True

### Get All Belts

- **URL:** `GET http://localhost:8000/belts`
- **Status Code:** 200
- **Response Time:** 9.80 ms
- **Response Size:** 1203 bytes
- **Success:** True

### Get Belt Mk1

- **URL:** `GET http://localhost:8000/belts/1`
- **Status Code:** 200
- **Response Time:** 15.68 ms
- **Response Size:** 198 bytes
- **Success:** True

### Get Belt Mk2

- **URL:** `GET http://localhost:8000/belts/2`
- **Status Code:** 200
- **Response Time:** 13.61 ms
- **Response Size:** 199 bytes
- **Success:** True

### Get Belt Mk3

- **URL:** `GET http://localhost:8000/belts/3`
- **Status Code:** 200
- **Response Time:** 10.58 ms
- **Response Size:** 199 bytes
- **Success:** True

### Get Belt Mk4

- **URL:** `GET http://localhost:8000/belts/4`
- **Status Code:** 200
- **Response Time:** 10.89 ms
- **Response Size:** 199 bytes
- **Success:** True

### Get Belt Mk5

- **URL:** `GET http://localhost:8000/belts/5`
- **Status Code:** 200
- **Response Time:** 11.10 ms
- **Response Size:** 200 bytes
- **Success:** True

### Get Belt Mk6

- **URL:** `GET http://localhost:8000/belts/6`
- **Status Code:** 200
- **Response Time:** 12.50 ms
- **Response Size:** 201 bytes
- **Success:** True

### Get All Recipes

- **URL:** `GET http://localhost:8000/recipes`
- **Status Code:** 200
- **Response Time:** 51.79 ms
- **Response Size:** 585361 bytes
- **Success:** True

### Get Recipes - Alternate Only

- **URL:** `GET http://localhost:8000/recipes?alternate_only=true`
- **Status Code:** 200
- **Response Time:** 55.31 ms
- **Response Size:** 84577 bytes
- **Success:** True

### Get Recipes - By Building (Constructor)

- **URL:** `GET http://localhost:8000/recipes?building=Constructor`
- **Status Code:** 200
- **Response Time:** 57.34 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Recipes - Combined Filters

- **URL:** `GET http://localhost:8000/recipes?alternate_only=true&building=Assembler`
- **Status Code:** 200
- **Response Time:** 60.03 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Recipe by Name (Class Name)

- **URL:** `GET http://localhost:8000/recipes/Recipe_IronRod_C`
- **Status Code:** 200
- **Response Time:** 62.73 ms
- **Response Size:** 520 bytes
- **Success:** True

### Get Recipe by Name (Display Name)

- **URL:** `GET http://localhost:8000/recipes/Iron%20Rod`
- **Status Code:** 200
- **Response Time:** 65.48 ms
- **Response Size:** 520 bytes
- **Success:** True

### Get Recipe by Name (Alternate)

- **URL:** `GET http://localhost:8000/recipes/Alternate:%20Pure%20Iron%20Ingot`
- **Status Code:** 200
- **Response Time:** 67.88 ms
- **Response Size:** 699 bytes
- **Success:** True

### Get All Buildings

- **URL:** `GET http://localhost:8000/buildings`
- **Status Code:** 200
- **Response Time:** 72.52 ms
- **Response Size:** 3077 bytes
- **Success:** True

### Get Buildings - By Type (Constructor)

- **URL:** `GET http://localhost:8000/buildings?building_type=Constructor`
- **Status Code:** 200
- **Response Time:** 38.08 ms
- **Response Size:** 447 bytes
- **Success:** True

### Get Building by Type (Constructor)

- **URL:** `GET http://localhost:8000/buildings/Constructor`
- **Status Code:** 200
- **Response Time:** 38.55 ms
- **Response Size:** 445 bytes
- **Success:** True

### Get Building by Type (Assembler)

- **URL:** `GET http://localhost:8000/buildings/Assembler`
- **Status Code:** 200
- **Response Time:** 39.97 ms
- **Response Size:** 441 bytes
- **Success:** True

### Get Building by Type (Manufacturer)

- **URL:** `GET http://localhost:8000/buildings/Manufacturer`
- **Status Code:** 200
- **Response Time:** 41.47 ms
- **Response Size:** 456 bytes
- **Success:** True

### Get All Items

- **URL:** `GET http://localhost:8000/items`
- **Status Code:** 200
- **Response Time:** 39.55 ms
- **Response Size:** 45081 bytes
- **Success:** True

### Get Items - By Type (Component)

- **URL:** `GET http://localhost:8000/items?item_type=component`
- **Status Code:** 200
- **Response Time:** 37.09 ms
- **Response Size:** 45081 bytes
- **Success:** True

### Get Items - By Type (Raw Resource)

- **URL:** `GET http://localhost:8000/items?item_type=raw_resource`
- **Status Code:** 200
- **Response Time:** 34.79 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Item by Name (Class Name)

- **URL:** `GET http://localhost:8000/items/Desc_IronPlate_C`
- **Status Code:** 200
- **Response Time:** 29.28 ms
- **Response Size:** 170 bytes
- **Success:** True

### Get Item by Name (Display Name)

- **URL:** `GET http://localhost:8000/items/Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 24.45 ms
- **Response Size:** 170 bytes
- **Success:** True

### Get Item by Name (Iron Ore)

- **URL:** `GET http://localhost:8000/items/Iron%20Ore`
- **Status Code:** 200
- **Response Time:** 19.78 ms
- **Response Size:** 175 bytes
- **Success:** True

### Get All Resource Nodes

- **URL:** `GET http://localhost:8000/resource-nodes`
- **Status Code:** 200
- **Response Time:** 17.57 ms
- **Response Size:** 3404 bytes
- **Success:** True

### Get All Raw Resources

- **URL:** `GET http://localhost:8000/raw-resources`
- **Status Code:** 200
- **Response Time:** 14.85 ms
- **Response Size:** 2393 bytes
- **Success:** True

### Get Wiki Reference

- **URL:** `GET http://localhost:8000/wiki/Iron%20Ore`
- **Status Code:** 200
- **Response Time:** 13.10 ms
- **Response Size:** 78 bytes
- **Success:** True

### Get All Pipelines

- **URL:** `GET http://localhost:8000/transportation/pipelines`
- **Status Code:** 200
- **Response Time:** 12.99 ms
- **Response Size:** 462 bytes
- **Success:** True

### Get Pipeline Mk1

- **URL:** `GET http://localhost:8000/transportation/pipelines/1`
- **Status Code:** 200
- **Response Time:** 12.56 ms
- **Response Size:** 228 bytes
- **Success:** True

### Get Pipeline Mk2

- **URL:** `GET http://localhost:8000/transportation/pipelines/2`
- **Status Code:** 200
- **Response Time:** 12.24 ms
- **Response Size:** 231 bytes
- **Success:** True

### Get All Pipeline Pumps

- **URL:** `GET http://localhost:8000/transportation/pipeline-pumps`
- **Status Code:** 200
- **Response Time:** 12.15 ms
- **Response Size:** 880 bytes
- **Success:** True

### Get Pipeline Pump Mk1

- **URL:** `GET http://localhost:8000/transportation/pipeline-pumps/1`
- **Status Code:** 200
- **Response Time:** 11.94 ms
- **Response Size:** 438 bytes
- **Success:** True

### Get Pipeline Pump Mk2

- **URL:** `GET http://localhost:8000/transportation/pipeline-pumps/2`
- **Status Code:** 200
- **Response Time:** 9.44 ms
- **Response Size:** 439 bytes
- **Success:** True

### Get All Locomotives

- **URL:** `GET http://localhost:8000/transportation/trains/locomotives`
- **Status Code:** 200
- **Response Time:** 7.68 ms
- **Response Size:** 380 bytes
- **Success:** True

### Get All Freight Cars

- **URL:** `GET http://localhost:8000/transportation/trains/freight-cars`
- **Status Code:** 200
- **Response Time:** 7.78 ms
- **Response Size:** 406 bytes
- **Success:** True

### Get All Train Stations

- **URL:** `GET http://localhost:8000/transportation/train-stations`
- **Status Code:** 200
- **Response Time:** 8.05 ms
- **Response Size:** 1362 bytes
- **Success:** True

### Get Train Stations - Solid Type

- **URL:** `GET http://localhost:8000/transportation/train-stations?station_type=solid`
- **Status Code:** 200
- **Response Time:** 8.11 ms
- **Response Size:** 762 bytes
- **Success:** True

### Get Train Stations - Liquid Type

- **URL:** `GET http://localhost:8000/transportation/train-stations?station_type=liquid`
- **Status Code:** 200
- **Response Time:** 8.40 ms
- **Response Size:** 411 bytes
- **Success:** True

### Get Train Stations - Empty Type

- **URL:** `GET http://localhost:8000/transportation/train-stations?station_type=empty`
- **Status Code:** 200
- **Response Time:** 8.86 ms
- **Response Size:** 191 bytes
- **Success:** True

### Get Locomotive by Name

- **URL:** `GET http://localhost:8000/transportation/trains/locomotives/Electric%20Locomotive`
- **Status Code:** 200
- **Response Time:** 8.79 ms
- **Response Size:** 378 bytes
- **Success:** True

### Get Freight Car by Name

- **URL:** `GET http://localhost:8000/transportation/trains/freight-cars/Freight%20Car`
- **Status Code:** 200
- **Response Time:** 9.28 ms
- **Response Size:** 404 bytes
- **Success:** True

### Get All Train Signals

- **URL:** `GET http://localhost:8000/transportation/trains/signals`
- **Status Code:** 200
- **Response Time:** 8.82 ms
- **Response Size:** 417 bytes
- **Success:** True

### Get Train Signals - Block Signal

- **URL:** `GET http://localhost:8000/transportation/trains/signals?signal_type=Block%20Signal`
- **Status Code:** 200
- **Response Time:** 8.86 ms
- **Response Size:** 143 bytes
- **Success:** True

### Get Train Signal - Block Signal

- **URL:** `GET http://localhost:8000/transportation/trains/signals/Block%20Signal`
- **Status Code:** 200
- **Response Time:** 7.64 ms
- **Response Size:** 141 bytes
- **Success:** True

### Get Train Signal - Path Signal

- **URL:** `GET http://localhost:8000/transportation/trains/signals/Path%20Signal`
- **Status Code:** 200
- **Response Time:** 7.83 ms
- **Response Size:** 139 bytes
- **Success:** True

### Get Train Signal - End Stop

- **URL:** `GET http://localhost:8000/transportation/trains/signals/End%20Stop`
- **Status Code:** 200
- **Response Time:** 5.79 ms
- **Response Size:** 133 bytes
- **Success:** True

### Get Train Station by Name

- **URL:** `GET http://localhost:8000/transportation/train-stations/Train%20Station`
- **Status Code:** 200
- **Response Time:** 5.42 ms
- **Response Size:** 363 bytes
- **Success:** True

### Get Train Station by Name - Fluid Freight Platform

- **URL:** `GET http://localhost:8000/transportation/train-stations/Fluid%20Freight%20Platform`
- **Status Code:** 200
- **Response Time:** 7.29 ms
- **Response Size:** 409 bytes
- **Success:** True

### Get All Railway Tracks

- **URL:** `GET http://localhost:8000/transportation/railway-tracks`
- **Status Code:** 200
- **Response Time:** 6.39 ms
- **Response Size:** 248 bytes
- **Success:** True

### Get All Trucks

- **URL:** `GET http://localhost:8000/transportation/vehicles/trucks`
- **Status Code:** 200
- **Response Time:** 6.82 ms
- **Response Size:** 860 bytes
- **Success:** True

### Get Truck

- **URL:** `GET http://localhost:8000/transportation/vehicles/trucks/truck`
- **Status Code:** 200
- **Response Time:** 6.50 ms
- **Response Size:** 410 bytes
- **Success:** True

### Get Tractor

- **URL:** `GET http://localhost:8000/transportation/vehicles/trucks/tractor`
- **Status Code:** 200
- **Response Time:** 6.53 ms
- **Response Size:** 447 bytes
- **Success:** True

### Get Truck Stations

- **URL:** `GET http://localhost:8000/transportation/truck-stations`
- **Status Code:** 200
- **Response Time:** 8.24 ms
- **Response Size:** 350 bytes
- **Success:** True

### Get All Drones

- **URL:** `GET http://localhost:8000/transportation/drones`
- **Status Code:** 200
- **Response Time:** 6.00 ms
- **Response Size:** 454 bytes
- **Success:** True

### Get Drone Stations

- **URL:** `GET http://localhost:8000/transportation/drone-stations`
- **Status Code:** 200
- **Response Time:** 6.86 ms
- **Response Size:** 481 bytes
- **Success:** True

### Get Drone by Name

- **URL:** `GET http://localhost:8000/transportation/drones/Drone`
- **Status Code:** 200
- **Response Time:** 6.23 ms
- **Response Size:** 452 bytes
- **Success:** True

### Get All Freight Platforms

- **URL:** `GET http://localhost:8000/transportation/freight-platforms`
- **Status Code:** 200
- **Response Time:** 6.57 ms
- **Response Size:** 2 bytes
- **Success:** True

### Production Rate

- **URL:** `GET http://localhost:8000/calculate/production-rate?recipe=Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 6.29 ms
- **Response Size:** 586 bytes
- **Success:** True

### Production Rate with Overclock

- **URL:** `GET http://localhost:8000/calculate/production-rate?recipe=Recipe_IronPlate_C&overclock=150`
- **Status Code:** 200
- **Response Time:** 6.69 ms
- **Response Size:** 588 bytes
- **Success:** True

### Buildings Needed

- **URL:** `GET http://localhost:8000/calculate/buildings-needed?recipe=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 6.46 ms
- **Response Size:** 245 bytes
- **Success:** True

### Buildings Needed with Overclock

- **URL:** `GET http://localhost:8000/calculate/buildings-needed?recipe=Iron%20Plate&target_rate=120&overclock=200`
- **Status Code:** 200
- **Response Time:** 5.48 ms
- **Response Size:** 247 bytes
- **Success:** True

### Production Chain

- **URL:** `GET http://localhost:8000/calculate/production-chain?item=Heavy%20Modular%20Frame&target_rate=10`
- **Status Code:** 200
- **Response Time:** 20.12 ms
- **Response Size:** 14973 bytes
- **Success:** True

### Production Chain - No Alternates

- **URL:** `GET http://localhost:8000/calculate/production-chain?item=Iron%20Plate&target_rate=60&include_alternates=false`
- **Status Code:** 200
- **Response Time:** 6.14 ms
- **Response Size:** 1233 bytes
- **Success:** True

### Production Chain - Preferred Recipe

- **URL:** `GET http://localhost:8000/calculate/production-chain?item=Computer&target_rate=5&preferred_recipe=Alternate:%20Caterium%20Computer`
- **Status Code:** 200
- **Response Time:** 32.25 ms
- **Response Size:** 12381 bytes
- **Success:** True

### Compare Recipes

- **URL:** `GET http://localhost:8000/calculate/compare-recipes?item=Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 19.38 ms
- **Response Size:** 3815 bytes
- **Success:** True

### Miner Output

- **URL:** `GET http://localhost:8000/calculate/miner-output?resource=Iron%20Ore&miner_mk=3&purity=pure&overclock=200`
- **Status Code:** 200
- **Response Time:** 20.15 ms
- **Response Size:** 240 bytes
- **Success:** True

### Miner Output - Normal Purity

- **URL:** `GET http://localhost:8000/calculate/miner-output?resource=Coal&miner_mk=2&purity=normal`
- **Status Code:** 200
- **Response Time:** 33.73 ms
- **Response Size:** 236 bytes
- **Success:** True

### Belt Requirements

- **URL:** `GET http://localhost:8000/calculate/belt-requirements?throughput=540`
- **Status Code:** 200
- **Response Time:** 30.09 ms
- **Response Size:** 671 bytes
- **Success:** True

### Belt Requirements - High Throughput

- **URL:** `GET http://localhost:8000/calculate/belt-requirements?throughput=1200`
- **Status Code:** 200
- **Response Time:** 31.54 ms
- **Response Size:** 440 bytes
- **Success:** True

### Perfect Ratios

- **URL:** `GET http://localhost:8000/calculate/perfect-ratios?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 33.55 ms
- **Response Size:** 1636 bytes
- **Success:** True

### Perfect Ratios - With Overclock

- **URL:** `GET http://localhost:8000/calculate/perfect-ratios?item=Heavy%20Modular%20Frame&target_rate=10&allow_overclock=true`
- **Status Code:** 200
- **Response Time:** 33.60 ms
- **Response Size:** 16653 bytes
- **Success:** True

### Optimize 100 Percent

- **URL:** `GET http://localhost:8000/calculate/optimize-100-percent?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 34.30 ms
- **Response Size:** 2352 bytes
- **Success:** True

### Optimize 100 Percent - With Overclock

- **URL:** `GET http://localhost:8000/calculate/optimize-100-percent?item=Computer&target_rate=5&allow_overclock=true`
- **Status Code:** 200
- **Response Time:** 42.85 ms
- **Response Size:** 19371 bytes
- **Success:** True

### Factory Efficiency

- **URL:** `GET http://localhost:8000/calculate/factory-efficiency?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 36.00 ms
- **Response Size:** 2144 bytes
- **Success:** True

### Factory Efficiency - Heavy Modular Frame

- **URL:** `GET http://localhost:8000/calculate/factory-efficiency?item=Heavy%20Modular%20Frame&target_rate=10`
- **Status Code:** 200
- **Response Time:** 49.48 ms
- **Response Size:** 20866 bytes
- **Success:** True

### Building Utilization

- **URL:** `GET http://localhost:8000/calculate/building-utilization?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 49.88 ms
- **Response Size:** 1355 bytes
- **Success:** True

### Building Utilization - Computer

- **URL:** `GET http://localhost:8000/calculate/building-utilization?item=Computer&target_rate=5`
- **Status Code:** 200
- **Response Time:** 59.07 ms
- **Response Size:** 12637 bytes
- **Success:** True

### Get All Generators

- **URL:** `GET http://localhost:8000/power/generators`
- **Status Code:** 200
- **Response Time:** 62.00 ms
- **Response Size:** 3046 bytes
- **Success:** True

### Get Generators - By Type (Coal)

- **URL:** `GET http://localhost:8000/power/generators?generator_type=Coal`
- **Status Code:** 200
- **Response Time:** 53.51 ms
- **Response Size:** 940 bytes
- **Success:** True

### Get Generator by Type (Coal)

- **URL:** `GET http://localhost:8000/power/generators/Coal`
- **Status Code:** 200
- **Response Time:** 55.43 ms
- **Response Size:** 938 bytes
- **Success:** True

### Get Generator by Type (Nuclear)

- **URL:** `GET http://localhost:8000/power/generators/Nuclear`
- **Status Code:** 200
- **Response Time:** 49.47 ms
- **Response Size:** 960 bytes
- **Success:** True

### Get Generator by Name - Coal Generator

- **URL:** `GET http://localhost:8000/power/generators/name/Coal%20Generator`
- **Status Code:** 200
- **Response Time:** 51.31 ms
- **Response Size:** 306 bytes
- **Success:** True

### Get Generator by Name - Biomass

- **URL:** `GET http://localhost:8000/power/generators/name/Biomass`
- **Status Code:** 200
- **Response Time:** 40.57 ms
- **Response Size:** 1144 bytes
- **Success:** True

### Get Generators by Tier

- **URL:** `GET http://localhost:8000/power/generators/tier/3`
- **Status Code:** 200
- **Response Time:** 42.80 ms
- **Response Size:** 940 bytes
- **Success:** True

### Get Power Storage

- **URL:** `GET http://localhost:8000/power/storage`
- **Status Code:** 200
- **Response Time:** 36.35 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Power Storage by Name

- **URL:** `GET http://localhost:8000/power/storage/Power%20Storage`
- **Status Code:** 200
- **Response Time:** 34.13 ms
- **Response Size:** 241 bytes
- **Success:** True

### Get All Power Poles

- **URL:** `GET http://localhost:8000/power/poles`
- **Status Code:** 200
- **Response Time:** 30.66 ms
- **Response Size:** 1053 bytes
- **Success:** True

### Get Power Pole Mk1

- **URL:** `GET http://localhost:8000/power/poles/1`
- **Status Code:** 200
- **Response Time:** 27.12 ms
- **Response Size:** 349 bytes
- **Success:** True

### Get Power Pole Mk2

- **URL:** `GET http://localhost:8000/power/poles/2`
- **Status Code:** 200
- **Response Time:** 24.34 ms
- **Response Size:** 349 bytes
- **Success:** True

### Get Power Pole Mk3

- **URL:** `GET http://localhost:8000/power/poles/3`
- **Status Code:** 200
- **Response Time:** 20.00 ms
- **Response Size:** 351 bytes
- **Success:** True

### Get Power Pole by Name

- **URL:** `GET http://localhost:8000/power/poles/name/Power%20Pole%20Mk.1`
- **Status Code:** 200
- **Response Time:** 16.82 ms
- **Response Size:** 349 bytes
- **Success:** True

### Get All Splitters

- **URL:** `GET http://localhost:8000/logistics/splitters`
- **Status Code:** 200
- **Response Time:** 17.46 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Splitters - By Type (Smart)

- **URL:** `GET http://localhost:8000/logistics/splitters?splitter_type=Smart`
- **Status Code:** 200
- **Response Time:** 17.36 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Splitter by Name - Conveyor Splitter

- **URL:** `GET http://localhost:8000/logistics/splitters/Conveyor%20Splitter`
- **Status Code:** 200
- **Response Time:** 18.24 ms
- **Response Size:** 251 bytes
- **Success:** True

### Get Splitter by Name - Smart

- **URL:** `GET http://localhost:8000/logistics/splitters/Smart`
- **Status Code:** 200
- **Response Time:** 21.35 ms
- **Response Size:** 253 bytes
- **Success:** True

### Get All Mergers

- **URL:** `GET http://localhost:8000/logistics/mergers`
- **Status Code:** 200
- **Response Time:** 24.47 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Merger by Name

- **URL:** `GET http://localhost:8000/logistics/mergers/Conveyor%20Merger`
- **Status Code:** 200
- **Response Time:** 26.68 ms
- **Response Size:** 221 bytes
- **Success:** True

### Get All Storage Containers

- **URL:** `GET http://localhost:8000/logistics/storage`
- **Status Code:** 200
- **Response Time:** 29.96 ms
- **Response Size:** 360 bytes
- **Success:** True

### Get Storage Containers - By Type (Industrial)

- **URL:** `GET http://localhost:8000/logistics/storage?container_type=Industrial`
- **Status Code:** 200
- **Response Time:** 33.06 ms
- **Response Size:** 360 bytes
- **Success:** True

### Get Storage Container by Name - Storage Container

- **URL:** `GET http://localhost:8000/logistics/storage/Storage%20Container`
- **Status Code:** 200
- **Response Time:** 31.74 ms
- **Response Size:** 242 bytes
- **Success:** True

### Get Storage Container by Name - Industrial

- **URL:** `GET http://localhost:8000/logistics/storage/Industrial`
- **Status Code:** 200
- **Response Time:** 31.81 ms
- **Response Size:** 358 bytes
- **Success:** True

### Get All Fluid Buffers

- **URL:** `GET http://localhost:8000/logistics/fluid-buffers`
- **Status Code:** 200
- **Response Time:** 31.98 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get All Valves

- **URL:** `GET http://localhost:8000/logistics/valves`
- **Status Code:** 200
- **Response Time:** 32.24 ms
- **Response Size:** 264 bytes
- **Success:** True

### Get Valves - By Type (Inverted)

- **URL:** `GET http://localhost:8000/logistics/valves?valve_type=Inverted`
- **Status Code:** 200
- **Response Time:** 31.94 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Valve by Name - Valve

- **URL:** `GET http://localhost:8000/logistics/valves/Valve`
- **Status Code:** 200
- **Response Time:** 31.67 ms
- **Response Size:** 262 bytes
- **Success:** True

### Get Valve by Name - Inverted

- **URL:** `GET http://localhost:8000/logistics/valves/Inverted`
- **Status Code:** 200
- **Response Time:** 32.01 ms
- **Response Size:** 215 bytes
- **Success:** True

### Get All Water Extractors

- **URL:** `GET http://localhost:8000/extractors/water-extractors`
- **Status Code:** 200
- **Response Time:** 28.74 ms
- **Response Size:** 452 bytes
- **Success:** True

### Get Water Extractor by Name

- **URL:** `GET http://localhost:8000/extractors/water-extractors/Water%20Extractor`
- **Status Code:** 200
- **Response Time:** 25.50 ms
- **Response Size:** 450 bytes
- **Success:** True

### Get All Resource Well Extractors

- **URL:** `GET http://localhost:8000/extractors/resource-well-extractors`
- **Status Code:** 200
- **Response Time:** 23.25 ms
- **Response Size:** 403 bytes
- **Success:** True

### Get Resource Well Extractors - By Type (Oil)

- **URL:** `GET http://localhost:8000/extractors/resource-well-extractors?resource_type=Oil`
- **Status Code:** 200
- **Response Time:** 21.25 ms
- **Response Size:** 403 bytes
- **Success:** True

### Get All Milestones

- **URL:** `GET http://localhost:8000/progression/milestones`
- **Status Code:** 200
- **Response Time:** 18.41 ms
- **Response Size:** 27106 bytes
- **Success:** True

### Get Milestones - By Tier

- **URL:** `GET http://localhost:8000/progression/milestones?tier=3`
- **Status Code:** 200
- **Response Time:** 15.46 ms
- **Response Size:** 2453 bytes
- **Success:** True

### Get Milestones - By Phase

- **URL:** `GET http://localhost:8000/progression/milestones?phase=2`
- **Status Code:** 200
- **Response Time:** 13.36 ms
- **Response Size:** 3081 bytes
- **Success:** True

### Get Milestones by Tier (Path Parameter)

- **URL:** `GET http://localhost:8000/progression/milestones/3`
- **Status Code:** 200
- **Response Time:** 9.59 ms
- **Response Size:** 2453 bytes
- **Success:** True

### Get Milestone by Name - Coal Power

- **URL:** `GET http://localhost:8000/progression/milestones/name/Coal%20Power`
- **Status Code:** 200
- **Response Time:** 9.49 ms
- **Response Size:** 543 bytes
- **Success:** True

### Get Milestone by Name - Quantum Encoding

- **URL:** `GET http://localhost:8000/progression/milestones/name/Quantum%20Encoding`
- **Status Code:** 200
- **Response Time:** 9.62 ms
- **Response Size:** 733 bytes
- **Success:** True

### Get All Unlocks

- **URL:** `GET http://localhost:8000/progression/unlocks`
- **Status Code:** 200
- **Response Time:** 108.79 ms
- **Response Size:** 175039 bytes
- **Success:** True

### Get Unlocks - By Type (Building)

- **URL:** `GET http://localhost:8000/progression/unlocks?unlock_type=building`
- **Status Code:** 200
- **Response Time:** 200.78 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Unlocks - By Tier

- **URL:** `GET http://localhost:8000/progression/unlocks?tier=4`
- **Status Code:** 200
- **Response Time:** 295.82 ms
- **Response Size:** 5689 bytes
- **Success:** True

### Get Unlocks - By Milestone

- **URL:** `GET http://localhost:8000/progression/unlocks?milestone=Coal%20Power`
- **Status Code:** 200
- **Response Time:** 391.14 ms
- **Response Size:** 1030 bytes
- **Success:** True

### Get Unlock by Name - Constructor

- **URL:** `GET http://localhost:8000/progression/unlocks/Constructor`
- **Status Code:** 200
- **Response Time:** 485.61 ms
- **Response Size:** 148 bytes
- **Success:** True

### Get Unlock by Name - Iron Plate

- **URL:** `GET http://localhost:8000/progression/unlocks/Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 679.93 ms
- **Response Size:** 148 bytes
- **Success:** True

### Get Unlocks by Type - Building

- **URL:** `GET http://localhost:8000/progression/unlocks/type/building`
- **Status Code:** 200
- **Response Time:** 583.36 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Unlocks by Type - Recipe

- **URL:** `GET http://localhost:8000/progression/unlocks/type/recipe`
- **Status Code:** 200
- **Response Time:** 780.39 ms
- **Response Size:** 161570 bytes
- **Success:** True

### Get Unlocks by Type - Schematic

- **URL:** `GET http://localhost:8000/progression/unlocks/type/schematic`
- **Status Code:** 200
- **Response Time:** 780.10 ms
- **Response Size:** 13470 bytes
- **Success:** True

### Swagger UI

- **URL:** `GET http://localhost:8000/docs`
- **Status Code:** 200
- **Response Time:** 686.28 ms
- **Response Size:** 950 bytes
- **Success:** True

### ReDoc

- **URL:** `GET http://localhost:8000/redoc`
- **Status Code:** 200
- **Response Time:** 590.45 ms
- **Response Size:** 907 bytes
- **Success:** True

### OpenAPI JSON

- **URL:** `GET http://localhost:8000/openapi.json`
- **Status Code:** 200
- **Response Time:** 495.53 ms
- **Response Size:** 73673 bytes
- **Success:** True

