from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"

def move_csv(folder):
    target_folder = folder / "csv_files"
    target_folder.mkdir(exist_ok=True)

    for file in folder.glob("*.csv"):
        if file.is_file():
            destination = target_folder / file.name

            if not destination.exists():
                shutil.move(file, destination)
                print(f"Moved: {file.name}")

if __name__ == "__main__":
    move_csv(DATA_DIR)