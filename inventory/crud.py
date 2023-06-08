from sqlalchemy import select
from sqlalchemy.orm import Session

from inventory.models import Item, StockChange, User
from inventory.schemas import (
    ItemCreateSchema,
    ItemUpdateSchema,
    LoginSchema,
    StockChangeCreateSchema,
    UserCreateSchema,
    UserUpdateSchema,
)


def insert_user(user_data: UserCreateSchema, session: Session) -> User:
    user = User(**user_data.dict())
    session.add(user)
    session.commit()
    session.refresh(user)

    return user


def select_users(session: Session):
    smt = select(User)
    return session.execute(smt).scalars().all()


def select_user(user_id: int, session: Session) -> User:
    smt = select(User).where(User.id == user_id)
    return session.execute(smt).scalar_one()


def update_user(user_id: int, user_data: UserUpdateSchema, session: Session) -> User:
    smt_user = select(User).where(User.id == user_id)
    user = session.execute(smt_user).scalar_one()
    for k, v in user_data.dict(exclude_unset=True).items():
        setattr(user, k, v)

    session.add(user)
    session.commit()

    return user


def check_password(login: LoginSchema, session: Session) -> bool:
    smt_user = select(User).where(User.name == login.user)
    user = session.execute(smt_user).scalar_one()

    return user.password == login.password


def insert_item(item_data: ItemCreateSchema, session: Session) -> Item:
    item = Item(**item_data.dict())
    session.add(item)
    session.commit()
    session.refresh(item)

    return item


def select_items(session: Session):
    smt = select(Item)
    return session.execute(smt).scalars().all()


def select_item(item_id: int, session: Session) -> Item:
    smt = select(Item).where(Item.id == item_id)
    return session.execute(smt).scalar_one()


def update_item(item_id: int, item_data: ItemUpdateSchema, session: Session) -> Item:
    smt_item = select(Item).where(Item.id == item_id)
    item = session.execute(smt_item).scalar_one()
    for k, v in item_data.dict(exclude_unset=True).items():
        setattr(item, k, v)

    session.add(item)
    session.commit()

    return item


def insert_stock_change(
    item_id: int, stock_change: StockChangeCreateSchema, session: Session
) -> StockChange:
    stock_change = StockChange(item_id=item_id, **stock_change.dict())
    session.add(stock_change)

    # update item stock
    item = select_item(stock_change.item_id, session)
    item.stock += stock_change.quantity
    session.add(item)

    # commit and refresh
    session.commit()
    session.refresh(stock_change)

    print(stock_change)

    return stock_change


def select_stock_changes(session: Session):
    smt = select(StockChange)
    return session.execute(smt).scalars().all()