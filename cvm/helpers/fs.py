import pathlib
from typing import Optional


def find_file_in_parent(filename: str, recursive: bool=False, current_path: Optional[pathlib.Path]=None) -> Optional[pathlib.Path]:
    if current_path is None:
        current_path = pathlib.Path.cwd()

    file_path = current_path / filename

    if file_path.exists():
        return file_path
    
    if recursive and str(current_path) != '/':
        return find_file_in_parent(filename, recursive=True, current_path=current_path.parent)
    
    return None
