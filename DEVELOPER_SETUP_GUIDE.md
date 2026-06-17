# Startleitfaden: Einrichtung der Entwicklungsumgebung

Willkommen im Projekt! Dieser Leitfaden führt dich Schritt für Schritt durch die Einrichtung deines PCs, damit wir reibungslos zusammenarbeiten können. Auch ohne große Vorerfahrung kannst du dieser Anleitung problemlos folgen.

---

## Phase 1: Installation der Basis-Software

Wir benötigen drei zentrale Programme, um den Code auszuführen und gemeinsam daran zu arbeiten.

### 1. Python (Die Laufzeitumgebung)
Python ist die Programmiersprache, in der wir unser Backend (die Server-Logik) schreiben.
* **Download:** Lade die neueste Version unter [python.org/downloads](https://python.org/downloads) herunter.
* **WICHTIG bei der Installation (Windows):** Bevor du auf "Install Now" klickst, setze ganz unten im ersten Fenster **zwingend das Häkchen bei "Add python.exe to PATH"**! Dies ist essenziell, damit dein PC Python später erkennt.

### 2. Git (Die Versionsverwaltung)
Git speichert jeden Zwischenstand unseres Codes und ermöglicht es uns, als Team an denselben Dateien zu arbeiten, ohne uns gegenseitig zu überschreiben.
* **Download:** Lade [Git für Windows](https://git-scm.com/downloads) herunter und klicke dich bei der Installation einfach mit den Standardeinstellungen ("Weiter" / "Next") durch.

### 3. Visual Studio Code (Der Code-Editor)
VS Code ist unser Hauptwerkzeug, in dem wir den Code schreiben und verwalten.
* **Download:** Lade [VS Code](https://code.visualstudio.com/) herunter und installiere es.

---

## Phase 2: VS Code mit GitHub verknüpfen

VS Code hat Git bereits integriert. Damit du unseren gemeinsamen Code aber herunterladen und später deine Änderungen hochladen darfst, müssen wir VS Code einmalig mit deinem GitHub-Account verbinden.

### 1. Bei GitHub in VS Code anmelden
1. Öffne VS Code.
2. Klicke ganz unten links in der schmalen Seitenleiste auf das **Konto-Symbol** (das kleine Männchen).
3. Wähle **Mit GitHub anmelden** (Sign in with GitHub) aus.
4. Dein Browser öffnet sich. Bestätige dort die Zugriffsrechte für VS Code.

### 2. Git konfigurieren
Git muss wissen, unter welchem Namen deine Code-Änderungen gespeichert werden.
1. Öffne in VS Code oben im Menü ein **Neues Terminal** (`Terminal` -> `New Terminal`).
2. Führe diese beiden Befehle nacheinander aus (ersetze die Daten mit deinen GitHub-Daten und bestätige jeweils mit Enter):

```bash
git config --global user.name "Dein GitHub Benutzername"
git config --global user.email "Deine GitHub E-Mail Adresse"
```

---

## Phase 3: Das Projekt herunterladen (Klonen)

Nun holen wir den aktuellen Projektstand aus der Cloud auf deinen Rechner.

1. Klicke in VS Code in der linken Leiste auf das Symbol für **Quellcodeverwaltung** (das Symbol mit den drei Knoten).
2. Klicke auf den blauen Button **Repository klonen** (Clone Repository).
3. Klicke oben in der Mitteleiste auf **Von GitHub klonen**.
4. Wähle unser Projekt-Repository aus der Liste aus.
5. Wähle einen Ordner auf deinem PC, in dem das Projekt gespeichert werden soll.
6. Klicke abschließend unten rechts auf **Ordner öffnen**. Du siehst nun links unsere Projektdateien.

---

## Phase 4: Die virtuelle Projektumgebung (Venv) einrichten

Um Konflikte mit anderen Programmen auf deinem PC zu vermeiden, erstellen wir für dieses Projekt eine isolierte Umgebung. Dort installieren wir alle benötigten Erweiterungen (wie z. B. FastAPI) ausschließlich für diese App.

### 1. Umgebung automatisch erstellen
1. Drücke in VS Code die Tastenkombination **`Strg + Shift + P`**.
2. Tippe **`Python: Create Environment`** ein und wähle den Punkt aus.
3. Wähle **`Venv`** und klicke auf deine installierte Python-Version.
4. Setze ein Häkchen bei der Datei **`requirements.txt`** und bestätige.
   * *VS Code richtet nun die Umgebung ein und installiert im Hintergrund automatisch alle benötigten Bibliotheken.*

### 2. Windows-Sicherheitsblockade aufheben (Nur für Windows)
Windows blockiert standardmäßig das Ausführen solcher Arbeitsumgebungen im Terminal. Das müssen wir einmalig erlauben:
1. Öffne ein neues Terminal in VS Code (`Terminal` -> `New Terminal`).
2. Führe folgenden Befehl aus:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

3. Bestätige die Nachfrage mit **`J`** (für Ja) oder **`Y`** (für Yes) und drücke Enter.

---

## Phase 5: Der erste Testlauf

Dein Setup ist komplett! Jetzt starten wir den lokalen Server, um zu prüfen, ob alles funktioniert.

1. Schließe dein aktuelles Terminal (klicke auf das kleine Mülleimer-Symbol oben rechts über dem Terminal) und öffne ein **Neues Terminal**.
2. Vorne in der Eingabezeile sollte nun grün **`(.venv)`** stehen. Das zeigt, dass deine isolierte Umgebung aktiv ist.
3. Starte unser Backend mit diesem Befehl:

```bash
uvicorn main:app --reload
```

4. Öffne deinen Browser und rufe diese Adresse auf: 
   **`http://127.0.0.1:8000/api/karteikarte/test`**

Wenn du nun Text im JSON-Format auf deinem Bildschirm siehst, funktioniert dein Setup einwandfrei! Du bist bereit, am Code mitzuarbeiten.