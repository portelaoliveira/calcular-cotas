import os
from typing import Optional

from .get_file import get_file


def read_file(
    path: str,
    filename: str,
    subfolder: Optional[str] = None,
    path_is_file=True,
) -> str:
    path = get_file(path, filename, subfolder, path_is_file)

    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read()
    else:
        return ""
