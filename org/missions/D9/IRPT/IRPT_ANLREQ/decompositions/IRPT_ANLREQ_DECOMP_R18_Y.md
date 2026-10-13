# IRPT_ANLREQ -- decomposition, round 18, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's round-18 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_18_20261012.md` @17bd7c9f43 (no PRD addendum; PRD v0.4 stands) answering the round-17 slug `REMEDIATION_v10.md` @5cf791e25f and the CVO's L9 grade (4 PASS; 5 rows OPEN, 2 ARMED).

**Thread:** FWD-1 is not live. Nothing of the upload check or the status rule is released; this round widens the header rule, counts what the old runtime stored, makes six test arms bite, and re-cuts the status rule's pair.

## How the ENRICHMENT LIST maps (CTO section 2)

| item | carrier |
|---|---|
| 1. the vocabulary widening and the `No. of Accounts` exclusion (row S24), with negative controls | cell `AR-y-181` |
| 2. the round-16 NORMALIZED count and disposition (row S29), read-only | cell `AR-y-182`: the existing count script run with the repaired reader by the seat that holds the decrypt; an ISSUER order to the laptop seat, cut after `AR-y-181` merges (no worker builds it) |
| 3. the test cell that makes each arm bite (row W54-S7) | cell `AR-y-183` |
| 4. the status rule's pair, re-cut: all eight functions named with their `served.py` pins, the caller-class log line, the population UNKNOWN until counted | cells `AR-y-184` (the ONE log line, built) and `AR-y-185` (the read of the eight functions and their pins); the pair itself is the issuer's act on their records |
| 5. the reader's release pair, the Lambda's third reader included, cut only after items 1 and 2 merge | cell `AR-y-186` (the trace extended by the third reader, after `AR-y-181`); the pair itself is the issuer's act |

**Standing, not a cell (row `IRPT_ANLREQ-D2-W53-S9`, owner this seat):** no rebuild of `irpt-ycharts-generate` is cut by any lane until each of its four unpinned members is pinned or released under its own pair.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-181` | the identifier vocabulary widened (`brokerage`, `ira`, `joint` as modifiers; `subaccount` as an account word; `seq`, `sequence` as identifier words) and `No. of Accounts` (a COUNT) a whole-cell exclusion with `No. of Account` still matching; each with its census line and a negative control named and committed BEFORE the change; `READER_VERSION` and the pin digest move in the same commit | `intake/template_reader.py`, the intake reader tests, the worker's deliverables | WORLD (BUILT, not released) |
| `AR-y-182` | the count of round-16 stored inputs the repaired reader would turn back, by cause, whether a report was generated and when last: counts only | the laptop seat's deliverables | WORLD (read-only) |
| `AR-y-183` | six new tests, one per final-release arm, each making its arm FAIL when its named check alone is removed | `_authz/tests/test_final_release_bites.py` | WORLD (tests only) |
| `AR-y-184` | ONE log line in `served.py` naming the caller CLASS of an internal caller that selects another firm (row present, row absent, row non-active) and the outcome; no identity | `_authz/served.py`, `_authz/tests/test_caller_class_log.py` | WORLD (BUILT, not released) |
| `AR-y-185` | a read: each of the eight functions that package `served.py`, how it packages it, its pin, and whether its tests run the pinned or the live file | the worker's deliverables | LOCAL |
| `AR-y-186` | the mixed-version trace extended by the Lambda's third, unversioned reader (pin `3f29017cfc`) against the repaired one | the worker's deliverables | LOCAL |

## Edges and chains

- `AR-y-181` -> `AR-y-186` and `AR-y-181` -> `AR-y-182`: the trace and the count run on the reader that will be released. Slot ~52 holds 181 then 186; the count is the issuer's order.
- `AR-y-183`, `AR-y-184`, `AR-y-185` have no edge. M = 4 worker chains: {181, 186}, {183}, {184}, {185}; `AR-y-182` is the issuer's order after `AR-y-181`.

fanout: 4 of 4 chains, cap 8, reason: four independent worker chains; `AR-y-186` and the count `AR-y-182` wait on the merge of `AR-y-181`.
