"""APSL command-line interface."""

import argparse
import getpass
import json
import sys
from pathlib import Path

from rich.console import Console
from rich.panel import Panel

from apsl import __version__
from apsl.audit import audit_password
from apsl.crypto import digest_text, hash_password, verify_password
from apsl.lab import dictionary_simulation
from apsl.reports import write_json_report

console = Console()


def build_parser():
    parser = argparse.ArgumentParser(prog="apsl", description="AssayFlux Password Security Lab")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    subs = parser.add_subparsers(dest="command")
    h = subs.add_parser("hash").add_subparsers(dest="action", required=True)
    create = h.add_parser("create")
    create.add_argument("--algorithm", choices=["argon2id", "bcrypt", "pbkdf2"], default="argon2id")
    create.add_argument("--output")
    verify = h.add_parser("verify")
    verify.add_argument("--hash", dest="encoded_hash", required=True)
    a = subs.add_parser("audit")
    a.add_argument("--report")
    lab = subs.add_parser("lab").add_subparsers(dest="action", required=True)
    d = lab.add_parser("dictionary")
    d.add_argument("--hash", dest="encoded_hash", required=True)
    d.add_argument("--wordlist", required=True)
    d.add_argument("--max-attempts", type=int, default=10_000)
    d.add_argument("--report")
    digest = subs.add_parser("digest")
    digest.add_argument("--algorithm", choices=["sha256", "sha512"], default="sha256")
    subs.add_parser("tui", help="Open the optional interactive terminal dashboard")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return
    try:
        if args.command == "hash" and args.action == "create":
            value = hash_password(getpass.getpass("Synthetic lab password: "), args.algorithm)
            if args.output:
                Path(args.output).expanduser().write_text(value + "\n", encoding="utf-8")
                console.print(f"Hash saved to {args.output}")
            else:
                console.print(Panel(value, title=args.algorithm))
        elif args.command == "hash" and args.action == "verify":
            ok = verify_password(getpass.getpass("Password: "), args.encoded_hash)
            console.print("[green]MATCH[/green]" if ok else "[red]NO MATCH[/red]")
        elif args.command == "audit":
            result = audit_password(getpass.getpass("Password to audit (not stored): "))
            console.print_json(json.dumps(result))
            if args.report:
                write_json_report(result, args.report)
        elif args.command == "lab" and args.action == "dictionary":
            result = dictionary_simulation(args.encoded_hash, args.wordlist, max_attempts=args.max_attempts)
            console.print_json(json.dumps(result))
            if args.report:
                write_json_report(result, args.report)
        elif args.command == "digest":
            console.print(digest_text(getpass.getpass("Demonstration input: "), args.algorithm))
            console.print("[yellow]Digest demonstration only; not password storage.[/yellow]")
        elif args.command == "tui":
            from apsl.tui import run_tui
            run_tui()
    except (ValueError, OSError) as exc:
        console.print(f"[red]Error:[/red] {exc}")
        sys.exit(2)


if __name__ == "__main__":
    main()
