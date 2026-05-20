# MDPF_ASSETS.017 -- Day-1-Zero Guard at build_legacy_compat_emit Producer Step

**Agent:** 0.4.0_DS_ClientPlatform (DS Base)
**Date:** 2026-05-20
**Branch:** CLOUD
**TO:** MDPF_ASSETS.017 (COO 2026-05-19; supersedes SXIN_DAY1ZG.001)

## Current State

COMPLETE -- day-1-zero guard shipped to the SmartX producer-side emit
(`build_legacy_compat_emit.py`, the sole SoT for `non_model_assets.json` under
the smartx-v1.0.1 producer-consumer split). Commit `468be5074`, pushed to
CLOUD, S3-deployed to `s3://opal-data-mdpf/code/scripts/backfill/` (etag MATCH).
All 7 ACs met. RAVC2 to COO + CC CTO.

## What shipped

`assert_model_aum_plausible(period, model_aum, prior_model_aum)` -- a pure,
side-effect-free helper that raises `Day1ZeroGuardError` (a `RuntimeError`
subclass) when the 49F 1a `model_aum` is missing, below the absolute floor, or
swings beyond the day-over-day tolerance vs the prior clean business day.

Wired into both period loops in `build_corrected_timeseries` -- the main loop
and the extension loop -- placed **after the 5-model coverage check** so that
legitimate partial-coverage gap dates still SKIP gracefully (a guard placed
before that check would have false-aborted on every partial-1a date, e.g.
2026-04-03). At the guard point, 5-model coverage is confirmed, so a low 49F 1a
is genuinely anomalous (zero / collapse, not a coverage gap).

The raise unwinds out of `build_corrected_timeseries` -> `main()` before
`put_object` is reached -- so `non_model_assets.json` is NOT overwritten and the
prior versioned S3 emit stays authoritative. Drop-rather-than-fabricate, the
same philosophy as the consumer-side fixes `fb9a910b8` + `e0f22b108`.

### Placement decision (compute step vs write step)

Chose **compute step, inside the per-date loop, after the 5-model check**.
Rationale: the script reprocesses the whole timeseries and writes once at the
end. The write step in `main()` only sees the final dicts, not the per-date 49F
1a component. The day-1-zero defect is a 49F-SmartX defect on the 49F 1a
specifically -- and on a day-1, Inflection 2a (~$93M, sourced from Eclipse, a
different pipeline) is still non-zero, so the *merged* `model_aum` field a
write-step guard would see is ~$93M, not $0 -- partially masked. Guarding the
49F 1a component (`derived["model_aum"]`) directly inside the loop is the
unmasked check. The raise still produces the write-step semantic ("do NOT write
+ preserve prior emit") because it unwinds before `put_object`.

### Thresholds + hard-fail-vs-transient boundary

| Param | Value | Rationale |
|-------|-------|-----------|
| `MIN_PLAUSIBLE_49F_MODEL_AUM` | $500,000,000 | 49F 1a on Schwab-clean dates runs ~$1.15B (Jan 2026) to ~$1.34B (2026-05-18 platinum: $1,340,415,278.02). $500M is ~37-43% of observed -- a zero or a >=57% collapse trips it; no legitimate single-day move in a short/intermediate muni-bond book comes near it. |
| `MODEL_AUM_DOD_TOLERANCE` | 15% | Observed 49F 1a day-over-day swings <5% on real dates. 15% is the secondary precise gate -- catches a partial-zero / large unexplained drop that clears the absolute floor, while tolerating real market moves. |

Hard-fail (raise) is correct here vs a transient WARN because: (a) the defect is
structural, not noise -- SmartX emits exact $0.00 across all model CSVs, a clean
binary signal; (b) the 5-model-coverage precondition already filters out the
"legitimately small / partial" class before the guard runs, so a guard trip is
never a low-AUM small-firm situation; (c) the masking class (identity_1 PASSES
on the wrong emit) means a silent over-stated artifact is worse than a missing
daily update -- preserving the prior emit is the safe failure mode.

## Acceptance Criteria

| AC | Result |
|----|--------|
| AC1 | PASS -- probe: forced `model_aum=$0.00` -> `Day1ZeroGuardError` raised. |
| AC2 | PASS -- probe: real 49F 1a ($1,340,415,278.02) -> guard quiet. `build_legacy_compat_emit.py --dry-run` completes exit 0 over all 80 rebuilt dates, NO false-positive. non_model_pct stable ~23.4-23.8% (2026-05-19 latest 23.80%). NOTE: the TO's "10-15% band" hint predates the broader-1b CEO methodology pivot (it was the Schwab-only-1b figure); the broader-1b methodology's observed band is ~23-24% -- DS Base confirms this as the current expected range. |
| AC3 | PASS -- probe: all 7 known 2026 zero-dates (01-02/03/04, 02-02, 03-02, 04-01, 05-01) as fixtures -> guard raised on every one. |
| AC4 | PASS -- commit `468be5074` via safe-commit.sh + push CLOUD + `aws s3 cp` to `s3://opal-data-mdpf/code/scripts/backfill/build_legacy_compat_emit.py` (etag `b8d4efc9cac9def6b01be0fa42facf8a`, size 42350 == local, MATCH). comp-pipescript deployed N/A -- script off the comp graph (see AC6); MATCH verified by md5/etag instead. |
| AC5 | PASS -- ds-commit-gate.sh exit 0 on both files. No emoji. `from __future__ import annotations` already the first import. This session log. |
| AC6 | PASS -- `comp-pipescript io build_legacy_compat_emit` -> "Script not found" + `comp-blast build_legacy_compat_emit` -> "No nodes matching": `data/mdpf/scripts/` is off the comp graph (re-flagged backlog, separate ADHC follow-up, not blocking). Direct file-read used for placement context. |
| AC7 | RAVC2 sent to COO + CC CTO. |

## Probe transcript

`org/tier2_senior/0.4.0_DS_ClientPlatform/probes/mdpf_assets_017_day1_zero_guard_probe.py`
-- 11/11 checks pass (AC1 anchor + AC2 false-positive + AC3 x7 zero-dates +
DoD-band bonus x2). Full transcript captured in the session (RESULT: 11 passed,
0 failed).

## Files Modified

| File | Change |
|------|--------|
| data/mdpf/scripts/backfill/build_legacy_compat_emit.py | Added `MIN_PLAUSIBLE_49F_MODEL_AUM` + `MODEL_AUM_DOD_TOLERANCE` constants, `Day1ZeroGuardError`, `assert_model_aum_plausible()`; wired the guard call into the main + extension period loops after the 5-model check. |
| org/tier2_senior/0.4.0_DS_ClientPlatform/probes/mdpf_assets_017_day1_zero_guard_probe.py | New -- 11-check acceptance probe (AC1/AC2/AC3 + DoD bonus). |

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-pipescript io build_legacy_compat_emit` | "Script not found" -- `data/mdpf/scripts/` off the comp graph. Documented as standing backlog (DS~B re-flagged 2026-05-19); not blocking per TO `if_mismatch`. |
| `comp-blast build_legacy_compat_emit` | "No nodes matching" -- same off-graph root cause. Fell back to direct file-read for placement context. |
| `.tools/ds-commit-gate.sh` | exit 0 on `build_legacy_compat_emit.py` and on the probe (py_compile + AST undefined-name scan + ruff). ADHC_DSFLOW.007 MSYS issue did not surface this session -- gate ran clean. |
| `.tools/safe-commit.sh` | 1 commit, explicit pathspec; probe `git add`-ed first (new untracked file, `--only` does not pick up untracked). |

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 -- MDPF_ASSETS.017 complete. AC1-AC7 met. On RAVC3-accept: flip TO status -> complete + add .017 closure entry to MDPF_ASSETS.json phase narrative. |
| **CTO 1.0.0** | CC on RAVC2. The TO's 10-15% non_model_pct band hint is stale (pre-broader-1b); observed band ~23-24% noted for the record. comp-graph gap on `data/mdpf/scripts/` re-flagged. |
| **DS Base (self)** | Continue to MDPF_ASSETS.019 (reconcile-block sentinels) then .016 (Cohort 0 historical backfill). |
