from fastapi import APIRouter, Depends
from config.db import conn
from src.models.pros import pros
from src.schemas.pros import Pro
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
from cryptography.fernet import Fernet
from fastapi_simple_security import api_key_security

router = APIRouter(
    prefix="/pros",
    tags=["pros"],
    responses={404: {"description": "Not found"}},
)
key = Fernet.generate_key()
f = Fernet(key)

@router.get(
    "",
    dependencies=[Depends(api_key_security)],
    response_model=List[Pro],
    description="Get a list of all professionals",
)
def get_pros():
    return conn.execute(pros.select()).fetchall()

@router.get(
    "/{id}",
    dependencies=[Depends(api_key_security)],
    response_model=Pro,
    description="Get a single professional by Id",
)
def get_pros(id: str):
    return conn.execute(pros.select().where(pros.c.id == id)).first()


@router.get(
    "/{speciality}/{city}",
    dependencies=[Depends(api_key_security)],
    response_model=List[Pro],
    description="Get a single professional by speciality and city",
)
def get_pros_by_speciality_and_city(speciality: str, city: str):
    return conn.execute(pros.select().where(pros.c.speciality == speciality).where(pros.c.city == city)).fetchall()


@router.post(
    "",
    dependencies=[Depends(api_key_security)],
    response_model=Pro, 
    description="Create a new Pro")
def create_pro(pro: Pro):
    new_pro = {"name": pro.name, "city": pro.city, "speciality": pro.speciality}
    result = conn.execute(pros.insert().values(new_pro))
    return conn.execute(pros.select().where(pros.c.id == result.lastrowid)).first()


@router.put(
    "/{id}",
    dependencies=[Depends(api_key_security)],
    response_model=Pro, 
    description="Update a professional by Id"
)
def update_pro(pro: Pro, id: int):
    conn.execute(
        pros.update()
        .values(id=pro.id, name=pro.name, city=pro.city, speciality=pro.speciality)
        .where(pros.c.id == id)
    )
    return conn.execute(pros.select().where(pros.c.id == id)).first()


@router.delete(
    "/{id}",
    dependencies=[Depends(api_key_security)],
    status_code=HTTP_204_NO_CONTENT
)
def delete_pro(id: int):
    conn.execute(pros.delete().where(pros.c.id == id))
    return conn.execute(pros.select().where(pros.c.id == id)).first()