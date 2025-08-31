"""
Demo for hashing functions.
Computes MD5, SHA-256, and SHA-512 for a sample string and prints results.
"""

from src.hashing.hashing_algorithms import compute_md5, compute_sha256, compute_sha512

text = "Hello! This is hashing demo."

md5 = compute_md5(text)
sha256 = compute_sha256(text)
sha512 = compute_sha512(text)

print("Hashing demo:")
print("Text:", text)
print("MD5   :", md5)
print("SHA256:", sha256)
print("SHA512:", sha512)
