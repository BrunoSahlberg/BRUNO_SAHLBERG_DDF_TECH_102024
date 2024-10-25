from pydantic import BaseModel
from typing import Optional
from datetime import date

class ProcessoBase(BaseModel):
    numero_processo: int
    autor: str
    reu: str
    status: str
    data_criacao: date

class ProcessoCreate(ProcessoBase):
    pass

class ProcessoUpdate(ProcessoBase):
    numero_processo: Optional[int] = None
    autor: Optional[str] = None
    reu: Optional[str] = None
    status: Optional[str] = None
    data_criacao: Optional[date] = None

class ProcessoResponse(ProcessoBase):
    id: int

    class Config:
        orm_mode = True
