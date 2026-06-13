import shutil
from pathlib import Path

folder = Path(r"d:\Nora AI Training\day14")

if folder.exists():
    if folder.is_dir():
        shutil.rmtree(folder) 
        print(f"Deleted folder: {folder}")
    else:
        print(f"Not a folder: {folder}")
else:
    print(f"Folder not found: {folder}")