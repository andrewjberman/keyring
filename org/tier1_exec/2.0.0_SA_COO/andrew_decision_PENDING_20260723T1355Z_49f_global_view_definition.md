# 49F definition for the Model Portfolios "Global" view — FULLY RULED (C2), serve held on build+verify

## >>> FINAL RULING @~15:12Z (Andrew VERBATIM): "We want to keep cash, C2." <<<
**49-TOTAL = C2 = `fact_rps_s2.net_mv_plus_cash` from `opal-data-assets/silver/schwab/08242234`** — positions
+ the FULL cash leg (settled cash + bank sweep + MMF, ~$33.76M). Current 07-17 = **$1,665,338,126.76**;
Global ~$1.93B. Source chain = **silver -> gold DDB -> portal** (Andrew premise: portal downstream of data;
gold DDB populated from opal-data-assets/silver buckets). This KILLS the circular emitter read
(was: partners[49financial].partner_custody_total from the SERVED mdpf aggregate = legacy schwab_canonical
positions-ex-cash, 07-15-stale).
**BUILD SEQUENCE (serve hard-held through it):** DS builds-to-C2 (net_mv_plus_cash from silver) -> 0.7.0
emitter re-source (raw-silver, not circular) + full-lookback backfill (541 partitions, 2024-05-24+;
CRS-era/pre-2024-05 = labeled boundary) -> DS reprocess 49+Global trends -> COO per-date byte-verify
(49[d]==net_mv_plus_cash[d] from silver; C2 ties to the cent) -> co-sign -> renders -> fire -> promote.
**21 registry rows: SUPERSEDED-with-mechanism** (they're legacy positions-ex-cash + 07-15-stale; pinned
+cash+vintage delta, NOT byte-controls). D-2 "legacy ~40% cash" RETRACTED (date-axis artifact; legacy = ZERO cash).
**Candidates (DS @145807Z, cited):** C1 positions-ex-cash $1,631.7M (=legacy, continuity) | **C2 chosen** full
$1,665.3M | C3 positions-account-grain $1,631.6M | C4 ex-options $1,598.1M. Andrew chose cash-IN.

---
**Status @~13:58Z (superseded by the C2 final ruling above):** 49F grounding CLOSED (no defect) + ANDREW
RULED THE SOURCE (08242234). Serve hard-held until DS builds to the ruled definition + COO re-verifies.

## >> ANDREW RULING @~13:58Z (VERBATIM):
"This is not complicated, the 49 full number should be whatever the aua content of the schwab 08242234
account serves."
**=> 49F leg = the served AUA of Schwab account 08242234 = the 0824 MODEL PORTFOLIOS master** (the
business-purpose-correct bucket for THIS view). **NOT a 0824/0833 substitution** — it uses 0824 for its own
purpose (Model Portfolios), sovereign-directed; the NEVER-substitute prohibition guards cross-using the two
masters, which this isn't. Options (i) legacy-partial and (iii) raw-full are BOTH retired by this ruling —
neither was the account that actually serves the view. DS building the 49F leg to 08242234's served AUA,
grounded (cite source). Flags to DS: (1) confirm 08242234 still serves current/live (0824 feeder marked
DEPRECATING 07-16); (2) cite WHICH quantity is the served AUA (0824 ~$1,621.6mm blended-preferred vs
SCHWAB-RPS ~$1,390mm+$23mm feeder split — cite, don't pick).

## The dispute (Andrew-direct, 2026-07-23 ~13:34-13:50Z)
Andrew: the staged Global's 49F = $1.69B is wrong; correct is ~$1.64B; Global should be ~$1.9B not $1.95B.
Then clarified: "the Model Portfolios 'Global' view is not a true aggregate, it is a business-logic driven
subsection." (VERBATIM recorded in the thread.)

## The mechanism — DS decomposed to the cent, ZERO residual (@135327Z), citable to bytes/ledger
`$1,688,831,869.52 (staged) − $1,644,993,954.34 (reference) = $43,837,915.18` =
- **(c) DEFINITION $20,344,172.42** — staged FULL envelope (`fact_rps_s2 net_mv_plus_cash`, real dailies,
  full cash) vs the legacy `schwab_canonical` PARTIAL-cash REDERIVED ESTIMATE (~40% of the $33.76M cash leg;
  history is estimate, not real dailies). D-2 named delta, ledger `@6eb54c186`, +1.24% at 07-17 common vintage.
- **(b) GROWTH $23,493,742.76** — real full-envelope movement 07-17→07-21, day-by-day in `fact_rps_s2`.
- **(a) DEFECT: NONE** — no double-count, no wrong source, non_model identity-enforced (D-2: 0 mismatches).

**KEY FINDING that flips the framing:** Andrew's $1.64B reference IS the legacy partial-cash rederived
ESTIMATE (D-2 ledger 07-17 common $1,644,993,954.34 = served_baseline_custody + DE's PROD verify). It is NOT
a truth the staged number missed — it is partial + estimated + ~2 weeks stale. The staged $1.69B is 49's
real, full, current envelope. So the decision is "which DEFINITION," not "which number is right."
(INF $136.8M + COT $124.4M are already model-only subsections; only 49F carries the envelope question, since
only 49F is `fee_scope=full`.)

## THE DECISION (Andrew's word — presented @135xxxZ, I present he decides)
Which 49F basis does the Model Portfolios Global view use?
- **(i) legacy partial estimate ~$1.64B** — re-serves a partial-cash rederived estimate + the staleness
  Andrew himself flagged. COO advised against.
- **(ii) subsection defined on REAL sources** — DS + COO recommendation; the honest form of Andrew's ruling.
  **NEEDS Andrew's one-line definition of what the subsection INCLUDES** (esp. the $33.76M cash-leg treatment
  + which account cohort). DS can decompose the $20.3M into cash-vs-noncash components to the definition.
- **(iii) raw full envelope $1.69B** — Andrew has ruled this out (it's the raw aggregate, not the view).

## Gate (CTO-bound): serve HARD-HELD, order
Andrew's definition word -> DS builds-to-definition (grounded, NOT "match $1.64B") -> COO re-verify against
the ruled definition -> downstream (basis-label re-emit `@189336618` [3 producers + methodology record + 5
under-stated artifacts, held to ride ONE churn], DE renders, co-sign, DT promote). No defect to fix.

## Discipline banked this session (my two own-goals, both caught)
1. Circular verification (validated $1.825B by its own trajectory, not vs truth) — caught by Andrew.
2. Bend-to-authority (leaned "reconcile to $1.64B") — caught by CTO (both numbers are claims; name the
   mechanism; a number corrected to match authority without grounding is the same defect pointing the other way).

**Delete/close when: Andrew rules the definition + DS builds + COO re-verifies + it serves.**  -- `2.0.0_SA_COO`, ~13:55Z
