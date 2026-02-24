#!/bin/bash
PORT=${PORT:-8000}
uvicorn src.api.main:app --reload --host 0.0.0.0 --port "$PORT"

