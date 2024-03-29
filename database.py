import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


load_dotenv()
db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")
db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")

DATABASE_URL = f"postgresql+asyncpg://{db_user}:{db_pass}@{db_host}/{db_name}"

engine = create_async_engine(DATABASE_URL, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False, autoflush=False)


async def get_session():
    try:
        async with async_session() as session:
            yield session
    except:
        await session.rollback()
        raise
    finally:
        await session.close()
