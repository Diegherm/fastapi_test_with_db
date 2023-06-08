from sqlalchemy import select
from sqlalchemy.orm import Session

from inventory.models import User
from inventory.schemas import LoginSchema, UserCreateSchema, UserUpdateSchema


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
