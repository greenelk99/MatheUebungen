import os
import re

def find_highest_numbered_file(files):
    highest_number = 0
    pattern = re.compile(r'(\d+)\.png')
    for file in files:
        match = pattern.match(file)
        if match:
            number = int(match.group(1))
            highest_number = max(highest_number, number)
    return highest_number

def rename_files(folder_path):
    # Liste aller Dateien im Ordner
    files = os.listdir(folder_path)
    
    # Filtern nach PNG-Dateien
    png_files = [file for file in files if file.endswith('.png')]
    
    # Finden der höchsten Nummer
    highest_number = find_highest_numbered_file(png_files)
    
    # Durchgehen und umbenennen der noch nicht nummerierten Dateien
    for file in png_files:
        if not re.match(r'\d+\.png', file):
            highest_number += 1
            new_name = f"{highest_number}.png"
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
            print(f"Umbenannt: {file} -> {new_name}")

if __name__ == "__main__":
    script_folder = os.path.dirname(os.path.abspath(__file__))
    rename_files(script_folder)
