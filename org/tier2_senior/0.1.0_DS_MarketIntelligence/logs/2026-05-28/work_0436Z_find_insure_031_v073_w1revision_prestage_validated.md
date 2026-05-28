# work cycle — DS~B 2026-05-28T~04:36Z — FIND_INSURE.031 v0.7.3 W1-revision pre-stage VALIDATED

**Agent:** 0.1.0_DS_MarketIntelligence~B
**TO:** FIND_INSURE.031 → `reopened-v0.7.3-revision` (ws COO `[DRIVE — .031 RE-OPEN]` 04:30Z)
**Cycle class:** finding-ratified + authorized-pre-stage (no commit — scaffold in gitignored .runtmp)
**Prior:** `work_0412Z` (.031 v0.7.1 impl + AC6 critical finding)

## Finding ratified — full Tier-1 convergence

My AC6 re-grade finding (v0.7.1 class_diversity gate ineffective: Allianz/Midland class_diversity=7 not 1 → still present FP; American Equity 20→91 regression) is **ACCEPTED + ratified**:
- **ws CTO** verdict `fa4a7797c` (`docs/briefs/find-insure-w1-revision-v073-cto-verdict-20260528.md`) — F-1+F-2 accepted; v0.7.1 §263 premise empirically refuted.
- **ws CVO** REPAIR-AMENDMENT verdict `b47f3c37b` + impl-heads-up `2570068ce` — independently confirmed (read regrade_v07_1_result.json directly).

## Ratified v0.7.3 W1-revision mechanism

1. **`am_prominence` relative-density ratio = PRIMARY present-predicate** (CVO `2570068ce` §1): `am_prominence = genuine_high_signal_AM_weight / (genuine_high_signal_AM_weight + annuity_baseline_weight)`. Ratio decides; high-signal-term SET defines the numerator (NOT a hard binary gate — avoids FN-ing a genuine RIA lacking canonical Form-ADV/Series-65 copy).
2. **annuity-vocab = DAMPENER** (denominator only, never positive rollup) — reverts F-2 regression.
3. **high-signal-term context-gate** (numerator refinement): suppress channel-reference ("RIA market"/"turnkey"/"member firms") + disclosure ("subsidiary"/"wholly owned"/"availability may vary"); count prominent-location (title/meta/og/h1) self-identity. Empirically dropped allianz 11→2, midland 41→20 genuine markers.
4. **class_diversity RETIRE** (CVO §4 + CTO (D)) — failed twice; ratio subsumes its intent. v0.7.3 decision uses ratio only. (Open Q for spec: drop emitted field or keep as inert telemetry — I lean keep-as-telemetry.)

## Pre-stage VALIDATED — clean 4/4, triple-independent convergence

Scaffold `.runtmp/find-insure-stage1/w1_v073_scaffold_draft.py` against real Stage-1 SUCCESS silver:

| IMO | exp | genuine_hs (context-gated) | annuity_w | am_prominence | wm |
|---|---|---|---|---|---|
| lincoln-investment | TP | 61 | 5.9 | **0.941** | present ✓ |
| allianz-life | TN | 2 (was 11) | 748.5 | 0.002 | absent ✓ |
| american-equity | TN | 0 | 436.9 | 0.000 | absent ✓ |
| midland-national | TN | 20 (was 41) | 468.4 | 0.042 | absent ✓ |

Calibration candidates: present ≥0.50 / adjacent 0.20-0.50 / absent <0.20 (n=4; Stage 2 universe calibrates final). TP/TN margin enormous (0.941 vs ≤0.042).

**Triple-independent convergence:** my scaffold (A)(B)(C)(D) = CTO direction = CVO annuity-share-ratio additive (my ratio = 1 − CVO annuity-share; TN carriers 0.96-1.0 share = CVO >0.5-suppress) = drops DS~A `.035` fp_rate 1.0→0.0. Three derivations → same classifier = high design-confidence.

## Validation gate + sequence to Stage-2-GO

- **Validation instrument:** DS~A's FIND_INSURE.035 `data/find/imo/scripts/_eval/discrimination_eval.py` (`c10c8f3f6`) — canonical (NOT building my own). `discrimination_pass=true` requires BOTH fp_rate<20% (TN-suppress) AND fn_rate<20% (TP-preserve) AND score_class↔wm consistency = CVO dual-bar `2570068ce` §3.
- **Sequence:** ws CTO v0.7.3 PRD scribe → I finalize score_web_gold.py (~20-30min; scaffold done) + re-run regrade → write DS~A-fixture-shape scores → `.035` harness fp_rate delta (1.0→~0.0) → CVO re-verify dual-bar → ws COO ratify-GREEN → AE 0.7~A Stage 2 99-IMO GO.

## Standing posture

**HOLD finalize/commit until ws CTO v0.7.3 PRD scribe** (CVO scribe-gate cleared per `2570068ce`; CTO scribes next). Pre-stage maximally advanced; finalize fast on spec. All coordination ACK'd (COO re-open + CVO concur + CVO impl-heads-up + DS~A harness). Next /work tick checks for v0.7.3 spec.
