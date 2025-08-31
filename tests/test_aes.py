import os
from src.symmetric.aes_encryption import AESCipher
from src.utils.file_handler import save_text, read_text, save_bytes, read_bytes, ensure_dir
import tempfile

def test_aes_encrypt_decrypt_roundtrip(tmp_path):
    # prepare sample file
    input_file = tmp_path / "plain.txt"
    encrypted_file = tmp_path / "encrypted.bin"
    decrypted_file = tmp_path / "decrypted.txt"
    sample_text = "Testing AES roundtrip - 12345"
    save_text(str(input_file), sample_text)

    # generate key and cipher
    key = AESCipher.generate_key(32)
    cipher = AESCipher(key)

    # encrypt file
    cipher.encrypt_file(str(input_file), str(encrypted_file))
    assert encrypted_file.exists()
    assert encrypted_file.stat().st_size > 16  # at least IV + something

    # decrypt file
    cipher.decrypt_file(str(encrypted_file), str(decrypted_file))
    result = read_text(str(decrypted_file))
    assert result == sample_text
