from pydantic import BaseSettings


class Config(BaseSettings):
    database_url: str

    class Config:
        env_file = ".env"


config = Config()  # type: ignore
