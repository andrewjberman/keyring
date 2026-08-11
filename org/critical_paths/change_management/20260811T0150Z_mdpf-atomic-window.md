# DEPLOY-COMPLETION LEDGER — MDPF ATOMIC WINDOW (RP-W1 + RP-W2 + RP-W3)

**Opened:** 2026-08-11T01:50Z by 2.0.0_SA_COO (window caller/coordinator)
**Status:** OPEN — closes only when every leg lands + the post-window QA read completes, or on full rollback
**Authority chain:** Andrew plan-order (via CTO @dbbbfa9cd3) → Andrew all-four ruling ~2334Z (Call 1
route (b): W1+W3 one atomic change; clock floor 13:30 / pulls 13:02) → COO topology decision (W2 in
the atomic set) → gate 1 DS BUILD-READY @bf74d031c1 (004145Z) → gate 2 clock ruling (satisfied
~2334Z) → precondition RP-W5b PROVEN (AE 014529Z, ledger @0a00e8f572). Andrew's clock tonight:
"This needs to be fixed tonight."

## LEGS (both land inside this window; NEITHER SHIPS ALONE; either fails → BOTH roll back in-window)

| leg | owner | content | state |
|---|---|---|---|
| L-A code cp | 0.4.0_DS_ClientPlatform | 2-file cp to s3://opal-data-mdpf/code/scripts/gold/: dim_mdpf_aggregate_aua_timeseries.py + build_mdpf_spine.py (measured invoke set; NO trio mint) from @bf74d031c1; then comp-pipescript deployed check | OPEN |
| L-B cadence apply | 0.7.0_AE_CloudOps | RP-W3: mirrors ahead of floor; floor → 13:30Z; pulls → 13:02Z; cutover-gap plan STATED pre-apply; targeted apply, plan READ (no daily-aua row possible — declaration removed by W5b); RP-W4 selector apply may ride before/with | OPEN |
| L-C QA read | AE fires, AE+DS read | ONE ad-hoc cycle post-L-A/L-B: (1) four scopes emit / which errored, (2) inflection legs carry corrected vintage, (3) inflection build reads zero smartx/** keys. FENCE: output never published, never the bar, discharges no acceptance | OPEN |

## PRE-REGISTERED READINGS (decided before evidence)
- QA read shows scopes emitting but FEEDERS STILL FROZEN → EXPECTED (separate WS-lambda mechanism,
  AE-surfaced, routed) — NOT a window failure.
- Any leg fails → both roll back inside this window; ledger closes on rollback with reason; COO
  escalates loud (no stranded leg overnight).
- 13:30Z 2026-08-11 unattended scheduled cycle = the ONLY completion-bar evidence (12/12 A4, served
  meta advancing, never S3 mtime). COO adjudicates.

## RECOVERY ANNOTATION — 20260811T025xZ (2.0.0_SA_COO respawn, PID 5820)
- COO session CRASHED mid-window (after open + GO fire; last inbound acted-on evidence: AE pre-apply
  statement 015806Z found un-acted in read/). Respawned + re-registered ~0245Z. CTO held the recovery
  picture in the interim; DS + AE respawned and directed to sync with CTO.
- Leg state at recovery: **L-B** — AE stated the cutover-gap plan pre-apply (015806Z, criterion 2 met)
  and applied ~020xZ; CTO live read reports L-B LIVE (verification evidence pointer to follow from
  CTO/AE — row flips to DONE on applied-truth evidence, not self-report). **L-A** — OPEN; DS respawned,
  reading the un-acted 014749Z GO, landing before 13:30Z. **L-C** — OPEN; fires only after L-A.
- **WINDOW RULING (COO, window caller): the crash is a COORDINATION interruption, NOT a leg failure.
  The pre-registered rollback trigger ("any leg fails → both roll back") does NOT fire on it.
  FORWARD-COMPLETE ratified (CTO recommendation, COO concurs): L-A lands, then L-C, window closes on
  the normal bar. Rollback trigger remains an actual leg FAILURE only.**
- Completion bar UNCHANGED: 13:30Z 2026-08-11 unattended scheduled cycle (12/12 A4, served meta
  advancing, never S3 mtime). COO adjudicates.

## CLOSE
- Closed: PENDING
