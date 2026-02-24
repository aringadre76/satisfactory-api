import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pathlib import Path
from datetime import datetime, timezone
from src.api.routers import miners, belts, resources, recipes, buildings, items, calculations, transportation, power, logistics, extractors, progression, planning_context
from src.parsers.game_descriptor_parser import GameDescriptorParser

app = FastAPI(
    title="Satisfactory Game Data API",
    description="REST API providing structured game data for Satisfactory factory planning tools",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(miners.router, prefix="/miners", tags=["miners"])
app.include_router(belts.router, prefix="/belts", tags=["belts"])
app.include_router(resources.router, prefix="", tags=["resources"])
app.include_router(recipes.router, prefix="/recipes", tags=["recipes"])
app.include_router(buildings.router, prefix="/buildings", tags=["buildings"])
app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(calculations.router, prefix="/calculate", tags=["calculations"])
app.include_router(transportation.router, prefix="/transportation", tags=["transportation"])
app.include_router(power.router, prefix="/power", tags=["power"])
app.include_router(logistics.router, prefix="/logistics", tags=["logistics"])
app.include_router(extractors.router, prefix="/extractors", tags=["extractors"])
app.include_router(progression.router, prefix="/progression", tags=["progression"])
app.include_router(planning_context.router, prefix="/planning-context", tags=["planning-context"])

DESCRIPTOR_FILE = Path(__file__).resolve().parent.parent.parent / "Docs" / "en-US.json"

@app.get("/")
async def root():
    base_url = os.environ.get("BASE_URL", "").rstrip("/")
    out = {
        "message": "Satisfactory Game Data API",
        "version": "1.0.0",
        "docs": "/docs",
        "openapi": "/openapi.json",
    }
    if base_url:
        out["base_url"] = base_url
    return out

@app.get("/health")
async def health():
    return {"status": "ok"}

def _game_data_meta():
    if not DESCRIPTOR_FILE.exists():
        return {"api_version": "1.0.0", "game_data_source": "descriptor", "game_data_last_updated": None, "overclock": {"min": 1, "max": 250, "presets": [100, 125, 150, 200, 250]}}
    mtime = DESCRIPTOR_FILE.stat().st_mtime
    dt = datetime.fromtimestamp(mtime, tz=timezone.utc)
    return {
        "api_version": "1.0.0",
        "game_data_source": "descriptor",
        "game_data_last_updated": dt.isoformat().replace("+00:00", "Z"),
        "overclock": {"min": 1, "max": 250, "presets": [100, 125, 150, 200, 250]},
    }

@app.get("/meta")
async def meta():
    data = _game_data_meta()
    if data["game_data_last_updated"] is None:
        return JSONResponse(status_code=200, content=data)
    resp = JSONResponse(status_code=200, content=data)
    resp.headers["X-Game-Data-Last-Updated"] = data["game_data_last_updated"]
    return resp

@app.get("/version")
async def version():
    return _game_data_meta()

@app.get("/ready")
async def ready():
    if not DESCRIPTOR_FILE.exists():
        return JSONResponse(
            status_code=503,
            content={"status": "not ready", "detail": "Game descriptor file not found"}
        )
    try:
        GameDescriptorParser(DESCRIPTOR_FILE)
        return {"status": "ready"}
    except Exception as e:
        return JSONResponse(
            status_code=503,
            content={"status": "not ready", "detail": str(e)}
        )


def run():
    import uvicorn
    import os
    port = int(os.environ.get("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
