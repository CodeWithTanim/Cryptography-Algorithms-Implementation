"""
Demo for AES encryption and decryption.
Creates an example plaintext, encrypts to outputs/encrypted_files/sample_encrypted.txt,
then decrypts back to outputs/decrypted_files/sample_decrypted.txt.
"""

from src.symmetric.aes_encryption import AESCipher
from src.utils.file_handler import ensure_dir, save_text, read_text, save_bytes, read_bytes, append_log
import base64
import os

# Prepare paths
ENC_DIR = "outputs/encrypted_files"
DEC_DIR = "outputs/decrypted_files"
LOG_DIR = "outputs/logs"
ensure_dir(ENC_DIR)
ensure_dir(DEC_DIR)
ensure_dir(LOG_DIR)

plaintext = "Hello! This is a demo message for AES encryption. — CodeWithTanim"
sample_input_path = "outputs/decrypted_files/sample_decrypted.txt"
sample_encrypted_path = os.path.join(ENC_DIR, "sample_encrypted.txt")
sample_decrypted_path = os.path.join(DEC_DIR, "sample_decrypted.txt")
log_path = os.path.join(LOG_DIR, "run_log.txt")

# Save original plaintext file
save_text(sample_input_path, plaintext)

# Generate key (32 bytes) and create cipher
key = AESCipher.generate_key(32)
cipher = AESCipher(key)

# Encrypt the file bytes and save
cipher.encrypt_file(sample_input_path, sample_encrypted_path)

# Decrypt to verify
cipher.decrypt_file(sample_encrypted_path, sample_decrypted_path)

# Log some info (we won't write the binary key in logs, but we will show key length)
append_log(log_path, "AES demo: encrypted -> decrypted successfully.")
append_log(log_path, f"AES key length (bytes): {len(key)}")

print("AES demo complete.")
print(f"Encrypted file: {sample_encrypted_path}")
print(f"Decrypted file: {sample_decrypted_path}")
