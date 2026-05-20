# DS~B Session Log -- MDPF_ASSETS.016 historical backfill v0.8 re-run

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-20
**Branch:** CLOUD
**TO:** MDPF_ASSETS.016 (re-issued ~B; amendment Corrections 1-8)

## Summary

Re-ran the MDPF historical platinum series on the PRD v0.8 / Andrew Ruling 2
basis. The pre-existing 81 partitions were empirically confirmed stale (old
1a+1b+1c+2a headline + Schwab-only 1b). Mechanism per amendment Correction 1:
extend `build_mdpf_process_backfill.py` (NOT a standalone aggregator re-run).

### Mechanism rework (build_mdpf_process_backfill.py)

- 1b basis (Corrections 5+6): `non_model_aua = certified_aua - model_aua(1a)`,
  full BD book, SMA-inclusive (no `-1c` term). certified_aua read via
  `wse.load_certified_aua` from BD gold `aua_certification/{date}.json`.
- Headline (Correction 3+6): `opal_aggregate_aua = 1a+1b+2a` (inherits the
  .024 aggregator import).
- AC8 empty-overwrite guard (Correction 2): band widened 5% -> 30%. The .016
  re-run is a cross-methodology rewrite (Schwab-only ~$294M 1b -> full-book
  ~$469M); a 5% band would reject every legitimately-moved partition. 30%
  still catches catastrophic corruption (zero/double/halve).
- Correction 7: the Schwab custodian-crosswalk was retired from the WS-E daily
  path; `build_custody_crosswalk_cache.py` retired (git rm); the WS-E LEGACY
  crosswalk block deleted (508 lines) once zero importers remained.
- Correction 8 (CTO~B ruling): machine-readable `methodology_version` field on
  every platinum artifact, conditional on the 1b basis.

## Early-window blocker + CTO~B ruling

Dry-run surfaced: `gold/aua_certification/` earliest partition is 2026-03-11
(42 partitions). Amendment Correction 5's "certified_aua daily-available
historically" was empirically false. The 2026-01-17 -> 2026-03-10 window has
no certified_aua -> v0.8 1b null -> AC8 correctly rejected (would null-overwrite
real figures). Surfaced to COO~B; CTO~B ruled **Option (a)** (Correction 8):
ship the 46 v0.8 dates, leave the 30 early dates' values untouched, tag the
basis via `methodology_version`.

## Outcome (81 in-scope dates, 2026-01-19 -> 2026-05-15)

| Bucket | Dates | methodology_version | Outcome |
|--------|-------|---------------------|---------|
| 46 | 2026-03-11 -> 2026-05-15 | v0_8_ruling2 | v0.8 re-run, written (AC8 pass) |
| 30 | 2026-01-20 -> 2026-03-10 | pre_ruling2 | AC8-preserved (cert unavailable), meta-tagged |
| 5  | 2026-01-19,01-26,01-28,02-05,02-16 | pre_ruling2 | market-holiday null-1b, written 1a-only |

`build_mdpf_process_backfill.py --upload`: WRITTEN 51/81, AC8 REJECTED 30
(all surfaced; resolved by the CTO~B ruling). Anchor 2026-05-15: 1a
$1,349,270,403.05 + 1b $455,549,312.64 = 49F total $1,804,819,715.69 (full-book
identity holds). Spot-check: 2026-03-11 (first v0.8) $1,609,173,693.37;
2026-05-18 daily-forward UNTOUCHED $1,848,563,071.88 (generated 05-19,
out of .016 scope -- confirmed no-move).

Early window meta-patched (one-shot, pure-additive -- every non-
methodology_version field asserted byte-identical; 2026-02-04 verified
$1,430,315,883.94 preserved). Timeseries `aggregate_aua_timeseries.json`
regenerated (98 dates) -- carries a parallel `methodology_version` array; ONE
clean basis-change boundary at 2026-03-11 (pre_ruling2 -> v0_8_ruling2).

## Files Modified

| File | Change | Commit |
|------|--------|--------|
| data/mdpf/scripts/backfill/build_mdpf_process_backfill.py | v0.8/Ruling-2 mechanism rework; AC8 30%; Correction 7 crosswalk removal; Correction 8 methodology_version (conditional on 1b basis) | 941f4205f, 4d2f78781, bc3b08c8f |
| data/mdpf/scripts/gold/build_mdpf_wse_49f_non_model_aua.py | Correction 7 -- WS-E LEGACY crosswalk block deleted (508 lines), orphaned constants/helpers removed | 941f4205f |
| data/mdpf/scripts/backfill/build_custody_crosswalk_cache.py | Correction 7 -- retired (git rm; methodology-superseded, zero consumers) | 941f4205f |
| data/mdpf/scripts/backfill/build_aggregate_aua_timeseries.py | Correction 8 -- per-date methodology_version array; stale meta string fixed | 4d2f78781 |
| docs/briefs/mdpf-assets-wsa-page-wire-note-20260520.md | AC6 -- page-wire note updated to the v0.8 headline + methodology_version basis split | (this commit) |

## Deploy cycle (Rule 13)

| Step | Result |
|------|--------|
| ds-commit-gate | exit 0 -- all .py edits (py_compile + AST + ruff) |
| Commits | 941f4205f (mechanism + Correction 7), 4d2f78781 (Correction 8 field), bc3b08c8f (Correction 8 conditional fix) -- all pushed origin/CLOUD |
| S3 deploy | s3://opal-data-mdpf/code/scripts/backfill/ + code/scripts/gold/ -- md5 local==S3 MATCH |
| Backfill run | --upload 2026-01-17..2026-05-17: 51 written, 30 AC8-preserved |
| Timeseries | aggregate_aua_timeseries.json regenerated (98 dates) |

## Compiler Tools

| Tool | Result |
|------|--------|
| comp-pipescript io / deployed | mdpf scripts off-graph + opal-data-mdpf bucket not covered -- known data/mdpf/ gap; md5 local-vs-S3 substituted (MATCH) |
| comp-blast mdpf_aggregate_aua | "No nodes matching" -- mdpf off-graph (graph built 1941 nodes, mdpf not indexed); documented gap |
| comp-validate | no mdpf artifact config -- verification via the script-embedded full-book identity + AC8 guard + the dry-run/upload transcripts |
| ds-commit-gate.sh | exit 0 every .py edit |

comp-tools backlog (re-flagged CTO): data/mdpf/scripts/ off the comp-graph;
comp-pipescript deployed does not cover opal-data-mdpf; comp-validate has no
mdpf config.

## Current State

MDPF_ASSETS.016 COMPLETE -- 46-date v0.8 re-run + 30-date pre_ruling2 meta-tag
+ Correction 7 crosswalk retirement + timeseries regen. RAVC2 to COO~B.

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO~B 2.0.0** | RAVC2 -- .016 complete. On accept, MDPF_ASSETS.json phase narrative. Tracked follow-ups (COO~B-owned): 05-18/05-19 tail-headline gap; optional BD aua_certification backfill 2026-01-17..03-10 for a uniform early series (CTO~B routed to Andrew). |
| **DS~B (self)** | Proceed to MDPF_ASSETS.022 (broader-1b WS-A/WS-E canonical alignment; align to PRD v0.8 + the methodology_version field defined here). |
