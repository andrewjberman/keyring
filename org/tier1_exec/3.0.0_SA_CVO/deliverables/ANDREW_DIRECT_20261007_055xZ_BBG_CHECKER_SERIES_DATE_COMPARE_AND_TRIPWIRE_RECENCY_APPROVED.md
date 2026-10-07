# ANDREW-DIRECT 2026-10-07 ~05:5xZ -- the Bloomberg freshness checker gains the per-series date compare (gap 1); go with the recommendation on gap 2 (the tripwire)

Channel: typed by Andrew at the `3.0.0_SA_CVO~Z` terminal (Claude Code session), ~05:55Z (1:55 AM ET). It answers this seat's
read-only assessment of
`org/tier0_utility/0.0.3_BG_BBGTerminal/deliverables/HANDOFF_STALENESS_GATE_WHAT_IT_CHECKS_AND_WHAT_IT_CANNOT_20261007.md`, which he
asked for at ~05:4xZ.

## VERBATIM

> Yeah we can close gap 1 with the checker compare you described, go with your recs on that matter and gap 2

## What "gap 1", "gap 2" and "your recs" resolve to (this seat's assessment, quoted as he read it)

- **Gap 1, as stated to him:** "Nothing summons when the guard nulls a series. The page shows N/A, but the 07:30 check still
  passes."
- **Gap 2, as stated to him:** "The pull-side tripwire still grades the date only (row `Z-S5`, open, no owner, waiting on your
  no-modify answer)."
- **The recommendation, as stated to him:** "close gap 1 by having the checker also compare each series' last date to
  `data_as_of`. It is one comparison, but it needs your word, because of the monitor moratorium and the no-modify order on
  `integrations/bloomberg/`. I recommend yes, and lifting the order for gap 2 as well."

## As written (not adjudicated here)

1. **Gap 1 is approved.** `integrations/bloomberg/pipeline/freshness_check.py` may compare each benchmark series' last date
   (`benchmark_last_date`, index and etf, per model, in the served `json/benchmarks/model_portfolio_benchmarks.json`) to
   `data_as_of`, and summon when a series is behind. This is his explicit ask for a change to a checker, which the standing
   moratorium requires.
2. **Gap 2 is approved on the recommendation.** The no-modify order on `integrations/bloomberg/` lifts for the tripwire's
   per-series recency fix (row `OPAL_BBGTML-Z-S5`).

## Scope, held at its verbatim reach

- The lift covers these two edits. It does not cover the sign-in rows (`Z-S1`..`Z-S4`), the publisher's same-date skip
  (`publish_to_portal.py` GATE 3), or any other file under `integrations/bloomberg/`.
- It authorizes no new alert, schedule or notification channel. The checker's existing summons is the carrier.
- Not stated by him: who builds it, and the summons kind's name. Site-Z Scheduled Tasks run the working tree, so an edit to
  `freshness_check.py` is live when it touches disk.

## Routing

This seat validates AMGT and builds nothing here. The build route is `1.0.0_SA_CTO~Z`'s. One line goes to that seat naming this
record.

-- 3.0.0_SA_CVO~Z
