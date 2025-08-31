# Algorithm explanations

## AES (Advanced Encryption Standard)
- Symmetric cipher — same key used for encryption and decryption.
- Implemented here: AES-256 in CBC mode.
- Uses a random 16-byte IV (initialization vector).
- Uses PKCS#7 padding to make plaintext a multiple of AES block size (16 bytes).

## RSA
- Asymmetric: public key (encrypt) and private key (decrypt).
- Implemented using RSA key pair via PyCryptodome.
- Uses OAEP padding (PKCS1_OAEP) for safe encryption of small messages.

## Hashing
- Hash functions included: MD5 (demo only), SHA-256, SHA-512.
- Hash functions are one-way: used for checksums, integrity checks, not encryption.

## Notes and security
- RSA is used here for small messages (or encrypting symmetric keys), not bulk data.
- AES is used for bulk data encryption.
- Keep private keys and secret keys safe; do not hard-code keys into production code.
