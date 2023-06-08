from datetime import datetime

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    is_enabled: Mapped[bool] = mapped_column(default=True, server_default="1")
    password: Mapped[str] = mapped_column(nullable=True)

    stock_changes: Mapped[list["StockChange"]] = relationship(back_populates="user")


class Item(Base):
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
