from typing import Optional
from pydantic import BaseModel

class Pro(BaseModel):
    id: Optional[int]
    name: str
    city: str
    speciality: str