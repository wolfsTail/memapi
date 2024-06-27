from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "postgresql://user:password@db/memes_db"

    class Config:
        env_file = ".env_example"


settings = Settings()