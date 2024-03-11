from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from db.db_setup import SQLALCHEMY_DATABASE_URL
from db.models import User

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/")
async def root():
    stmt = select(User).where(User.name == "one")
    print(stmt)
    with engine.connect() as conn:
        for row in conn.execute(stmt):
            print(row)
    return {"message": "Hello World"}
