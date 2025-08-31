from src.asymmetric.rsa_encryption import RSAHelper

def test_rsa_encrypt_decrypt():
    private_key, public_key = RSAHelper.generate_keypair(2048)
    message = b"small message for rsa"
    ciphertext = RSAHelper.encrypt_message(public_key, message)
    assert ciphertext != message
    plaintext = RSAHelper.decrypt_message(private_key, ciphertext)
    assert plaintext == message
