import datetime
from enum import Enum

from pydantic import BaseModel


class SexEnum(str, Enum):
    female = "F"
    male = "M"


class BaseSchema(BaseModel):
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
