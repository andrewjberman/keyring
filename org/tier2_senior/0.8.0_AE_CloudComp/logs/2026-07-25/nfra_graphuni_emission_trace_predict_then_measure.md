# NFRA_GRAPHUNI EMISSION-FILTER TRACE + predict-then-measure control — 0.8.0_AE_CloudComp~D

**Date:** 2026-07-25
**Task Order:** CTO~Z dispatch NFRA_GRAPHUNI EMISSION_TRACE (20260725T070827Z, supersedes 070657Z per
CVO~Z's 070754Z ruling)
**Status:** COMPLETE

---

## Objective

Attribute each of the sharp case's 17 in-scope missing members to the specific predicate in
`extract_gold_compute.py` that drops it (confirm/refute CVO~Z's/CTO~Z's three named predictions), then
build a predict-then-measure control (forecast an un-fitted target's missing-member composition, write it
down, measure, compare) to test whether the resulting model is a mechanism or just a description.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `python3` (residual_sweep.py) | ran before the supersession arrived (crossed messages) | PASS | supplementary data, not the core deliverable, kept and disclosed rather than discarded |
| `python3` (emission_trace.py) | per-member GENUINELY-ABSENT vs PRESENT-UNREACHABLE classification | PASS (TRUE_RC=0) | zero self-check failures, 13/17 PRESENT-UNREACHABLE |
| `python3` (emission_trace_control.py) | predict-then-measure, prediction committed to the script's own docstring before running | PASS (TRUE_RC=0) | dominant-mechanism prediction held (87% vs predicted majority), composition detail partially missed |

**What worked:** writing the prediction directly into the script file's docstring, then running the same
file, made the "prediction written down first" requirement mechanically enforced rather than relying on
memory or a separate note that could drift.

**What failed:** nothing outright; the composition-detail miss in the control (2 unpredicted `gold:`
genuinely-absent members) is disclosed as a partial miss, not smoothed into "prediction confirmed."

**Gap found:** the three predicted predicates (`:94`, `:160`, `:175`/`:185`, key-form canonicalization)
only explain a minority of the residual; the dominant, unpredicted cause is a reachability gap between the
seed and otherwise-present, correctly-formed edges — not attempted to trace further this pass.

Appended to `org/compiler-tools-log.md`.

---

## Work Completed

Conceded the 7-vs-12 split per CVO~Z's arithmetic (14 `WRITES_S3`-carrying members cannot fit in a
12-member in-scope set), restated as 2-vs-17 matching CVO~Z's own 8-gold/2-lambda/7-s3 partition exactly
(independently re-derived from my own sidecar, not copied). Confirmed the `:94` GOLD_SCRIPT-only
prediction for both `lambda:` members (structurally impossible for this producer to emit under any of its
three edge branches). Refuted the key-form-canonicalization prediction for 5 of 7 `s3:` members (their
edges are already correctly bucket-qualified in the producer's raw output — my reconstruction's
strip-the-firm-prefix canonicalization recovers them exactly, no map needed) and refuted the `:160`/`:175`/
`:185` prediction for all 8 `gold:` members (their own edges are all present and correctly attributed).
Built a from-scratch classification (`GENUINELY-ABSENT` vs `PRESENT-UNREACHABLE`, checked by searching the
producer's raw edges for a canonicalized-id match under any form, then testing reconstruction-graph BFS
reachability) that found the actual dominant cause: **13 of 17 (76%) are PRESENT-UNREACHABLE** — the
member's own edges exist and are correctly formed, but the seed cannot reach them via the BFS, meaning
some intermediate hop is broken. This was not one of the three predicted causes. Ran a predict-then-measure
control on a held-out target (`s3:gold/timeseries/client_performance.parquet`, prediction committed to the
control script's docstring before execution): the dominant-mechanism prediction held (87% PRESENT-
UNREACHABLE, predicted "majority"), the composition detail (all genuinely-absent skewing to `lambda:`) was
only partially right (2 of 7 genuinely-absent were `gold:`, not predicted by the sharp-case model). Also
ran 2 more function-level controls (`D_02.advisor_client_detail:main`,
`INF_D_02.advisor_client_detail:build_advisor_books`) — both exact, extending the clean-function-grain
pattern.

Delivered `GRAPHUNI_EMISSION_TRACE.md` + sidecar to the census dir.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Report the reachability finding as the headline, not force it into the predicted-predicate framing | The dispatch asked to confirm/refute specific predictions, and honestly refuting most of them in favor of an unpredicted dominant cause is more useful than stretching the evidence to fit the asked-for shape. |
| Disclose the predict-then-measure control's partial miss rather than round it to "confirmed" | The dispatch explicitly asked for "no smoothing if they diverge" — the mechanism-level prediction held, the composition-level detail didn't, and both facts matter differently to whoever rules the next step. |
| Keep the pre-supersession 17-target sweep as disclosed supplementary data rather than discard it | Real, valid data (crossed messages, not wasted effort); omitting it silently would be worse than including it clearly labeled as not the core deliverable. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/GRAPHUNI_EMISSION_TRACE.md` | New — the trace + control memo | No — CTO~Z's BASE_EXEC lane |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/GRAPHUNI_EMISSION_TRACE.sidecar.json` | New — combined result JSON | No — same |
| `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_GRAPHUNI_REASSERT/residual_sweep.py` + result | New — pre-supersession sweep (supplementary) | Yes — own lane |
| `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_GRAPHUNI_REASSERT/emission_trace.py` + result | New — sharp-case classification | Yes |
| `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_GRAPHUNI_REASSERT/emission_trace_control.py` + result | New — predict-then-measure control | Yes |
| `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/nfra_graphuni_emission_trace_predict_then_measure.md` | This log | Yes |

---

## Blockers

None. Ingestion stays hard-gated.

---

## Current State

Emission-filter trace delivered: 2 of 3 predicted predicates refuted at the member level, the third
confirmed for exactly the 2 members it covers; the actual dominant cause (reachability, 76% of the sharp
case's residual) was not predicted by anyone in the thread and is now the load-bearing finding. Predict-
then-measure control confirms the mechanism generalizes (87% on a held-out target) while the finer
composition detail does not yet reduce to a simple rule. Reported to CTO~Z + CVO~Z this turn.

---

## Next Steps

1. **[3.0.0_SA_CVO~Z]** Verify the classification method and the control result; rule on whether tracing
   the reachability gap's specific intermediate hop is the next bounded step.
2. **[1.0.0_SA_CTO~Z]** Commit the deliverable; the disposition table's "UNDETERMINED, different
   remediation class" finding for 13-15 of 19 members likely changes the shape of any closure ruling.
3. **[0.8.0_AE_CloudComp~D]** Event-driven, standing by.
