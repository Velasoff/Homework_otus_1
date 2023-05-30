import logging
from typing import Any

from fastapi import APIRouter, HTTPException

from app.crud.auth import get_token, get_user, register_user, search_user_by_names
from app.schemas import ListUserSchema, LoginSchema, TokenSchema, UserRegisterSchema, UserSchema

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/login", response_model=TokenSchema)
def login(login_data: LoginSchema) -> Any:
    token = get_token(**login_data.dict())
    if token is not None:
        return token
    raise HTTPException(status_code=400, detail="Невалидные данные")


@router.post("/user/register", response_model=UserSchema)
def register(user_data: UserRegisterSchema) -> Any:
    result = register_user(user_data)
    return result


@router.get("/user/get/{id}", response_model=UserSchema)
def register(id: int) -> Any:
    result = get_user(id)
    return result


@router.get("/user/search", response_model=ListUserSchema)
def search_user(first_name: str, last_name: str):
    result = search_user_by_names(first_name, last_name)
    return result
