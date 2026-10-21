# RESEARCH 2026-10-21 -- NFRA_FIDUPL: empirical backfill probe method + ownership

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1). **Order:** ms on Andrew's direct word (bus 02abe551, 01:27Z, relayed by MSTR msg 8911): the
agents drive the backfill empirically, do not wait on Andrew's two inputs; find how far back the channel serves.
**Ownership:** the backfill RUN is 2.0.0_SA_COO~P1's execution lane (the box pipeline, the planner FR-s-3). The CRO owns this METHOD and the
REPORT to ms. (M) measured from prior captures; (I) inferred.

## What backfill depends on, by file type (measured from the file shapes)

Two different shapes, two different backfill routes:

1. **Transactions (`transact.txt`) -- a DATE-RANGE export.** The standard `.trn` already served 2026-05-26 to 2026-10-16 in one pull (M),
   so the Custom export's step 1 ("Enter Criteria") takes a transaction date range. **Backfill route:** run on-demand Custom exports with
   the `Enter Criteria` from-date stepped progressively earlier; each run lands transactions for that window.
2. **Positions / balances / prices / securities / accounts -- AS-OF snapshots (one date per file).** These carry a single as-of date per
   run (M: position/prices/security are per-business-date files). They are not range exports. **Backfill route:** either the
   `Historical Prices and Positions Export` (one as-of date per run; not yet walked), or repeat the as-of export per target business day.
   Account/security/prices are reference/slowly-changing; positions and balances are the per-day snapshots that matter.

## The empirical probe (for the COO's worker to run; stop at refusal)

1. Start from the known-good window and step the `Enter Criteria` from-date earlier in fixed jumps (e.g. 3 months, then 1 month to narrow)
   for transactions; for as-of files, step the as-of date earlier by business day / month.
2. After each run, **classify the outcome, no values:**
   - **SERVED** -- files land with rows; record the earliest business date actually in the content (not the requested date).
   - **EMPTY** -- the export returns a file with no data rows (channel has no history that far back): the floor is the last SERVED date.
   - **REFUSED** -- the wizard rejects the date (min-date validation) or Export Status shows a failed/zero request: record the exact
     refusal text as the hard limit.
3. **Land what it gives**, each window under its own business date in `fidelity/alongside/bronze/{type}/{YYYYMMDD}/` (the lander already
   partitions by content date).
4. **Guardrails:** space the runs (the throttle lesson -- do not stack exports); one authenticated session reused across the stepped
   exports; never loop-retry a refusal.

## What to report to ms (the CRO compiles once runs land)

- Earliest business date **actually landed** per file type: position, prices, security, account, balance, transact.
- Total volume landed (bytes / row counts per type).
- The hard limit hit, with evidence (the refusal text or the empty-file date), separately for the date-range path (transactions) and the
  as-of path (positions/balances).

## The one step that may need Andrew (named precisely, as ms asked)

**Creating an on-demand Custom export PROFILE with a back-dated range, if the box's browser automation cannot drive the wizard's step-1
date field.** The daily v1.0.1 profile exists; a backfill needs either a new on-demand run with an earlier date, or the Historical Prices &
Positions export opened once. If the COO's first automated attempt to set the step-1 date fails in the wizard, THAT is the step to bring to
Andrew (a one-time profile setup or the Historical export walk). Everything else proceeds without him. Until that failure is observed,
assume it proceeds.

## Not measured

- Whether the Custom wizard enforces a minimum from-date (the refusal path will show it).
- The Historical Prices and Positions export's options (never walked; the as-of backfill depth for positions/balances hinges on it).
