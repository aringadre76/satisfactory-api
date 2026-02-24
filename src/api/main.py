from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pathlib import Path
from src.api.routers import miners, belts, resources, recipes, buildings, items, calculations, transportation, power, logistics, extractors, progression
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

DESCRIPTOR_FILE = Path(__file__).resolve().parent.parent.parent / "Docs" / "en-US.json"

@app.get("/")
async def root():
    return {
        "message": "Satisfactory Game Data API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health():
    return {"status": "ok"}

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
