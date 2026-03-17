from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent # __file__ là đường dẫn của file Python hiện tại. resolve() giúp chuyển path thành absolute path
DATA_DIR = BASE_DIR.parent / "data"


def list_txt_file(folder):
    for file in folder.iterdir():
        if file.suffix == ".txt":
            print(file.name)

if __name__ == "__main__":
    list_txt_file(DATA_DIR)