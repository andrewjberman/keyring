# NNA (INF_C_01/canonical_nna) staleness -- bounded finding, handoff note

**Status:** OPEN, handoff for the ADVI_INFREF durable-fix owner (Andrew-gated
decision, per COO). Author: 0.4.0_DS_ClientPlatform~A. 2026-07-09, as a
parallel/lower-priority thread alongside the P0 inf-value-parity phantom-
divergence fix (docs/briefs -- see the parity-guard patch handoff for that
separate, primary finding).

## The finding

`gold/canonical/canonical_nna_*.parquet` stops at **2026-07-07** -- no
`canonical_nna_2026-07-08.parquet` exists, even though the same nightly batch
(written 2026-07-08 ~10:45 UTC) successfully advanced sibling artifacts
(holdings, positions_mv) through 2026-07-08. The served `header_metrics.json`
/ `dashboard.json`'s `as_of_by_dim.nna` correctly reflects this lag (currently
`2026-07-06` after the Orion forward-label normalization is applied on top of
the raw 1-day lag) -- comp-freshness flags it WARN, "3 trading days behind."

**This is INF_C_01 (`data/inf/scripts/gold/INF_C_01.canonical_nna.py`)
genuinely not producing fresh output**, not a label artifact like the AUA
phantom-divergence (that one turned out to be a parity-guard bug, not a real
data issue -- this one is real).

## Silent-green-chain (a separate, real finding on its own)

`gold/meta/pipeline-complete.json` reports the full chain **COMPLETE** for
`run_date=2026-07-08` (`completed_at: 2026-07-08T14:57:44Z`) despite NNA not
advancing. The chain-completion signal is not grounded in per-producer
freshness -- a "COMPLETE" that doesn't mean every producer actually refreshed.
Same family as the alarm-into-the-void pattern this whole investigation
started from (a green/passing signal masking a real gap underneath it).

## Ruled out

**Skip-gate (`data/inf/scripts/gold/lib/skip_gate.py`'s `should_skip()`) is
NOT the mechanism.** Read directly: if the output partition does not exist
(confirmed -- `canonical_nna_2026-07-08.parquet` is absent), `should_skip()`
unconditionally returns `False` (compute), no exceptions, regardless of
`INFINC_PHASE1`/rebuild flags. This isn't the same class of bug the 07-06
ADHC_GLDINC marathon found elsewhere (skip-gates keyed on persistent-output-
existence that skip forever once a file exists once) -- here the file simply
never gets written in the first place, so the gate never even engages.

## Confirmed (not the cause, but ruled out as an explanation)

`silver/transactions/2026-07-08.parquet` **exists** (written 2026-07-08
09:46:56 UTC, same-day cadence as every recent date, 1,393,821 rows) -- so
`INF_C_01.list_silver_dates()` should see 2026-07-08 as an available date to
attempt. The chain is not lying about silver freshness; the underlying raw
transaction data for that day is present.

## The untraced boundary (where the deep-dig stopped, proportionately)

The raw `silver/transactions/{date}.parquet` file has **camelCase** columns
(`transDate`, `accountId`, `transactionDescription`, `transAmount` -- looks
like a full-history cumulative snapshot, not a single day's delta). But
`classify_nna()` (the actual NNA classifier inside INF_C_01) operates on a
**different, snake_case schema** (`trade_date`, `type_desc`, `trans_amount`,
`activity_category`). There is a transformation step, `load_all_transactions()`
(called at `INF_C_01.canonical_nna.py:673`), between the raw file and what
`classify_nna` sees -- **not traced**. The open question: does 2026-07-08
genuinely have zero NNA-classifiable transactions after that transform (a
legitimate content gap, not a bug), or does the transform itself drop/mis-map
2026-07-08's rows (a real bug)? Answering this requires reading
`load_all_transactions()` in full and probably loading its actual output for
this date -- a bigger investment than was proportionate to spend on this
parallel/lower-priority thread while the primary P0 (inf value-parity
phantom-divergence) was still open.

## Corroborating signal (MSTR-grounded, COO-flagged)

The gold-runner EC2 (`i-0ed5afded2ebd4ed4`) SSM command history is dominated
by FAILED runs across the past week -- including a `2026-07-02` "AE INFREF
guarded 3600s retry (post perf-abort)" (Failed) explicitly targeting this
exact problem class, plus a `2026-07-08T19:32Z` unlabeled Failed run only
~11h before this investigation. NNA's staleness sits on a persistently-
failing chain, not in isolation -- this leans the ADVI_INFREF-ownership
decision COO is holding for Andrew toward RECURRING/pressing, not a one-off.

## Recommended next step (cheap disambiguator, per COO)

**Watch tonight's scheduled 2026-07-09 run** (do not trigger an ad-hoc rerun
-- validate on the nightly's own artifacts, per CLAUDE.md discipline). If
`canonical_nna_2026-07-09.parquet` also fails to appear (or the lag persists/
widens), that's a strong signal this is structural, not a one-off content
gap -- sharpening the urgency of the ADVI_INFREF durable-fix decision. If it
DOES appear on schedule, that narrows the open question to "why did 07-08
specifically come up short" (transient) rather than "the pipeline can't keep
NNA current at all" (structural).

## Grounding

- `comp-freshness inf` (2026-07-09) -- `inf_platinum_header_metrics`/
  `dashboard` WARN, worst dim 'nna' as_of 2026-07-06, 3 trading-days behind.
- `aws s3 ls s3://opal-data-inf/gold/canonical/` -- confirmed no
  `canonical_nna_2026-07-08.parquet`.
- `aws s3 ls s3://opal-data-inf/silver/transactions/` -- confirmed
  `2026-07-08.parquet` present.
- `aws s3 cp .../gold/meta/pipeline-complete.json` -- confirmed COMPLETE for
  run_date=2026-07-08 despite the above.
- `data/inf/scripts/gold/lib/skip_gate.py` (read in full) -- confirmed
  missing-output always forces compute, no skip path applies here.
- `aws ssm list-commands --instance-id i-0ed5afded2ebd4ed4` (MSTR + DS,
  cross-checked epoch timestamps precisely) -- confirmed the FAILED-run
  pattern spans 2026-07-02 through 2026-07-08.
