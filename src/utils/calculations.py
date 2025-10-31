from typing import Dict, List, Optional, Tuple
from src.parsers.game_descriptor_parser import GameDescriptorParser

class SatisfactoryCalculator:
    def __init__(self, parser: GameDescriptorParser):
        self.parser = parser
        self._recipes_cache = None
        self._items_cache = None
        self._buildings_cache = None
    
    def _get_recipes(self):
        if self._recipes_cache is None:
            self._recipes_cache = self.parser.extract_recipes()
        return self._recipes_cache
    
    def _get_items(self):
        if self._items_cache is None:
            self._items_cache = self.parser.extract_all_items()
        return self._items_cache
    
    def _get_buildings(self):
        if self._buildings_cache is None:
            self._buildings_cache = self.parser.extract_buildings()
        return self._buildings_cache
    
    def _find_item_by_name(self, item_name: str):
        items = self._get_items()
        for item in items:
            if item["class_name"] == item_name or item["display_name"].lower() == item_name.lower():
                return item
        return None
    
    def _find_recipe_by_product(self, item_class_or_name: str, include_alternates: bool = True):
        recipes = self._get_recipes()
        matching = []
        
        item_obj = self._find_item_by_name(item_class_or_name)
        if item_obj:
            item_class = item_obj["class_name"]
            item_display_name = item_obj["display_name"]
        else:
            item_class = item_class_or_name
            item_display_name = None
        
        for recipe in recipes:
            if not include_alternates and recipe.get("is_alternate", False):
                continue
            for product in recipe.get("products", []):
                product_class = product["item_class"]
                product_class_short = self._extract_class_name_from_path(product_class)
                
                match = False
                if item_obj:
                    item_name_short = item_class.replace("Desc_", "").replace("_C", "")
                    product_name_short = product_class_short.replace("Desc_", "").replace("_C", "") if product_class_short else ""
                    
                    if (product_class_short and product_class_short == item_class):
                        match = True
                    elif item_name_short in product_class:
                        match = True
                    elif product_name_short and product_name_short == item_name_short:
                        match = True
                    elif item_display_name and (recipe["display_name"] == item_display_name or 
                        recipe["display_name"].startswith(item_display_name + " ") or
                        recipe["display_name"].startswith("Alternate: " + item_display_name)):
                        match = True
                else:
                    if (product_class == item_class or 
                        product_class_short == item_class or
                        item_class in product_class):
                        match = True
                
                if match:
                    matching.append(recipe)
                    break
        return matching
    
    def _extract_class_name_from_path(self, item_class_path: str) -> str:
        if "/Desc_" in item_class_path:
            parts = item_class_path.split("/Desc_")
            if len(parts) > 1:
                class_part = parts[-1].split(".")[0]
                return f"Desc_{class_part}_C"
        return item_class_path
    
    def calculate_production_rate(self, recipe_name: str, building_name: Optional[str] = None, overclock_percentage: float = 100.0) -> Dict:
        recipes = self._get_recipes()
        recipe = None
        for r in recipes:
            if r["class_name"] == recipe_name or r["display_name"].lower() == recipe_name.lower():
                recipe = r
                break
        
        if not recipe:
            return {"error": f"Recipe '{recipe_name}' not found"}
        
        if not recipe.get("produced_in"):
            return {"error": "Recipe has no building information"}
        
        building_type = building_name or recipe["produced_in"][0]
        buildings = self._get_buildings()
        
        building = None
        for b in buildings:
            if building_type.lower() in b["building_type"].lower() or b["building_type"].lower() in building_type.lower():
                building = b
                break
        
        if not building:
            building_type_clean = building_type.replace("Mk1", "").replace("Mk", "").replace("_C", "").replace("Build_", "")
            building = next((b for b in buildings if b["building_type"].lower() == building_type_clean.lower()), None)
        
        if not building:
            return {"error": f"Building '{building_type}' not found"}
        
        duration = recipe["manufacturing_duration"]
        overclock_multiplier = overclock_percentage / 100.0
        effective_duration = duration / overclock_multiplier
        
        products = recipe.get("products", [])
        results = []
        
        for product in products:
            items_per_minute = (60.0 / effective_duration) * product["amount"]
            results.append({
                "item_class": product["item_class"],
                "amount_per_cycle": product["amount"],
                "items_per_minute": round(items_per_minute, 3),
                "items_per_hour": round(items_per_minute * 60, 3)
            })
        
        ingredients = recipe.get("ingredients", [])
        ingredient_rates = []
        for ingredient in ingredients:
            items_per_minute = (60.0 / effective_duration) * ingredient["amount"]
            ingredient_rates.append({
                "item_class": ingredient["item_class"],
                "amount_per_cycle": ingredient["amount"],
                "items_per_minute": round(items_per_minute, 3),
                "items_per_hour": round(items_per_minute * 60, 3)
            })
        
        power_consumption = building["power_consumption"]
        if overclock_percentage != 100.0:
            exponent = building.get("power_consumption_exponent", 1.321929)
            power_consumption = power_consumption * ((overclock_percentage / 100.0) ** exponent)
        
        return {
            "recipe": recipe["display_name"],
            "building": building["display_name"],
            "overclock_percentage": overclock_percentage,
            "production_duration": duration,
            "effective_duration": round(effective_duration, 3),
            "products": results,
            "ingredients": ingredient_rates,
            "power_consumption_mw": round(power_consumption, 3)
        }
    
    def calculate_buildings_needed(self, recipe_name: str, target_rate: float, building_name: Optional[str] = None, overclock_percentage: float = 100.0) -> Dict:
        production = self.calculate_production_rate(recipe_name, building_name, overclock_percentage)
        
        if "error" in production:
            return production
        
        if not production["products"]:
            return {"error": "Recipe has no products"}
        
        items_per_minute_per_building = production["products"][0]["items_per_minute"]
        buildings_needed = target_rate / items_per_minute_per_building
        
        power_per_building = production["power_consumption_mw"]
        total_power = buildings_needed * power_per_building
        
        return {
            "recipe": production["recipe"],
            "building": production["building"],
            "target_production_rate": target_rate,
            "production_rate_per_building": items_per_minute_per_building,
            "buildings_needed": round(buildings_needed, 3),
            "buildings_needed_rounded": round(buildings_needed),
            "power_per_building_mw": power_per_building,
            "total_power_mw": round(total_power, 3),
            "overclock_percentage": overclock_percentage
        }
    
    def calculate_production_chain(self, item_name: str, target_rate: float, include_alternates: bool = True, preferred_recipe: Optional[str] = None) -> Dict:
        item = self._find_item_by_name(item_name)
        if not item:
            return {"error": f"Item '{item_name}' not found"}
        
        chain = {
            "target_item": item["display_name"],
            "target_rate": target_rate,
            "total_power_mw": 0.0,
            "buildings": [],
            "raw_resources": {},
            "steps": []
        }
        
        processed_items = set()
        
        def process_item(item_class_or_name: str, required_rate: float, depth: int = 0):
            if depth > 20:
                return
            
            item_obj = self._find_item_by_name(item_class_or_name)
            if not item_obj:
                item_class = item_class_or_name
            else:
                item_class = item_obj["class_name"]
            
            if item_class in processed_items:
                return
            processed_items.add(item_class)
            
            recipes = self._find_recipe_by_product(item_class, include_alternates)
            if not recipes:
                raw_resource = self._find_item_by_name(item_class_or_name)
                if raw_resource and raw_resource.get("item_type") == "raw_resource":
                    if raw_resource["display_name"] not in chain["raw_resources"]:
                        chain["raw_resources"][raw_resource["display_name"]] = 0.0
                    chain["raw_resources"][raw_resource["display_name"]] += required_rate
                return
            
            recipe = None
            if preferred_recipe:
                for r in recipes:
                    if r["class_name"] == preferred_recipe or r["display_name"].lower() == preferred_recipe.lower():
                        recipe = r
                        break
            
            if not recipe:
                recipe = recipes[0]
            
            produced_in = recipe.get("produced_in", [])
            if not produced_in:
                return
            building_type = produced_in[0]
            
            duration = recipe["manufacturing_duration"]
            products = recipe.get("products", [])
            
            if not products:
                return
            
            product_amount = products[0]["amount"]
            items_per_minute_per_building = (60.0 / duration) * product_amount
            
            buildings_needed = required_rate / items_per_minute_per_building
            
            buildings = self._get_buildings()
            building = None
            for b in buildings:
                if building_type.lower() in b["building_type"].lower() or b["building_type"].lower() in building_type.lower():
                    building = b
                    break
            
            if not building:
                building_type_clean = building_type.replace("Mk1", "").replace("Mk", "").replace("_C", "").replace("Build_", "")
                building = next((b for b in buildings if b["building_type"].lower() == building_type_clean.lower()), None)
            
            if not building:
                return
            
            power_per_building = building["power_consumption"]
            total_power_for_step = buildings_needed * power_per_building
            chain["total_power_mw"] += total_power_for_step
            
            step = {
                "item": item_obj["display_name"] if item_obj else item_class_or_name,
                "recipe": recipe["display_name"],
                "is_alternate": recipe.get("is_alternate", False),
                "building": building["display_name"],
                "buildings_needed": round(buildings_needed, 3),
                "buildings_needed_rounded": round(buildings_needed),
                "production_rate_per_building": round(items_per_minute_per_building, 3),
                "target_production_rate": required_rate,
                "power_per_building_mw": power_per_building,
                "total_power_mw": round(total_power_for_step, 3),
                "ingredients": []
            }
            
            ingredients = recipe.get("ingredients", [])
            for ingredient in ingredients:
                ingredient_rate = (required_rate / product_amount) * ingredient["amount"]
                step["ingredients"].append({
                    "item_class": ingredient["item_class"],
                    "amount_per_cycle": ingredient["amount"],
                    "required_rate_per_minute": round(ingredient_rate, 3)
                })
                process_item(ingredient["item_class"], ingredient_rate, depth + 1)
            
            chain["steps"].append(step)
            chain["buildings"].append({
                "building": building["display_name"],
                "count": round(buildings_needed),
                "power_mw": round(total_power_for_step, 3)
            })
        
        process_item(item_name, target_rate)
        
        chain["total_power_mw"] = round(chain["total_power_mw"], 3)
        
        return chain
    
    def compare_recipes(self, item_name: str) -> Dict:
        item = self._find_item_by_name(item_name)
        if not item:
            return {"error": f"Item '{item_name}' not found"}
        
        item_class = item["class_name"]
        recipes = self._find_recipe_by_product(item_class, include_alternates=True)
        
        if not recipes:
            return {"error": f"No recipes found for '{item_name}'"}
        
        comparisons = []
        for recipe in recipes:
            produced_in = recipe.get("produced_in", [])
            if not produced_in:
                continue
            building_type = produced_in[0]
            
            buildings = self._get_buildings()
            building = None
            for b in buildings:
                if building_type.lower() in b["building_type"].lower() or b["building_type"].lower() in building_type.lower():
                    building = b
                    break
            
            if not building:
                building_type_clean = building_type.replace("Mk1", "").replace("Mk", "").replace("_C", "").replace("Build_", "")
                building = next((b for b in buildings if b["building_type"].lower() == building_type_clean.lower()), None)
            
            if not building:
                continue
            
            duration = recipe["manufacturing_duration"]
            products = recipe.get("products", [])
            ingredients = recipe.get("ingredients", [])
            
            if not products:
                continue
            
            product_amount = products[0]["amount"]
            items_per_minute = (60.0 / duration) * product_amount
            
            total_ingredient_amount = sum(ing["amount"] for ing in ingredients)
            efficiency = product_amount / total_ingredient_amount if total_ingredient_amount > 0 else 0
            
            power_per_building = building["power_consumption"]
            power_per_item = power_per_building / items_per_minute if items_per_minute > 0 else 0
            
            comparison = {
                "recipe_name": recipe["display_name"],
                "is_alternate": recipe.get("is_alternate", False),
                "building": building["display_name"],
                "items_per_minute_per_building": round(items_per_minute, 3),
                "production_duration_seconds": duration,
                "ingredients": [
                    {
                        "item_class": ing["item_class"],
                        "amount": ing["amount"]
                    } for ing in ingredients
                ],
                "product_amount": product_amount,
                "resource_efficiency": round(efficiency, 3),
                "power_per_building_mw": power_per_building,
                "power_per_item_mw": round(power_per_item, 6)
            }
            comparisons.append(comparison)
        
        return {
            "item": item["display_name"],
            "recipes_count": len(comparisons),
            "recipes": comparisons
        }
    
    def calculate_miner_output(self, resource_name: str, miner_mk: int, purity: str = "normal", overclock_percentage: float = 100.0) -> Dict:
        miners = self.parser.extract_miners()
        miner = next((m for m in miners if m["mk"] == miner_mk), None)
        
        if not miner:
            return {"error": f"Miner Mk.{miner_mk} not found"}
        
        purity_multipliers = {"impure": 0.5, "normal": 1.0, "pure": 2.0}
        multiplier = purity_multipliers.get(purity.lower(), 1.0)
        
        overclock_multiplier = overclock_percentage / 100.0
        base_extraction_rate = (60.0 / miner["extract_cycle_time"]) * miner["items_per_cycle"]
        
        effective_rate = base_extraction_rate * multiplier * overclock_multiplier
        
        power = miner["power_consumption"]
        if overclock_percentage != 100.0:
            exponent = miner.get("power_consumption_exponent", 1.321929)
            power = power * ((overclock_percentage / 100.0) ** exponent)
        
        return {
            "resource": resource_name,
            "miner_mk": miner_mk,
            "purity": purity,
            "overclock_percentage": overclock_percentage,
            "base_extraction_rate_per_minute": round(base_extraction_rate, 3),
            "effective_extraction_rate_per_minute": round(effective_rate, 3),
            "effective_extraction_rate_per_hour": round(effective_rate * 60, 3),
            "power_consumption_mw": round(power, 3)
        }
    
    def calculate_belt_requirements(self, throughput_per_minute: float) -> Dict:
        belts = self.parser.extract_belts()
        suitable_belts = []
        
        for belt in belts:
            if belt["speed"] >= throughput_per_minute:
                suitable_belts.append({
                    "mk": belt["mk"],
                    "display_name": belt["display_name"],
                    "speed_per_minute": belt["speed"],
                    "utilization_percentage": round((throughput_per_minute / belt["speed"]) * 100, 2),
                    "headroom": round(belt["speed"] - throughput_per_minute, 2)
                })
        
        suitable_belts.sort(key=lambda x: x["speed_per_minute"])
        
        if not suitable_belts:
            return {"error": f"No belt can handle {throughput_per_minute} items/minute"}
        
        return {
            "required_throughput_per_minute": throughput_per_minute,
            "recommended_belt": suitable_belts[0],
            "all_suitable_belts": suitable_belts
        }
    
    def calculate_perfect_ratios(self, item_name: str, target_rate: float, include_alternates: bool = True, preferred_recipe: Optional[str] = None, allow_overclock: bool = True) -> Dict:
        """
        Calculate perfect building ratios for 100% efficiency.
        Uses exact decimal building counts and optional overclocking to achieve perfect ratios.
        """
        item = self._find_item_by_name(item_name)
        if not item:
            return {"error": f"Item '{item_name}' not found"}
        
        result = {
            "target_item": item["display_name"],
            "target_rate": target_rate,
            "allow_overclock": allow_overclock,
            "total_power_mw": 0.0,
            "overall_efficiency_percentage": 100.0,
            "buildings": [],
            "steps": [],
            "raw_resources": {}
        }
        
        processed_items = set()
        building_counts = {}
        
        def process_item_for_perfect_ratio(item_class_or_name: str, required_rate: float, depth: int = 0):
            if depth > 20:
                return
            
            item_obj = self._find_item_by_name(item_class_or_name)
            if not item_obj:
                item_class = item_class_or_name
            else:
                item_class = item_obj["class_name"]
            
            if item_class in processed_items:
                return
            processed_items.add(item_class)
            
            recipes = self._find_recipe_by_product(item_class, include_alternates)
            if not recipes:
                raw_resource = self._find_item_by_name(item_class_or_name)
                if raw_resource and raw_resource.get("item_type") == "raw_resource":
                    if raw_resource["display_name"] not in result["raw_resources"]:
                        result["raw_resources"][raw_resource["display_name"]] = 0.0
                    result["raw_resources"][raw_resource["display_name"]] += required_rate
                return
            
            recipe = None
            if preferred_recipe:
                for r in recipes:
                    if r["class_name"] == preferred_recipe or r["display_name"].lower() == preferred_recipe.lower():
                        recipe = r
                        break
            
            if not recipe:
                recipe = recipes[0]
            
            produced_in = recipe.get("produced_in", [])
            if not produced_in:
                return
            building_type = produced_in[0]
            
            duration = recipe["manufacturing_duration"]
            products = recipe.get("products", [])
            if not products:
                return
            
            product_amount = products[0]["amount"]
            base_items_per_minute = (60.0 / duration) * product_amount
            
            buildings = self._get_buildings()
            building = None
            for b in buildings:
                if building_type.lower() in b["building_type"].lower() or b["building_type"].lower() in building_type.lower():
                    building = b
                    break
            
            if not building:
                building_type_clean = building_type.replace("Mk1", "").replace("Mk", "").replace("_C", "").replace("Build_", "")
                building = next((b for b in buildings if b["building_type"].lower() == building_type_clean.lower()), None)
            
            if not building:
                return
            
            exact_buildings_needed = required_rate / base_items_per_minute
            optimal_overclock = 100.0
            
            if allow_overclock and exact_buildings_needed < 1.0:
                optimal_overclock = min(250.0, (1.0 / exact_buildings_needed) * 100.0)
                exact_buildings_needed = 1.0
            elif allow_overclock and exact_buildings_needed > 1.0:
                whole_buildings = int(exact_buildings_needed)
                fractional = exact_buildings_needed - whole_buildings
                if fractional > 0.001:
                    remaining_rate = fractional * base_items_per_minute
                    needed_for_remaining = remaining_rate / base_items_per_minute
                    if needed_for_remaining < 0.4:
                        overclock_needed = (1.0 / needed_for_remaining) * 100.0
                        if overclock_needed <= 250.0:
                            exact_buildings_needed = whole_buildings + 1
                            optimal_overclock = overclock_needed
            
            if optimal_overclock > 100.0:
                effective_rate_per_building = base_items_per_minute * (optimal_overclock / 100.0)
                exact_buildings_needed = required_rate / effective_rate_per_building
            else:
                effective_rate_per_building = base_items_per_minute
            
            building_key = building["display_name"]
            if building_key not in building_counts:
                building_counts[building_key] = {
                    "building": building["display_name"],
                    "exact_count": 0.0,
                    "rounded_count": 0,
                    "overclock_percentage": 100.0,
                    "total_power_mw": 0.0,
                    "production_rate_per_building": effective_rate_per_building
                }
            
            building_counts[building_key]["exact_count"] += exact_buildings_needed
            
            power_per_building = building["power_consumption"]
            power_exponent = building.get("power_consumption_exponent", 1.321929)
            if optimal_overclock > 100.0:
                power_per_building = power_per_building * ((optimal_overclock / 100.0) ** power_exponent)
            
            total_power_for_step = exact_buildings_needed * power_per_building
            result["total_power_mw"] += total_power_for_step
            building_counts[building_key]["total_power_mw"] += total_power_for_step
            
            step = {
                "item": item_obj["display_name"] if item_obj else item_class_or_name,
                "recipe": recipe["display_name"],
                "is_alternate": recipe.get("is_alternate", False),
                "building": building["display_name"],
                "exact_buildings_needed": round(exact_buildings_needed, 6),
                "optimal_overclock_percentage": round(optimal_overclock, 2),
                "production_rate_per_building": round(effective_rate_per_building, 6),
                "target_production_rate": round(required_rate, 6),
                "actual_production_rate": round(exact_buildings_needed * effective_rate_per_building, 6),
                "efficiency_percentage": round(min(100.0, (required_rate / (exact_buildings_needed * effective_rate_per_building)) * 100.0), 4),
                "power_per_building_mw": round(power_per_building, 3),
                "total_power_mw": round(total_power_for_step, 6),
                "ingredients": []
            }
            
            ingredients = recipe.get("ingredients", [])
            for ingredient in ingredients:
                ingredient_rate = (required_rate / product_amount) * ingredient["amount"]
                step["ingredients"].append({
                    "item_class": ingredient["item_class"],
                    "amount_per_cycle": ingredient["amount"],
                    "required_rate_per_minute": round(ingredient_rate, 6)
                })
                process_item_for_perfect_ratio(ingredient["item_class"], ingredient_rate, depth + 1)
            
            result["steps"].append(step)
        
        process_item_for_perfect_ratio(item_name, target_rate)
        
        for building_key, building_info in building_counts.items():
            building_info["rounded_count"] = round(building_info["exact_count"])
            result["buildings"].append(building_info)
        
        result["total_power_mw"] = round(result["total_power_mw"], 6)
        
        return result
    
    def optimize_for_100_percent_efficiency(self, item_name: str, target_rate: float, include_alternates: bool = True, preferred_recipe: Optional[str] = None, allow_overclock: bool = True) -> Dict:
        """
        Optimize production chain for 100% efficiency.
        Returns configuration with perfect ratios, optimal overclocking, and efficiency analysis.
        """
        perfect_ratios = self.calculate_perfect_ratios(item_name, target_rate, include_alternates, preferred_recipe, allow_overclock)
        
        if "error" in perfect_ratios:
            return perfect_ratios
        
        efficiency_analysis = {
            "overall_efficiency_percentage": 100.0,
            "building_efficiency": [],
            "bottlenecks": [],
            "optimization_recommendations": [],
            "waste_analysis": {
                "has_waste": False,
                "wasted_resources": []
            }
        }
        
        for step in perfect_ratios["steps"]:
            efficiency = step.get("efficiency_percentage", 100.0)
            building_eff = {
                "building": step["building"],
                "item": step["item"],
                "efficiency_percentage": efficiency,
                "utilization_percentage": efficiency,
                "is_bottleneck": efficiency < 99.0,
                "production_rate": step["actual_production_rate"],
                "target_rate": step["target_production_rate"]
            }
            
            efficiency_analysis["building_efficiency"].append(building_eff)
            
            if efficiency < 99.0:
                efficiency_analysis["bottlenecks"].append({
                    "building": step["building"],
                    "item": step["item"],
                    "efficiency": efficiency,
                    "issue": f"Building producing {step['item']} at {efficiency:.2f}% efficiency",
                    "recommendation": f"Adjust overclocking or building count to reach 100%"
                })
        
        if len(efficiency_analysis["bottlenecks"]) == 0:
            efficiency_analysis["optimization_recommendations"].append("All buildings operating at 100% efficiency")
        
        result = {
            **perfect_ratios,
            "efficiency_analysis": efficiency_analysis,
            "is_100_percent_efficient": len(efficiency_analysis["bottlenecks"]) == 0
        }
        
        return result
    
    def calculate_factory_efficiency(self, item_name: str, target_rate: float, include_alternates: bool = True, preferred_recipe: Optional[str] = None, allow_overclock: bool = True) -> Dict:
        """
        Calculate comprehensive factory efficiency metrics.
        Includes building utilization, belt utilization, bottlenecks, and waste analysis.
        """
        optimized = self.optimize_for_100_percent_efficiency(item_name, target_rate, include_alternates, preferred_recipe, allow_overclock)
        
        if "error" in optimized:
            return optimized
        
        belts = self.parser.extract_belts()
        belt_utilization = []
        
        for step in optimized["steps"]:
            throughput = step["actual_production_rate"]
            suitable_belts = [b for b in belts if b["speed"] >= throughput]
            
            if suitable_belts:
                recommended_belt = suitable_belts[0]
                utilization = (throughput / recommended_belt["speed"]) * 100.0
                
                belt_utilization.append({
                    "step": step["item"],
                    "throughput_per_minute": round(throughput, 3),
                    "recommended_belt_mk": recommended_belt["mk"],
                    "belt_speed": recommended_belt["speed"],
                    "utilization_percentage": round(utilization, 2),
                    "is_optimal": 95.0 <= utilization <= 100.0
                })
        
        building_utilization_summary = {}
        for building_info in optimized["buildings"]:
            building_utilization_summary[building_info["building"]] = {
                "exact_count": building_info["exact_count"],
                "rounded_count": building_info["rounded_count"],
                "utilization_efficiency": round((building_info["exact_count"] / building_info["rounded_count"]) * 100.0, 2) if building_info["rounded_count"] > 0 else 100.0
            }
        
        overall_efficiency = optimized["efficiency_analysis"]["overall_efficiency_percentage"]
        avg_building_efficiency = sum([b["efficiency_percentage"] for b in optimized["efficiency_analysis"]["building_efficiency"]]) / len(optimized["efficiency_analysis"]["building_efficiency"]) if optimized["efficiency_analysis"]["building_efficiency"] else 100.0
        avg_belt_efficiency = sum([b["utilization_percentage"] for b in belt_utilization]) / len(belt_utilization) if belt_utilization else 100.0
        
        return {
            "target_item": optimized["target_item"],
            "target_rate": optimized["target_rate"],
            "overall_efficiency_percentage": round(overall_efficiency, 2),
            "average_building_efficiency": round(avg_building_efficiency, 2),
            "average_belt_efficiency": round(avg_belt_efficiency, 2),
            "is_100_percent_efficient": optimized["is_100_percent_efficient"],
            "total_power_mw": optimized["total_power_mw"],
            "building_utilization": building_utilization_summary,
            "belt_utilization": belt_utilization,
            "bottlenecks": optimized["efficiency_analysis"]["bottlenecks"],
            "waste_analysis": optimized["efficiency_analysis"]["waste_analysis"],
            "optimization_recommendations": optimized["efficiency_analysis"]["optimization_recommendations"],
            "detailed_steps": optimized["steps"]
        }
    
    def calculate_building_utilization(self, item_name: str, target_rate: float, include_alternates: bool = True, preferred_recipe: Optional[str] = None) -> Dict:
        """
        Calculate per-building utilization percentages.
        Identifies under-utilized and over-utilized buildings.
        """
        chain = self.calculate_production_chain(item_name, target_rate, include_alternates, preferred_recipe)
        
        if "error" in chain:
            return chain
        
        utilization_analysis = {
            "target_item": chain["target_item"],
            "target_rate": chain["target_rate"],
            "buildings": {},
            "under_utilized": [],
            "over_utilized": [],
            "optimally_utilized": []
        }
        
        for step in chain["steps"]:
            building_name = step["building"]
            buildings_needed = step["buildings_needed"]
            buildings_rounded = step.get("buildings_needed_rounded", round(buildings_needed))
            
            if buildings_rounded == 0:
                utilization_percentage = 0.0
            else:
                utilization_percentage = (buildings_needed / buildings_rounded) * 100.0 if buildings_rounded > 0 else 0.0
            
            building_data = {
                "building": building_name,
                "item": step["item"],
                "recipe": step["recipe"],
                "exact_buildings_needed": round(buildings_needed, 6),
                "rounded_buildings_used": buildings_rounded,
                "utilization_percentage": round(utilization_percentage, 2),
                "production_rate_per_building": step["production_rate_per_building"],
                "target_rate": step["target_production_rate"],
                "actual_rate": round(buildings_rounded * step["production_rate_per_building"], 3),
                "efficiency_gap": round(abs(step["target_production_rate"] - (buildings_rounded * step["production_rate_per_building"])), 3)
            }
            
            if building_name not in utilization_analysis["buildings"]:
                utilization_analysis["buildings"][building_name] = []
            
            utilization_analysis["buildings"][building_name].append(building_data)
            
            if utilization_percentage < 90.0:
                utilization_analysis["under_utilized"].append(building_data)
            elif utilization_percentage > 100.0:
                utilization_analysis["over_utilized"].append(building_data)
            else:
                utilization_analysis["optimally_utilized"].append(building_data)
        
        return utilization_analysis

