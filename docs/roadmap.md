# Roadmap

Milestones are targets. Mark features complete only after implementation and verification. The Android app is a planned product track; do not describe planned Android features as already implemented.

## 0.1.0 Foundation — current Python baseline
- [x] Python package, CLI, optional Textual TUI
- [x] Argon2id, bcrypt, PBKDF2 and SHA-2 demonstrations
- [x] Heuristic password audit
- [x] Bounded local dictionary simulation
- [x] JSON reporting and initial tests
- [x] Initial architecture, security and Termux documentation

## 0.2.0 Research core
- [ ] Hash metadata inspection
- [ ] Improved pattern and passphrase analysis
- [ ] Bounded brute-force search-space simulator
- [ ] Reproducible experiment manifests
- [ ] CSV and HTML reporting

## 0.3.0 Authentication research
- [ ] Local synthetic-account login simulator
- [ ] Rate limiting and lockout experiments
- [ ] Session lifetime demonstrations
- [ ] Defensive timing comparisons
- [ ] Instagram-/Facebook-style local simulation only; no real Meta login attempts or network authentication

## Android app — terminal-first product track
- [ ] Define Android application shell and lifecycle
- [ ] Implement terminal view with monospace rendering and preserved whitespace
- [ ] Reproduce docs/terminal_ui_spec.md startup transcript exactly
- [ ] Apply mandatory [π°] prefix to every runtime output line
- [ ] Implement stable prompt/input row and command history
- [ ] Implement width-aware wrapping without losing alignment or spaces
- [ ] Implement semantic terminal colours and accessible contrast
- [ ] Connect terminal commands to shared research-core services
- [ ] Keep lab data local; offline operation is the default
- [ ] Verify narrow-screen behaviour and copy/select text

## 0.4.0 Benchmarking
- [ ] CPU and memory benchmarks
- [ ] Environment metadata and reproducible results
- [ ] Expanded research workflows and terminal output

## 1.0.0 Stable research release
- [ ] Android app feature-complete and tested on supported devices
- [ ] Full automated test matrix
- [ ] Dependency and security review
- [ ] Complete documentation and release validation
