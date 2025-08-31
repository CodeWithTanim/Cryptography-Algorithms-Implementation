"""
Simple file handling utilities used by examples and tests.

Functions:
- ensure_dir(path)
- save_text(path, text)
- read_text(path) -> str
- save_bytes(path, data)
- read_bytes(path) -> bytes
- append_log(path, text)
"""

import os
from typing import Union


def ensure_dir(path: str) -> None:
    """Ensure directory exists (create if missing)."""
    os.makedirs(path, exist_ok=True)


def save_text(path: str, text: str, encoding: str = "utf-8") -> None:
    ensure_dir(os.path.dirname(path) or ".")
    with open(path, "w", encoding=encoding) as f:
        f.write(text)


def read_text(path: str, encoding: str = "utf-8") -> str:
    with open(path, "r", encoding=encoding) as f:
        return f.read()


def save_bytes(path: str, data: Union[bytes, bytearray]) -> None:
    ensure_dir(os.path.dirname(path) or ".")
    with open(path, "wb") as f:
        f.write(data)


def read_bytes(path: str) -> bytes:
    with open(path, "rb") as f:
        return f.read()


def append_log(path: str, text: str) -> None:
    ensure_dir(os.path.dirname(path) or ".")
    with open(path, "a", encoding="utf-8") as f:
        f.write(text + "\n")
