from datetime import datetime

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class UserCreateSchema(UserBaseSchema):
    password: str


class UserReadSchema(UserBaseSchema):
    id: int
    is_enabled: bool


class UserUpdateSchema(BaseModel):
    name: str | None
    is_enabled: bool | None
    password: str | None


class ItemBaseSchema(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True


class ItemCreateSchema(ItemBaseSchema):
    pass


class ItemReadSchema(ItemBaseSchema):
    id: int
    stock: int


class ItemUpdateSchema(BaseModel):
    name: str | None
    description: str | None
    stock: int | None


class StockChangeBaseSchema(BaseModel):
    item_id: int
    timestamp: datetime
    quantity: int

    class Config:
        orm_mode = True


class StockChangeCreateBaseSchema(StockChangeBaseSchema):
    pass


class StockChangeReadBaseSchema(StockChangeBaseSchema):
    user_id: int

    item: ItemReadSchema


class LoginSchema(BaseModel):
    user: str
    password: str
