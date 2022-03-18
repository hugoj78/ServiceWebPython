from fastapi import FastAPI
from src.routes.health import router as health
from src.routes.pros import router as pro
from src.routes.patients import router as patient
from src.routes.callbackPatient import router as callbackPatient
from config.openapi import tags_metadata
from fastapi_simple_security import api_key_router
import os

app = FastAPI(
    title="WebServicePython",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.include_router(health)
app.include_router(pro)
app.include_router(patient)
app.include_router(callbackPatient)
app.include_router(api_key_router, prefix="/auth", tags=["_auth"])