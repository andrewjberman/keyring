# MDPF_ASSETS.019 -- Reconcile-Block Detect-Class Sentinels

**Agent:** 0.4.0_DS_ClientPlatform (DS Base)
**Date:** 2026-05-20
**Branch:** CLOUD
**TO:** MDPF_ASSETS.019 (COO 2026-05-19; sister to .018 prevent-class)

## Current State

COMPLETE -- three detect-class sentinels added to the WS-A reconcile block in
`data/mdpf/scripts/gold/mdpf_aggregate_aua.py`. Commit `754ab83f9`, pushed to
CLOUD, S3-deployed to `s3://opal-data-mdpf/code/scripts/gold/` (etag MATCH).
All 7 ACs met. RAVC2 to COO + CC CTO.

## What shipped

The 2026-05-19 Cohort 0 incident (platinum emitted 49F-only because the WS-C
Inflection feeder ran after the MDPF chain; Cohort 0 understated $17.80M / 19%;
identity_1 PASSED on the internally-consistent partial data -- masking class
anchor #6) exposed two structural gaps: the reconcile block never checked (a)
absolute-scale day-over-day plausibility, nor (b) WHICH partners were present.
Three sentinels, all ERROR-gated in `reconcile()`:

### SENTINEL 1 -- day-over-day Cohort 0 plausibility

Reads the prior platinum partition's `etf_public_residual_total` via
`load_prior_cohort0()` (S3 list -> max date < as-of -> read). If
`abs(today - prior) / prior > 0.50` -> reconcile ERROR. **SKIPs** when the
prior is absent, <= RECON_TOLERANCE (zero), or pre-dates the
`etf_public_residual_total` field (amendment 41f0b2605) -- a DoD ratio off a
zero/absent base is meaningless, and this also makes the .016 backfill's
`0 -> real` Cohort 0 transition skip cleanly. S3-only; local-fixture runs SKIP.

### SENTINEL 2 -- expected partners present

`expected_partners_for(date)` -- date-aware: `{49financial, inflection}` for
dates >= `INFLECTION_PARTNER_ONBOARD_DATE` (2026-05-18, the AE 0.7.0 ENABLE
partition), `{49financial}` before. ERROR when a partition has partners
present but an expected one is MISSING (the precise 5/19 partial-emission
catch). A wholly-empty artifact (zero partners -- the valid-empty fixture case
+ a distinct total-failure class) reports SKIP, not ERROR.

### SENTINEL 3 -- 2nd-producer cross-validation

Recomputes `opal_aggregate_aua` straight from the feeders via a
non-`build_partners` code path (flat `cohort_class in (model,sma)` filter +
sum, plus last-per-firm `non_model_aua`; no per-firm grouping / registry /
by_model). `> 1% relative` divergence vs the WS-A value -> ERROR. Catches
`build_partners` aggregation bugs (dropped firm, mis-grouping) that the WS-A
path alone would pass internally-consistently.

### Write-gating (failure semantic)

`main()` now gates the platinum write on reconcile PASS: a reconciliation
ERROR (identity OR sentinel) skips `write_s3` and preserves the prior emit
(drop-rather-than-fabricate). The loud ERROR log + non-zero exit are the EC2
gold-script equivalent of the TO's "DLQ alert" -- there is no SQS DLQ at this
layer; the chain-integration DLQ wiring is MDPF_ASSETS.018 (AE lane). This
also tightens the pre-existing identity_1/2/3 gates (previously they wrote the
bad artifact then exit-1) -- a strict improvement, aligned with the TO intent.

## Chosen thresholds + configs

| Param | Value | Rationale |
|-------|-------|-----------|
| `COHORT0_DOD_THRESHOLD` | 50% | Cohort 0 (~$91M residual) legitimate DoD drivers are ETF NAV moves (~1-3%) + a 3-day-RPS-lag partner-held step. 50% is the unambiguous-catastrophe net (zero / double / halve). |
| `XPROD_DIVERGENCE_TOLERANCE` | 1% (relative) | Option (b) is exact-match-expected (both paths read the same feeders the same date) -- on real 2026-05-18/19 data the divergence was $0.00. 1% catches a cohort-level bug while never false-tripping on rounding; a synthetic 5% injection fires cleanly. |
| `INFLECTION_PARTNER_ONBOARD_DATE` | 2026-05-18 | The AE 0.7.0 ENABLE'd daily-forward partition (12ec0b93d). Earlier dates expect 49financial only -- so the .016 backfill of 2026-01-17 -> 2026-05-17 does not false-trip sentinel 2. |

### DoD-sentinel tuning note (per TO Phase 6)

The 5/19 incident's Cohort 0 move was -19% -- **below** the 50% sentinel-1
threshold by design. Sentinel 1 is the catastrophic-absolute-move net; the
precise 5/19 partner-absence class (-19%, within plausible-DoD range) is the
job of **sentinel 2** (partners-present). The two sentinels form combined
coverage: S1 catches large absolute-scale anomalies even when all partners are
present (e.g. a partner emitting a wrong value); S2 catches partner-absence
even when the resulting move is within DoD range. Tightening S1 below ~20% to
"also catch" 5/19 was rejected -- it would false-trip on a legitimate
RPS-lag-step + NAV-move combination (alarm fatigue, the TO's stated concern).

### 2nd-producer reference path choice (TO Phase 3: a/b/c)

Chose **(b)** -- a fresh independent recomputation inside
`mdpf_aggregate_aua.py`. Rejected (a) cross-validate vs
`build_legacy_compat_emit.py`: that script *consumes* the WS-A platinum output
as its input, so cross-validating WS-A against it is circular; and its
legacy-compat / broader-1b methodology produces non-comparable scalars.
Rejected (c) prior-day + DoD-bound: lowest defense quality and overlaps S1.
(b) is self-contained, non-circular, and exact-match-expected.

## Acceptance Criteria

| AC | Result |
|----|--------|
| AC1 | PASS -- probe: synthetic -56% Cohort 0 move -> S1 ERROR; clean +1.2% -> quiet; absent prior -> SKIP. |
| AC2 | PASS -- probe: replay 5/19 (49F-only, 2026-05-19) -> S2 ERROR ("inflection ... MISSING"); both partners -> quiet; pre-onboard 2026-03-15 49F-only -> quiet (backfill-safe). |
| AC3 | PASS -- probe: injected +5% divergence ($210M vs $200M feeder-direct) -> S3 ERROR (4.762%); matched $200M == $200M -> quiet. |
| AC4 | PASS -- commit `754ab83f9` via safe-commit.sh + push CLOUD + `aws s3 cp` to `s3://opal-data-mdpf/code/scripts/gold/mdpf_aggregate_aua.py` (etag `b13f90b28f3ad43723738b8ddd3459e7` == local md5, MATCH). |
| AC5 | PASS -- ds-commit-gate.sh exit 0. No emoji. `from __future__ import annotations` already first import. This session log. |
| AC6 | PASS -- per CTO 2026-05-20 directive, `data/mdpf/scripts/` is off the comp graph (builder scan-path gap, routed to comp-tooling-backlog); used Read/Grep for tracing. comp-pipescript io / comp-blast confirmed non-resolving earlier this session. |
| AC7 | RAVC2 sent to COO + CC CTO. |

## Verification evidence

- **Probe** `mdpf_assets_019_sentinels_probe.py`: 8/8 checks pass (AC1 x3 + AC2 x3 + AC3 x2).
- **Fixtures regression** `mdpf_aggregate_aua_fixtures.py`: 5/5 pass -- no regression (test_valid overall PASS, test_zero_feeders overall PASS, the 3 ERROR tests still ERROR).
- **Real-data dry-run 2026-05-18** (`--source s3`): overall PASS; S1 SKIP (prior 5/15 pre-amendment-field), S2 PASS (both partners), S3 PASS ($1,848,563,071.88 == independent, diff $0.00).
- **Real-data dry-run 2026-05-19**: overall PASS; **S1 ACTIVATED** -- prior Cohort 0 $91,328,983.13 from 2026-05-18, today $91,310,278.05, DoD 0.0% -> PASS; S2 PASS; S3 PASS ($1,848,801,032.18 == independent, diff $0.00). Confirms S1 activates correctly once a Cohort-0-bearing prior exists, with no false-positive.

## Files Modified

| File | Change |
|------|--------|
| data/mdpf/scripts/gold/mdpf_aggregate_aua.py | Added `COHORT0_DOD_THRESHOLD` / `XPROD_DIVERGENCE_TOLERANCE` / `INFLECTION_PARTNER_ONBOARD_DATE` constants, `expected_partners_for()`, `load_prior_cohort0()`; 3 sentinels in `reconcile()` (+ `date`/`prior_cohort0`/`prior_cohort0_date` params); `build_artifact()` + `run()` thread the prior-Cohort-0; `main()` gates `write_s3` on reconcile PASS. |
| org/tier2_senior/0.4.0_DS_ClientPlatform/probes/mdpf_assets_019_sentinels_probe.py | New -- 8-check acceptance probe (AC1/AC2/AC3). |

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-pipescript io mdpf_aggregate_aua` / `comp-blast mdpf_aggregate_aua` | Non-resolving -- `data/mdpf/scripts/` off the comp graph. CTO 2026-05-20 confirmed this is a builder SCAN-PATH gap (the builder globs `data/*/scripts/{gold,silver,bronze}/*.py` but the graph still does not index MDPF; routed to comp-tooling-backlog). Per CTO directive, used Read/Grep for MDPF tracing. Not blocking per TO AC6. |
| `.tools/ds-commit-gate.sh` | exit 0 on `mdpf_aggregate_aua.py` and on the probe. |
| `mdpf_aggregate_aua_fixtures.py` | 5/5 -- used as the regression gate (no comp-graph node to blast). |
| `.tools/safe-commit.sh` | 1 commit, explicit pathspec; probe `git add`-ed first. |

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 -- MDPF_ASSETS.019 complete. AC1-AC7 met. On RAVC3-accept: flip TO status -> complete + add .019 closure entry to MDPF_ASSETS.json phase narrative (project stays active pending .017 + .018 + SXIN_PRODCT.001). |
| **CTO 1.0.0** | CC on RAVC2. Sister-coordination: .019 (detect) + .018 (AE prevent) close the partner-absence class together. |
| **DS Base (self)** | Continue to MDPF_ASSETS.016 (Cohort 0 historical backfill) -- runs the .019-hardened aggregator; sentinels verified backfill-safe. |
