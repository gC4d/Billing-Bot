from sqlmodel import Session, SQLModel, create_engine
from app.core.config import settings

engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})

def get_db():
    with Session(engine) as session:
        yield session

SQLModel.metadata.create_all(engine)
