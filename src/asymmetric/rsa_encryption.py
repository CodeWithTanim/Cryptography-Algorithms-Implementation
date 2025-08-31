"""
RSA encryption helper

Functions:
- generate_keypair
- export_public_key / export_private_key
- encrypt_message / decrypt_message (PKCS1_OAEP)
- save/load keys using strings
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from typing import Tuple


class RSAHelper:
    @staticmethod
    def generate_keypair(key_size: int = 2048) -> Tuple[RSA.RsaKey, RSA.RsaKey]:
        """
        Generate RSA key pair.
        Returns (private_key, public_key)
        """
        key = RSA.generate(key_size)
        private_key = key
        public_key = key.publickey()
        return private_key, public_key

    @staticmethod
    def export_private_key(private_key: RSA.RsaKey, passphrase: bytes = None) -> bytes:
        """Return PEM-encoded private key. Optionally encrypt with passphrase (bytes)."""
        if passphrase:
            return private_key.export_key(format='PEM', passphrase=passphrase, pkcs=8, protection="scryptAndAES128-CBC")
        return private_key.export_key(format='PEM')

    @staticmethod
    def export_public_key(public_key: RSA.RsaKey) -> bytes:
        """Return PEM-encoded public key."""
        return public_key.export_key(format='PEM')

    @staticmethod
    def import_private_key(pem_data: bytes, passphrase: bytes = None) -> RSA.RsaKey:
        """Load private key from PEM."""
        return RSA.import_key(pem_data, passphrase=passphrase)

    @staticmethod
    def import_public_key(pem_data: bytes) -> RSA.RsaKey:
        """Load public key from PEM."""
        return RSA.import_key(pem_data)

    @staticmethod
    def encrypt_message(public_key: RSA.RsaKey, message: bytes) -> bytes:
        """Encrypt a small message with public key using OAEP."""
        cipher = PKCS1_OAEP.new(public_key)
        return cipher.encrypt(message)

    @staticmethod
    def decrypt_message(private_key: RSA.RsaKey, ciphertext: bytes) -> bytes:
        """Decrypt a ciphertext with private key using OAEP."""
        cipher = PKCS1_OAEP.new(private_key)
        return cipher.decrypt(ciphertext)
