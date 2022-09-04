from pydantic import BaseModel
from datetime import date


class Bank(BaseModel):
    name: str
    mfo: int | None
    edrpou: int | None
    ipn: int | None
    iban: str | None
    swift: str | None

    class Config:
        orm_mode = True


class Currency(BaseModel):
    code: str
    name: str

    class Config:
        orm_mode = True


class Exchange(BaseModel):
    bank: str
    currency: str
    purchase: float
    sale: float
    date: date

    class Config:
        orm_mode = True
