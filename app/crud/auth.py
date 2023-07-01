import datetime
from uuid import uuid4

from fastapi import HTTPException
from sqlalchemy import text

from app.db import engine
from app.schemas import (ListUserSchema, TokenSchema, UserRegisterSchema,
                         UserSchema)


def get_token(id: int, password: str) -> TokenSchema | None:
    user_query = text("SELECT * FROM users WHERE id = :id")
    query = text(
        """
        INSERT INTO tokens (user_id, token, expired_at)
        SELECT :id, :token, :expired_at
        WHERE (SELECT (password = crypt(:password, password)) AS pswmatch FROM users WHERE id = :id)
        RETURNING token
    """
    )
    with engine.connect() as conn:
        result = conn.execute(user_query, {"id": id})
        if result.one_or_none() is None:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        result = conn.execute(
            query,
            {
                "id": id,
                "password": password,
                "token": uuid4(),
                "expired_at": (datetime.datetime.now() + datetime.timedelta(hours=3)).isoformat(),
            },
        )
        if (token_data := result.one_or_none()) is not None:
            return TokenSchema.from_orm(token_data)
    return None


def register_user(user_data: UserRegisterSchema) -> UserSchema:
    query = text(
        """
        INSERT INTO users (password, first_name, second_name, birthday, age, sex, biography, city)
        VALUES (crypt(:password, gen_salt('md5')), :first_name, :second_name, :birthday, :age, :sex, :biography, :city)
        RETURNING id, first_name, second_name, birthday, age, sex, biography, city
    """
    )
    with engine.connect() as conn:
        result = conn.execute(query, user_data.dict())
        conn.commit()
        return UserSchema.from_orm(result.one_or_none())


def get_user(user_id: int) -> UserSchema:
    query = text("SELECT * FROM users WHERE id = :id")
    with engine.connect() as conn:
        result = conn.execute(query, {"id": user_id})
        if (user := result.one_or_none()) is None:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        return UserSchema.from_orm(user)


def search_user_by_names(first_name: str, last_name: str) -> ListUserSchema:
    query = text(
        """
        SELECT id,
               first_name,
               second_name,
               birthday,
               age,
               sex,
               biography,
               city
        FROM users
        WHERE first_name LIKE '%' || :first_name || '%'
          AND second_name LIKE '%' || :second_name || '%'
        ORDER BY id
        """
    )
    with engine.connect() as conn:
        result = conn.execute(query, {"first_name": first_name, "second_name": last_name})
        results = result.all()
        return ListUserSchema(items=[UserSchema.from_orm(row) for row in results])
