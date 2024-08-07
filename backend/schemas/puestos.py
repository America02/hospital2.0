from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

class TurnoEnum(str, Enum):
    Manana = "Mañana"
    Tarde = "Tarde"
    Noche = "Noche"

class PuestoBase(BaseModel):
    Nombre: str
    Descripcion: Optional[str] = None
    Salario: Optional[float] = None
    Turno: TurnoEnum

class PuestoCreate(PuestoBase):
    pass

class PuestoUpdate(PuestoBase):
    pass

class Puesto(PuestoBase):
    PuestoID: int
    Creado: datetime
    Modificado: datetime

    class Config:
        orm_mode = True
