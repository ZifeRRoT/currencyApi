import app.exchanges.sechemas as schemas
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date as data

from models import *
from sqlalchemy import select
from database import get_session


router = APIRouter()


async def token_verify(token: str, session: AsyncSession = Depends(get_session)):
    token = await session.execute(select(Account).filter_by(api_key=token))
    token = token.scalar()
    if token:
        if token.is_active:
            return True
    return False


@router.get('/{token}', response_model=list[schemas.Exchange])
async def get(
        token: str = Depends(token_verify),
        date: data = None,
        code: str = None,
        mfo: int = None,
        bank_name: bool = False,
        session: AsyncSession = Depends(get_session)
):
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid API key')
    if not date:
        date = data.today()
    request = select(ExchangeRates).filter(ExchangeRates.date == date)
    if mfo:
        request = request.join(BankList).filter(BankList.mfo == mfo)
    if code:
        request = request.join(Currency).filter(Currency.code == code)

    currencies = await session.execute(request)
    currencies = currencies.scalars().all()
    if not currencies:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    new_list = [schemas.Exchange(
        bank=x.bank.name if bank_name==True else x.bank.mfo,
        currency=x.currency.code,
        purchase=x.purchase,
        sale=x.sale,
        date=x.date
    ) for x in currencies]
    return new_list
