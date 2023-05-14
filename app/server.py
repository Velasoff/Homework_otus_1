import logging

from fastapi import FastAPI

from app.config import settings

logger = logging.getLogger(__name__)


application = FastAPI(
        title=settings.SERVICE_NAME,
        root_path=settings.ROOT_PATH,
        debug=settings.DEBUG,
    )
