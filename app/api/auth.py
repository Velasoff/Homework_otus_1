import logging
from typing import Any

from fastapi import APIRouter, HTTPException

from app.crud.auth import register_user, get_user, get_token
from app.schemas import UserSchema, UserRegisterSchema, LoginSchema, TokenSchema

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
