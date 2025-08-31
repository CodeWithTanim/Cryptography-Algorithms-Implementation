"""
AES encryption utilities.

Implements:
- AESCipher class with methods:
    - generate_key (random 32 bytes for AES-256)
    - encrypt_bytes / decrypt_bytes
    - encrypt_file / decrypt_file (using utils.file_handler)
"""

import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from typing import Tuple
from ..utils.file_handler import save_bytes, read_bytes

BLOCK_SIZE = AES.block_size  # 16


def pkcs7_pad(data: bytes) -> bytes:
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([pad_len]) * pad_len


def pkcs7_unpad(data: bytes) -> bytes:
    if not data:
        raise ValueError("Invalid PKCS#7 padding (empty input)")
    pad_len = data[-1]
    if pad_len < 1 or pad_len > BLOCK_SIZE:
        raise ValueError("Invalid PKCS#7 padding.")
    if data[-pad_len:] != bytes([pad_len]) * pad_len:
        raise ValueError("Invalid PKCS#7 padding.")
    return data[:-pad_len]


class AESCipher:
    """
    AES-256 CBC cipher helper.

    Key: 32 bytes (AES-256)
    IV: 16 bytes, randomly generated for each encryption
    Output format for encrypt_*: IV || ciphertext
    """

    def __init__(self, key: bytes):
        if not isinstance(key, (bytes, bytearray)):
            raise TypeError("Key must be bytes.")
        if len(key) not in (16, 24, 32):
            raise ValueError("Key length must be 16, 24, or 32 bytes (AES-128/192/256).")
        self.key = key

    @staticmethod
    def generate_key(length: int = 32) -> bytes:
        """Generate a random key. Default 32 bytes (AES-256)."""
        if length not in (16, 24, 32):
            raise ValueError("Key length must be 16, 24 or 32.")
        return get_random_bytes(length)

    def encrypt_bytes(self, plaintext: bytes) -> bytes:
        """Encrypt bytes and return IV + ciphertext."""
        iv = get_random_bytes(BLOCK_SIZE)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        padded = pkcs7_pad(plaintext)
        ciphertext = cipher.encrypt(padded)
        return iv + ciphertext

    def decrypt_bytes(self, iv_cipher: bytes) -> bytes:
        """Decrypt IV + ciphertext bytes and return plaintext."""
        if len(iv_cipher) < BLOCK_SIZE:
            raise ValueError("Input too short.")
        iv = iv_cipher[:BLOCK_SIZE]
        ciphertext = iv_cipher[BLOCK_SIZE:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        padded = cipher.decrypt(ciphertext)
        return pkcs7_unpad(padded)

    def encrypt_file(self, input_path: str, output_path: str) -> None:
        """Read file bytes, encrypt, and save to output (IV + ciphertext)."""
        data = read_bytes(input_path)
        enc = self.encrypt_bytes(data)
        save_bytes(output_path, enc)

    def decrypt_file(self, input_path: str, output_path: str) -> None:
        """Read IV + ciphertext from file, decrypt, and save plaintext."""
        enc = read_bytes(input_path)
        data = self.decrypt_bytes(enc)
        save_bytes(output_path, data)
