from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from inventory.config import config


engine = create_engine(config.database_url)

# Session = sessionmaker(engine)


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session