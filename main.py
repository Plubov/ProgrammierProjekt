from fastapi import FastAPI

# Hier initialisieren wir unsere App
app = FastAPI(title="Lern-App API", version="0.1")

# Der Basis-Endpunkt (Root)
@app.get("/")
def read_root():
    return {"status": "Erfolgreich!", "nachricht": "Das Backend läuft perfekt."}

# Ein Test-Endpunkt für eure Karteikarten-Logik
@app.get("/api/karteikarte/test")
def get_test_flashcard():
    # Später kommen diese Daten natürlich dynamisch aus eurer PostgreSQL Datenbank
    return {
        "id": 101,
        "vorderseite": "안녕하세요",
        "rueckseite": "Hallo / Guten Tag",
        "kategorie": "Vokabeln",
        "level": 1,
        "nächste_wiederholung_in_tagen": 3
    }