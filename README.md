# AssayFlux Password Security Lab

**APSL** is an offline-first Python password-security research toolkit, developed Termux-first and designed to remain portable.

> **Authorized laboratory use only.** Experiments are restricted to synthetic credentials and hashes created for your own local lab. APSL does not attack online accounts, connect to third-party login services, collect credentials, or extract sessions.

## Status

Version 0.1.0 · Early development · CLI plus optional Textual TUI.

## Initial capabilities

- Argon2id, bcrypt, and PBKDF2-HMAC-SHA256 password hashing and verification.
- SHA-256 and SHA-512 demonstrations (not suitable for password storage).
- Basic password-strength heuristics.
- Bounded dictionary simulation against one explicitly supplied local lab hash.
- JSON reports without plaintext password fields.
- CLI and optional TUI entry points.

## Install

~~~bash
pkg update && pkg upgrade
pkg install python clang rust libffi openssl git
git clone https://github.com/AssayFlux/PasswordSecurityLab.git
cd PasswordSecurityLab
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -e ".[dev]"
~~~

## Run

~~~bash
apsl --help
apsl hash create --algorithm argon2id
apsl hash verify --hash '<encoded-hash>'
apsl audit
apsl lab dictionary --hash '<lab-hash>' --wordlist ./synthetic.txt --max-attempts 1000
apsl tui
pytest
~~~

Password entry uses hidden terminal prompts. Avoid passing actual passwords as command-line arguments. See docs/termux_setup.md, docs/security_model.md, SECURITY.md, and docs/roadmap.md.

Designed by **AssayFlux**. Licensed under Apache-2.0; see LICENSE.
