# IRPT_ANLREQ -- decomposition, round 23C: C-SWAP STEPS (1) AND (2), cells A to C, workstream Y (issuer 2.0.0_SA_COO~Y2, the ONE driver)

**Input:** the C-SWAP read (`AR-y-278`, record `0.9.0_WK_IRPT_ANLREQ~99/r23/C_SWAP_STEPS_1_2_READ.json`, drained @de81ce19c1) and the CTO's rulings (msg 7210): "Cut A to C. D and E are dell1's; I route them through MSTR when your cells name them." K = 10 unknown symbols checked per upload, one call each, paced at 1 s; unknowns beyond 10 get the existing proxy prompt worded "not checked"; a yfinance exception, timeout or error-shaped empty reads CHECK_FAILED, shown in words and never treated as absent (make the client raise); KEEP still requires history; no Andrew word is needed for the Yahoo egress (standing law, CLAUDE.md Agent Autonomy, Andrew-direct 2026-10-09). The PRD's C-SWAP (`prd/IRPT_ANLREQ_PRD.md` :104): `resolution_kimi`'s model-proposed swap is retired (reverted @c822052bc4); the proxy step (4) and the record (5) are later cells. MEASURED: `TIMXX` has 20 daily rows (close 1.0) and is KEPT; `ALPPL`, `BREIT`, `CCCQ` return no rows and yfinance hides the error by default.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-291` (A) | step 1: the registry identity port reads `etf-classifications` (and MDPF_SECHIST's index if a read-only way exists) as EVIDENCE, never FOUND; a read error is `registry_unavailable`; no IAM or Terraform edited | the resolver, the resident's identity argument and the session factory, two test files | WORLD |
| `AR-y-292` (B) | step 2: the yfinance history checker, a new module: cap 10, 1 s pace, exceptions raise and read CHECK_FAILED, KEPT needs history, the history port injected | one new module and its test file | WORLD |
| `AR-y-293` (C) | the KEPT state: the resolver gains `KEPT`, the freeze passes it, the upload page says so in words (and says CHECK_FAILED and "not checked" in words); no checker injected means today's behaviour | the resolver, the freeze, the words table and the lock test, one new test file | WORLD |

## Edges and chains

- None blocking the builds: the interface of the checker and the new resolver state are fixed in each order. `AR-y-291` and `AR-y-293` both edit `intake/security_resolution.py` in different functions and drain one at a time. Nothing turns on in production until a release wires the checker into the resident (a later pair: the package member, yfinance as a dependency if the resident lacks it, the table read in the resident's IAM). D (the registry row for a KEPT symbol, MDPF_SECCLASS) and E (the price landing, MDPF_SECHIST) are dell1's: the CTO routes them through MSTR once these cells name them.

fanout: 3 of 3 chains, cap 8, reason: three independent cells against a fixed checker interface; two share one file and drain in sequence.
