from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "My FastAPI Project"
    secret_key: str = "supersecretkey"
    
    # Database settings
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str
    
    # Using the new SettingsConfigDict for configuration
    model_config = SettingsConfigDict(env_file=".env")
    
    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


settings = Settings()
