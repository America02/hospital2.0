from typing import List, Union
from pydantic import BaseModel
<<<<<<< HEAD
from datetime import datetime, date
=======
from datetime import datetime
>>>>>>> 629e4c2f68ac99f01ea12e71625724effa5e3822

class PersonBase(BaseModel):
    Titulo_Cortesia: str
    Nombre: str
    Primer_Apellido: str
    Segundo_Apellido: str
<<<<<<< HEAD
    Fecha_Nacimiento: date
=======
    Fecha_Nacimiento: datetime
>>>>>>> 629e4c2f68ac99f01ea12e71625724effa5e3822
    Fotografia: str
    Genero: str
    Tipo_Sangre: str
    Estatus: bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    pass

class Person(PersonBase):
<<<<<<< HEAD
    ID: int
    class Config:
        orm_mode = True


=======
    id: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True
>>>>>>> 629e4c2f68ac99f01ea12e71625724effa5e3822
