from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ---------------------------------------------------------
# Hier tauschen wir später die URL für den Hostinger-Server aus.
# Beispiel für PostgreSQL: "postgresql://benutzer:passwort@server-ip/datenbankname"
# ---------------------------------------------------------
# Für den lokalen Test nutzen wir eine einfache SQLite-Datei:
SQLALCHEMY_DATABASE_URL = "sqlite:///./lernapp.db"

# Die "Engine" ist der tatsächliche Motor, der die Verbindung hält
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} # (Dieser Zusatz ist nur für SQLite nötig)
)

# Eine Session ist wie ein einzelnes Gesprächfenster mit der Datenbank
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Das ist die Basis-Klasse, von der alle unsere Tabellen später erben
Base = declarative_base()