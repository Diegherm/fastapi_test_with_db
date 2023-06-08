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

    stock_changes: list["StockChangePlainReadSchema"]


class ItemPlainReadSchema(ItemBaseSchema):
    id: int
    stock: int


class ItemUpdateSchema(BaseModel):
    name: str | None
    description: str | None
    stock: int | None


class StockChangeBaseSchema(BaseModel):
    user_id: int
    quantity: int

    class Config:
        orm_mode = True


class StockChangeCreateSchema(StockChangeBaseSchema):
    pass


class StockChangeReadSchema(StockChangeBaseSchema):
    item_id: int
    timestamp: datetime

    item: ItemPlainReadSchema
    user: UserReadSchema


class StockChangePlainReadSchema(StockChangeBaseSchema):
    item_id: int
    timestamp: datetime


class LoginSchema(BaseModel):
    user: str
    password: str


ItemReadSchema.update_forward_refs()
