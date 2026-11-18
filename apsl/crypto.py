"""Password hashing and digest demonstrations."""

import hashlib
import hmac
import secrets

import bcrypt
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError, VerifyMismatchError

DEFAULT_PBKDF2_ITERATIONS = 600_000
_ARGON2 = PasswordHasher(
    time_cost=3, memory_cost=65_536, parallelism=2, hash_len=32, salt_len=16
)


def hash_password(
    password: str,
    algorithm: str = "argon2id",
    *,
    pbkdf2_iterations: int = DEFAULT_PBKDF2_ITERATIONS,
    bcrypt_rounds: int = 12,
) -> str:
    if not isinstance(password, str) or not password:
        raise ValueError("Password must be a non-empty string.")
    if algorithm == "argon2id":
        return _ARGON2.hash(password)
    if algorithm == "bcrypt":
        if not 4 <= bcrypt_rounds <= 16:
            raise ValueError("bcrypt rounds must be between 4 and 16.")
        result = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=bcrypt_rounds))
        return result.decode("ascii")
    if algorithm == "pbkdf2":
        if not 100_000 <= pbkdf2_iterations <= 5_000_000:
            raise ValueError("PBKDF2 iterations must be between 100,000 and 5,000,000.")
        salt = secrets.token_bytes(16)
        dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, pbkdf2_iterations)
        return f"pbkdf2_sha256${pbkdf2_iterations}${salt.hex()}${dk.hex()}"
    raise ValueError("Choose argon2id, bcrypt, or pbkdf2.")


def verify_password(password: str, encoded_hash: str) -> bool:
    if not isinstance(password, str) or not isinstance(encoded_hash, str):
        return False
    try:
        if encoded_hash.startswith("$argon2id$"):
            return _ARGON2.verify(encoded_hash, password)
        if encoded_hash.startswith("$2"):
            return bcrypt.checkpw(password.encode(), encoded_hash.encode("ascii"))
        if encoded_hash.startswith("pbkdf2_sha256$"):
            parts = encoded_hash.split("$")
            if len(parts) != 4:
                return False
            _, count, salt_hex, expected_hex = parts
            iterations = int(count)
            if not 100_000 <= iterations <= 5_000_000:
                return False
            actual = hashlib.pbkdf2_hmac(
                "sha256", password.encode(), bytes.fromhex(salt_hex), iterations
            )
            return hmac.compare_digest(actual, bytes.fromhex(expected_hex))
    except (
        ValueError,
        TypeError,
        UnicodeError,
        VerificationError,
        VerifyMismatchError,
        InvalidHashError,
    ):
        return False
    return False


def digest_text(value: str, algorithm: str = "sha256") -> str:
    if algorithm not in {"sha256", "sha512"}:
        raise ValueError("Choose sha256 or sha512.")
    return hashlib.new(algorithm, value.encode()).hexdigest()
