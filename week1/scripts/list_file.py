from pathlib import Path

import shutil

# folder = Path("..\data") # Path là object đại diện cho đường dẫn file. "../" lấy thư mục cha của đường dẫn trong terminal hiện tại

BASE_DIR = Path(__file__).resolve().parent # method resolve() lấy đường dẫn tuyệt đối
DATA_DIR = BASE_DIR.parent / "data"

def list_file(folder):
    for file in folder.iterdir(): # Liệt kê tất cả các file trong folder đường dẫn
        print(file)

def filter_file(folder):
    for file in folder.iterdir(): # Lọc những file .txt
        if file.suffix == ".txt": # Suffix của file là đuôi file. Suffix của Baigiang.pdf là .pdf
            print(file)

def check_file_or_folder(folder):
    for file in folder.iterdir():
        if file.is_file():
            print(file.name) # file.name chỉ in tên file chứ không in đường dẫn

def filter_file_glob(folder):
    for file in folder.glob("*txt"): # glob() trả về generator
        print(file)

def move_txt_files(folder): # Pipeline: Scan -> Filter -> Process -> Move
    # 1. Tạo thư mục đích (SCAN)
    target_folder = folder / "txt_files"
    target_folder.mkdir(exist_ok = True)

    # 2. Tìm file .txt (FILTER)
    for file in folder.glob("*txt"):
        if file.is_file():
            # 3. Tạo đường dẫn mới (PROCESS)
            destination = target_folder / file.name

            if not destination.exists():
                # 4. Move file (MOVE)
                shutil.move(file, destination)

        print(f"Moved: {file.name}")


if __name__ == "__main__":
    # list_file(DATA_DIR)
    # filter_file(DATA_DIR)
    # check_file_or_folder(DATA_DIR)
    # filter_file_glob(DATA_DIR)
    move_txt_files(DATA_DIR)

