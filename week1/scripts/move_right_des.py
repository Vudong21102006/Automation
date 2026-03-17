from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"


def move_right_des(folder):
    mapping = {
        ".txt": "txt_files",
        ".csv": "csv_files",
        ".png": "images"
    }

    for folder_name in mapping.values():
        (folder / folder_name).mkdir(exist_ok=True)

    for file in folder.iterdir():
        if file.is_file():
            ext = file.suffix

            if ext in mapping:
                destination = folder / mapping[ext] / file.name

                if not destination.exists():
                    shutil.move(file, destination)
                    print(f"Moved: {file} -> {destination}")

if __name__ == "__main__":
    move_right_des(DATA_DIR)

