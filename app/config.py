from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_host_name: str = "localhost"
    database_port: str = "5432"
    database_password: str = "postgres"
    database_name: str = "fastapi"
    database_username: str = "postgres"
    secret_key: str = "secret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()

