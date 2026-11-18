# Security model

## Assets
User-entered passwords, encoded hashes, synthetic wordlists, experiment metadata, and local reports.

## Trust boundaries
Experiments are local. APSL sends no passwords, hashes, wordlists, or reports over a network. Network access is needed only to install dependencies.

## Controls
- Password prompts use hidden terminal input.
- Password hashes use library-managed salts.
- Verification delegates to established libraries or constant-time digest comparison.
- Dictionary simulation accepts one explicit hash and one explicit wordlist, with candidate and file-size ceilings.
- Reports reject obvious plaintext-password field names.

## Limitations
The auditor is heuristic, not a crack-time predictor. APSL is research software, not a production identity system. Native package support and resource limits vary across Android devices.
