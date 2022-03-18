from fastapi import APIRouter, Depends
from config.db import conn
from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select
from cryptography.fernet import Fernet
from fastapi_simple_security import api_key_security
from pydantic import BaseModel, HttpUrl
from typing import Optional
import requests
from src.schemas.callbackPatient import CallbackPatient

router = APIRouter(
    prefix="/callbackPatient",
    tags=["callbackPatient"],
    responses={404: {"description": "Not found"}},
)
key = Fernet.generate_key()
f = Fernet(key)

@router.post(
    "/{id}",
    #dependencies=[Depends(api_key_security)],
    response_model=CallbackPatient,
    description="Get an Patient from another WebService"
    )
def get_callback_patient(id: str):

    patient_url = f"http://serviceweb-java:8081/patient/{id}"
    get_patient = requests.get(url = patient_url)

    if get_patient .status_code == 200:
        return (get_patient.json())
    else:
        return {"not found"}