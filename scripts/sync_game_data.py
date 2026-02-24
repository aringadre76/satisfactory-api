#!/usr/bin/env python3
"""
Copy Satisfactory game descriptor JSON files into project Docs/ so the API
uses current game data (miner mk, belt speeds, recipes, etc.).

Default source: Satisfactory CommunityResources (or game install) path.
Override with SATISFACTORY_SOURCE env or first CLI argument.
"""
import argparse
import os
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = PROJECT_ROOT / "Docs"

DEFAULT_SOURCE_WIN = r"C:\Program Files (x86)\Steam\steamapps\common\Satisfactory\CommunityResources"
DEFAULT_SOURCE_WSL = "/mnt/c/Program Files (x86)/Steam/steamapps/common/Satisfactory/CommunityResources"


def find_source_dir(env_path=None, cli_path=None):
    if cli_path:
        p = Path(cli_path)
        return p if p.is_dir() else None
    if env_path:
        p = Path(env_path)
        if p.is_dir():
            return p
    for candidate in (DEFAULT_SOURCE_WSL, Path(DEFAULT_SOURCE_WIN)):
        if Path(candidate).is_dir():
            return Path(candidate)
    return None


def collect_json_files(source):
    out = []
    if (source / "Docs").is_dir():
        for f in (source / "Docs").iterdir():
            if f.suffix.lower() == ".json":
                out.append(f)
    for f in source.iterdir():
        if f.is_file() and f.suffix.lower() == ".json":
            out.append(f)
    return sorted(out)


def main():
    parser = argparse.ArgumentParser(
        description="Sync Satisfactory game descriptor JSON into project Docs/"
    )
    parser.add_argument(
        "source",
        nargs="?",
        default=None,
        help="Source directory (default: CommunityResources or env SATISFACTORY_SOURCE)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only print what would be copied",
    )
    args = parser.parse_args()
    source_dir = find_source_dir(cli_path=args.source)
    if not source_dir and os.environ.get("SATISFACTORY_SOURCE"):
        source_dir = find_source_dir(env_path=os.environ["SATISFACTORY_SOURCE"])
    if not source_dir:
        print("No source directory found.", file=sys.stderr)
        print("Set SATISFACTORY_SOURCE or pass the path, e.g.:", file=sys.stderr)
        print('  python3 scripts/sync_game_data.py "C:\\...\\Satisfactory\\CommunityResources"', file=sys.stderr)
        print("  python3 scripts/sync_game_data.py \"/mnt/c/Program Files (x86)/Steam/.../CommunityResources\"", file=sys.stderr)
        return 1
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    files = collect_json_files(source_dir)
    if not files:
        print("No JSON files under {}".format(source_dir), file=sys.stderr)
        return 1
    for src in files:
        dest = DOCS_DIR / src.name
        if args.dry_run:
            print("Would copy: {} -> {}".format(src, dest))
        else:
            shutil.copy2(src, dest)
            print("Copied: {} -> Docs/".format(src.name))
    if not args.dry_run:
        print("Done. {} file(s) in Docs/. Run: python3 scripts/verify_data.py".format(len(files)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
