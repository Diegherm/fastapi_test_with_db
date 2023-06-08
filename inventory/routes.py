from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from inventory.crud import (
    check_password,
    insert_user,
    select_user,
    select_users,
    update_user,
)
from inventory.database import get_db
from inventory.models import User
from inventory.schemas import (
    LoginSchema,
    UserCreateSchema,
    UserReadSchema,
    UserUpdateSchema,
)

router = APIRouter()


@router.post("/users/", response_model=UserReadSchema)
async def create_user(
    user: UserCreateSchema, session: Session = Depends(get_db)
) -> User:
    return insert_user(user, session)


@router.get("/users/", response_model=list[UserReadSchema])
async def read_users(session: Session = Depends(get_db)):
    return select_users(session)


@router.get("/users/{user_id}", response_model=UserReadSchema)
async def read_user(user_id: int, session: Session = Depends(get_db)) -> User:
    try:
        return select_user(user_id, session)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="El usuario no existe")


@router.patch("/users/{user_id}", response_model=UserReadSchema)
async def patch_user(
    user_id: int, user_data: UserUpdateSchema, session: Session = Depends(get_db)
) -> User:
    return update_user(user_id, user_data, session)


@router.post("/login")
async def login(login: LoginSchema, session: Session = Depends(get_db)):
    if check_password(login, session):
        return {"detail": "Contraseña correcta"}
    else:
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")
