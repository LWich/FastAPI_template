from functools import lru_cache

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import async_sessionmaker

import config


@lru_cache
def get_session_maker() -> async_sessionmaker:
    engine = create_async_engine(config.get_postgres_url())
    return async_sessionmaker(engine)


async def get_session():
    cached_sessionmaker = get_session_maker()
    async with cached_sessionmaker.begin() as session:
        yield session


class Base(DeclarativeBase):
    ...
    