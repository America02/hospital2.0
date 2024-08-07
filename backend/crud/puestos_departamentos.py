from sqlalchemy.orm import Session
import models.puestos_departamentos as models
import schemas.puestos_departamentos as schemas

def get_puesto(db: Session, puesto_id: int):
    return db.query(models.PuestoDepartamento).filter(models.PuestoDepartamento.PuestoID == puesto_id).first()

def get_puestos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.PuestoDepartamento).offset(skip).limit(limit).all()

def create_puesto(db: Session, puesto: schemas.PuestoDepartamentoCreate):
    db_puesto = models.PuestoDepartamento(**puesto.dict())
    db.add(db_puesto)
    db.commit()
    db.refresh(db_puesto)
    return db_puesto

def update_puesto(db: Session, puesto_id: int, puesto: schemas.PuestoDepartamentoUpdate):
    db_puesto = db.query(models.PuestoDepartamento).filter(models.PuestoDepartamento.PuestoID == puesto_id).first()
    if db_puesto:
        for var, value in vars(puesto).items():
            setattr(db_puesto, var, value) if value else None
        db.commit()
        db.refresh(db_puesto)
    return db_puesto

def delete_puesto(db: Session, puesto_id: int):
    db_puesto = db.query(models.PuestoDepartamento).filter(models.PuestoDepartamento.PuestoID == puesto_id).first()
    if db_puesto:
        db.delete(db_puesto)
        db.commit()
    return db_puesto
