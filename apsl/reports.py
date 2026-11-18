"""Privacy-conscious JSON reporting."""

import json
from pathlib import Path


def write_json_report(data: dict, destination: str | Path) -> Path:
    forbidden = {"password", "plaintext_password", "candidate_password"}
    if forbidden.intersection(key.lower() for key in data):
        raise ValueError("Reports must not contain plaintext-password fields.")
    path = Path(destination).expanduser()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path
