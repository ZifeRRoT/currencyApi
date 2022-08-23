import app.users.schemas as schemas
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from models import Account
from sqlalchemy import select
from database import get_session


router = APIRouter()


@router.post('/create')
async def create_user(user: schemas.UserCreate, session: AsyncSession = Depends(get_session)):
    session.add(Account(**user.dict()))
    await session.commit()


@router.get('/get_all', response_model=list[schemas.User])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    users = await session.execute(select(Account))
    return users.scalars().all()
