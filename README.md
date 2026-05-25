

Erster Stand erstellt in Gemini CLI (v0.43.0) mit folgendem Prompt:

Schreibe mir ein Python-Skript für eine Web-App zur Zeitmessung, die speziell für mein Gymnastik- und Trainingstraining gedacht ist. Die App soll drei Buttons haben, deren Laufzeiten aus einer Konfigurationsdatei geladen werden, um sie einfach anpassen zu können. Zudem soll es einen Checkbutton geben, mit dem ausgewählt werden kann, ob bei der Hälfte der Zeit ein weiteres Signal ertönt. Nach dem Antippen soll der Timer starten und am Ende sowie gegebenenfalls in der Mitte ein hörbares Signal erklingen. Bitte schlage auch vor, welches Framework sich für die Umsetzung am besten eignet.

python venv:

python3 -m venv .venv

pip install niceguy

python main.py


git config --local --add user.name "Carsten Vosshenrich"
git config --local --add user.email carsten@vosshenrich.de
