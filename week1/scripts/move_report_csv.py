from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"

def move_report(folder):
    target_folder = folder / "reports"
    target_folder.mkdir(exist_ok=True)

    for file in folder.glob("report*.csv"):
        if file.is_file():
            destination = target_folder / file.name


            if not destination.exists():
                shutil.move(file, destination)
                print(f"Moved: {file.name}")

if __name__ == "__main__":
    move_report(DATA_DIR)