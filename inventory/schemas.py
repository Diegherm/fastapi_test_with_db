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
    is_enabled: str | None
    password: str | None


class ItemSchema(BaseModel):
    id: int
    name: str
    description: str
    stock: int

    class Config:
        orm_mode = True


class StockChangeSchema(BaseModel):
    item_id: int
    user_id: int
    timestamp: datetime
    change: int

    class Config:
        orm_mode = True


class LoginSchema(BaseModel):
    user: str
    password: str
