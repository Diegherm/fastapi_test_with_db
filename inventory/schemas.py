from datetime import datetime

from pydantic import BaseModel


class PetBaseSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class PetCreateSchema(PetBaseSchema):
    species: str
    breed: str
    chip: bool = False


class PetReadSchema(PetBaseSchema):
    id: int
    species: str
    breed: str
    chip: bool


class PetUpdateSchema(BaseModel):
    name: str | None
    species: str | None
    breed: str | None
    chip: bool | None


class UserBaseSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class UserCreateSchema(UserBaseSchema):
    rut: str
    email: str
    phone: int


class UserReadSchema(UserBaseSchema):
    id: int
    rut: str
    email: str
    phone: int
    pets: list[PetReadSchema] = []


class UserUpdateSchema(BaseModel):
    name: str | None
    rut: str | None
    email: str | None
    phone: int | None


class BenefitBaseSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class BenefitCreateSchema(BenefitBaseSchema):
    price: int


class BenefitReadSchema(BenefitBaseSchema):
    price: int


class AttentionBaseSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class AttentionCreateSchema(AttentionBaseSchema):
    date: datetime
    pet_id: int


class AttentionReadSchema(AttentionBaseSchema):
    id: int
    name: str
    date: datetime
    pet_id: int
    benefits: list[BenefitReadSchema] = []


'''class UserUpdateSchema(BaseModel):
    name: str | None
    is_enabled: bool | None
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
'''
