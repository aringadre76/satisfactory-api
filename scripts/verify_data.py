#!/usr/bin/env python3

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parsers.game_descriptor_parser import GameDescriptorParser

DESCRIPTOR_FILE = Path(__file__).parent.parent / "Docs" / "en-US.json"

def verify_data():
    print("Verifying data extraction from game descriptors...")
    print("=" * 60)
    
    if not DESCRIPTOR_FILE.exists():
        print(f"ERROR: Descriptor file not found: {DESCRIPTOR_FILE}")
        return False
    
    try:
        parser = GameDescriptorParser(DESCRIPTOR_FILE)
    except Exception as e:
        print(f"ERROR: Failed to load parser: {e}")
        return False
    
    all_good = True
    
    print("\n1. Testing Miners...")
    try:
        miners = parser.extract_miners()
        print(f"   ✓ Found {len(miners)} miners")
        for miner in miners:
            if miner.get("power_consumption", 0) == 0:
                print(f"   ⚠ WARNING: {miner.get('display_name')} has zero power consumption")
                all_good = False
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        all_good = False
    
    print("\n2. Testing Belts...")
    try:
        belts = parser.extract_belts()
        print(f"   ✓ Found {len(belts)} belts")
        for belt in belts:
            if belt.get("speed", 0) == 0:
                print(f"   ⚠ WARNING: {belt.get('display_name')} has zero speed")
                all_good = False
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        all_good = False
    
    print("\n3. Testing Pipelines...")
    try:
        pipelines = parser.extract_pipelines()
        print(f"   ✓ Found {len(pipelines)} pipelines")
        for pipeline in pipelines:
            flow_rate = pipeline.get("flow_rate", 0)
            if flow_rate == 0:
                print(f"   ⚠ WARNING: {pipeline.get('display_name')} has zero flow rate")
                all_good = False
            else:
                print(f"   ✓ {pipeline.get('display_name')}: {flow_rate} m³/min")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        all_good = False
    
    print("\n4. Testing Pipeline Pumps...")
    try:
        pumps = parser.extract_pipeline_pumps()
        print(f"   ✓ Found {len(pumps)} pipeline pumps")
        for pump in pumps:
            head_lift = pump.get("head_lift", 0)
            if head_lift == 0:
                print(f"   ⚠ WARNING: {pump.get('display_name')} has zero head lift")
                all_good = False
            else:
                print(f"   ✓ {pump.get('display_name')}: {head_lift} m head lift, {pump.get('power_consumption')} MW")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        all_good = False
    
    print("\n5. Testing Train Locomotives...")
    try:
        locomotives = parser.extract_train_locomotives()
        print(f"   ✓ Found {len(locomotives)} locomotives")
        for loco in locomotives:
            power_min = loco.get("power_consumption_min", 0)
            power_max = loco.get("power_consumption_max", 0)
            if power_max == 0:
                print(f"   ⚠ WARNING: {loco.get('display_name')} has invalid power range")
                all_good = False
            else:
                print(f"   ✓ {loco.get('display_name')}: {power_min}-{power_max} MW")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        all_good = False
    
    print("\n6. Testing Train Freight Cars...")
    try:
        freight_cars = parser.extract_train_freight_cars()
        print(f"   ✓ Found {len(freight_cars)} freight cars")
        for car in freight_cars:
            slots = car.get("storage_slots", 0)
            fluid = car.get("fluid_capacity_m3", 0)
            if slots == 0 or fluid == 0:
                print(f"   ⚠ WARNING: {car.get('display_name')} has invalid capacity")
                all_good = False
            else:
                print(f"   ✓ {car.get('display_name')}: {slots} slots, {fluid} m³ fluid")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        all_good = False
    
    print("\n7. Testing Trucks...")
    try:
        trucks = parser.extract_trucks()
        print(f"   ✓ Found {len(trucks)} vehicles")
        for truck in trucks:
            slots = truck.get("storage_slots", 0)
            fuel = truck.get("fuel_consumption_rate", 0)
            if slots == 0:
                print(f"   ⚠ WARNING: {truck.get('display_name')} has zero storage")
                all_good = False
            else:
                print(f"   ✓ {truck.get('display_name')}: {slots} slots, {fuel} fuel/min")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        all_good = False
    
    print("\n8. Testing Drones...")
    try:
        drones = parser.extract_drones()
        print(f"   ✓ Found {len(drones)} drones")
        for drone in drones:
            slots = drone.get("cargo_slots", 0)
            if slots == 0:
                print(f"   ⚠ WARNING: {drone.get('display_name')} has zero cargo slots")
                all_good = False
            else:
                print(f"   ✓ {drone.get('display_name')}: {slots} cargo slots")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        all_good = False
    
    print("\n9. Testing Train Stations...")
    try:
        stations = parser.extract_train_stations()
        print(f"   ✓ Found {len(stations)} train stations")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        all_good = False
    
    print("\n10. Testing Truck Stations...")
    try:
        stations = parser.extract_truck_stations()
        print(f"   ✓ Found {len(stations)} truck stations")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        all_good = False
    
    print("\n11. Testing Drone Stations...")
    try:
        stations = parser.extract_drone_stations()
        print(f"   ✓ Found {len(stations)} drone stations")
    except Exception as e:
        print(f"   ✗ ERROR: {e}")
        all_good = False
    
    print("\n" + "=" * 60)
    if all_good:
        print("✓ All data verification passed!")
        return True
    else:
        print("⚠ Some warnings detected. Please review above.")
        return False

if __name__ == "__main__":
    success = verify_data()
    sys.exit(0 if success else 1)

