from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/processos", response_model=schemas.ProcessoResponse)
def create_processo(processo: schemas.ProcessoCreate, db: Session = Depends(get_db)):
    return crud.create_processo(db=db, processo=processo)

@app.get("/processos/{processo_id}", response_model=schemas.ProcessoResponse)
def get_processo(processo_id: int, db: Session = Depends(get_db)):
    db_processo = crud.get_processo(db, processo_id=processo_id)
    if not db_processo:
        raise HTTPException(status_code=404, detail="Processo não encontrado")
    return db_processo

@app.put("/processos/{processo_id}", response_model=schemas.ProcessoResponse)
def update_processo(processo_id: int, processo: schemas.ProcessoUpdate, db: Session = Depends(get_db)):
    db_processo = crud.get_processo(db, processo_id=processo_id)
    if not db_processo:
        raise HTTPException(status_code=404, detail="Processo não encontrado")
    return crud.update_processo(db=db, processo_id=processo_id, processo=processo)

@app.delete("/processos/{processo_id}", response_model=schemas.ProcessoResponse)
def delete_processo(processo_id: int, db: Session = Depends(get_db)):
    db_processo = crud.delete_processo(db=db, processo_id=processo_id)
    if not db_processo:
        raise HTTPException(status_code=404, detail="Processo não encontrado")
    return db_processo

@app.get("/processos", response_model=list[schemas.ProcessoResponse])
def get_all_processos(db: Session = Depends(get_db)):
    processos = crud.get_all_processos(db=db)
    return processos
