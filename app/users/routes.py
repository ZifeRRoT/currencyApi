import app.users.schemas as schemas
import models

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from app.users.auth.router import router as auth, get_hashed_password


router = APIRouter()
router.include_router(auth, prefix="/auth", tags=["Auth"])


@router.post('/signup')
async def signup(data: schemas.UserCreate, session: AsyncSession = Depends(get_session)):
    user = await session.execute(select(models.Account).filter(models.Account.email.ilike(data.email)))
    if user.scalar():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User with this email already exist"
                            )
    data.password = await get_hashed_password(data.password)
    session.add(models.Account(**data.dict()))
    user = await session.commit()
    return user


@router.get('/signin')
async def signin():
    pass


@router.get('/get_all', response_model=list[schemas.UserOut])
async def get_all_users(session: AsyncSession = Depends(get_session)):
    users = await session.execute(select(models.Account))
    return users.scalars().all()
