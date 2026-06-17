from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# ---------------------------------------------------------
# 1. DAS BENUTZER-MODELL (Gamification & Accounts)
# ---------------------------------------------------------
class Benutzer(BaseModel):
    id: int
    benutzername: str
    email: str
    
    # Gamification-Elemente (Duolingo-Style)
    xp: int = 0                  # Erfahrungspunkte
    streak_tage: int = 0         # Wie viele Tage in Folge gelernt?
    letzter_login: Optional[datetime] = None

# ---------------------------------------------------------
# 2. DAS NOTIZ-MODELL (RemNote-Style Wissensmanagement)
# ---------------------------------------------------------
class NotizBlock(BaseModel):
    id: int
    benutzer_id: int             # Wem gehört diese Notiz?
    titel: str
    inhalt: str                  # Hier steht der eigentliche Text (z.B. als Markdown)
    
    # KI-Integration
    ai_generiert: bool = False   # Wurde dieser Block von eurer KI erstellt?
    erstellt_am: datetime = Field(default_factory=datetime.now)

# ---------------------------------------------------------
# 3. DAS DECK-MODELL (Ordner für Karteikarten)
# ---------------------------------------------------------
class Deck(BaseModel):
    id: int
    benutzer_id: int
    titel: str
    beschreibung: Optional[str] = None
    
    # Optional: Ein Deck kann aus einer spezifischen Notiz generiert worden sein
    ursprungs_notiz_id: Optional[int] = None 

# ---------------------------------------------------------
# 4. DAS KARTEIKARTEN-MODELL (Erweitert)
# ---------------------------------------------------------
class Karteikarte(BaseModel):
    id: int
    deck_id: int                 # Zu welchem Deck gehört die Karte?
    vorderseite: str
    rueckseite: str
    
    # Spaced Repetition Logik (Wann muss die Karte wiederholt werden?)
    level: int = 1
    naechste_wiederholung: Optional[datetime] = None