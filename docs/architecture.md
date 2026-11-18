# Architecture

APSL is an offline-first password-security research project. The current 0.1.0 implementation is a Python research foundation. The product direction is an Android application whose primary interaction surface is a terminal-style interface.

## Current Python foundation

- apsl/crypto.py: password-hashing adapters and SHA-2 demonstrations.
- apsl/audit.py: heuristic strength analysis.
- apsl/lab.py: bounded local-only dictionary experiments.
- apsl/reports.py: JSON serialization with plaintext-field rejection.
- apsl/cli.py: command parsing and terminal presentation.
- apsl/tui.py: optional Textual TUI.

## Target Android application

The Android app presents the research core through a terminal-first UI. The terminal is the primary app experience, not a decorative console embedded in a card dashboard. Keep the UI layer separate from cryptographic and authentication services so the same tested services can be called by the CLI, TUI, and Android interface.

Terminal rendering requirements are specified in terminal_ui_spec.md:
- preserve the supplied startup transcript and deliberate whitespace;
- prefix every runtime terminal output line with [π°];
- use a monospace font and preserve spaces rather than collapsing them;
- apply semantic status colours without changing text geometry;
- keep the command prompt/input column stable;
- wrap long lines deliberately on narrow screens, retaining the prefix and readable continuation indentation.

## Security boundaries

All password experiments must operate on synthetic lab accounts, user-provided lab hashes, or other explicitly owned local test data. The Android app must not automate or attempt authentication against Instagram, Facebook, Meta, or any third-party service. Keep network authentication disabled; the lab should work offline by default.

Future modules should expose small, testable functions. UI code calls application services and does not implement cryptographic logic itself.
