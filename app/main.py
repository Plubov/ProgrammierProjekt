from fastapi import FastAPI
from app import db_models
from app.database import engine
from app.models import Karteikarte # <-- Diese Zeile hat gefehlt!

# Dieser Befehl sagt SQLAlchemy: "Schau dir alle Tabellen in db_models.py an. 
# Wenn sie in der Datenbank noch nicht existieren, erstelle sie jetzt!"
db_models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lern-App API", version="0.1")

@app.get("/")
def read_root():
    return {"status": "Erfolgreich", "nachricht": "Datenbank ist verbunden!"}

# Wir sagen FastAPI, dass dieser Endpunkt zwingend unser Modell "Karteikarte" zurückgibt
@app.get("/api/karteikarte/test", response_model=Karteikarte)
def get_test_flashcard():
    # Wir erstellen ein echtes Objekt aus unserer Blaupause
    test_karte = Karteikarte(
        id=1,
        deck_id=1, # <-- WICHTIG: Das hast du vorhin in den Modellen hinzugefügt!
        vorderseite="사과",
        rueckseite="Apfel",
        level=1
    )
    return test_karte