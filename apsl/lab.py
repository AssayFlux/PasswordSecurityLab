"""Bounded offline dictionary simulation against one explicitly supplied lab hash."""

from pathlib import Path
from apsl.crypto import verify_password

MAX_DICTIONARY_ATTEMPTS = 100_000
MAX_WORDLIST_BYTES = 5 * 1024 * 1024


def dictionary_simulation(encoded_hash: str, wordlist_path: str | Path, *,
                          max_attempts: int = 10_000) -> dict[str, object]:
    if not 1 <= max_attempts <= MAX_DICTIONARY_ATTEMPTS:
        raise ValueError(f"max_attempts must be between 1 and {MAX_DICTIONARY_ATTEMPTS}.")
    path = Path(wordlist_path).expanduser()
    if not path.is_file():
        raise FileNotFoundError(path)
    if path.stat().st_size > MAX_WORDLIST_BYTES:
        raise ValueError("Wordlist exceeds 5 MiB.")
    attempts = 0
    matched = False
    with path.open(encoding="utf-8", errors="strict") as stream:
        for line in stream:
            if attempts >= max_attempts:
                break
            attempts += 1
            if verify_password(line.rstrip("\r\n"), encoded_hash):
                matched = True
                break
    return {"experiment": "local_dictionary_simulation", "attempts": attempts,
            "matched": matched, "target_scope": "one explicitly supplied local lab hash",
            "plaintext_included": False, "limit": max_attempts}
