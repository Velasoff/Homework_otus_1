import logging
from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.deps import get_db

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/login", response_model=schemas.Items)
async def login(db: AsyncSession = Depends(get_db)) -> Any:
    items = await models.Item.filter(db, prefetch=("parts", "categories"))
    return {"items": items}


@router.post("/user/register", response_model=schemas.Item)
async def register(items_id: PositiveInt, db: AsyncSession = Depends(get_db)) -> Any:
    item = await models.Item.get_by_id(db, items_id, prefetch=("parts", "categories"))
    if item is None:
        raise ResourceNotFoundError
    return item
