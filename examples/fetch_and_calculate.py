#!/usr/bin/env python3
"""
Example: call the Satisfactory API (live or local) to fetch alternate recipes
and compute how many buildings are needed for a target production rate.

Usage:
  python3 examples/fetch_and_calculate.py
  python3 examples/fetch_and_calculate.py --base-url http://localhost:8000

Requires: pip install httpx
"""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Fetch alternate recipes and run a buildings-needed calculation")
    parser.add_argument(
        "--base-url",
        default="https://satisfactory-api-yfw1.onrender.com",
        help="API base URL (default: live instance)",
    )
    args = parser.parse_args()
    base = args.base_url.rstrip("/")

    try:
        import httpx
    except ImportError:
        print("This example requires httpx. Run: pip install httpx", file=sys.stderr)
        sys.exit(1)

    with httpx.Client(timeout=30.0) as client:
        r = client.get(f"{base}/recipes", params={"alternate_only": True, "limit": 3})
        r.raise_for_status()
        recipes = r.json()
        print(f"Fetched {len(recipes)} alternate recipe(s). Examples: {[x.get('display_name') or x.get('displayName') for x in recipes[:3]]}")

        r2 = client.get(
            f"{base}/calculate/buildings-needed",
            params={"recipe": "Iron Ingot", "target_rate": 60},
        )
        r2.raise_for_status()
        data = r2.json()
        print(f"Buildings needed for 60 Iron Ingot/min: {data}")


if __name__ == "__main__":
    main()
