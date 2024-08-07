from sqlalchemy import Column, Integer, String, DECIMAL, Enum, TIMESTAMP
from config.db import Base
import enum

class Turno(str, enum.Enum):
    Manana = "Mañana"
    Tarde = "Tarde"
    Noche = "Noche"

class PuestoDepartamento(Base):
    __tablename__ = "tbd_puestos_departamentos"

    PuestoID = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String(100), nullable=False)
    Descripcion = Column(String(255))
    Salario = Column(DECIMAL(10, 2))
    Turno = Column(Enum(Turno))
    Creado = Column(TIMESTAMP, default="CURRENT_TIMESTAMP")
    Modificado = Column(TIMESTAMP, default="CURRENT_TIMESTAMP", onupdate="CURRENT_TIMESTAMP")
    DepartamentoID = Column(Integer, nullable=False)
