# Architecture

The initial package separates responsibilities:

- apsl/crypto.py: password-hashing adapters and SHA-2 demonstrations.
- apsl/audit.py: heuristic strength analysis.
- apsl/lab.py: bounded local-only dictionary experiments.
- apsl/reports.py: JSON serialization with plaintext-field rejection.
- apsl/cli.py: command parsing and terminal presentation.
- apsl/tui.py: optional Textual dashboard.

The interfaces must call application services; they must not implement cryptographic logic. Future modules should expose small, testable functions.
