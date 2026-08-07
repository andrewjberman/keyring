# Mutation exercise record (R7 limb 2) — FAIL + LOCALISE shown before any PASS is citable

**Run:** 2026-08-07 00:22Z by `3.0.0_SA_CVO~Z` · TO `MDPF_CANPLAT.G2` @f123fbf6e
**Baseline:** `baseline_manifest_20260807T000753Z.json` (pin instant 2026-08-07T00:07:53Z, VersionId-pinned)
**§B derivation commit:** `411e8e8a3` · **Canonicalisation:** README.md declared six rules (joint w/ DS~Z msg `20260807T000529Z`)
**Method:** three mutants built from VersionId-pinned baseline bodies (scratchpad-only, S3 never touched),
each compared in an ISOLATED invocation. The mutant baselines tie to the CONTRACT's own measurement:
cottonwood `non_model_aua` len=446, nulls=438 (= the "8 of 446 populated" W-2 row).

## M1 — business-value mutant (the classic regression)

`49financial/aum-metrics` `total.aum` `1706973077.81 -> 1706973078.81` (+1)

```
REGRESSIONS(1): 49financial/aum-metrics  paths_compared=117 diffs=1 excused=0 regressions=1
  REGRESSION total.aum: NUMBER -> NUMBER  baseline="1706973077.81" candidate="1706973078.81"
DENOMINATOR: 1 of 1 pairs compared; total regressions=1; PASS-NOT-CITABLE (mutation exercise not on record)
```

**FAILED and LOCALISED**: exactly one regression, at exactly the mutated path, 117 paths compared. rc=2.

## M2 — the Guard-3 one-token class (`else None` -> `else 0`), requested by DS~Z (P1-1)

`cottonwood/aggregate-aua-timeseries` `non_model_aua[0]` (date 2024-11-01, an unreached/honest-absent date) `null -> 0`

```
REGRESSIONS(1): cottonwood/aggregate-aua-timeseries  paths_compared=8276 diffs=1 excused=0 regressions=1
  REGRESSION non_model_aua[0]: NULL -> ZERO  baseline=null candidate="0"
DENOMINATOR: 1 of 1 pairs compared; total regressions=1; PASS-NOT-CITABLE (mutation exercise not on record)
```

**FAILED with the DISTINCT NULL->ZERO verdict** — not absorbed as numeric noise, and NOT excused by the
W-2 coverage exemption (which is `null_to_nonzero_value_only` by construction). rc=2.

## M3 — exemption positive control (the excusal excuses exactly what it should)

Same path, same index: `non_model_aua[0]` `null -> 123.45` (a nonzero coverage fill, the W-2 legitimate class)

```
EXCUSED-ONLY: cottonwood/aggregate-aua-timeseries  paths_compared=8276 diffs=1 excused=1 regressions=0
DENOMINATOR: 1 of 1 pairs compared; total regressions=0; PASS-NOT-CITABLE (mutation exercise not on record)
```

**EXCUSED-ONLY, zero regressions.** rc=0.

## What the pair M2/M3 establishes

Same artifact, same path, same baseline state — the only difference is the candidate value (0 vs 123.45).
The exemption boundary sits EXACTLY at zero: the comparison that has never failed has now failed (M1, M2),
localised to the exact JSON path both times, and the named exemption excuses the named legitimate
transition and nothing else (M3). R7's PASS is citable from this record forward.

— 3.0.0_SA_CVO
