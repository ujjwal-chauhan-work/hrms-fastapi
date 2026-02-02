import logging
import sys
from typing import Optional
from app.core.config import get_settings

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging(log_level: Optional[str] = None) -> None:
    """
    Configure global logging for the application.

    - Uses stdout (container-friendly)
    - Controls log level via env (LOG_LEVEL)
    - Avoids duplicate handlers on reloads
    """
    settings = get_settings()
    level_name = (log_level or settings.log_level or "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)

    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    for h in list(root_logger.handlers):
        root_logger.removeHandler(h)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)

    formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=_DATE_FORMAT)
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)

    for logger_name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        logger = logging.getLogger(logger_name)
        logger.handlers = []
        logger.propagate = True
        logger.setLevel(level)


def get_logger(name: str) -> logging.Logger:
    """
    Get a module logger.
    """
    return logging.getLogger(name)
