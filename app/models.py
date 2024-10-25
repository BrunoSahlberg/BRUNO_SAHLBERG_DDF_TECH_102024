from sqlalchemy import Column, Integer, String, Date
from .database import Base
import datetime

class Processo(Base):
    __tablename__ = "processos"

    id = Column(Integer, primary_key=True, index=True)
    numero_processo = Column(Integer, unique=True, index=True, nullable=False)
    autor = Column(String)
    reu = Column(String)
    status = Column(String)
    data_criacao = Column(Date, default=datetime.date.today)

