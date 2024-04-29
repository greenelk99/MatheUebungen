import os

def rename_files(folder_path):
    # Liste aller Dateien im Ordner
    files = os.listdir(folder_path)
    
    # Filtern nach PNG-Dateien
    png_files = [file for file in files if file.endswith('.png')]
    
    # Durchgehen und umbenennen
    for i, file in enumerate(png_files, start=1):
        new_name = f"{i}.png"
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
        print(f"Umbenannt: {file} -> {new_name}")

if __name__ == "__main__":
    script_folder = os.path.dirname(os.path.abspath(__file__))
    rename_files(script_folder)
