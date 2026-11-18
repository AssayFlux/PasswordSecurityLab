import pytest

from apsl.audit import audit_password
from apsl.crypto import digest_text, hash_password, verify_password
from apsl.lab import dictionary_simulation


@pytest.mark.parametrize("algorithm", ["argon2id", "bcrypt", "pbkdf2"])
def test_hash_verify(algorithm):
    encoded = hash_password("synthetic-lab-password", algorithm)
    assert verify_password("synthetic-lab-password", encoded)
    assert not verify_password("wrong-password", encoded)


def test_pbkdf2_bounds():
    with pytest.raises(ValueError):
        hash_password("synthetic", "pbkdf2", pbkdf2_iterations=1)


def test_sha2_demo():
    assert len(digest_text("sample", "sha256")) == 64
    assert len(digest_text("sample", "sha512")) == 128


def test_audit_does_not_return_password():
    result = audit_password("password123")
    assert result["findings"]
    assert "password" not in result


def test_dictionary_is_bounded_and_local(tmp_path):
    words = tmp_path / "synthetic.txt"
    words.write_text("first\\nlab-secret\\n", encoding="utf-8")
    encoded = hash_password("lab-secret", "pbkdf2", pbkdf2_iterations=100_000)
    result = dictionary_simulation(encoded, words, max_attempts=10)
    assert result["matched"] is True
    assert result["attempts"] == 2
    assert result["plaintext_included"] is False


def test_dictionary_limit(tmp_path):
    words = tmp_path / "words.txt"
    words.write_text("one\\n", encoding="utf-8")
    with pytest.raises(ValueError):
        dictionary_simulation("not-a-hash", words, max_attempts=100_001)
