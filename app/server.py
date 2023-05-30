import logging

from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.config import settings

logger = logging.getLogger(__name__)


app = FastAPI(
    title=settings.SERVICE_NAME,
    root_path=settings.ROOT_PATH,
    debug=settings.DEBUG,
)

app.include_router(auth_router)
