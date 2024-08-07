from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.puestos as crud
import schemas.puestos as schemas
import models.puestos as models
from config.db import SessionLocal
from typing import List

puesto = APIRouter()

models.Base.metadata.create_all(bind=SessionLocal().get_bind())

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@puesto.get("/puestos/", response_model=List[schemas.Puesto], tags=["Puestos"])
def read_puestos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_puestos = crud.get_puestos(db=db, skip=skip, limit=limit)
    return db_puestos

@puesto.get("/puesto/{puesto_id}", response_model=schemas.Puesto, tags=["Puestos"])
def read_puesto(puesto_id: int, db: Session = Depends(get_db)):
    db_puesto = crud.get_puesto(db=db, puesto_id=puesto_id)
    if db_puesto is None:
        raise HTTPException(status_code=404, detail="Puesto no encontrado")
    return db_puesto

@puesto.post("/puesto/", response_model=schemas.Puesto, tags=["Puestos"])
def create_puesto(puesto: schemas.PuestoCreate, db: Session = Depends(get_db)):
    return crud.create_puesto(db=db, puesto=puesto)

@puesto.put("/puesto/{puesto_id}", response_model=schemas.Puesto, tags=["Puestos"])
def update_puesto(puesto_id: int, puesto: schemas.PuestoUpdate, db: Session = Depends(get_db)):
    db_puesto = crud.update_puesto(db=db, puesto_id=puesto_id, puesto=puesto)
    if db_puesto is None:
        raise HTTPException(status_code=404, detail="Puesto no encontrado")
    return db_puesto

@puesto.delete("/puesto/{puesto_id}", response_model=schemas.Puesto, tags=["Puestos"])
def delete_puesto(puesto_id: int, db: Session = Depends(get_db)):
    db_puesto = crud.delete_puesto(db=db, puesto_id=puesto_id)
    if db_puesto is None:
        raise HTTPException(status_code=404, detail="Puesto no encontrado")
    return db_puesto
