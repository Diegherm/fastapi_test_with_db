from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from inventory.crud import (
    insert_pet,
    select_pet,
    select_pets,
    update_pet,
    select_user,
    select_users,
    update_user,
    insert_benefit,
    select_benefit,
    select_benefits,
    insert_attention,
    select_attentions,
)
from inventory.database import get_db
from inventory.models import Pet, User, Benefit, Attention
from inventory.schemas import (
    PetCreateSchema,
    PetReadSchema,
    PetUpdateSchema,
    UserCreateSchema,
    UserReadSchema,
    UserUpdateSchema,
    BenefitCreateSchema,
    BenefitReadSchema,
    AttentionCreateSchema,
    AttentionReadSchema,
)

router = APIRouter()


@router.post("/pets/", response_model=PetReadSchema)
async def create_pet(
    pet: PetCreateSchema, user: UserCreateSchema, session: Session = Depends(get_db)) -> Pet:
    try:
        return insert_pet(pet, user, session)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="La mascota no existe")


@router.get("/pets/", response_model=list[PetReadSchema])
async def read_pets(session: Session = Depends(get_db)):
    return select_pets(session)


@router.get("/pets/{pet_id}", response_model=PetReadSchema)
async def read_pet(pet_id: int, session: Session = Depends(get_db)) -> Pet:
    try:
        return select_pet(pet_id, session)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="La mascota no existe")


@router.patch("/pets/{pet_id}", response_model=PetReadSchema)
async def patch_pet(
    pet_id: int, pet_data: PetUpdateSchema, session: Session = Depends(get_db)
) -> Pet:
    return update_pet(pet_id, pet_data, session)


@router.get("/users/", response_model=list[UserReadSchema])
async def read_users(session: Session = Depends(get_db)):
    return select_users(session)


@router.get("/users/{user_rut}", response_model=UserReadSchema)
async def read_user(user_rut: str, session: Session = Depends(get_db)) -> User:
    try:
        return select_user(user_rut, session)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    

@router.patch("/users/{user_id}", response_model=UserReadSchema)
async def patch_user(
    user_id: int, user_data: UserUpdateSchema, session: Session = Depends(get_db)
) -> User:
    return update_user(user_id, user_data, session)


@router.post("/benefits/", response_model=BenefitReadSchema)
async def create_benefit(
    benefit: BenefitCreateSchema, attention_id: int, session: Session = Depends(get_db)) -> Benefit:
    try:
        return insert_benefit(benefit, attention_id, session)
    except NoResultFound:
        return HTTPException(status_code=404, detail="El beneficio no existe")


@router.get("/benefits/", response_model=list[BenefitReadSchema])
async def read_benefits(session: Session = Depends(get_db)):
    return select_benefits(session)


@router.get("/benefits/{benefit_id}", response_model=BenefitReadSchema)
async def read_benefit(benefit_id: int, session: Session = Depends(get_db)) -> Benefit:
    try:
        return select_benefit(benefit_id, session)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="El usuario no existe")


@router.post("/attentions/", response_model=AttentionReadSchema)
async def create_attention(
    attention: AttentionCreateSchema, benefit: BenefitCreateSchema, session: Session = Depends(get_db)) -> Attention:
    try:
        return insert_attention(attention, benefit, session)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="La mascota no existe")
    

@router.get("/attentions/", response_model=list[AttentionReadSchema])
async def read_attentions(session: Session = Depends(get_db)):
    return select_attentions(session)


'''
@router.post("/login")
async def login(login: LoginSchema, session: Session = Depends(get_db)):
    if check_password(login, session):
        return {"detail": "Contraseña correcta"}
    else:
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")
'''
