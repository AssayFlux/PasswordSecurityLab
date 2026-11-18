# Terminal UI Specification

**Status:** Approved visual direction for the Android app  
**Product:** AssayFlux Password Security Lab (APSL)  
**Version shown:** 0.1.0

This is the source of truth for the terminal's visual layout. The primary Android app experience is a terminal, not a dashboard made of cards.

## Product identity

- App name: AssayFlux Password Security Lab
- Powered By: AssayFlux Cyber Security
- Operation: AssayFlux White Hat ©
- Terminal line marker: [π°]
- Default mode: OFFLINE
- Initial status: READY

## Golden startup transcript

Preserve this reference's wording, line order, punctuation, and deliberate spaces. Render it in a monospace surface with whitespace preservation.

~~~text
AssayFlux Password Security Lab
Powered By : AssayFlux Cyber Security
Operation.    : AssayFlux White Hat ©
─────────────────────────────────────
VERSION  :       0.1.0
MODE      :       OFFLINE
STATUS    :       READY
[π°]  ─────────────────────────────────────
[π°]  [SUCCESS]        Terminal initialized
[π°]  [INFO]               Local database connected
[π°]  [WARNING]       No lab accounts found
[π°]  [SECURITY]       Online access disabled
[π°]  [CRYPTO]          Argon2id module available
[π°]  [AUTH]              Authentication lab ready
[π°]  AssayFlux White Hat ©
[π°]  _
~~~

The identity header and metadata before the first [π°] divider intentionally remain unprefixed. After that divider, every runtime terminal output line begins with [π°]. The final underscore is the initial command-entry cursor position.

## Whitespace and alignment rules

1. Use a true monospace font and whitespace-preserving renderer. Never collapse repeated spaces.
2. Treat the transcript above as the visual acceptance fixture. Do not replace its spacing with a newly invented universal colon or separator layout.
3. Keep the command-entry position in one consistent vertical column on every prompt.
4. Preserve the deliberate label-to-message spacing in the sample. Do not add colons after status labels.
5. Do not use proportional fonts, automatic text justification, or unpredictable word reflow.
6. On narrow screens, wrap long output without losing content. Prefix continuation rows with [π°] and indent continuation text consistently.
7. Copy, selection, and export must preserve meaningful spaces and line breaks.
8. Colour styling must not alter the underlying text or its alignment.

## Semantic colour palette

| Colour family | Suggested hex | Meaning |
|---|---|---|
| Coral / red | #FF6B6B / #FF7777 | Critical errors and blocked operations |
| Orange | #FFB86B | High-risk findings |
| Yellow | #E5C15B | Warnings |
| Lime | #B9D66D | Active work and progress |
| Green | #69D391 | Success and completed operations |
| Turquoise | #36CFC9 | Completed checks |
| Teal | #35D0B0 | Authentication and trusted local state |
| Cyan | #42D9E8 | System information and headings |
| Blue | #80B8FF | Commands and navigation |
| Indigo | #8B9CFF | Analysis |
| Purple | #C39BEB | Cryptography |
| Pink | #E5A4D7 | Reports and statistics |
| Grey | #A0AAA4 | Metadata and timestamps |
| White | #FFFFFF | Primary output |

Maintain readable contrast. Pair colour with textual labels so meaning is not conveyed by colour alone.

## Runtime output conventions

- Prefix every runtime output line with [π°]: information, status, errors, progress, separators, command echoes, and prompts.
- The supplied identity header and metadata block are the explicit exception before the first prefixed divider.
- Use semantic labels such as [SUCCESS], [INFO], [WARNING], [SECURITY], [CRYPTO], and [AUTH].
- Never claim a module is available unless it has actually initialized.
- Default to OFFLINE. Authentication research uses synthetic local accounts only.

## Acceptance checklist

- [ ] Startup transcript matches the reference in wording, order, punctuation, and spaces.
- [ ] Header and metadata remain unprefixed; subsequent runtime lines begin with [π°].
- [ ] Command input begins at the same horizontal position on every prompt.
- [ ] Repeated spaces survive rendering, copy, and export.
- [ ] Status classes use the documented semantic palette.
- [ ] Long output wraps cleanly on narrow Android screens.
- [ ] Text remains readable without colour.
- [ ] No credentials are sent to third-party login services.
