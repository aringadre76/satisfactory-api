# Endpoint Test Report

**Generated:** 2026-02-23 17:20:37

## Summary

- **Total Endpoints Tested:** 134
- **Successful:** 134 (100.0%)
- **Failed:** 0 (0.0%)

### Performance Metrics

- **Average Response Time:** 554.15 ms
- **Minimum Response Time:** 100.11 ms
- **Maximum Response Time:** 9514.37 ms

---

## Detailed Results

### Root

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/`
- **Status Code:** 200
- **Response Time:** 165.75 ms
- **Response Size:** 73 bytes
- **Success:** True

### Get All Miners

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/miners`
- **Status Code:** 200
- **Response Time:** 159.47 ms
- **Response Size:** 1365 bytes
- **Success:** True

### Get Miner Mk1

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/miners/1`
- **Status Code:** 200
- **Response Time:** 169.74 ms
- **Response Size:** 452 bytes
- **Success:** True

### Get Miner Mk2

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/miners/2`
- **Status Code:** 200
- **Response Time:** 159.49 ms
- **Response Size:** 454 bytes
- **Success:** True

### Get Miner Mk3

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/miners/3`
- **Status Code:** 200
- **Response Time:** 162.23 ms
- **Response Size:** 455 bytes
- **Success:** True

### Get All Belts

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts`
- **Status Code:** 200
- **Response Time:** 161.57 ms
- **Response Size:** 1203 bytes
- **Success:** True

### Get Belt Mk1

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/1`
- **Status Code:** 200
- **Response Time:** 147.72 ms
- **Response Size:** 198 bytes
- **Success:** True

### Get Belt Mk2

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/2`
- **Status Code:** 200
- **Response Time:** 154.99 ms
- **Response Size:** 199 bytes
- **Success:** True

### Get Belt Mk3

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/3`
- **Status Code:** 200
- **Response Time:** 124.82 ms
- **Response Size:** 199 bytes
- **Success:** True

### Get Belt Mk4

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/4`
- **Status Code:** 200
- **Response Time:** 153.44 ms
- **Response Size:** 199 bytes
- **Success:** True

### Get Belt Mk5

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/5`
- **Status Code:** 200
- **Response Time:** 1216.46 ms
- **Response Size:** 200 bytes
- **Success:** True

### Get Belt Mk6

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/belts/6`
- **Status Code:** 200
- **Response Time:** 121.65 ms
- **Response Size:** 201 bytes
- **Success:** True

### Get All Recipes

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes`
- **Status Code:** 200
- **Response Time:** 642.67 ms
- **Response Size:** 585361 bytes
- **Success:** True

### Get Recipes - Alternate Only

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes?alternate_only=true`
- **Status Code:** 200
- **Response Time:** 702.93 ms
- **Response Size:** 84577 bytes
- **Success:** True

### Get Recipes - By Building (Constructor)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes?building=Constructor`
- **Status Code:** 200
- **Response Time:** 770.12 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Recipes - Combined Filters

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes?alternate_only=true&building=Assembler`
- **Status Code:** 200
- **Response Time:** 256.14 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Recipe by Name (Class Name)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes/Recipe_IronRod_C`
- **Status Code:** 200
- **Response Time:** 281.19 ms
- **Response Size:** 520 bytes
- **Success:** True

### Get Recipe by Name (Display Name)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes/Iron%20Rod`
- **Status Code:** 200
- **Response Time:** 201.77 ms
- **Response Size:** 520 bytes
- **Success:** True

### Get Recipe by Name (Alternate)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/recipes/Alternate:%20Pure%20Iron%20Ingot`
- **Status Code:** 200
- **Response Time:** 199.29 ms
- **Response Size:** 699 bytes
- **Success:** True

### Get All Buildings

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings`
- **Status Code:** 200
- **Response Time:** 215.58 ms
- **Response Size:** 3077 bytes
- **Success:** True

### Get Buildings - By Type (Constructor)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings?building_type=Constructor`
- **Status Code:** 200
- **Response Time:** 285.60 ms
- **Response Size:** 447 bytes
- **Success:** True

### Get Building by Type (Constructor)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings/Constructor`
- **Status Code:** 200
- **Response Time:** 303.33 ms
- **Response Size:** 445 bytes
- **Success:** True

### Get Building by Type (Assembler)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings/Assembler`
- **Status Code:** 200
- **Response Time:** 302.36 ms
- **Response Size:** 441 bytes
- **Success:** True

### Get Building by Type (Manufacturer)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/buildings/Manufacturer`
- **Status Code:** 200
- **Response Time:** 288.56 ms
- **Response Size:** 456 bytes
- **Success:** True

### Get All Items

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items`
- **Status Code:** 200
- **Response Time:** 208.61 ms
- **Response Size:** 45081 bytes
- **Success:** True

### Get Items - By Type (Component)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items?item_type=component`
- **Status Code:** 200
- **Response Time:** 115.58 ms
- **Response Size:** 45081 bytes
- **Success:** True

### Get Items - By Type (Raw Resource)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items?item_type=raw_resource`
- **Status Code:** 200
- **Response Time:** 189.97 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Item by Name (Class Name)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items/Desc_IronPlate_C`
- **Status Code:** 200
- **Response Time:** 125.46 ms
- **Response Size:** 170 bytes
- **Success:** True

### Get Item by Name (Display Name)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items/Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 144.71 ms
- **Response Size:** 170 bytes
- **Success:** True

### Get Item by Name (Iron Ore)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/items/Iron%20Ore`
- **Status Code:** 200
- **Response Time:** 146.30 ms
- **Response Size:** 175 bytes
- **Success:** True

### Get All Resource Nodes

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/resource-nodes`
- **Status Code:** 200
- **Response Time:** 119.50 ms
- **Response Size:** 3404 bytes
- **Success:** True

### Get All Raw Resources

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/raw-resources`
- **Status Code:** 200
- **Response Time:** 170.49 ms
- **Response Size:** 2393 bytes
- **Success:** True

### Get Wiki Reference

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/wiki/Iron%20Ore`
- **Status Code:** 200
- **Response Time:** 957.65 ms
- **Response Size:** 78 bytes
- **Success:** True

### Get All Pipelines

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipelines`
- **Status Code:** 200
- **Response Time:** 1031.30 ms
- **Response Size:** 462 bytes
- **Success:** True

### Get Pipeline Mk1

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipelines/1`
- **Status Code:** 200
- **Response Time:** 982.44 ms
- **Response Size:** 228 bytes
- **Success:** True

### Get Pipeline Mk2

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipelines/2`
- **Status Code:** 200
- **Response Time:** 901.11 ms
- **Response Size:** 231 bytes
- **Success:** True

### Get All Pipeline Pumps

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipeline-pumps`
- **Status Code:** 200
- **Response Time:** 131.10 ms
- **Response Size:** 880 bytes
- **Success:** True

### Get Pipeline Pump Mk1

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipeline-pumps/1`
- **Status Code:** 200
- **Response Time:** 139.22 ms
- **Response Size:** 438 bytes
- **Success:** True

### Get Pipeline Pump Mk2

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/pipeline-pumps/2`
- **Status Code:** 200
- **Response Time:** 156.28 ms
- **Response Size:** 439 bytes
- **Success:** True

### Get All Locomotives

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/locomotives`
- **Status Code:** 200
- **Response Time:** 138.88 ms
- **Response Size:** 380 bytes
- **Success:** True

### Get All Freight Cars

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/freight-cars`
- **Status Code:** 200
- **Response Time:** 132.68 ms
- **Response Size:** 406 bytes
- **Success:** True

### Get All Train Stations

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations`
- **Status Code:** 200
- **Response Time:** 135.91 ms
- **Response Size:** 1362 bytes
- **Success:** True

### Get Train Stations - Solid Type

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations?station_type=solid`
- **Status Code:** 200
- **Response Time:** 137.27 ms
- **Response Size:** 762 bytes
- **Success:** True

### Get Train Stations - Liquid Type

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations?station_type=liquid`
- **Status Code:** 200
- **Response Time:** 181.20 ms
- **Response Size:** 411 bytes
- **Success:** True

### Get Train Stations - Empty Type

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations?station_type=empty`
- **Status Code:** 200
- **Response Time:** 128.30 ms
- **Response Size:** 191 bytes
- **Success:** True

### Get Locomotive by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/locomotives/Electric%20Locomotive`
- **Status Code:** 200
- **Response Time:** 127.16 ms
- **Response Size:** 378 bytes
- **Success:** True

### Get Freight Car by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/freight-cars/Freight%20Car`
- **Status Code:** 200
- **Response Time:** 117.77 ms
- **Response Size:** 404 bytes
- **Success:** True

### Get All Train Signals

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/signals`
- **Status Code:** 200
- **Response Time:** 130.14 ms
- **Response Size:** 417 bytes
- **Success:** True

### Get Train Signals - Block Signal

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/signals?signal_type=Block%20Signal`
- **Status Code:** 200
- **Response Time:** 101.31 ms
- **Response Size:** 143 bytes
- **Success:** True

### Get Train Signal - Block Signal

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/signals/Block%20Signal`
- **Status Code:** 200
- **Response Time:** 125.90 ms
- **Response Size:** 141 bytes
- **Success:** True

### Get Train Signal - Path Signal

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/signals/Path%20Signal`
- **Status Code:** 200
- **Response Time:** 119.53 ms
- **Response Size:** 139 bytes
- **Success:** True

### Get Train Signal - End Stop

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/trains/signals/End%20Stop`
- **Status Code:** 200
- **Response Time:** 106.50 ms
- **Response Size:** 133 bytes
- **Success:** True

### Get Train Station by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations/Train%20Station`
- **Status Code:** 200
- **Response Time:** 118.19 ms
- **Response Size:** 363 bytes
- **Success:** True

### Get Train Station by Name - Fluid Freight Platform

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/train-stations/Fluid%20Freight%20Platform`
- **Status Code:** 200
- **Response Time:** 125.95 ms
- **Response Size:** 409 bytes
- **Success:** True

### Get All Railway Tracks

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/railway-tracks`
- **Status Code:** 200
- **Response Time:** 140.65 ms
- **Response Size:** 248 bytes
- **Success:** True

### Get All Trucks

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/vehicles/trucks`
- **Status Code:** 200
- **Response Time:** 134.47 ms
- **Response Size:** 860 bytes
- **Success:** True

### Get Truck

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/vehicles/trucks/truck`
- **Status Code:** 200
- **Response Time:** 127.39 ms
- **Response Size:** 410 bytes
- **Success:** True

### Get Tractor

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/vehicles/trucks/tractor`
- **Status Code:** 200
- **Response Time:** 131.23 ms
- **Response Size:** 447 bytes
- **Success:** True

### Get Truck Stations

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/truck-stations`
- **Status Code:** 200
- **Response Time:** 129.99 ms
- **Response Size:** 350 bytes
- **Success:** True

### Get All Drones

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/drones`
- **Status Code:** 200
- **Response Time:** 129.13 ms
- **Response Size:** 454 bytes
- **Success:** True

### Get Drone Stations

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/drone-stations`
- **Status Code:** 200
- **Response Time:** 143.76 ms
- **Response Size:** 481 bytes
- **Success:** True

### Get Drone by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/drones/Drone`
- **Status Code:** 200
- **Response Time:** 119.27 ms
- **Response Size:** 452 bytes
- **Success:** True

### Get All Freight Platforms

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/transportation/freight-platforms`
- **Status Code:** 200
- **Response Time:** 124.14 ms
- **Response Size:** 2 bytes
- **Success:** True

### Production Rate

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/production-rate?recipe=Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 136.80 ms
- **Response Size:** 586 bytes
- **Success:** True

### Production Rate with Overclock

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/production-rate?recipe=Recipe_IronPlate_C&overclock=150`
- **Status Code:** 200
- **Response Time:** 126.55 ms
- **Response Size:** 588 bytes
- **Success:** True

### Buildings Needed

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/buildings-needed?recipe=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 108.56 ms
- **Response Size:** 245 bytes
- **Success:** True

### Buildings Needed with Overclock

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/buildings-needed?recipe=Iron%20Plate&target_rate=120&overclock=200`
- **Status Code:** 200
- **Response Time:** 126.65 ms
- **Response Size:** 247 bytes
- **Success:** True

### Production Chain

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/production-chain?item=Heavy%20Modular%20Frame&target_rate=10`
- **Status Code:** 200
- **Response Time:** 159.51 ms
- **Response Size:** 14973 bytes
- **Success:** True

### Production Chain - No Alternates

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/production-chain?item=Iron%20Plate&target_rate=60&include_alternates=false`
- **Status Code:** 200
- **Response Time:** 147.61 ms
- **Response Size:** 1233 bytes
- **Success:** True

### Production Chain - Preferred Recipe

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/production-chain?item=Computer&target_rate=5&preferred_recipe=Alternate:%20Caterium%20Computer`
- **Status Code:** 200
- **Response Time:** 302.25 ms
- **Response Size:** 12381 bytes
- **Success:** True

### Compare Recipes

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/compare-recipes?item=Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 254.31 ms
- **Response Size:** 3815 bytes
- **Success:** True

### Miner Output

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/miner-output?resource=Iron%20Ore&miner_mk=3&purity=pure&overclock=200`
- **Status Code:** 200
- **Response Time:** 202.92 ms
- **Response Size:** 240 bytes
- **Success:** True

### Miner Output - Normal Purity

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/miner-output?resource=Coal&miner_mk=2&purity=normal`
- **Status Code:** 200
- **Response Time:** 198.30 ms
- **Response Size:** 236 bytes
- **Success:** True

### Belt Requirements

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/belt-requirements?throughput=540`
- **Status Code:** 200
- **Response Time:** 197.35 ms
- **Response Size:** 671 bytes
- **Success:** True

### Belt Requirements - High Throughput

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/belt-requirements?throughput=1200`
- **Status Code:** 200
- **Response Time:** 141.95 ms
- **Response Size:** 440 bytes
- **Success:** True

### Perfect Ratios

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/perfect-ratios?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 191.53 ms
- **Response Size:** 1636 bytes
- **Success:** True

### Perfect Ratios - With Overclock

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/perfect-ratios?item=Heavy%20Modular%20Frame&target_rate=10&allow_overclock=true`
- **Status Code:** 200
- **Response Time:** 297.40 ms
- **Response Size:** 16653 bytes
- **Success:** True

### Optimize 100 Percent

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/optimize-100-percent?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 251.07 ms
- **Response Size:** 2352 bytes
- **Success:** True

### Optimize 100 Percent - With Overclock

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/optimize-100-percent?item=Computer&target_rate=5&allow_overclock=true`
- **Status Code:** 200
- **Response Time:** 402.05 ms
- **Response Size:** 19371 bytes
- **Success:** True

### Factory Efficiency

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/factory-efficiency?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 397.84 ms
- **Response Size:** 2144 bytes
- **Success:** True

### Factory Efficiency - Heavy Modular Frame

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/factory-efficiency?item=Heavy%20Modular%20Frame&target_rate=10`
- **Status Code:** 200
- **Response Time:** 490.86 ms
- **Response Size:** 20866 bytes
- **Success:** True

### Building Utilization

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/building-utilization?item=Iron%20Plate&target_rate=60`
- **Status Code:** 200
- **Response Time:** 606.82 ms
- **Response Size:** 1355 bytes
- **Success:** True

### Building Utilization - Computer

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/calculate/building-utilization?item=Computer&target_rate=5`
- **Status Code:** 200
- **Response Time:** 410.25 ms
- **Response Size:** 12637 bytes
- **Success:** True

### Get All Generators

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators`
- **Status Code:** 200
- **Response Time:** 406.09 ms
- **Response Size:** 3046 bytes
- **Success:** True

### Get Generators - By Type (Coal)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators?generator_type=Coal`
- **Status Code:** 200
- **Response Time:** 299.03 ms
- **Response Size:** 940 bytes
- **Success:** True

### Get Generator by Type (Coal)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators/Coal`
- **Status Code:** 200
- **Response Time:** 200.81 ms
- **Response Size:** 938 bytes
- **Success:** True

### Get Generator by Type (Nuclear)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators/Nuclear`
- **Status Code:** 200
- **Response Time:** 298.98 ms
- **Response Size:** 960 bytes
- **Success:** True

### Get Generator by Name - Coal Generator

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators/name/Coal%20Generator`
- **Status Code:** 200
- **Response Time:** 137.47 ms
- **Response Size:** 306 bytes
- **Success:** True

### Get Generator by Name - Biomass

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators/name/Biomass`
- **Status Code:** 200
- **Response Time:** 302.70 ms
- **Response Size:** 1144 bytes
- **Success:** True

### Get Generators by Tier

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/generators/tier/3`
- **Status Code:** 200
- **Response Time:** 257.43 ms
- **Response Size:** 940 bytes
- **Success:** True

### Get Power Storage

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/storage`
- **Status Code:** 200
- **Response Time:** 291.07 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Power Storage by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/storage/Power%20Storage`
- **Status Code:** 200
- **Response Time:** 198.59 ms
- **Response Size:** 241 bytes
- **Success:** True

### Get All Power Poles

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/poles`
- **Status Code:** 200
- **Response Time:** 116.49 ms
- **Response Size:** 1053 bytes
- **Success:** True

### Get Power Pole Mk1

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/poles/1`
- **Status Code:** 200
- **Response Time:** 121.58 ms
- **Response Size:** 349 bytes
- **Success:** True

### Get Power Pole Mk2

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/poles/2`
- **Status Code:** 200
- **Response Time:** 128.90 ms
- **Response Size:** 349 bytes
- **Success:** True

### Get Power Pole Mk3

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/poles/3`
- **Status Code:** 200
- **Response Time:** 129.44 ms
- **Response Size:** 351 bytes
- **Success:** True

### Get Power Pole by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/power/poles/name/Power%20Pole%20Mk.1`
- **Status Code:** 200
- **Response Time:** 128.16 ms
- **Response Size:** 349 bytes
- **Success:** True

### Get All Splitters

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/splitters`
- **Status Code:** 200
- **Response Time:** 154.85 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Splitters - By Type (Smart)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/splitters?splitter_type=Smart`
- **Status Code:** 200
- **Response Time:** 135.33 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Splitter by Name - Conveyor Splitter

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/splitters/Conveyor%20Splitter`
- **Status Code:** 200
- **Response Time:** 163.82 ms
- **Response Size:** 251 bytes
- **Success:** True

### Get Splitter by Name - Smart

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/splitters/Smart`
- **Status Code:** 200
- **Response Time:** 156.57 ms
- **Response Size:** 253 bytes
- **Success:** True

### Get All Mergers

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/mergers`
- **Status Code:** 200
- **Response Time:** 218.93 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Merger by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/mergers/Conveyor%20Merger`
- **Status Code:** 200
- **Response Time:** 232.31 ms
- **Response Size:** 221 bytes
- **Success:** True

### Get All Storage Containers

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/storage`
- **Status Code:** 200
- **Response Time:** 9514.37 ms
- **Response Size:** 360 bytes
- **Success:** True

### Get Storage Containers - By Type (Industrial)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/storage?container_type=Industrial`
- **Status Code:** 200
- **Response Time:** 197.21 ms
- **Response Size:** 360 bytes
- **Success:** True

### Get Storage Container by Name - Storage Container

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/storage/Storage%20Container`
- **Status Code:** 200
- **Response Time:** 198.26 ms
- **Response Size:** 242 bytes
- **Success:** True

### Get Storage Container by Name - Industrial

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/storage/Industrial`
- **Status Code:** 200
- **Response Time:** 118.53 ms
- **Response Size:** 358 bytes
- **Success:** True

### Get All Fluid Buffers

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/fluid-buffers`
- **Status Code:** 200
- **Response Time:** 202.72 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get All Valves

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/valves`
- **Status Code:** 200
- **Response Time:** 199.63 ms
- **Response Size:** 264 bytes
- **Success:** True

### Get Valves - By Type (Inverted)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/valves?valve_type=Inverted`
- **Status Code:** 200
- **Response Time:** 189.96 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Valve by Name - Valve

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/valves/Valve`
- **Status Code:** 200
- **Response Time:** 192.08 ms
- **Response Size:** 262 bytes
- **Success:** True

### Get Valve by Name - Inverted

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/logistics/valves/Inverted`
- **Status Code:** 200
- **Response Time:** 118.94 ms
- **Response Size:** 215 bytes
- **Success:** True

### Get All Water Extractors

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/extractors/water-extractors`
- **Status Code:** 200
- **Response Time:** 114.97 ms
- **Response Size:** 452 bytes
- **Success:** True

### Get Water Extractor by Name

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/extractors/water-extractors/Water%20Extractor`
- **Status Code:** 200
- **Response Time:** 118.46 ms
- **Response Size:** 450 bytes
- **Success:** True

### Get All Resource Well Extractors

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/extractors/resource-well-extractors`
- **Status Code:** 200
- **Response Time:** 4182.53 ms
- **Response Size:** 403 bytes
- **Success:** True

### Get Resource Well Extractors - By Type (Oil)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/extractors/resource-well-extractors?resource_type=Oil`
- **Status Code:** 200
- **Response Time:** 111.83 ms
- **Response Size:** 403 bytes
- **Success:** True

### Get All Milestones

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones`
- **Status Code:** 200
- **Response Time:** 110.73 ms
- **Response Size:** 27106 bytes
- **Success:** True

### Get Milestones - By Tier

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones?tier=3`
- **Status Code:** 200
- **Response Time:** 127.17 ms
- **Response Size:** 2453 bytes
- **Success:** True

### Get Milestones - By Phase

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones?phase=2`
- **Status Code:** 200
- **Response Time:** 106.97 ms
- **Response Size:** 3081 bytes
- **Success:** True

### Get Milestones by Tier (Path Parameter)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones/3`
- **Status Code:** 200
- **Response Time:** 126.22 ms
- **Response Size:** 2453 bytes
- **Success:** True

### Get Milestone by Name - Coal Power

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones/name/Coal%20Power`
- **Status Code:** 200
- **Response Time:** 100.11 ms
- **Response Size:** 543 bytes
- **Success:** True

### Get Milestone by Name - Quantum Encoding

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/milestones/name/Quantum%20Encoding`
- **Status Code:** 200
- **Response Time:** 102.64 ms
- **Response Size:** 733 bytes
- **Success:** True

### Get All Unlocks

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks`
- **Status Code:** 200
- **Response Time:** 1185.70 ms
- **Response Size:** 175039 bytes
- **Success:** True

### Get Unlocks - By Type (Building)

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks?unlock_type=building`
- **Status Code:** 200
- **Response Time:** 2608.81 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Unlocks - By Tier

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks?tier=4`
- **Status Code:** 200
- **Response Time:** 2585.35 ms
- **Response Size:** 5689 bytes
- **Success:** True

### Get Unlocks - By Milestone

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks?milestone=Coal%20Power`
- **Status Code:** 200
- **Response Time:** 2406.52 ms
- **Response Size:** 1030 bytes
- **Success:** True

### Get Unlock by Name - Constructor

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks/Constructor`
- **Status Code:** 200
- **Response Time:** 3506.03 ms
- **Response Size:** 148 bytes
- **Success:** True

### Get Unlock by Name - Iron Plate

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks/Iron%20Plate`
- **Status Code:** 200
- **Response Time:** 3496.64 ms
- **Response Size:** 148 bytes
- **Success:** True

### Get Unlocks by Type - Building

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks/type/building`
- **Status Code:** 200
- **Response Time:** 3400.81 ms
- **Response Size:** 2 bytes
- **Success:** True

### Get Unlocks by Type - Recipe

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks/type/recipe`
- **Status Code:** 200
- **Response Time:** 4022.22 ms
- **Response Size:** 161570 bytes
- **Success:** True

### Get Unlocks by Type - Schematic

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/progression/unlocks/type/schematic`
- **Status Code:** 200
- **Response Time:** 3996.54 ms
- **Response Size:** 13470 bytes
- **Success:** True

### Swagger UI

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/docs`
- **Status Code:** 200
- **Response Time:** 2797.70 ms
- **Response Size:** 950 bytes
- **Success:** True

### ReDoc

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/redoc`
- **Status Code:** 200
- **Response Time:** 2793.44 ms
- **Response Size:** 910 bytes
- **Success:** True

### OpenAPI JSON

- **URL:** `GET https://satisfactory-api-yfw1.onrender.com/openapi.json`
- **Status Code:** 200
- **Response Time:** 119.99 ms
- **Response Size:** 73659 bytes
- **Success:** True

