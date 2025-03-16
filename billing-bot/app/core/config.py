from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My FastAPI Project"
    database_url: str
    secret_key: str = "supersecretkey"

    class Config:
        env_file = ".env"

    @property
    def sqlmodel_database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str

settings = Settings()
settings.database_url = settings.sqlmodel_database_url