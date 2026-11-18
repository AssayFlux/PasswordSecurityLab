# AssayFlux Password Security Lab

**APSL** is an offline-first password-security research project, developed Termux-first. Its product direction is an Android app with a terminal-first interface; the current 0.1.0 foundation is a Python CLI with an optional Textual TUI.

> **Authorized laboratory use only.** Experiments are restricted to synthetic credentials and hashes created for your own local lab. APSL does not attack online accounts, connect to third-party login services, collect credentials, or extract sessions.

## Identity and status

- Product: AssayFlux Password Security Lab
- Powered by: AssayFlux Cyber Security
- Operation identity: AssayFlux White Hat ©
- Version: 0.1.0
- Current implementation: Python CLI and optional TUI
- Product direction: Android app with a terminal-style interface

## Initial capabilities

- Argon2id, bcrypt, and PBKDF2-HMAC-SHA256 password hashing and verification.
- SHA-256 and SHA-512 demonstrations (not suitable for password storage).
- Basic password-strength heuristics.
- Bounded dictionary simulation against one explicitly supplied local lab hash.
- JSON reports without plaintext password fields.
- CLI and optional TUI entry points.

## Terminal interface direction

The Android app's primary interface is a terminal, not a dashboard made of cards. Its exact startup text, whitespace rules, [π°] line prefix, status colours, wrapping behaviour, and command prompt are documented in docs/terminal_ui_spec.md. Treat that document's startup transcript as the golden visual reference.

## Install the current Python foundation

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

## Run the current Python foundation

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
