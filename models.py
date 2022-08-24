import sqlalchemy as sa
import secrets

from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Account(Base):
    __tablename__ = "account"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.VARCHAR(30), nullable=False, unique=True)
    email = sa.Column(sa.String, nullable=False, unique=True)
    password = sa.Column(sa.String, nullable=False)
    is_active = sa.Column(sa.BOOLEAN, default=True)
    is_admin = sa.Column(sa.BOOLEAN, default=False)
    registered_at = sa.Column(sa.DateTime, server_default=sa.func.now())
    api_key = sa.Column(sa.String, unique=True, default=secrets.token_urlsafe, index=True)


class BankList(Base):
    __tablename__ = "bank_list"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False, unique=True, index=True)
    mfo = sa.Column(sa.Integer, unique=True)
    edrpou = sa.Column(sa.Integer, unique=True)
    ipn = sa.Column(sa.BigInteger, unique=True)
    iban = sa.Column(sa.String, unique=True)
    swift = sa.Column(sa.String, unique=True)
    rates = relationship("ExchangeRates", backref="bank")


class Currency(Base):
    __tablename__ = "currency"

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    code = sa.Column(sa.String, nullable=False, unique=True, index=True)
    name = sa.Column(sa.String, nullable=False, unique=True)
    rates = relationship("ExchangeRates", backref="currency")


class ExchangeRates(Base):
    __tablename__ = "exchange_rates"
    __table_args__ = (
        sa.UniqueConstraint("bank_id", "currency_id", "date", name="unique_exchange_rates"),
    )
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    bank_id = sa.Column(sa.Integer, sa.ForeignKey("bank_list.id"))
    currency_id = sa.Column(sa.Integer, sa.ForeignKey("currency.id"))
    purchase = sa.Column(sa.Float, nullable=False)
    sale = sa.Column(sa.Float, nullable=False)
    date = sa.Column(sa.Date, server_default=sa.func.now())
