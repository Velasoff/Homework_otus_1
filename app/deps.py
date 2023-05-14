from app.db import session


def get_db():
    db = session()
    try:
        yield db
    finally:
        await db.close()
