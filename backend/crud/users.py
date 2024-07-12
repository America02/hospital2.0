import models.users
import schemas.users
from sqlalchemy.orm import Session
import models, schemas

def get_user(db: Session, id: int):
<<<<<<< HEAD
    return db.query(models.users.User).filter(models.users.User.ID == id).first()

def get_user_by_usuario(db: Session, usuario: str):
    return db.query(models.users.User).filter(models.users.User.Nombre_Usuario == usuario).first()
=======
    return db.query(models.users.User).filter(models.users.User.id == id).first()

def get_user_by_usuario(db: Session, usuario: str):
    return db.query(models.users.User).filter(models.users.User.usuario == usuario).first()
>>>>>>> 629e4c2f68ac99f01ea12e71625724effa5e3822

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.users.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.users.UserCreate):
<<<<<<< HEAD
    db_user = models.users.User(Persona_ID = user.Persona_ID,
                                Nombre_Usuario=user.Nombre_Usuario,
                                Correo_Electronico = user.Correo_Electronico,
                                Contrasena = user.Contrasena, 
                                Numero_Telefonico_Movil=user.Numero_Telefonico_Movil, 
                                Estatus=user.Estatus,
                                Fecha_Registro = user.Fecha_Registro,
                                Fecha_Actualizacion = user.Fecha_Actualizacion 
                                )
=======
    db_user = models.users.User(usuario=user.usuario, password=user.password, created_at=user.created_at, estatus=user.estatus, Id_persona=user.Id_persona)
>>>>>>> 629e4c2f68ac99f01ea12e71625724effa5e3822
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, id: int, user: schemas.users.UserUpdate):
<<<<<<< HEAD
    db_user = db.query(models.users.User).filter(models.users.User.ID == id).first()
=======
    db_user = db.query(models.users.User).filter(models.users.User.id == id).first()
>>>>>>> 629e4c2f68ac99f01ea12e71625724effa5e3822
    if db_user:
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, id: int):
<<<<<<< HEAD
    db_user = db.query(models.users.User).filter(models.users.User.ID == id).first()
=======
    db_user = db.query(models.users.User).filter(models.users.User.id == id).first()
>>>>>>> 629e4c2f68ac99f01ea12e71625724effa5e3822
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user