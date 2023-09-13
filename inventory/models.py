from datetime import datetime

from sqlalchemy import ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Pet(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(64))
    species: Mapped[str] = mapped_column(String(64))
    breed: Mapped[str] = mapped_column(String(64))
    chip: Mapped[bool] = mapped_column(default=False, server_default="0")

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="pets")
    attentions: Mapped[list["Attention"]] = relationship(back_populates="pet")


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    rut: Mapped[str] = mapped_column(String(10), index=True, unique=True)
    name: Mapped[str] = mapped_column(String(64))
    email: Mapped[str] = mapped_column(String(64))
    phone: Mapped[int] = mapped_column(Integer)

    pets: Mapped[list["Pet"]] = relationship(back_populates="user")


class Benefit(Base):
    __tablename__ = "benefits"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(64))
    price: Mapped[int] = mapped_column(Integer)

    '''attentions_benefits: Mapped[list["Attention_benefit"]] = relationship(back_populates="benefits_id")'''
    attentions: Mapped[list["Attention"]] = relationship(back_populates="benefits", secondary="attentions_benefits")
    


class Attention(Base):
    __tablename__ = "attentions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(64))
    date: Mapped[datetime] = mapped_column(DateTime)

    pet_id: Mapped[int] = mapped_column(ForeignKey("pets.id"))

    '''attentions_benefits: Mapped[list["Attention_benefit"]] = relationship(back_populates="attentions_id")'''
    benefits: Mapped[list["Benefit"]] = relationship(back_populates="attentions", secondary="attentions_benefits")
    

    pet: Mapped["Pet"] = relationship(back_populates="attentions")


class Attention_benefit(Base):
    __tablename__ = "attentions_benefits"

    benefit_id: Mapped[int] = mapped_column(ForeignKey("benefits.id"), primary_key=True)
    attention_id: Mapped[int] = mapped_column(ForeignKey("attentions.id"), primary_key=True)

    '''benefits_id: Mapped["Benefit"] = relationship(back_populates="attentions_benefits")
    attentions_id: Mapped["Attention"] = relationship(back_populates="attentions_benefits")'''


'''class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    description: Mapped[str]
    stock: Mapped[int] = mapped_column(default=0, server_default="0")

    stock_changes: Mapped[list["StockChange"]] = relationship(back_populates="item")


class StockChange(Base):
    __tablename__ = "stock_changes"

    item_id: Mapped[int] = mapped_column(ForeignKey("items.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(default=datetime.now)
    change: Mapped[int]

    item: Mapped["Item"] = relationship(back_populates="stock_changes")
    user: Mapped["User"] = relationship(back_populates="stock_changes")
'''
