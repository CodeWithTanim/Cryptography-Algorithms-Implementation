from src.hashing.hashing_algorithms import compute_md5, compute_sha256, compute_sha512

def test_hash_lengths():
    data = "abc123"
    md5 = compute_md5(data)
    sha256 = compute_sha256(data)
    sha512 = compute_sha512(data)

    assert len(md5) == 32  # 128-bit hex
    assert len(sha256) == 64  # 256-bit hex
    assert len(sha512) == 128  # 512-bit hex

def test_hash_consistency():
    data = "same input"
    assert compute_sha256(data) == compute_sha256(data)
