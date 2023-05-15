import datetime
from enum import Enum

from fastapi import HTTPException
from pydantic import BaseModel, ValidationError


class SexEnum(str, Enum):
    female = "F"
    male = "M"


class BaseSchema(BaseModel):
    def __init__(self, *args, **kwargs):
        try:
            super().__init__(*args, **kwargs)
        except ValidationError:
            raise HTTPException(status_code=400, detail="Невалидные данные")

    class Config:
        orm_mode = True


class BaseUserSchema(BaseSchema):
    first_name: str
    second_name: str
    birthday: datetime.date
    age: int
    sex: SexEnum
    biography: str | None
    city: str | None


class UserSchema(BaseUserSchema):
    id: int


class UserRegisterSchema(UserSchema):
    password: str


class LoginSchema(BaseModel):
    id: int
    password: str


class TokenSchema(BaseSchema):
    token: str | None
