"""Optional Textual terminal dashboard."""


def run_tui() -> None:
    try:
        from textual.app import App, ComposeResult
        from textual.containers import Container
        from textual.widgets import Footer, Header, Static
    except ImportError as exc:
        raise SystemExit('Install the TUI extra: pip install ".[tui]"') from exc

    class APSLApp(App):
        CSS = "Screen { align: center middle; } #panel { width: 90%; max-width: 72; border: round $accent; padding: 1 2; }"
        TITLE = "AssayFlux Password Security Lab"
        SUB_TITLE = "Local educational research environment"

        def compose(self) -> ComposeResult:
            yield Header()
            with Container(id="panel"):
                yield Static("[b]APSL 0.1.0[/b]\n\nPassword hashing and verification\nPassword strength audit\nBounded local dictionary experiment\n\nUse apsl --help for commands.\nAll experiments are local and authorized-only.")
            yield Footer()

    APSLApp().run()
