import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional

class GameDescriptorParser:
    def __init__(self, descriptor_file: Path):
        self.descriptor_file = descriptor_file
        self.data: List[Dict[str, Any]] = []
        self._load_data()
    
    def _load_data(self):
        if not self.descriptor_file.exists():
            raise FileNotFoundError(f"Descriptor file not found: {self.descriptor_file}")
        
        encodings = ['utf-16-le', 'utf-16', 'utf-8', 'utf-8-sig', 'latin-1']
        for encoding in encodings:
            try:
                with open(self.descriptor_file, 'r', encoding=encoding) as f:
                    self.data = json.load(f)
                if isinstance(self.data, list):
                    return
            except (UnicodeDecodeError, json.JSONDecodeError):
                continue
        
        raise ValueError(f"Could not decode descriptor file {self.descriptor_file} with any supported encoding")
    
    def _parse_float(self, value: str) -> float:
        try:
            return float(value)
        except (ValueError, TypeError):
            return 0.0
    
    def _parse_int(self, value: str) -> int:
        try:
            return int(float(value))
        except (ValueError, TypeError):
            return 0
    
    def _extract_number_from_text(self, text: str, pattern: str, default: float = 0.0) -> float:
        if not text:
            return default
        match = re.search(pattern, text)
        if match:
            try:
                return float(match.group(1).replace(',', '').replace(' ', ''))
            except (ValueError, IndexError):
                pass
        return default
    
    def _get_class_by_name(self, class_name_pattern: str) -> Optional[Dict[str, Any]]:
        pattern = re.compile(class_name_pattern)
        for entry in self.data:
            if "Classes" in entry:
                for class_obj in entry["Classes"]:
                    if "ClassName" in class_obj and pattern.match(class_obj["ClassName"]):
                        return class_obj
        return None
    
    def _get_display_info(self, desc_class_name: str) -> Dict[str, str]:
        desc_class = self._get_class_by_name(desc_class_name)
        if desc_class:
            return {
                "display_name": desc_class.get("mDisplayName", ""),
                "description": desc_class.get("mDescription", "")
            }
        return {"display_name": "", "description": ""}
    
    def extract_miners(self) -> List[Dict[str, Any]]:
        miners = []
        for mk in [1, 2, 3]:
            build_class_name = f"Build_MinerMk{mk}_C"
            build_class = self._get_class_by_name(build_class_name)
            
            if build_class:
                desc_class_name = f"Desc_MinerMk{mk}_C"
                display_info = self._get_display_info(desc_class_name)
                
                miner_data = {
                    "mk": mk,
                    "class_name": build_class.get("ClassName", ""),
                    "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                    "description": build_class.get("mDescription") or display_info.get("description", ""),
                    "extract_cycle_time": self._parse_float(build_class.get("mExtractCycleTime", "0")),
                    "items_per_cycle": self._parse_int(build_class.get("mItemsPerCycle", "0")),
                    "power_consumption": self._parse_float(build_class.get("mPowerConsumption", "0")),
                    "power_consumption_exponent": self._parse_float(build_class.get("mPowerConsumptionExponent", "0")) if build_class.get("mPowerConsumptionExponent") else None,
                    "extract_startup_time": self._parse_float(build_class.get("mExtractStartupTime", "0")) if build_class.get("mExtractStartupTime") else None
                }
                miners.append(miner_data)
        
        return miners
    
    def extract_belts(self) -> List[Dict[str, Any]]:
        belts = []
        for mk in [1, 2, 3, 4, 5, 6]:
            build_class_name = f"Build_ConveyorBeltMk{mk}_C"
            build_class = self._get_class_by_name(build_class_name)
            
            if build_class:
                desc_class_name = f"Desc_ConveyorBeltMk{mk}_C"
                display_info = self._get_display_info(desc_class_name)
                
                belt_data = {
                    "mk": mk,
                    "class_name": build_class.get("ClassName", ""),
                    "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                    "description": build_class.get("mDescription") or display_info.get("description", ""),
                    "speed": self._parse_float(build_class.get("mSpeed", "0"))
                }
                belts.append(belt_data)
        
        return belts
    
    def extract_raw_resources(self) -> List[Dict[str, Any]]:
        raw_resources = []
        resource_patterns = [
            r"Desc_(OreIron|OreCopper|OreGold|OreBauxite|OreUranium)_C",
            r"Desc_(Coal|Stone|Sulfur|RawQuartz|LiquidOil|Water|NitrogenGas|Geyser|SAM)_C",
            r"Desc_(CrudeOil|LiquidOil)_C"
        ]
        
        seen_resources = set()
        
        for entry in self.data:
            if "Classes" in entry:
                for class_obj in entry["Classes"]:
                    class_name = class_obj.get("ClassName", "")
                    
                    for pattern in resource_patterns:
                        if re.match(pattern, class_name) and class_name not in seen_resources:
                            seen_resources.add(class_name)
                            
                            resource_type = class_name.replace("Desc_", "").replace("_C", "")
                            resource_type = re.sub(r'([A-Z])', r' \1', resource_type).strip()
                            
                            raw_resource = {
                                "class_name": class_name,
                                "display_name": class_obj.get("mDisplayName", ""),
                                "description": class_obj.get("mDescription", ""),
                                "resource_type": resource_type
                            }
                            raw_resources.append(raw_resource)
                            break
        
        return raw_resources
    
    def extract_resource_nodes(self) -> List[Dict[str, Any]]:
        resource_nodes = []
        
        purity_multipliers = {
            "impure": 0.5,
            "normal": 1.0,
            "pure": 2.0
        }
        
        raw_resources = self.extract_raw_resources()
        resource_types = {r["resource_type"] for r in raw_resources}
        
        for resource_type in resource_types:
            for purity, multiplier in purity_multipliers.items():
                node = {
                    "resource_type": resource_type,
                    "purity": purity,
                    "multiplier": multiplier,
                    "display_name": None
                }
                
                resource_obj = next((r for r in raw_resources if r["resource_type"] == resource_type), None)
                if resource_obj:
                    node["display_name"] = resource_obj.get("display_name")
                
                resource_nodes.append(node)
        
        return resource_nodes
    
    def _parse_recipe_items(self, items_str: str) -> List[Dict[str, Any]]:
        if not items_str or items_str == "":
            return []
        
        items = []
        pattern = r'ItemClass="([^"]+)"[^A]*Amount=(\d+)'
        matches = re.findall(pattern, items_str)
        
        for item_class, amount in matches:
            items.append({
                "item_class": item_class,
                "amount": self._parse_int(amount)
            })
        
        return items
    
    def _parse_produced_in(self, produced_in_str: str) -> List[str]:
        if not produced_in_str or produced_in_str == "":
            return []
        
        buildings = []
        pattern = r'"([^"]+Build_[^"]+)"'
        matches = re.findall(pattern, produced_in_str)
        
        for match in matches:
            building_match = re.search(r'Build_(\w+)\.Build_\w+_C', match)
            if building_match:
                buildings.append(building_match.group(1))
        
        return buildings
    
    def _is_alternate_recipe(self, class_name: str, full_name: str, display_name: str) -> bool:
        if "Recipe_Alternate_" in class_name:
            return True
        if "AlternateRecipes" in full_name:
            return True
        if display_name and display_name.startswith("Alternate:"):
            return True
        return False
    
    def extract_recipes(self) -> List[Dict[str, Any]]:
        recipes = []
        
        for entry in self.data:
            if "Classes" in entry:
                for class_obj in entry["Classes"]:
                    class_name = class_obj.get("ClassName", "")
                    if class_name.startswith("Recipe_") and class_name != "Recipe_Pattern_" and not class_name.endswith("_Icon_C"):
                        full_name = class_obj.get("FullName", "")
                        display_name = class_obj.get("mDisplayName", "N/A")
                        
                        if display_name == "N/A":
                            continue
                        
                        ingredients_str = class_obj.get("mIngredients", "")
                        product_str = class_obj.get("mProduct", "")
                        produced_in_str = class_obj.get("mProducedIn", "")
                        
                        ingredients = self._parse_recipe_items(ingredients_str)
                        products = self._parse_recipe_items(product_str)
                        produced_in = self._parse_produced_in(produced_in_str)
                        
                        if ingredients or products:
                            recipe = {
                                "class_name": class_name,
                                "display_name": display_name,
                                "is_alternate": self._is_alternate_recipe(class_name, full_name, display_name),
                                "ingredients": ingredients,
                                "products": products,
                                "manufacturing_duration": self._parse_float(class_obj.get("mManufactoringDuration", "0")),
                                "produced_in": produced_in,
                                "variable_power_consumption_constant": self._parse_float(class_obj.get("mVariablePowerConsumptionConstant", "0")) if class_obj.get("mVariablePowerConsumptionConstant") else None,
                                "variable_power_consumption_factor": self._parse_float(class_obj.get("mVariablePowerConsumptionFactor", "0")) if class_obj.get("mVariablePowerConsumptionFactor") else None
                            }
                            recipes.append(recipe)
        
        return recipes
    
    def extract_buildings(self) -> List[Dict[str, Any]]:
        buildings = []
        unlock_map = self._build_unlock_mapping()
        building_types = [
            ("Build_ConstructorMk1_C", "Constructor", "Recipe_Constructor"),
            ("Build_AssemblerMk1_C", "Assembler", "Recipe_Assembler"),
            ("Build_ManufacturerMk1_C", "Manufacturer", "Recipe_Manufacturer"),
            ("Build_SmelterMk1_C", "Smelter", "Recipe_Smelter"),
            ("Build_FoundryMk1_C", "Foundry", "Recipe_Foundry"),
            ("Build_OilRefinery_C", "Refinery", "Recipe_OilRefinery"),
            ("Build_BlenderMk1_C", "Blender", "Recipe_Blender"),
            ("Build_ParticleAccelerator_C", "ParticleAccelerator", "Recipe_ParticleAccelerator"),
            ("Build_Packager_C", "Packager", "Recipe_Packager")
        ]
        
        for build_class_name, building_type, recipe_prefix in building_types:
            build_class = self._get_class_by_name(build_class_name)
            
            if build_class:
                display_name = build_class.get("mDisplayName", "")
                description = build_class.get("mDescription", "")
                
                unlock_info = self._get_unlock_info(f"{recipe_prefix}_C", unlock_map)
                
                building_data = {
                    "class_name": build_class.get("ClassName", ""),
                    "display_name": display_name,
                    "description": description,
                    "building_type": building_type,
                    "power_consumption": self._parse_float(build_class.get("mPowerConsumption", "0")),
                    "power_consumption_exponent": self._parse_float(build_class.get("mPowerConsumptionExponent", "0")) if build_class.get("mPowerConsumptionExponent") else None,
                    "tier_unlocked": unlock_info.get("tier"),
                    "milestone": unlock_info.get("milestone")
                }
                buildings.append(building_data)
        
        return buildings
    
    def extract_all_items(self) -> List[Dict[str, Any]]:
        items = []
        excluded_prefixes = [
            "Desc_ConveyorBeltMk",
            "Desc_MinerMk",
            "Desc_PowerPole",
            "Desc_Pipeline",
            "Desc_Build_",
            "Desc_BlueprintDesigner",
            "Desc_Pattern_",
            "Desc_Swatch_"
        ]
        
        for entry in self.data:
            if "Classes" in entry:
                for class_obj in entry["Classes"]:
                    class_name = class_obj.get("ClassName", "")
                    
                    if class_name.startswith("Desc_") and not any(class_name.startswith(prefix) for prefix in excluded_prefixes):
                        display_name = class_obj.get("mDisplayName", "")
                        
                        if not display_name or display_name == "N/A":
                            continue
                        
                        item_type = "component"
                        if "RawResources" in class_obj.get("FullName", ""):
                            item_type = "raw_resource"
                        elif "Equipment" in class_obj.get("FullName", ""):
                            item_type = "equipment"
                        elif any(building in class_obj.get("FullName", "") for building in ["Buildable", "Factory"]):
                            item_type = "building_part"
                        
                        item = {
                            "class_name": class_name,
                            "display_name": display_name,
                            "description": class_obj.get("mDescription", ""),
                            "item_type": item_type,
                            "stack_size": class_obj.get("mStackSize") if class_obj.get("mStackSize") else None
                        }
                        items.append(item)
        
        return items
    
    def extract_pipelines(self) -> List[Dict[str, Any]]:
        pipelines = []
        for mk in [1, 2]:
            if mk == 1:
                build_class_name = "Build_Pipeline_C"
                desc_class_name = "Desc_Pipeline_C"
            else:
                build_class_name = "Build_PipelineMK2_C"
                desc_class_name = "Desc_PipelineMK2_C"
            
            build_class = self._get_class_by_name(build_class_name)
            
            if build_class:
                display_info = self._get_display_info(desc_class_name)
                description = build_class.get("mDescription") or display_info.get("description", "")
                
                flow_rate = self._extract_number_from_text(
                    description, 
                    r'Capacity:\s*(\d+(?:[,\s]\d+)*)\s*m³',
                    300.0 if mk == 1 else 600.0
                )
                
                pipeline_data = {
                    "mk": mk,
                    "class_name": build_class.get("ClassName", ""),
                    "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                    "description": description,
                    "flow_rate": flow_rate
                }
                pipelines.append(pipeline_data)
        
        return pipelines
    
    def extract_pipeline_pumps(self) -> List[Dict[str, Any]]:
        pumps = []
        for mk in [1, 2]:
            if mk == 1:
                build_class_name = "Build_PipelinePump_C"
                desc_class_name = "Desc_PipelinePump_C"
                default_head_lift = 20.0
            else:
                build_class_name = "Build_PipelinePumpMk2_C"
                desc_class_name = "Desc_PipelinePumpMk2_C"
                default_head_lift = 50.0
            
            build_class = self._get_class_by_name(build_class_name)
            
            if build_class:
                display_info = self._get_display_info(desc_class_name)
                description = build_class.get("mDescription") or display_info.get("description", "")
                
                head_lift = self._extract_number_from_text(
                    description,
                    r'Maximum Head Lift:\s*(\d+(?:\.\d+)?)\s*m',
                    default_head_lift
                )
                
                if head_lift == default_head_lift:
                    design_pressure = self._parse_float(build_class.get("mDesignPressure", "0"))
                    if design_pressure > 0:
                        head_lift = design_pressure
                
                pump_data = {
                    "mk": mk,
                    "class_name": build_class.get("ClassName", ""),
                    "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                    "description": description,
                    "power_consumption": self._parse_float(build_class.get("mPowerConsumption", "0")),
                    "head_lift": head_lift,
                    "flow_rate": None
                }
                pumps.append(pump_data)
        
        return pumps
    
    def extract_train_stations(self) -> List[Dict[str, Any]]:
        stations = []
        station_configs = [
            ("Build_TrainStation_C", "Desc_TrainStation_C", "solid", 100),
            ("Build_TrainDockingStation_C", "Desc_TrainDockingStation_C", "solid", 100),
            ("Build_TrainDockingStationLiquid_C", "Desc_TrainDockingStationLiquid_C", "liquid", 100),
            ("Build_TrainPlatformEmpty_C", "Desc_TrainPlatformEmpty_C", "empty", 100)
        ]
        
        for build_class_name, desc_class_name, station_type, power in station_configs:
            build_class = self._get_class_by_name(build_class_name)
            
            if build_class:
                display_info = self._get_display_info(desc_class_name)
                
                platform_count = 2
                if "Empty" in build_class_name:
                    platform_count = 1
                
                station_data = {
                    "class_name": build_class.get("ClassName", ""),
                    "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                    "description": build_class.get("mDescription") or display_info.get("description", ""),
                    "power_consumption": self._parse_float(build_class.get("mPowerConsumption", str(power))),
                    "platform_count": platform_count,
                    "station_type": station_type
                }
                stations.append(station_data)
        
        return stations
    
    def extract_truck_stations(self) -> List[Dict[str, Any]]:
        stations = []
        build_class_name = "Build_TruckStation_C"
        desc_class_name = "Desc_TruckStation_C"
        
        build_class = self._get_class_by_name(build_class_name)
        
        if build_class:
            display_info = self._get_display_info(desc_class_name)
            
            station_data = {
                "class_name": build_class.get("ClassName", ""),
                "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                "description": build_class.get("mDescription") or display_info.get("description", ""),
                "power_consumption": self._parse_float(build_class.get("mPowerConsumption", "50")),
                "input_output_rate": None
            }
            stations.append(station_data)
        
        return stations
    
    def extract_drone_stations(self) -> List[Dict[str, Any]]:
        stations = []
        build_class_name = "Build_DroneStation_C"
        desc_class_name = "Desc_DroneStation_C"
        
        build_class = self._get_class_by_name(build_class_name)
        
        if build_class:
            display_info = self._get_display_info(desc_class_name)
            
            station_data = {
                "class_name": build_class.get("ClassName", ""),
                "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                "description": build_class.get("mDescription") or display_info.get("description", ""),
                "power_consumption": self._parse_float(build_class.get("mPowerConsumption", "100")),
                "drone_capacity": 1,
                "charging_rate": None,
                "throughput_rate": None
            }
            stations.append(station_data)
        
        return stations
    
    def _parse_power_consumption_range(self, power_str: str) -> Dict[str, float]:
        if not power_str or power_str == "":
            return {"min": 0.0, "max": 0.0}
        
        match = re.search(r'Min=([0-9.]+).*Max=([0-9.]+)', power_str)
        if match:
            return {
                "min": self._parse_float(match.group(1)),
                "max": self._parse_float(match.group(2))
            }
        return {"min": 0.0, "max": 0.0}
    
    def extract_train_locomotives(self) -> List[Dict[str, Any]]:
        locomotives = []
        desc_class_name = "Desc_Locomotive_C"
        desc_class = self._get_class_by_name(desc_class_name)
        
        if desc_class:
            power_consumption = desc_class.get("mPowerConsumption", "")
            power_range = self._parse_power_consumption_range(power_consumption)
            
            locomotive_data = {
                "class_name": desc_class.get("ClassName", ""),
                "display_name": desc_class.get("mDisplayName", ""),
                "description": desc_class.get("mDescription", ""),
                "power_consumption_min": power_range["min"],
                "power_consumption_max": power_range["max"],
                "power_consumption": power_range["max"]
            }
            locomotives.append(locomotive_data)
        
        return locomotives
    
    def extract_train_freight_cars(self) -> List[Dict[str, Any]]:
        freight_cars = []
        desc_class_name = "Desc_FreightWagon_C"
        desc_class = self._get_class_by_name(desc_class_name)
        
        if desc_class:
            storage_slots = self._parse_int(desc_class.get("mInventorySize", "32"))
            description = desc_class.get("mDescription", "")
            
            fluid_capacity = self._extract_number_from_text(
                description,
                r'(\d+(?:[,\s]\d+)*)\s*m³',
                1600.0
            )
            
            freight_car_data = {
                "class_name": desc_class.get("ClassName", ""),
                "display_name": desc_class.get("mDisplayName", ""),
                "description": description,
                "storage_slots": storage_slots,
                "fluid_capacity_m3": fluid_capacity,
                "throughput_rate": None
            }
            freight_cars.append(freight_car_data)
        
        return freight_cars
    
    def extract_trucks(self) -> List[Dict[str, Any]]:
        trucks = []
        vehicle_configs = [
            ("Desc_Truck_C", "Truck"),
            ("Desc_Tractor_C", "Tractor")
        ]
        
        for desc_class_name, vehicle_type in vehicle_configs:
            desc_class = self._get_class_by_name(desc_class_name)
            
            if desc_class:
                storage_slots = self._parse_int(desc_class.get("mInventorySize", "0"))
                fuel_consumption = self._parse_float(desc_class.get("mFuelConsumption", "0"))
                
                vehicle_data = {
                    "class_name": desc_class.get("ClassName", ""),
                    "display_name": desc_class.get("mDisplayName", ""),
                    "description": desc_class.get("mDescription", ""),
                    "vehicle_type": vehicle_type,
                    "storage_slots": storage_slots,
                    "fuel_consumption_rate": fuel_consumption,
                    "max_speed": None,
                    "tier_unlocked": None
                }
                trucks.append(vehicle_data)
        
        return trucks
    
    def extract_drones(self) -> List[Dict[str, Any]]:
        drones = []
        desc_class_name = "Desc_DroneTransport_C"
        desc_class = self._get_class_by_name(desc_class_name)
        
        if desc_class:
            cargo_slots = self._parse_int(desc_class.get("mInventorySize", "9"))
            
            drone_data = {
                "class_name": desc_class.get("ClassName", ""),
                "display_name": desc_class.get("mDisplayName", ""),
                "description": desc_class.get("mDescription", ""),
                "cargo_slots": cargo_slots,
                "battery_capacity": None,
                "max_speed": None,
                "range_limit": None
            }
            drones.append(drone_data)
        
        return drones
    
    def extract_freight_platforms(self) -> List[Dict[str, Any]]:
        platforms = []
        build_class_name = "Build_FreightPlatform_C"
        desc_class_name = "Desc_FreightPlatform_C"
        
        build_class = self._get_class_by_name(build_class_name)
        
        if build_class:
            display_info = self._get_display_info(desc_class_name)
            
            platform_data = {
                "class_name": build_class.get("ClassName", ""),
                "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                "description": build_class.get("mDescription") or display_info.get("description", ""),
                "power_consumption": self._parse_float(build_class.get("mPowerConsumption", "0")),
                "storage_slots": 32,
                "input_rate": None,
                "output_rate": None
            }
            platforms.append(platform_data)
        
        return platforms
    
    def extract_power_generators(self) -> List[Dict[str, Any]]:
        generators = []
        unlock_map = self._build_unlock_mapping()
        generator_configs = [
            ("Build_GeneratorBiomass_Automated_C", "Desc_GeneratorBiomass_Automated_C", "Biomass", 30.0, "Recipe_GeneratorBiomass_Automated"),
            ("Build_GeneratorCoal_C", "Desc_GeneratorCoal_C", "Coal", 75.0, "Recipe_GeneratorCoal"),
            ("Build_FuelGenerator_C", "Desc_FuelGenerator_C", "Fuel", 150.0, "Recipe_GeneratorFuel"),
            ("Build_GeothermalGenerator_C", "Desc_GeothermalGenerator_C", "Geothermal", 200.0, "Recipe_GeneratorGeoThermal"),
            ("Build_GeneratorNuclear_C", "Desc_GeneratorNuclear_C", "Nuclear", 2500.0, "Recipe_GeneratorNuclear")
        ]
        
        for build_class_name, desc_class_name, gen_type, default_power, recipe_prefix in generator_configs:
            build_class = self._get_class_by_name(build_class_name)
            
            if build_class:
                display_info = self._get_display_info(desc_class_name)
                
                power_output = self._parse_float(build_class.get("mPowerProduction", str(default_power)))
                
                fuel_types = []
                fuel_class_name = build_class.get("mFuel", "")
                if fuel_class_name:
                    fuel_types = [fuel_class_name]
                
                unlock_info = self._get_unlock_info(f"{recipe_prefix}_C", unlock_map)
                
                generator_data = {
                    "class_name": build_class.get("ClassName", ""),
                    "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                    "description": build_class.get("mDescription") or display_info.get("description", ""),
                    "generator_type": gen_type,
                    "power_output": power_output,
                    "power_consumption": self._parse_float(build_class.get("mPowerConsumption", "0")),
                    "fuel_types": fuel_types if fuel_types else None,
                    "fuel_consumption_rate": self._parse_float(build_class.get("mSupplementalLoadAmount", "0")) if build_class.get("mSupplementalLoadAmount") else None,
                    "water_consumption_rate": self._parse_float(build_class.get("mSupplementalToConsume", "0")) if gen_type == "Coal" else None,
                    "tier_unlocked": unlock_info.get("tier"),
                    "milestone": unlock_info.get("milestone")
                }
                generators.append(generator_data)
        
        return generators
    
    def extract_power_storage(self) -> List[Dict[str, Any]]:
        storage = []
        unlock_map = self._build_unlock_mapping()
        build_class_name = "Build_PowerStorage_C"
        desc_class_name = "Desc_PowerStorage_C"
        
        build_class = self._get_class_by_name(build_class_name)
        
        if build_class:
            display_info = self._get_display_info(desc_class_name)
            
            capacity = self._parse_float(build_class.get("mPowerCapacity", "100"))
            
            unlock_info = self._get_unlock_info("Recipe_PowerStorage_C", unlock_map)
            
            storage_data = {
                "class_name": build_class.get("ClassName", ""),
                "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                "description": build_class.get("mDescription") or display_info.get("description", ""),
                "capacity": capacity,
                "charge_rate": self._parse_float(build_class.get("mPowerConsumption", "0")),
                "discharge_rate": self._parse_float(build_class.get("mPowerConsumption", "0")),
                "efficiency": 1.0,
                "tier_unlocked": unlock_info.get("tier"),
                "milestone": unlock_info.get("milestone")
            }
            storage.append(storage_data)
        
        return storage
    
    def extract_power_poles(self) -> List[Dict[str, Any]]:
        poles = []
        pole_configs = [
            (1, "Build_PowerPoleMk1_C", "Desc_PowerPoleMk1_C", 4),
            (2, "Build_PowerPoleMk2_C", "Desc_PowerPoleMk2_C", 7),
            (3, "Build_PowerPoleMk3_C", "Desc_PowerPoleMk3_C", 10)
        ]
        
        for mk, build_class_name, desc_class_name, connection_limit in pole_configs:
            build_class = self._get_class_by_name(build_class_name)
            
            if build_class:
                display_info = self._get_display_info(desc_class_name)
                
                pole_data = {
                    "mk": mk,
                    "class_name": build_class.get("ClassName", ""),
                    "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                    "description": build_class.get("mDescription") or display_info.get("description", ""),
                    "connection_limit": connection_limit,
                    "power_transmission": None
                }
                poles.append(pole_data)
        
        return poles
    
    def extract_conveyor_splitters(self) -> List[Dict[str, Any]]:
        splitters = []
        unlock_map = self._build_unlock_mapping()
        splitter_configs = [
            ("Build_ConveyorSplitter_C", "Desc_ConveyorSplitter_C", "Regular", 3, "Recipe_ConveyorSplitter"),
            ("Build_ConveyorSplitterSmart_C", "Desc_ConveyorSplitterSmart_C", "Smart", 3, "Recipe_ConveyorSplitterSmart"),
            ("Build_ConveyorSplitterProgrammable_C", "Desc_ConveyorSplitterProgrammable_C", "Programmable", 3, "Recipe_ConveyorSplitterProgrammable")
        ]
        
        for build_class_name, desc_class_name, splitter_type, output_count, recipe_prefix in splitter_configs:
            build_class = self._get_class_by_name(build_class_name)
            
            if build_class:
                display_info = self._get_display_info(desc_class_name)
                
                unlock_info = self._get_unlock_info(f"{recipe_prefix}_C", unlock_map)
                
                splitter_data = {
                    "class_name": build_class.get("ClassName", ""),
                    "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                    "description": build_class.get("mDescription") or display_info.get("description", ""),
                    "splitter_type": splitter_type,
                    "output_count": output_count,
                    "throughput_capacity": None,
                    "tier_unlocked": unlock_info.get("tier"),
                    "milestone": unlock_info.get("milestone")
                }
                splitters.append(splitter_data)
        
        return splitters
    
    def extract_conveyor_mergers(self) -> List[Dict[str, Any]]:
        mergers = []
        unlock_map = self._build_unlock_mapping()
        build_class_name = "Build_ConveyorMerger_C"
        desc_class_name = "Desc_ConveyorMerger_C"
        
        build_class = self._get_class_by_name(build_class_name)
        
        if build_class:
            display_info = self._get_display_info(desc_class_name)
            
            unlock_info = self._get_unlock_info("Recipe_ConveyorMerger_C", unlock_map)
            
            merger_data = {
                "class_name": build_class.get("ClassName", ""),
                "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                "description": build_class.get("mDescription") or display_info.get("description", ""),
                "input_count": 3,
                "throughput_capacity": None,
                "tier_unlocked": unlock_info.get("tier"),
                "milestone": unlock_info.get("milestone")
            }
            mergers.append(merger_data)
        
        return mergers
    
    def extract_storage_containers(self) -> List[Dict[str, Any]]:
        containers = []
        unlock_map = self._build_unlock_mapping()
        container_configs = [
            ("Build_StorageContainer_C", "Desc_StorageContainer_C", "Storage", 48, "Recipe_StorageContainer"),
            ("Build_StorageContainerMk2_C", "Desc_StorageContainerMk2_C", "Industrial", 48, "Recipe_StorageContainerMk2"),
            ("Build_IndustrialStorageBuffer_C", "Desc_IndustrialStorageBuffer_C", "Buffer", 48, "Recipe_IndustrialStorageBuffer")
        ]
        
        for build_class_name, desc_class_name, container_type, storage_slots, recipe_prefix in container_configs:
            build_class = self._get_class_by_name(build_class_name)
            
            if build_class:
                display_info = self._get_display_info(desc_class_name)
                
                unlock_info = self._get_unlock_info(f"{recipe_prefix}_C", unlock_map)
                
                container_data = {
                    "class_name": build_class.get("ClassName", ""),
                    "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                    "description": build_class.get("mDescription") or display_info.get("description", ""),
                    "container_type": container_type,
                    "storage_slots": storage_slots,
                    "input_rate": None,
                    "output_rate": None,
                    "tier_unlocked": unlock_info.get("tier"),
                    "milestone": unlock_info.get("milestone")
                }
                containers.append(container_data)
        
        return containers
    
    def extract_fluid_buffers(self) -> List[Dict[str, Any]]:
        buffers = []
        unlock_map = self._build_unlock_mapping()
        buffer_configs = [
            ("Build_PipelineJunction_Cross_C", "Desc_PipelineJunctionCross_C", 0, None),
            ("Build_FluidBuffer_C", "Desc_FluidBuffer_C", 50, "Recipe_PipeStorageTank"),
            ("Build_IndustrialFluidBuffer_C", "Desc_IndustrialFluidBuffer_C", 200, "Recipe_IndustrialFluidBuffer")
        ]
        
        for build_class_name, desc_class_name, capacity, recipe_prefix in buffer_configs:
            build_class = self._get_class_by_name(build_class_name)
            
            if build_class:
                display_info = self._get_display_info(desc_class_name)
                
                if capacity > 0:
                    unlock_info = {}
                    if recipe_prefix:
                        unlock_info = self._get_unlock_info(f"{recipe_prefix}_C", unlock_map)
                    
                    buffer_data = {
                        "class_name": build_class.get("ClassName", ""),
                        "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                        "description": build_class.get("mDescription") or display_info.get("description", ""),
                        "capacity": float(capacity),
                        "input_rate": None,
                        "output_rate": None,
                        "tier_unlocked": unlock_info.get("tier") if unlock_info else None,
                        "milestone": unlock_info.get("milestone") if unlock_info else None
                    }
                    buffers.append(buffer_data)
        
        return buffers
    
    def extract_valves(self) -> List[Dict[str, Any]]:
        valves = []
        unlock_map = self._build_unlock_mapping()
        valve_configs = [
            ("Build_Valve_C", "Desc_Valve_C", "Regular", "Recipe_Valve"),
            ("Build_ValveInverted_C", "Desc_ValveInverted_C", "Inverted", "Recipe_ValveInverted")
        ]
        
        for build_class_name, desc_class_name, valve_type, recipe_prefix in valve_configs:
            build_class = self._get_class_by_name(build_class_name)
            
            if build_class:
                display_info = self._get_display_info(desc_class_name)
                
                unlock_info = self._get_unlock_info(f"{recipe_prefix}_C", unlock_map)
                
                valve_data = {
                    "class_name": build_class.get("ClassName", ""),
                    "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                    "description": build_class.get("mDescription") or display_info.get("description", ""),
                    "valve_type": valve_type,
                    "max_flow_rate": None,
                    "tier_unlocked": unlock_info.get("tier"),
                    "milestone": unlock_info.get("milestone")
                }
                valves.append(valve_data)
        
        return valves
    
    def extract_water_extractors(self) -> List[Dict[str, Any]]:
        extractors = []
        build_class_name = "Build_WaterPump_C"
        desc_class_name = "Desc_WaterPump_C"
        
        build_class = self._get_class_by_name(build_class_name)
        
        if build_class:
            display_info = self._get_display_info(desc_class_name)
            
            extraction_rate = self._parse_float(build_class.get("mExtractStartupTime", "120"))
            
            extractor_data = {
                "class_name": build_class.get("ClassName", ""),
                "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                "description": build_class.get("mDescription") or display_info.get("description", ""),
                "extraction_rate": extraction_rate,
                "power_consumption": self._parse_float(build_class.get("mPowerConsumption", "20")),
                "power_consumption_exponent": self._parse_float(build_class.get("mPowerConsumptionExponent", "0")) if build_class.get("mPowerConsumptionExponent") else None
            }
            extractors.append(extractor_data)
        
        return extractors
    
    def extract_resource_well_extractors(self) -> List[Dict[str, Any]]:
        extractors = []
        well_configs = [
            ("Build_ResourceExtractor_C", "Desc_ResourceExtractor_C", "Oil"),
            ("Build_OilPump_C", "Desc_OilPump_C", "Oil"),
            ("Build_ResourceWellExtractor_C", "Desc_ResourceWellExtractor_C", "Generic"),
            ("Build_NitrogenExtractor_C", "Desc_NitrogenExtractor_C", "Nitrogen")
        ]
        
        for build_class_name, desc_class_name, resource_type in well_configs:
            build_class = self._get_class_by_name(build_class_name)
            
            if build_class:
                display_info = self._get_display_info(desc_class_name)
                
                extractor_data = {
                    "class_name": build_class.get("ClassName", ""),
                    "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                    "description": build_class.get("mDescription") or display_info.get("description", ""),
                    "resource_type": resource_type,
                    "extraction_rate": self._parse_float(build_class.get("mExtractStartupTime", "0")) if build_class.get("mExtractStartupTime") else None,
                    "power_consumption": self._parse_float(build_class.get("mPowerConsumption", "0")),
                    "pressure_requirement": None
                }
                extractors.append(extractor_data)
        
        return extractors
    
    def _parse_cost_items(self, cost_str: str) -> List[Dict[str, Any]]:
        if not cost_str or cost_str == "":
            return []
        
        cost_items = []
        pattern = r'ItemClass="([^"]+)"[^A]*Amount=(\d+)'
        matches = re.findall(pattern, cost_str)
        
        for item_class, amount in matches:
            cost_items.append({
                "item_class": item_class,
                "amount": self._parse_int(amount)
            })
        
        return cost_items
    
    def _parse_recipe_unlocks(self, recipes_str: str) -> List[str]:
        if not recipes_str or recipes_str == "":
            return []
        
        recipes = []
        pattern = r'Recipe_([^.\']+)\.Recipe_([^.\']+)_C'
        matches = re.findall(pattern, recipes_str)
        
        for match in matches:
            recipe_name = f"Recipe_{match[1]}_C"
            recipes.append(recipe_name)
        
        return recipes
    
    def extract_milestones(self) -> List[Dict[str, Any]]:
        milestones = []
        
        for entry in self.data:
            if "Classes" in entry:
                for class_obj in entry["Classes"]:
                    schematic_type = class_obj.get("mType", "")
                    
                    if schematic_type == "EST_Milestone":
                        tier = self._parse_int(class_obj.get("mTechTier", "0"))
                        phase = tier if tier > 0 else 0
                        
                        cost = self._parse_cost_items(class_obj.get("mCost", ""))
                        
                        milestone_data = {
                            "class_name": class_obj.get("ClassName", ""),
                            "display_name": class_obj.get("mDisplayName", ""),
                            "description": class_obj.get("mDescription", ""),
                            "tier": tier,
                            "phase": phase,
                            "cost": cost if cost else None
                        }
                        milestones.append(milestone_data)
        
        return milestones
    
    def _build_unlock_mapping(self) -> Dict[str, Dict[str, Any]]:
        unlock_map = {}
        
        for entry in self.data:
            if "Classes" in entry:
                for class_obj in entry["Classes"]:
                    schematic_type = class_obj.get("mType", "")
                    tier = self._parse_int(class_obj.get("mTechTier", "0"))
                    milestone_name = class_obj.get("mDisplayName", "")
                    unlocks = class_obj.get("mUnlocks", [])
                    
                    for unlock_obj in unlocks:
                        unlock_class = unlock_obj.get("Class", "")
                        
                        if unlock_class == "BP_UnlockRecipe_C":
                            recipes_str = unlock_obj.get("mRecipes", "")
                            recipe_list = self._parse_recipe_unlocks(recipes_str)
                            
                            for recipe in recipe_list:
                                if recipe not in unlock_map:
                                    unlock_map[recipe] = {
                                        "tier": tier if tier > 0 else None,
                                        "milestone": milestone_name if milestone_name else None,
                                        "unlock_type": "recipe"
                                    }
                        
                        elif unlock_class == "BP_UnlockSchematic_C":
                            schematics_str = unlock_obj.get("mSchematics", "")
                            pattern = r'([^./]+)\.([^.\']+)_C'
                            matches = re.findall(pattern, schematics_str)
                            
                            for match in matches:
                                schematic_name = f"{match[1]}_C"
                                if schematic_name not in unlock_map:
                                    unlock_map[schematic_name] = {
                                        "tier": tier if tier > 0 else None,
                                        "milestone": milestone_name if milestone_name else None,
                                        "unlock_type": "schematic"
                                    }
        
        return unlock_map
    
    def _get_building_class_from_recipe(self, recipe_class_name: str) -> Optional[str]:
        build_prefixes = {
            "Recipe_GeneratorBiomass_Automated": "Build_GeneratorBiomass_Automated",
            "Recipe_GeneratorBiomass": "Build_GeneratorBiomass_Automated",
            "Recipe_GeneratorCoal": "Build_GeneratorCoal",
            "Recipe_GeneratorFuel": "Build_FuelGenerator",
            "Recipe_GeneratorGeoThermal": "Build_GeothermalGenerator",
            "Recipe_GeneratorNuclear": "Build_GeneratorNuclear",
            "Recipe_Constructor": "Build_ConstructorMk1",
            "Recipe_Assembler": "Build_AssemblerMk1",
            "Recipe_Manufacturer": "Build_ManufacturerMk1",
            "Recipe_Smelter": "Build_SmelterMk1",
            "Recipe_Foundry": "Build_FoundryMk1",
            "Recipe_OilRefinery": "Build_OilRefinery",
            "Recipe_Blender": "Build_BlenderMk1",
            "Recipe_ParticleAccelerator": "Build_ParticleAccelerator",
            "Recipe_Packager": "Build_Packager",
            "Recipe_WaterPump": "Build_WaterPump",
            "Recipe_PowerStorage": "Build_PowerStorage",
            "Recipe_ConveyorSplitter": "Build_ConveyorSplitter",
            "Recipe_ConveyorMerger": "Build_ConveyorMerger",
            "Recipe_StorageContainer": "Build_StorageContainer",
            "Recipe_StorageContainerMk2": "Build_StorageContainerMk2",
            "Recipe_IndustrialStorageBuffer": "Build_IndustrialStorageBuffer",
            "Recipe_FluidBuffer": "Build_FluidBuffer",
            "Recipe_IndustrialFluidBuffer": "Build_IndustrialFluidBuffer",
            "Recipe_Valve": "Build_Valve",
            "Recipe_ValveInverted": "Build_ValveInverted",
            "Recipe_PipeStorageTank": "Build_FluidBuffer"
        }
        
        for recipe_prefix, build_prefix in build_prefixes.items():
            if recipe_class_name.startswith(recipe_prefix):
                return f"{build_prefix}_C"
        
        return None
    
    def _get_unlock_info(self, class_name: str, unlock_map: Dict[str, Dict[str, Any]]) -> Dict[str, Optional[Any]]:
        recipe_patterns = [
            r"Recipe_([^_]+)(?:_.+)?_C",
            r"Recipe_([^_]+)_C"
        ]
        
        for pattern in recipe_patterns:
            match = re.match(pattern, class_name)
            if match:
                recipe_name = f"Recipe_{match.group(1)}"
                if recipe_name in unlock_map:
                    return unlock_map[recipe_name]
                
                building_class = self._get_building_class_from_recipe(class_name)
                if building_class and building_class in unlock_map:
                    return unlock_map[building_class]
        
        if class_name in unlock_map:
            return unlock_map[class_name]
        
        for key, value in unlock_map.items():
            if class_name in key or key in class_name:
                return value
        
        return {"tier": None, "milestone": None, "unlock_type": None}
    
    def extract_railway_tracks(self) -> List[Dict[str, Any]]:
        tracks = []
        build_class_name = "Build_RailroadTrack_C"
        desc_class_name = "Desc_RailroadTrack_C"
        
        build_class = self._get_class_by_name(build_class_name)
        
        if build_class:
            display_info = self._get_display_info(desc_class_name)
            
            track_data = {
                "class_name": build_class.get("ClassName", ""),
                "display_name": build_class.get("mDisplayName") or display_info.get("display_name", ""),
                "description": build_class.get("mDescription") or display_info.get("description", ""),
                "mesh_length": self._parse_float(build_class.get("mMeshLength", "1200")),
                "power_transmission": None,
                "connection_limit": None
            }
            tracks.append(track_data)
        
        return tracks
    
    def extract_train_signals(self) -> List[Dict[str, Any]]:
        signals = []
        signal_configs = [
            ("Desc_RailroadBlockSignal_C", "Block Signal"),
            ("Desc_RailroadPathSignal_C", "Path Signal"),
            ("Desc_RailroadEndStop_C", "End Stop")
        ]
        
        for desc_class_name, signal_type in signal_configs:
            desc_class = self._get_class_by_name(desc_class_name)
            
            if desc_class:
                signal_data = {
                    "class_name": desc_class.get("ClassName", ""),
                    "display_name": desc_class.get("mDisplayName", ""),
                    "description": desc_class.get("mDescription", ""),
                    "signal_type": signal_type,
                    "power_consumption": None,
                    "range": None
                }
                signals.append(signal_data)
        
        return signals
    
    def extract_unlocks(self) -> List[Dict[str, Any]]:
        unlocks = []
        unlock_map = self._build_unlock_mapping()
        
        seen_unlocks = set()
        
        for entry in self.data:
            if "Classes" in entry:
                for class_obj in entry["Classes"]:
                    class_name = class_obj.get("ClassName", "")
                    
                    unlock_info = self._get_unlock_info(class_name, unlock_map)
                    
                    if unlock_info.get("unlock_type"):
                        if class_name not in seen_unlocks:
                            seen_unlocks.add(class_name)
                            
                            unlock_data = {
                                "class_name": class_name,
                                "display_name": class_obj.get("mDisplayName", ""),
                                "unlock_type": unlock_info.get("unlock_type", "unknown"),
                                "tier": unlock_info.get("tier"),
                                "milestone": unlock_info.get("milestone"),
                                "mam_research": None
                            }
                            unlocks.append(unlock_data)
                    
                    unlocks_list = class_obj.get("mUnlocks", [])
                    for unlock_obj in unlocks_list:
                        unlock_class = unlock_obj.get("Class", "")
                        
                        if unlock_class == "BP_UnlockBuildable_C":
                            buildables_str = unlock_obj.get("mBuildables", "")
                            pattern = r'([^./]+)\.([^.\']+)_C'
                            matches = re.findall(pattern, buildables_str)
                            
                            for match in matches:
                                buildable_name = f"{match[1]}_C"
                                if buildable_name not in seen_unlocks:
                                    seen_unlocks.add(buildable_name)
                                    
                                    buildable_info = self._get_unlock_info(buildable_name, unlock_map)
                                    tier = self._parse_int(class_obj.get("mTechTier", "0"))
                                    milestone_name = class_obj.get("mDisplayName", "")
                                    
                                    buildable_class = self._get_class_by_name(buildable_name)
                                    display_name = buildable_class.get("mDisplayName", "") if buildable_class else ""
                                    
                                    unlock_data = {
                                        "class_name": buildable_name,
                                        "display_name": display_name,
                                        "unlock_type": "building",
                                        "tier": tier if tier > 0 else buildable_info.get("tier"),
                                        "milestone": milestone_name if milestone_name else buildable_info.get("milestone"),
                                        "mam_research": None
                                    }
                                    unlocks.append(unlock_data)
        
        return unlocks

