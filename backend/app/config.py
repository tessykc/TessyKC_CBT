from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "CBT Examination Platform"
    app_env: str = "development"

    secret_key: str = "change-this-secret-key"

    access_token_expire_minutes: int = 60

    database_url: str = (
        "postgresql+psycopg://cbt_user:password@localhost:5432/CBT_EXAM"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()