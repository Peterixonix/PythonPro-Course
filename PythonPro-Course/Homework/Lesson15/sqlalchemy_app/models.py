from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime
import datetime
Base = declarative_base()

class Zadanie(Base):
    __tablename__ = 'zadania' # Nazwa tabeli w bazie danych
    id = Column(Integer, primary_key=True)
    opis = Column(String, nullable=False)
    zrobione = Column(Boolean, default=False, nullable=False)
    data_utworzenia = Column(DateTime, default=datetime.datetime.utcnow)

def __repr__(self):
    return f"<Zadanie(id={self.id}, opis='{self.opis}', zrobione={self.zrobione})>"


