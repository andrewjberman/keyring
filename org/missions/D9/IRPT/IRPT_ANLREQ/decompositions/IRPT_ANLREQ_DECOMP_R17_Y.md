# IRPT_ANLREQ -- decomposition, round 17, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's round-17 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_17_20261012.md` @a493793845
(no PRD addendum; PRD v0.4 stands) answering the round-16 slug `REMEDIATION_v9.md`, and the CVO's L9 grade
`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_16_L9_GRADE_20261012.md` @54382c3f9d (2 PASS, 1 FAIL: `AR162-y-AC3J`).

**Thread:** FWD-1 is not live. Nothing of the upload check is released; this round repairs the re-landed reader and prepares its release pair.

## How the ENRICHMENT LIST maps (CTO section 2)

| item | carrier |
|---|---|
| 1. the account-header rule's repair (row W52-S20), with a negative control | cell `AR-y-171` |
| 2. the S48 cell on the STATUS rule (row W53-S10), built; its pair carries a census | cell `AR-y-172` (the build) and cell `AR-y-173` (the read-only census script, whose one run is a separate order to an applier) |
| 3. the re-landed reader's release pair, tracing the mixed-version case (row W52-S18), cut only after item 1 merges | cell `AR-y-174` (the trace, read-only) after `AR-y-171`; the pair itself is the issuer's act on its record |

**Standing, not a cell (row `IRPT_ANLREQ-D2-W53-S9`, owner this seat):** no rebuild of `irpt-ycharts-generate` is cut by any lane until each of its
four unpinned members is pinned or released under its own pair.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-171` | the reader splits a header on hyphen and slash before the leading word; the measured attribute forms join the whole-cell exclusions, each with its census line and reason; a sentence on whether a last-word match is admitted; `READER_VERSION` and the pin digest move in the same commit; the population read again | `intake/template_reader.py`, the intake reader tests, the worker's deliverables | WORLD (the path's floor; BUILT, not released) |
| `AR-y-172` | the investor-reporting internal reader admits an internal caller that selects a firm only on a users row whose `status` is exactly `active`; a caller with NO row, or a disabled or absent status, is refused FIRM_BINDING; service and client callers unchanged | `_authz/served.py`, `_authz/tests/test_internal_status_active.py` | WORLD (BUILT, not released) |
| `AR-y-173` | a read-only counting script, proven offline on synthetic rows: internal users rows whose status is not exactly `active`, by firm and status value; and, where the function's logs carry the caller, the distinct internal callers with no row. Counts only | the worker's deliverables | LOCAL |
| `AR-y-174` | a read-only trace of the mixed-version case: every consumer of `template_reader` / `READER_VERSION`, and what each of the four writer/reader version pairs does, run in process on the two readers | the worker's deliverables | LOCAL |

## Edges and chains

- `AR-y-171` -> `AR-y-174`: the trace is cut after the repair merges, so it traces the reader that will be released. One queue, slot ~52.
- `AR-y-172`, `AR-y-173` have no edge. M = 3 chains: {171, 174}, {172}, {173}.

fanout: 3 of 3 chains, cap 8, reason: three independent chains; `AR-y-174` waits on the merge of `AR-y-171`.
