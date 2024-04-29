import os
import random
import platform
import sys

def open_random_file(folder_path, script_name):
    # Überprüfen, ob der Ordner existiert
    if not os.path.exists(folder_path):
        print("Der angegebene Ordner existiert nicht.")
        return

    # Liste aller Dateien im Ordner
    files = os.listdir(folder_path)

    # Filtern von Dateien, um nur nicht-versteckte Dateien zu erhalten
    files = [f for f in files if not f.startswith('.')]

    # Überprüfen, ob im Ordner Dateien vorhanden sind
    if len(files) == 0:
        print("Der Ordner enthält keine Dateien.")
        return

    # Auswahl einer zufälligen Datei
    random_file = random.choice(files)

    # Überprüfen, ob die ausgewählte Datei das Skript ist
    if random_file == script_name:
        print("Die ausgewählte Datei ist das Skript selbst. Eine andere Datei wird geöffnet.")
        files.remove(script_name)  # Entfernen des Skriptnamens aus der Liste
        random_file = random.choice(files)  # Auswahl einer anderen Datei

    # Erstellen des vollständigen Dateipfads
    file_path = os.path.join(folder_path, random_file)

    # Öffnen der Datei basierend auf dem Betriebssystem
    try:
        if platform.system() == "Windows":
            os.startfile(file_path)
        elif platform.system() == "Darwin":  # macOS
            os.system("open " + file_path)
        else:  # Linux
            os.system("xdg-open " + file_path)
        print(f"Die Datei '{random_file}' wurde geöffnet.")
    except Exception as e:
        print(f"Fehler beim Öffnen der Datei: {e}")

# Pfad zum Ordner mit den Dateien
script_directory = os.path.dirname(os.path.abspath(__file__))
folder_path = script_directory

# Name des Skripts
script_name = os.path.basename(__file__)

# Aufrufen der Funktion, um eine zufällige Datei zu öffnen
open_random_file(folder_path, script_name)
