# Workout Timer (Gymnastik-Timer)

Eine minimalistische, webbasierte Timer-App für Gymnastik- und Fitnesstraining, entwickelt mit **NiceGUI**.

## Projektübersicht
Die App ermöglicht es Benutzern, vordefinierte Timer-Intervalle zu starten, die über eine externe Konfigurationsdatei gesteuert werden. Ein besonderes Feature ist das optionale akustische Signal bei der Hälfte der abgelaufenen Zeit.

### Technologien
- **Python 3.x**: Hauptprogrammiersprache.
- **NiceGUI**: Framework für die Benutzeroberfläche (UI) und Web-Server.
- **Web Audio API**: Wird via JavaScript genutzt, um akustische Signale (Pieptöne) im Browser zu erzeugen.
- **JSON**: Für die Konfiguration der Timer-Dauern.

## Architektur
- `main.py`: Enthält die gesamte Logik der Web-App, einschließlich UI-Definitionen, Timer-Steuerung und Audio-Triggerung.
- `config.json`: Definiert die verfügbaren Timer (Label und Dauer in Sekunden).

## Installation und Ausführung

### Voraussetzungen
- Python 3.7 oder höher installiert.

### Setup
1. Virtuelle Umgebung erstellen:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Auf Windows: .venv\Scripts\activate
   ```
2. Abhängigkeiten installieren:
   ```bash
   pip install nicegui
   ```

### App starten
```bash
python main.py
```
Die App ist standardmäßig unter `http://localhost:8080` erreichbar (bei direktem Start) bzw. unter `http://localhost:9081` (beim Betrieb im Docker-Container).

## Docker-Betrieb
Das Projekt enthält ein `Dockerfile` und eine `docker-compose.yml` für den Betrieb im Container.

### Mit Docker Compose (Empfohlen)
```bash
docker compose up -d --build
```
Dies startet die App im Hintergrund. Da die `config.json` direkt in das Image kopiert wird, müssen Änderungen an der Konfiguration mit einem Rebuild des Images (`--build`) übernommen werden.

### Mit reinem Docker
1. Image bauen:
   ```bash
   docker build -t workout-timer .
   ```
2. Container starten:
   ```bash
   docker run -p 9081:8080 workout-timer
   ```

## Entwicklungskonventionen
- **UI-Struktur**: Die UI ist in der Klasse `WorkoutTimer` gekapselt, um den Zustand (verbleibende Zeit, Signal-Status) sauber zu verwalten.
- **Akustische Signale**: Signale werden über `ui.run_javascript` ausgelöst, um eine niedrige Latenz und Kompatibilität ohne externe Audio-Dateien zu gewährleisten.
- **Konfiguration**: Änderungen an den Timer-Dauern sollten ausschließlich in der `config.json` vorgenommen werden.

## TODOs / Zukünftige Erweiterungen
- Unterstützung für mehrere aufeinanderfolgende Sätze (Intervall-Training).
- Auswahl verschiedener Signaltöne.
- Dark-Mode-Unterstützung.
