import logging

from fastapi import FastAPI

from app.config import settings
from app.api.auth import router as auth_router

logger = logging.getLogger(__name__)


application = FastAPI(
        title=settings.SERVICE_NAME,
        root_path=settings.ROOT_PATH,
        debug=settings.DEBUG,
    )

application.include_router(auth_router)
