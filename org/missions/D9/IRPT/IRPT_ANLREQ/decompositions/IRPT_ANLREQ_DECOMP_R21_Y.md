# IRPT_ANLREQ -- decomposition, round 21, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's round-21 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_21_20261013.md` (msg 6988) answering the round-20 slug and the CVO's grade `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_20_L9_GRADE_20261013.md` (AR211-y-AC3J FAIL). Enrichment list items 1 to 3 in this issuance; item 4 (the r19.3 two-leg release pair) follows item 1 and is not a cell.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-221` | the r19.2 backstop rebuilt on the ALLOWLIST (a root header enters only when every other word is an identifier-tail word; `alias` a tail word, `primary` a modifier), `READER_VERSION` r19.3, the CVO's six neighbours as controls | `intake/template_reader.py` and its tests | WORLD (built, not released) |
| `AR-y-222` | `infra/aws/lambda/ci/build-and-upload.sh` verify step fixed: a landed upload verifies, exits 0 and updates the map; a failing head-object exits non-zero with the CLI's error printed; shown on two offline arms | the script and a new ci test file | WORLD (offline arms only) |
| `AR-y-223` | the DESIGN of the driven status-rule exercise (identities, request, expected outcomes predicted offline, log lines, removal) from the R2-cw-1 precedent; nothing is minted | the worker's deliverables | LOCAL |

## Edges and chains

- None among the three. `AR-y-221` feeds the r19.3 release pair (item 4); `AR-y-223` feeds the exercise's never-widen pair; `AR-y-222` feeds a live scratch-key arm run by an applier. M = 3 chains.

fanout: 3 of 3 chains, cap 8, reason: three independent build-and-prove or read cells.
