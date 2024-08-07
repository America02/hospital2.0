from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.puestos_departamentos as crud
import schemas.puestos_departamentos as schemas
import models.puestos_departamentos as models
from config.db import SessionLocal
from typing import List

puesto_departamento = APIRouter()

models.Base.metadata.create_all(bind=SessionLocal().get_bind())

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@puesto_departamento.get("/puestos_departamentos/", response_model=List[schemas.PuestoDepartamento], tags=["Puestos Departamentos"])
def read_puestos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_puestos = crud.get_puestos(db=db, skip=skip, limit=limit)
    return db_puestos

@puesto_departamento.get("/puesto_departamento/{puesto_id}", response_model=schemas.PuestoDepartamento, tags=["Puestos Departamentos"])
def read_puesto(puesto_id: int, db: Session = Depends(get_db)):
    db_puesto = crud.get_puesto(db=db, puesto_id=puesto_id)
    if db_puesto is None:
        raise HTTPException(status_code=404, detail="Puesto no encontrado")
    return db_puesto

@puesto_departamento.post("/puesto_departamento/", response_model=schemas.PuestoDepartamento, tags=["Puestos Departamentos"])
def create_puesto(puesto: schemas.PuestoDepartamentoCreate, db: Session = Depends(get_db)):
    return crud.create_puesto(db=db, puesto=puesto)

@puesto_departamento.put("/puesto_departamento/{puesto_id}", response_model=schemas.PuestoDepartamento, tags=["Puestos Departamentos"])
def update_puesto(puesto_id: int, puesto: schemas.PuestoDepartamentoUpdate, db: Session = Depends(get_db)):
    db_puesto = crud.update_puesto(db=db, puesto_id=puesto_id, puesto=puesto)
    if db_puesto is None:
        raise HTTPException(status_code=404, detail="Puesto no encontrado")
    return db_puesto

@puesto_departamento.delete("/puesto_departamento/{puesto_id}", response_model=schemas.PuestoDepartamento, tags=["Puestos Departamentos"])
def delete_puesto(puesto_id: int, db: Session = Depends(get_db)):
    db_puesto = crud.delete_puesto(db=db, puesto_id=puesto_id)
    if db_puesto is None:
        raise HTTPException(status_code=404, detail="Puesto no encontrado")
    return db_puesto
