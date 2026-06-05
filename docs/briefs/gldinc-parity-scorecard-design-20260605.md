# GLDINC Parity Scorecard + Parity-Run-Machine + Top-of-Month Bracket — design (build-LEAD)

**Author:** 0.6.0_AE_PartnerETL (LEAD) · co: 0.4.0_DS (§5/§5a reconcile + rebaseline detection), 1.0.0_SA_CTO (PRD/parity-spec), 2.0.0_SA_COO (attests the daily scorecard) ·
**PRD:** ADHC_GLDINC §4b (d80a50932), Andrew-direct sharpening. **Scope:** design only — emit starts when P1 parity goes live; month-long daily-tracked through 2026-07-05. No prod cutover (separately Andrew-gated).

## 1. Daily quantitative scorecard — `gold/_parity/{phase}/{run_date}/scorecard.json`
Per nightly parity run, **machine-readable + auditable**, NOT pass/fail. One record per **output artifact** the phase's incremental script(s) produce, plus a run-level roll-up. Schema:
```json
{
  "schema_version": "1.0",
  "phase": "P5_D00b", "run_date": "2026-06-12", "generated_at": "...Z",
  "oracle_commit": "<gold_dispatch sha>", "incremental_commit": "<sha>",
  "epsilon": {"abs": 0.005, "rel": 1e-6, "frozen_by": "CTO+0.4.0 review <date>"},
  "artifacts": [
    {
      "artifact": "gold/timeseries/<...>.parquet | <...>.json",
      "key_set_symmetric_diff": 0,            // target 0 (keys present in one not the other)
      "row_count_delta": 0,                    // oracle_rows - incremental_rows, target 0
      "exact_match_rate": 1.0,                 // ids/counts/categoricals exact, target 1.0
      "exact_mismatch_examples": [],           // first N diffing (key,col,oracle,incr) on miss
      "within_epsilon_rate": 1.0,              // computed-float cells within frozen epsilon, target 1.0
      "max_abs_diff": 0.0,                     // must be < epsilon.abs
      "max_rel_diff": 0.0,                     // must be < epsilon.rel
      "headline_metric_diffs": {               // the decision-grade numbers, 0/within-eps
        "total_aua": 0.0,
        "total_account_count": 0, "per_model_account_count_max_diff": 0,
        "nna_p10": 0.0, "nna_p50": 0.0, "nna_p90": 0.0
      },
      "verdict": "CLEAN | DRIFT"               // DRIFT iff any target missed
    }
  ],
  "run_verdict": "CLEAN | DRIFT",
  "clean_night_counter": 5,                    // consecutive clean nights for THIS phase (resets to 0 on DRIFT)
  "spans": {"period_boundary": false, "injection_date": false, "reassignment_day": false}
}
```
- **Epsilon is a FROZEN reviewed parameter** (CTO+0.4.0 sign-off), recorded in every scorecard — float order-of-operations differences only; 0 for ids/counts/categoricals. A widened epsilon = a re-review, never a silent fudge (PRD §4.2).
- `clean_night_counter` is the N≥5 cutover gate (PRD §4.3); it MUST have spanned the phase's reconcile triggers (`spans.*`) before a cutover is proposed — a phase can be clean 5 steady-state nights and still not be cutover-eligible until it has a clean injection/boundary/reassignment night.
- COO attests this file nightly; CTO surfaces. `exact_mismatch_examples` (bounded) makes a DRIFT immediately diagnosable.

## 2. Parity-run-machine (phased, Andrew-accepted)
- **P1:** shadow runs on the EXISTING nightly runner, **sequenced AFTER the oracle** (never parallel — re-creates the 1.38 TB-RSS paging the DAG serializes B to avoid; my PRD-review Flag 4). No new EC2. The shadow writes `gold/_parity/...`; the harness diffs + emits the scorecard.
- **P2+:** a **DEDICATED SMALL EC2** launched **parallel** to the nightly, runs the incremental shadow, **auto-shuts-off at completion** — viable once P2's working-set drop (A_03 memory-floor) fits a small box. **I LEAD the small-EC2 launch + auto-shutoff spec at P2:** self-shutdown-on-complete (orion/bd-gold pattern) + R8 3h idle-cap as the backstop + R3b-Spot economics (short shadow run = low interruption exposure). This isolates the shadow's compute from the served nightly entirely.

## 3. Top-of-month rebuild = the CRITICAL benchmark (Andrew "most critically")
The freeze-baseline **rebaseline at the 2026-07-01 month boundary** (P5 D_00b et al.) is the highest-risk reconcile — steady-state daily parity never exercises it. The scorecard BRACKETS it:
- **T-3..T-1 (6/28-6/30):** steady-state daily parity (open-period incremental vs oracle), building the clean-night counter.
- **T0 (7/1 the rebuild):** the incremental **freeze-and-roll of the closed period (June) MUST match the oracle full-recompute of that closed period value-for-value** — `key_set_symmetric_diff=0`, `headline_metric_diffs=0`, every cumulative curve identical. This is the gold-standard scorecard.
- **T+1..T+3 (7/2-7/4):** post-rebaseline steady-state — confirm July dailies run clean against the newly-frozen June baseline.
- **HARD GATE:** no freeze-baseline phase (P5 / FRI-residue) cuts over without a full clean **T-3→T+3** pass. The §4a scoped single-date carve-out (one date, small box, NOT c6i) can **pre-simulate** a rebaseline date before 7/1 to de-risk, but the **real 7/1 pass is the gold standard**.
- **Reconcile coupling (0.4.0_DS, §5a):** the rebaseline parity is where §5a restatement-detection binds — late/restated June data arriving after the freeze must trigger a re-freeze; the T0 scorecard + the T+1..T+3 nights must show that the re-freeze re-converges to oracle. Coordinate the rebaseline-parity + restatement-trigger design with 0.4.0.

## Cadence + ownership
Daily emit begins when **P1 parity goes live**; **month-long daily-tracked through 2026-07-05** (Andrew). COO attests the nightly scorecard; CTO surfaces; 0.4.0 owns the reconcile/rebaseline-parity correctness; I (LEAD) own the scorecard harness + the P2 small-EC2 spec + the bracket mechanics. Feeds the per-phase cutover ask (each separately Andrew-gated).

## Next
On P0 CTO-concur → build P0 (checkpoint). The scorecard harness + schema above is built alongside P1 (the first phase that produces a shadow artifact to score). The P2 small-EC2 auto-shutoff spec I draft when P2 is reached. Coordinate the top-of-month bracket + §5a restatement design with 0.4.0 ahead of the 7/1 boundary.
