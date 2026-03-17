from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"

def count_files_glob(folder):
    for file in folder.glob("report*"):
        print(file)

if __name__ == "__main__":
    count_files_glob(DATA_DIR)