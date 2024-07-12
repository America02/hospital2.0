from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
<<<<<<< HEAD
    Persona_ID: int
    Nombre_Usuario: str
    Correo_Electronico: str
    Contrasena: str
    Numero_Telefonico_Movil: str
    Estatus: str
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime
=======
    usuario: str
    password: str
    created_at: datetime
    estatus: bool
    Id_persona: int
>>>>>>> 629e4c2f68ac99f01ea12e71625724effa5e3822

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
<<<<<<< HEAD
    ID: int
    Persona_ID: int
    class Config:
        orm_mode = True
        
class UserLogin(BaseModel):
    Nombre_Usuario: str
    Correo_electronico: str
    Contrasena: str
    Numero_Telefonico_Movil: str

=======
    id: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True
        
    usuario: str
    password: str
>>>>>>> 629e4c2f68ac99f01ea12e71625724effa5e3822

