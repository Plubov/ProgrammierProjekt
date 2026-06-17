from sqlalchemy import Column, Integer, String
from app.database import Base

class DBKarteikarte(Base):
    __tablename__ = "karteikarten" # So heißt die Tabelle später in PostgreSQL

    # Hier definieren wir die Spalten der Tabelle
    id = Column(Integer, primary_key=True, index=True)
    vorderseite = Column(String, index=True)
    rueckseite = Column(String)
    kategorie = Column(String, default="Allgemein")
    level = Column(Integer, default=1)
    notizen = Column(String, nullable=True) # Darf leer sein