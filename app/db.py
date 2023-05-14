from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.config import settings


engine = create_engine(settings.DB_DSN)
session = sessionmaker(engine, expire_on_commit=False, class_=Session, future=True, autoflush=False)
