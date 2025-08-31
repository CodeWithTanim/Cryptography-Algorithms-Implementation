"""
Demo for RSA key generation, encryption, and decryption.
This demo:
- generates a keypair,
- exports public/private keys to variables,
- encrypts a message with public key,
- decrypts with private key,
- writes simple outputs to outputs/logs/run_log.txt
"""

from src.asymmetric.rsa_encryption import RSAHelper
from src.utils.file_handler import ensure_dir, append_log
import os

LOG_DIR = "outputs/logs"
ensure_dir(LOG_DIR)
log_path = os.path.join(LOG_DIR, "run_log.txt")

# Generate keys
private_key, public_key = RSAHelper.generate_keypair(2048)

# Export PEM (bytes)
private_pem = RSAHelper.export_private_key(private_key)
public_pem = RSAHelper.export_public_key(public_key)

message = b"RSA demo message - small plaintext"
ciphertext = RSAHelper.encrypt_message(public_key, message)
decrypted = RSAHelper.decrypt_message(private_key, ciphertext)

append_log(log_path, "RSA demo: generated keypair, encrypted and decrypted sample message.")
append_log(log_path, f"RSA ciphertext length: {len(ciphertext)} bytes")
append_log(log_path, f"RSA decrypted equals original: {decrypted == message}")

print("RSA demo complete.")
print("Check outputs/logs/run_log.txt for a short log.")
