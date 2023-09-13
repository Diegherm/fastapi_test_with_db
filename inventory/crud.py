from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from inventory.models import Pet, User, Benefit, Attention
#from inventory.schemas import LoginSchema, PetCreateSchema, UserUpdateSchema
from inventory.schemas import PetCreateSchema, PetUpdateSchema, UserCreateSchema, UserUpdateSchema, BenefitCreateSchema, AttentionCreateSchema


def insert_pet(pet_data: PetCreateSchema, user_data: UserCreateSchema, session: Session) -> Pet:
    existing_user = session.query(User).filter_by(rut=user_data.rut).first()

    if existing_user:   
        pet = Pet(**pet_data.dict())
        pet.user = existing_user

        session.add(pet)

        session.commit()
        session.refresh(pet)

        return pet

    user = User(**user_data.dict())
    pet = Pet(**pet_data.dict())
    pet.user = user

    session.add(pet)
    session.add(user)

    session.commit()
    session.refresh(pet)

    return pet


def select_pets(session: Session):
    smt = select(Pet)
    return session.execute(smt).scalars().all()


def select_pet(pet_id: int, session: Session) -> Pet:
    smt = select(Pet).where(Pet.id == pet_id)
    return session.execute(smt).scalar_one()


def update_pet(pet_id: int, pet_data: PetUpdateSchema, session: Session) -> Pet:
    smt_pet = select(Pet).where(Pet.id == pet_id)
    pet = session.execute(smt_pet).scalar_one()
    for k, v in pet_data.dict(exclude_unset=True).items():
        setattr(pet, k, v)

    session.add(pet)
    session.commit()

    return pet


def select_users(session: Session):
    smt = select(User)
    return session.execute(smt).scalars().all()


def select_user(user_id: int, session: Session) -> User:
    return session.query(User).filter_by(rut=user_id).first()


def update_user(user_rut: str, user_data: UserUpdateSchema, session: Session) -> User:
    smt_user = select(User).where(User.id == user_rut)
    user = session.execute(smt_user).scalar_one()
    for k, v in user_data.dict(exclude_unset=True).items():
        setattr(user, k, v)

    session.add(user)
    session.commit()

    return user


def insert_benefit(benefit_data: BenefitCreateSchema, attention_id: int, session: Session) -> Benefit:
    attention = session.query(Attention).filter_by(id=attention_id).one()
 
    benefit = Benefit(**benefit_data.dict())
    attention.benefits.append(benefit)

    session.add(benefit)
    session.add(attention)

    session.commit()
    session.refresh(benefit)

    return benefit


def select_benefits(session: Session):
    smt = select(Benefit)
    return session.execute(smt).scalars().all()


def select_benefit(benefit_id: int, session: Session) -> Benefit:
    return session.query(Benefit).filter_by(id=benefit_id).first()


def insert_attention(attention_data: AttentionCreateSchema, benefit_data: BenefitCreateSchema, session: Session) -> Attention:
    existing_pet = session.query(Pet).filter_by(id=attention_data.pet_id).one()
 
    attention = Attention(**attention_data.dict())
    benefit = Benefit(**benefit_data.dict())
    attention.pet = existing_pet
    attention.benefits.append(benefit)

    session.add(benefit)
    session.add(attention)

    session.commit()
    session.refresh(attention)

    return attention


def select_attentions(session: Session):
    smt = select(Attention)
    return session.execute(smt).scalars().all()


'''def select_user(user_id: int, session: Session) -> User:
    smt = select(User).where(User.id == user_id)
    return session.execute(smt).scalar_one()
'''


'''
def check_password(login: LoginSchema, session: Session) -> bool:
    smt_user = select(User).where(User.name == login.user)
    user = session.execute(smt_user).scalar_one()

    return user.password == login.password
'''
