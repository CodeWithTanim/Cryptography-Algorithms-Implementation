"""
Hashing algorithms helpers.

Functions:
- compute_md5
- compute_sha256
- compute_sha512
Each returns hexadecimal digest string.
"""

import hashlib
from typing import Union


def _to_bytes(data: Union[str, bytes]) -> bytes:
    return data.encode("utf-8") if isinstance(data, str) else data


def compute_md5(data: Union[str, bytes]) -> str:
    b = _to_bytes(data)
    h = hashlib.md5()
    h.update(b)
    return h.hexdigest()


def compute_sha256(data: Union[str, bytes]) -> str:
    b = _to_bytes(data)
    h = hashlib.sha256()
    h.update(b)
    return h.hexdigest()


def compute_sha512(data: Union[str, bytes]) -> str:
    b = _to_bytes(data)
    h = hashlib.sha512()
    h.update(b)
    return h.hexdigest()
