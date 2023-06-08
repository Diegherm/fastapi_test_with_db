from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from inventory.crud import (
    check_password,
    insert_item,
    insert_stock_change,
    insert_user,
    select_item,
    select_items,
    select_stock_changes,
    select_user,
    select_users,
    update_user,
)
from inventory.database import get_db
from inventory.models import User
from inventory.schemas import (
    ItemCreateSchema,
    ItemReadSchema,
    LoginSchema,
    StockChangeCreateSchema,
    StockChangeReadSchema,
    UserCreateSchema,
    UserReadSchema,
    UserUpdateSchema,
)

router = APIRouter()


@router.post("/users/", response_model=UserReadSchema)
async def create_user(
    user_data: UserCreateSchema, session: Session = Depends(get_db)
) -> User:
    return insert_user(user_data, session)


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


@router.post("/items", response_model=ItemReadSchema)
async def create_item(item_data: ItemCreateSchema, session: Session = Depends(get_db)):
    return insert_item(item_data, session)


@router.get("/items", response_model=list[ItemReadSchema])
async def read_items(session: Session = Depends(get_db)):
    return select_items(session)


@router.get("/items/{item_id}", response_model=ItemReadSchema)
async def read_item(item_id: int, session: Session = Depends(get_db)):
    return select_item(item_id, session)


@router.post("/items/{item_id}/stock-change", response_model=StockChangeReadSchema)
async def create_stock_change(
    item_id: int,
    stock_change: StockChangeCreateSchema,
    session: Session = Depends(get_db),
):
    return insert_stock_change(item_id, stock_change, session)


@router.get("/stock-changes", response_model=list[StockChangeReadSchema])
async def read_stock_changes(session: Session = Depends(get_db)):
    return select_stock_changes(session)
