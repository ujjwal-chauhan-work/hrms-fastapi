from fastapi import FastAPI

from app.core.config import get_settings
from app.core.logging import setup_logging, get_logger

settings = get_settings()
setup_logging()

logger = get_logger(__name__)

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)


@app.get("/health")
def health():
    logger.info("Health check requested")
    return {"status": "ok", "service": settings.app_name, "env": settings.environment}
