from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # -------------------------
    # App
    # -------------------------
    app_name: str = Field(..., validation_alias="APP_NAME")
    environment: str = Field(..., validation_alias="ENVIRONMENT")
    debug: bool = Field(default=False, validation_alias="DEBUG")

    # -------------------------
    # Security
    # -------------------------
    jwt_secret_key: str = Field(..., validation_alias="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(default="HS256", validation_alias="JWT_ALGORITHM")
    access_token_expire_minutes: int = Field(
        default=30, validation_alias="ACCESS_TOKEN_EXPIRE_MINUTES"
    )
    refresh_token_expire_days: int = Field(
        default=7, validation_alias="REFRESH_TOKEN_EXPIRE_DAYS"
    )

    # -------------------------
    # Database
    # -------------------------
    postgres_user: str = Field(..., validation_alias="POSTGRES_USER")
    postgres_password: str = Field(..., validation_alias="POSTGRES_PASSWORD")
    postgres_db: str = Field(..., validation_alias="POSTGRES_DB")
    postgres_host: str = Field(..., validation_alias="POSTGRES_HOST")
    postgres_port: int = Field(default=5432, validation_alias="POSTGRES_PORT")

    # -------------------------
    # Redis
    # -------------------------
    redis_host: str = Field(..., validation_alias="REDIS_HOST")
    redis_port: int = Field(default=6379, validation_alias="REDIS_PORT")

    # -------------------------
    # Logging
    # -------------------------
    log_level: str = Field(default="INFO", validation_alias="LOG_LEVEL")

    # -------------------------
    # Pydantic Settings Config
    # -------------------------
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.postgres_user}:"
            f"{self.postgres_password}@"
            f"{self.postgres_host}:"
            f"{self.postgres_port}/"
            f"{self.postgres_db}"
        )

    @property
    def redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}"


@lru_cache
def get_settings() -> Settings:
    """
    Cached settings object.
    Ensures env is read once per process.
    """
    return Settings() # type: ignore[call-arg]  # type: ignore[arg-type]
