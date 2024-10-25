from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas

def create_processo(db: Session, processo: schemas.ProcessoCreate):
    db_processo = models.Processo(
        numero_processo=processo.numero_processo,
        autor=processo.autor,
        reu=processo.reu,
        status=processo.status,
        data_criacao=processo.data_criacao or None
    )
    db.add(db_processo)
    db.commit()
    db.refresh(db_processo)
    return db_processo

def get_processo(db: Session, processo_id: int):
    return db.query(models.Processo).filter(models.Processo.id == processo_id).first()

def update_processo(db: Session, processo_id: int, processo: schemas.ProcessoUpdate):
    db_processo = db.query(models.Processo).filter(models.Processo.id == processo_id).first()
    
    # Atualiza apenas se o campo não for None
    if processo.autor is not None:
        db_processo.autor = processo.autor
    if processo.reu is not None:
        db_processo.reu = processo.reu
    if processo.status is not None:
        db_processo.status = processo.status
    if processo.data_criacao is not None:
        db_processo.data_criacao = processo.data_criacao

    db.commit()
    db.refresh(db_processo)
    return db_processo

def delete_processo(db: Session, processo_id: int):
    db_processo = db.query(models.Processo).filter(models.Processo.id == processo_id).first()
    if db_processo:
        db.delete(db_processo)
        db.commit()
    return db_processo

def get_all_processos(db: Session):
    return db.query(models.Processo).all()