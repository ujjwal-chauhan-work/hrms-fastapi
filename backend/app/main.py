from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.api.v1.api import router as api_v1_router
from app.core.config import get_settings
from app.core.logging import get_logger, setup_logging
from app.db.session import engine

settings = get_settings()
setup_logging()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    App startup/shutdown lifecycle.
    We'll later add things here like: cache warmups, job schedulers, etc.
    """
    logger.info("Starting HRMS API (%s)", settings.environment)
    yield
    logger.info("Shutting down HRMS API")


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    lifespan=lifespan,
)

# API versioning
app.include_router(api_v1_router, prefix="/api/v1")


@app.get("/health")
def health():
    logger.info("Health check requested")
    return {"status": "ok", "service": settings.app_name, "env": settings.environment}


@app.get("/health/db")
async def health_db():
    """
    Verifies DB connectivity without needing any models yet.
    """
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        value = result.scalar_one()
    return {"db": "ok", "result": value}
