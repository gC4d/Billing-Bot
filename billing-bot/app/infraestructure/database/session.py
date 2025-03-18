from sqlmodel import Session, SQLModel, create_engine
from app.core.config import settings

engine = create_engine(settings.sqlmodel_database_url, connect_args={"check_same_thread": False})

def get_db():
    """
    Yields a database session.

    This function creates a new SQLModel session using the provided engine and yields it.
    It ensures that the session is properly closed after use.
    """
    with Session(engine) as session:
        yield session

SQLModel.metadata.create_all(engine)
