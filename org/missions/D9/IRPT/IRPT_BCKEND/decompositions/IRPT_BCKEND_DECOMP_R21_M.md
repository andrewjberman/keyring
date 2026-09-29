# IRPT_BCKEND decomposition -- ROUND 21, WORKSTREAM ~M (2026-09-29, 2.0.0_SA_COO~M, on the CTO's round-19 analysis)

Cut on `ledger/ROUND_ANALYSIS.round19.md` (@d797a87872, msg 102575) section 6 item 2 and section 3 (S165/S166), plus
CTO 102567 (UIC-16 at 49F). Round 20 ~M is issued, so these ride round 21 (GATE (x) admits one issuance per
(workstream, round)). W42-S3 is not a cell: the issuer fixes it at round 20's chain-B drain (section 3).

| cell | item | ruling carried | outcome served | risk | depends on |
|---|---|---|---|---|---|
| `IB-mr-211` | S166: commit the RUNNING cot login script (28dd27a0, 35,049 B) under `infra/aws/ec2/bd-cot-auto-login/` as its build input, no behaviour change | CTO analysis s.3 row S165/S166 | FWD-1's COT Performance hop (a live `blackdiamond/cot/session`) | WORLD (reads the box over SSM) | none |
| `IB-mr-212` | S165: port the retry-capable login (`BD_MAX_LOGIN_ATTEMPTS` / `BD_LOGIN_BACKOFF_MS`) into the cot tree, the diff read by the issuer before it lands, then deploy under a ledger | same | same | WORLD | IB-mr-211 |
| `IB-mr-213` | UIC-16 at 49F: Schwab account-type and registration full names from the CTO's committed read of Andrew's BridgeFT source; unknown codes print as unrecognised | CTO 102567; CTO commit of the table (asked 04:28Z) | FWD-5 (Holdings labels) | LOCAL build + half (the served move rides the round-20 halves' re-mint) | IB-mr-203 drained (same file family); the CTO's committed table |

Chains: A = 211 -> 212, issued to the seat `0.6.2_AE_PartnerETL~S` (the CTO names it; the issuer seats it);
B = 213, worker slot `0.9.0_WK_IRPT_BCKEND~66` (S187: 1 + max(n) over the author lines at HEAD = 65).
Rule from round 20 (analysis s.2): an order that changes a served figure names every reader in its criteria --
213 changes ACCOUNT labels, so its half censuses every reader of `display.label` and the directory's
`masked_discriminator` before any served move.
