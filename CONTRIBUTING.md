# Contributing

- Keep APSL offline-first, Termux-first, and portable.
- Separate cryptographic services from CLI and TUI presentation.
- Keep attack demonstrations confined to synthetic local lab data.
- Never add third-party account attacks, credential collection, or session extraction.
- Never log or report plaintext passwords.
- Add tests for functional behavior and security boundaries.
- Document platform limitations and dependency changes.
- Do not claim tests passed unless they were run.

Setup: create a virtual environment, install with pip install -e ".[dev]", then run pytest and ruff check ..
