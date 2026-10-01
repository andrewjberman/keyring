# MDPF_SECCLASS -- rounds 4 and 5 (chain A): L8 compile and L9 review (`3.0.0_SA_CVO`)

**Packets:** `2.0.0_SA_COO~M` 103328: `DRAIN_END_R4_20260930.md` @044157b073 (SC-e10) and
`DRAIN_END_R5_CHAIN_A_20260930.md` @1fb1c96bf6 (SC-e11). Both orders `complete` at HEAD, `<risk>WORLD`, issuer re-runs
3 of 3 and proofs VALID. **Outside this compile:** SC-e12 (`parked`, `0.7.0_AE_CloudOps`, CTO 103327).
**Watermark:** 2026-09-30T14:39Z. **Carriers:** `ADJUDICATION_v3.md` (C-S8..C-S10) and `REMEDIATION_v3.md` (S4 new), with
S3 and W5-S3 closed IN PLACE in `REMEDIATION_v2.md` by their clocks alone (the row gate admits only disarm,
remediation and closed moving in place, and refuses a remediation id re-stated in a second document). This review is
the disarm evidence for both. W6-S2 is unchanged in its carrier: the parked TO-SC-e12 names its new owner. Co-committed.

## L9

No order carries a JUDGMENT criterion (0 in 2 files). L9 is vacuous.

## What this seat read live or at HEAD (17:3xZ to 17:5xZ)

| read | result | bears on |
|---|---|---|
| `etf-classifications` scan COUNT | 2,657 rows; 348 `CUSIP:`-keyed; `classified_by` scheduled 2,281 / legacy 238 / seed 138 (sum 2,657); `model` 0 | the CUSIP act served as the ledger says (348 of 349); MODEL_ROWS not yet written, consistent with its unsigned half |
| `etf-classifications` get VNQI | alternatives / International Real Estate, `classified_by` seed, `last_updated` 13:48:39Z | FWD-3's first correction served, as the round-4 packet says |
| `bd-securities` scan `begins_with(ticker,'CUSIP:')` | 0 of 10,929 scanned; control `begins_with 'A'` 293 | the CUSIP guard holds against real rows (W9-S1) |
| `r27_suite_whole.py` over `investor_reporting/tests` at c812be9885 | SUITE-WHOLE 319 passed, rc=0 | S3's own disarm test passes: closed |
| `git fetch` + `rev-list` | origin CLOUD 410818259a; local 60 ahead, 0 behind | W5-S3 closed |
| `missions-tree-index.py check` | RESULT: 0 violation(s) | W9-S3 closed |
| `etf_classification_model.py:45-50,174` | MAX_TOKENS 4000 with the probe recorded | W8-S1 closed |
| `label-legacy-classified-by.py:89`, `set-instrument-kind.py:96` | `attribute_not_exists(<attr>)` only | S4 still latent: graduated |
| `shared-infra/main.tf:402-407` | the write grant, last touched 2026-06-16 | W6-S2 stays ARMED |

Not re-run by this seat: SC4-e10-AC2's MODEL-CENSUS (it calls Kimi K3; Andrew's per-use word is the issuer's for that
use). The 260 / 130 figures are the issuer's re-run on CLOUD.

## Rows: 6 undispositioned, all compiled; 3 carried rows re-graded

| row | disposition | basis |
|---|---|---|
| W8-S1 | dismissed (C-S8) | the measured budget is in the shipped module |
| W8-S2 | dismissed (C-S9) | a harness property; no artifact moved |
| W9-S1, W9-S2, W9-S3 | dismissed (C-S10) | guard exercised live; truthful count; index fixed |
| S4 (INERT) | graduated to 2.0.0_SA_COO~M, round-6 hygiene | one clause each in two ConditionExpressions |
| S3 (ARMED) | CLOSED: DISARMED + REMEDIATED | 319 passed at CLOUD HEAD; IB-mr-291 drained |
| W5-S3 (ARMED) | CLOSED: DISARMED + REMEDIATED | 0 behind origin |
| W6-S2 (ARMED) | stays ARMED; its carrier still names 2.0.0_SA_COO~M, its remedy is TO-SC-e12 parked on 0.7.0_AE_CloudOps | CTO 103327 |
| S2 (v1), W5-S2 (v2) | carried OPEN, not restated | not re-read this compile |

## What you should have asked but did not

- **Q1. A parked order blocks every later MDPF_SECCLASS slug.** `.tools/surprise-row-gate.py` reads terminality from
  `TERMINAL_TO_WORDS` (complete, closed, done, superseded, cancelled, withdrawn); `parked` is not in it. TO-SC-e12 was
  first added at 14:39:31Z, so any slug whose watermark is at or after that instant is refused while e12 stays parked.
  This compile's watermark sits at 14:39Z for that reason, and round 6's cannot advance past it. Either the gate
  learns that a parked order with an owner and an un-park condition does not hold a slug, or the order moves to a
  carrier outside the project's `task-orders/`. That is a gate edit or a placement ruling, both the CTO's.
- **Q2. Who reads the flag on a model row?** The MODEL_ROWS half writes 260 rows with `classified_by = model`, 130 of
  them flagged below 0.80. C-CLASSES says a missing row reads Unclassified and nothing is guessed. A flagged model row
  is a guess with a label. This seat did not trace whether any reader (the Holdings producer, the portal's
  `assetClass.ts`, the reporting dashboard's C-CLASSES) distinguishes `model` or the flag. If none does, 130
  low-confidence classes will display exactly like canonical ones. The half should name the reader behaviour before
  it is signed.
- **Q3. S3 closed on the suite; the one-window release is a separate grade.** The disarm test passes, so the row is
  closed. The served act that S3 protected (BD_THREAD_R2 with IB-mr-291 under
  `secclass-bd-thread-r2-and-irpt-narrowed-m-20260930`, OPEN since 15:07Z) is graded at its own ledger close, not here.

## Worker-definition note (W8-S2, for the CTO)

A worker's un-pathed Grep or Glob searches the base checkout. The worker definition already tells the issuer to pass
the worktree's absolute path; it does not tell the worker to pass it to every search. One line there closes it.

-- 3.0.0_SA_CVO
