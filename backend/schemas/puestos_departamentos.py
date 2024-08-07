from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

class TurnoEnum(str, Enum):
    Manana = "Mañana"
    Tarde = "Tarde"
    Noche = "Noche"

class PuestoDepartamentoBase(BaseModel):
    Nombre: str
    Descripcion: Optional[str] = None
    Salario: Optional[float] = None
    Turno: TurnoEnum
    DepartamentoID: int

class PuestoDepartamentoCreate(PuestoDepartamentoBase):
    pass

class PuestoDepartamentoUpdate(PuestoDepartamentoBase):
    pass

class PuestoDepartamento(PuestoDepartamentoBase):
    PuestoID: int
    Creado: datetime
    Modificado: datetime

    class Config:
        orm_mode = True
