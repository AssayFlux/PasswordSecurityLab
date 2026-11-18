# Termux setup

APSL requires no root access.

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

Run apsl --help, apsl hash create --algorithm argon2id, apsl audit, apsl tui, and pytest.

Native dependency compatibility can vary by Android architecture and Termux version. If installation fails, record the package, Python version, architecture, and complete compiler error before changing constraints. Do not silently remove Argon2id or bcrypt.
