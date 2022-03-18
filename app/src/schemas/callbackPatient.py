from pydantic import BaseModel

class CallbackPatient(BaseModel):
    id: str
    name: str
    age: int
    id_pro: str