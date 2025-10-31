from typing import Dict, Optional
import httpx

WIKI_BASE_URL = "https://satisfactory.fandom.com/wiki"

def get_wiki_url(item: str) -> str:
    item_normalized = item.replace(" ", "_").replace(".", "").replace("'", "")
    return f"{WIKI_BASE_URL}/{item_normalized}"

def get_item_wiki_mapping() -> Dict[str, str]:
    common_items = {
        "miner": "Miner",
        "belt": "Conveyor_Belt",
        "iron_ore": "Iron_Ore",
        "copper_ore": "Copper_Ore",
        "coal": "Coal",
        "limestone": "Limestone",
        "sulfur": "Sulfur",
        "quartz": "Raw_Quartz",
        "bauxite": "Bauxite",
        "uranium": "Uranium",
        "oil": "Crude_Oil"
    }
    return {k: get_wiki_url(v) for k, v in common_items.items()}

async def fetch_wiki_page(item: str) -> Optional[Dict]:
    try:
        url = get_wiki_url(item)
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10.0)
            if response.status_code == 200:
                return {
                    "url": url,
                    "status": "available",
                    "content_length": len(response.text)
                }
            else:
                return {
                    "url": url,
                    "status": "not_found",
                    "status_code": response.status_code
                }
    except Exception as e:
        return {
            "url": get_wiki_url(item),
            "status": "error",
            "error": str(e)
        }

