# DS~B Session Log -- MDPF_ASSETS.022 part (a)

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-20
**Branch:** CLOUD
**TO:** MDPF_ASSETS.022 (staged; GO-dispatched in the COO~B MDPF-lane sequence)

## Scope inversion finding

MDPF_ASSETS.022 (authored 2026-05-19) is empirically superseded by today's
.024/.025/.016 ships. Its premise -- "LEGACY file = correct broader-1b,
PLATINUM = stale Schwab-only" -- is INVERTED:

- .022 Phase 1-2 ("update WS-A aggregator + WS-E feeder to emit broader-1b to
  PLATINUM") is DONE: .024 shipped the 2-term headline; .025 re-scoped WS-E to
  full-book certified_aua.
- The LEGACY file `build_legacy_compat_emit.py` is now the stale one --
  L499-503: `non_model_aum = broader_custody - 1a - sma_aua` (SMA-EXCLUDED),
  `total_49f = model + sma + non_model` (3-TERM) -- the pre-v0.8 3-way
  taxonomy. Different 1b basis too (compute_49f_broader_custody off BD
  silver/allocations, not certified_aua).
- .022 AC1 (platinum==legacy to-the-cent) cannot hold across the SMA-inclusive
  vs SMA-excluded mismatch; AC4 (don't touch the legacy file) blocks the real
  alignment work.

Surfaced to COO~B before executing the stale TO. COO~B concurred. Split:
- **(a)** -- methodology_version on the daily-forward aggregator. Unambiguous,
  in-scope. SHIPPED (this log).
- **(b)** -- bring `build_legacy_compat_emit.py` to the v0.8 taxonomy. Changes
  the live partner-facing `non_model_assets.json` numbers. HELD for CTO~B
  re-scope (amendment vs fresh TO; possible Andrew sign-off). NOT executed.

## (a) shipped

`mdpf_aggregate_aua.py`: added a top-level `methodology_version` field to the
artifact -- module constant `METHODOLOGY_VERSION = "v0_8_ruling2"`. The
daily-forward aggregator always emits on the v0.8/Ruling-2 basis (post-.024
2-term headline + .025 full-book certified_aua 1b), so daily partitions are
unconditionally `v0_8_ruling2`. SAME field MDPF_ASSETS.016 stamps on the
historical partitions -- a downstream consumer reads it to detect the
historical basis discontinuity at 2026-03-11.

Fixture `mdpf_aggregate_aua_fixtures.py`: added a methodology_version
assertion to test_valid. 6/6 fixtures PASS.

## Files Modified

| File | Change |
|------|--------|
| data/mdpf/scripts/gold/mdpf_aggregate_aua.py | METHODOLOGY_VERSION constant + methodology_version field on the artifact |
| data/mdpf/scripts/gold/mdpf_aggregate_aua_fixtures.py | methodology_version fixture assertion |

## Deploy cycle (Rule 13)

| Step | Result |
|------|--------|
| ds-commit-gate | exit 0 -- both files |
| Commit | 21bfd1313 -- pushed origin/CLOUD |
| S3 deploy | s3://opal-data-mdpf/code/scripts/gold/ -- both files md5 MATCH |
| Fixtures | 6/6 PASS (incl the new methodology_version check) |

## Compiler Tools

| Tool | Result |
|------|--------|
| ds-commit-gate.sh | exit 0 both files |
| comp-pipescript / comp-validate | mdpf off-graph + opal-data-mdpf bucket uncovered (known gap); md5 local-vs-S3 MATCH substituted; fixture suite 6/6 |

## Current State

MDPF_ASSETS.022 part (a) COMPLETE + shipped. Part (b) HELD for the CTO~B
re-scope ruling. The .022 TO stays OPEN -- COO~B is folding the AC1/AC4
supersession + the (b) scope into a .022 re-scope amendment.

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO~B 2.0.0** | RAVC2 -- .022(a) shipped. (b) held for CTO~B re-scope (build_legacy_compat_emit.py v0.8 alignment -- live partner-facing page change). |
| **DS~B (self)** | Execute .022(b) on the CTO~B ruling -- a small change (mirror the .024 2-term fix into build_legacy_compat_emit.py). |
