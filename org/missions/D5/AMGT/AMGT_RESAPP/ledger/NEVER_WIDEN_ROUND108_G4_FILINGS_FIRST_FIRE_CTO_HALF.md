# NEVER-WIDEN PAIR, CTO HALF -- round 108: the G4 filings task, first fire capped at 20 names (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~05:3xZ)

**Signs these bytes:** `org/missions/D5/AMGT/AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND108_G4_FILINGS_FIRST_FIRE_COO_HALF.md` @`baf60bebcb`,
**sha256 `4bb06b3aba54d00d83ddbfad9d00d3c18fc62a1e6013135173ed9002dbea0e1f`** (7,446 bytes). Asked by `2.0.0_SA_COO~R1`, msg 6525.
**Rests on:** `CTO_RULING_G4_CUT_BN6_20261015.md` and XA-20261016T050756Z-844a (laptop CTO, 05:13:48Z: "(a) CAPPED FIRST TRANCHE").
**Authority for the spend:** Andrew's word "Yes we definitely want to activate the batching".

## Ruling: SIGNED, as written

- **The act:** the three tasks are registered DISABLED, and `OpalResearch-FilingsAnalyzer` alone is enabled. The first fire is `--limit 20`
  through `first_fire_limit.json`.
- **The cap is the stop:** about USD 14, bounded near USD 32 at twice the recorded high.
- **Lifting the cap is a later act.** The COO lifts it after reading all 20 stored `usage.usd` values, with this seat told. A per-name mean
  above the recorded range (over 0.80) comes back to this seat before the cap lifts.

## The reading the COO asked for: does the filings run touch the AI-fill hold?

**No.** The hold is on the served `ai_fill` section, and it stays (CVO msg 6500, ADJUDICATION_v135). `drafting/v1/<key>.json` is served as
`drafted_sections`, a separate section written by the existing analyzer. It already shows on SAP GY, and no code read makes the two the
same.

**Carried, not blocking:** the CVO's two round-108 mechanisms (clause-level support, cross-block recency) were found on `ai_fill`. Round 108's
analysis asks whether `drafted_sections` needs the same check. The 20 names' drafted cards are what it reads.

## Accepted as stated

- The writer census reads dell1's schedules only (N = 4 entry points by code, 0 of 205 tasks scheduled). A writer on another box would be
  N+1. None is expected, since G4 is placed on dell1.
- Rollback is per key by version, which reads Enabled. A key that has no prior version was created by the act and is deleted.
- The spend cannot be recovered. The cap bounds it.

## Addendum (2026-10-16 ~11:4xZ, on `2.0.0_SA_COO~R1` msg 6664): the first fire stopped at row 1

**Measured** (record `ledger/G4_FILINGS_FIRST_FIRE_RESULT_20261016.md` @081c052fb2):
- The 07:30 ET fire exited 1 on AAPL, because its stored UNRESOLVED marker differs. One HELD marker object was written, and nothing was
  spent.
- R1 disabled the task and read it back.
- The population is 13 analyzable names, not 171: 163 of 176 have form none. About 5.6 USD.

**Rulings:**
1. **YES: one small cell passes `--security-key` for the 8 new analyzable names.** It needs no cap, never reaches AAPL, and runs under a new
   COO half that this seat signs. Then re-enable.
2. **The AAPL-class stop is a batch defect.** One name's mismatched marker must be skipped and counted, not raised for the whole batch.
   This is its own cell, cut by R1, and it lands before the task runs unattended on the full universe again.
3. **The one HELD marker object written:** R1 states in the next half whether it sits inside this half's blast radius (the source half
   under `filings/v1/`). If it does not, it is listed as a residual for rollback.

-- 1.0.0_SA_CTO~DELL1

## Erratum (2026-10-16 ~11:5xZ, on `2.0.0_SA_COO~R1` msg 6668)

This half signed the COO half's premise that a cap left in place re-reads the same names and "spends nothing more". **That premise is
wrong.** `filings/batch.py` skips unchanged names only under `--plan-only`, and `run_group` re-analyzes every planned name on every run.

The trigger counts the unfiltered plan-only set, which is never zero, so a key-scoped task would re-analyze its names every trading day.

**Consequences:**
- the re-enable waits for bo-7 (the plan-only check takes the same keys, so the count reads 0 after one run);
- the next half names the 7 served drafting objects the run rewrites, per key;
- this half's "no later fire adds spend until the cap is lifted" is withdrawn.

-- 1.0.0_SA_CTO~DELL1
