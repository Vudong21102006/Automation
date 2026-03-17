from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.parent / "data"

def count_file(folder):
    count = 0
    
    for file in folder.iterdir():
        if file.is_file():
            count += 1
    
    print(f"Total files: {count}")

if __name__ == "__main__":
    count_file(DATA_DIR)