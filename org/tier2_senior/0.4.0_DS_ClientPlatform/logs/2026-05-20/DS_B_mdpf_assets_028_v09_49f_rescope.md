# DS~B Session Log -- MDPF_ASSETS.028 (v0.9 49F re-scope)

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-20
**Branch:** CLOUD
**TO:** MDPF_ASSETS.028 -- v0.9 49F re-scope (WS-E 1b-residual + aggregator 3-term, atomic co-land)
**PRD:** docs/architecture/MDPF_ASSETS.md v0.9 (8951ce8f0)

## Summary

PRD v0.9 (Andrew Mandate Change 3, the 3rd + final 49F-basis revision):
49F (Cohort 1) = the full Schwab 49F book (~$1.65B); 1a/1b/1c DISJOINT;
1b = Schwab_49F_whole - 1a - 1c (SMA-EXCLUSIVE residual); the aggregator 49F
partition is the 3-term sum 1a+1c+1b; headline ~$1.75B. v0.9 SUPERSEDES v0.7
(full-BD-book certified_aua) AND v0.8 (1c-nested-in-1b / 2-way sum).

## Phase 0 -- Schwab-whole source (CTO~B-ruled)

Empirical RPS-vs-crosswalk comparison. CTO~B ruled the CROSSWALK: RPS silver
(opal-data-bd/schwab/silver/rps/, lowercase -- path corrected by Andrew)
structurally undershoots by ~$56M; the crosswalk lands on the mandate figure.
Brief: docs/briefs/mdpf-assets-028-phase0-schwab-whole-source-20260520.md.

## Phases 1-2 -- the re-scope (revert-and-relabel)

v0.9's formula IS the pre-v0.7 disjoint three-way framing, so both scripts
were re-scoped by restoring a tested vintage + relabelling, not new logic
(CTO~B endorsed this as the correct lowest-risk path for a methodology
reversion):
- WS-E `build_mdpf_wse_49f_non_model_aua.py`: restored the pre-.025
  Schwab-crosswalk shape (21b203acc^) -- its non_model = partner_custody_total
  - model_aua_input - sma_aua_input IS the v0.9 SMA-exclusive residual.
  Relabelled PRD v0.9 + methodology_version=v0_9 + method/custody_scope tags
  + the ~$275M v0.9 reference.
- Aggregator `mdpf_aggregate_aua.py`: restored the 70e73d4e8 3-term base
  (total_aua = model + sma + non_model IS v0.9's arithmetic; headline =
  partner_total - cohort_2b = 1a+1c+1b+2a). Added the methodology_version
  field (=v0_9) + a v0.9 docstring paragraph + PRD-citation relabel.

## Phase 3 -- reconciliation (validates the base-commit vintages)

Per CTO~B: the reconciliation empirically validates the base-commit picks --
hitting the anchors confirms 21b203acc^ / 70e73d4e8 were the right vintage.

WS-E v0.9 live run (2026-05-20): partner_custody_total (Schwab whole 49F
book) = $1,654,331,683.26 (6,156 accounts; certified_aua cross-check PASS at
$1,812,084,304.28; 0 crosswalk conflicts over 1,859 silver/fees partitions);
1b = $280,129,391.88 (= 1,654,331,683.26 - 1a 1,349,272,608.00 - 1c
24,929,683.38); section-7 dual feed-sync PASS.

Aggregator v0.9 end-to-end (platinum 2026-05-20.json):

| Field | Value |
|-------|-------|
| opal_aggregate_aua (headline 1a+1b+1c+2a) | **$1,748,030,393.45** |
| 49financial 3-term | model $1,349,272,608.00 + sma $24,929,683.38 + non_model $280,129,391.88 = total $1,654,331,683.26 |
| inflection | model(2a) $93,698,710.19 / non_model(2b) $106,254,365.08 |
| partner_aua_subtotal | $1,854,284,758.53 |
| cohort_2b_audit / etf_public_residual_total | $106,254,365.08 / $91,335,123.78 (audit-only) |
| reconciliation.overall | **PASS** (identity_1/2/3 + sentinel_1/2/3 all PASS) |
| sentinel-3 independent recompute | WS-A $1,748,030,393.45 == independent $1,748,030,393.45 -- **diff $0.00** |

Anchors (CTO~B/COO~B): 49F_total $1,654.33M ~= ~$1,648.85M (within 0.33%,
date/market); headline $1,748.03M ~= ~$1,742.5M; sentinel-3 == headline to
$0.00. ALL HIT -- base-commit vintages confirmed correct. Fixtures 6/6 PASS
(3-term, methodology_version=v0_9).

## Phase 4 -- atomic co-land (AC3)

WS-E + aggregator + fixtures landed in ONE commit + ONE S3 deploy -- no
intermediate v0.9/v0.8 mixed state.

## Files Modified

| File | Change |
|------|--------|
| data/mdpf/scripts/gold/build_mdpf_wse_49f_non_model_aua.py | WS-E 1b = Schwab_whole - 1a - 1c (SMA-exclusive, crosswalk basis); v0.9 relabel; methodology_version=v0_9 |
| data/mdpf/scripts/gold/mdpf_aggregate_aua.py | 49F partition 3-term (1a+1c+1b); v0.9 docstring; methodology_version field |
| data/mdpf/scripts/gold/mdpf_aggregate_aua_fixtures.py | 3-term v0.9 fixtures + methodology_version assertion |

## Deploy cycle (Rule 13)

| Step | Result |
|------|--------|
| ds-commit-gate | exit 0 -- all 3 files |
| Commit (atomic co-land) | dd3cd4d22 -- WS-E + aggregator + fixtures, one commit; pushed origin/CLOUD |
| S3 deploy | s3://opal-data-mdpf/code/scripts/gold/ -- all 3, md5 local==S3 MATCH (one deploy, co-landed) |
| End-to-end run | platinum 2026-05-20.json written, reconciliation PASS |

## Compiler Tools

| Tool | Result |
|------|--------|
| ds-commit-gate.sh | exit 0 all 3 .py edits (Rule 15 first-import; ruff; AST) |
| comp-pipescript / comp-validate | data/mdpf/ off-graph + opal-data-mdpf bucket uncovered (known gap); md5 local-vs-S3 MATCH + the script-embedded reconcile block (all PASS) + fixtures 6/6 substituted |

## Current State

MDPF_ASSETS.028 COMPLETE -- v0.9 49F re-scope shipped + verified. RAVC2 to
COO~B CC CTO~B.

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO~B 2.0.0** | RAVC2 -- .028 complete. On accept, COO~B authors .029 (full Schwab+SmartX historical backfill, non-destructive dry-run first) + .030 (legacy-emit v0.9 re-scope). |
| **CTO~B 1.0.0** | CC on RAVC2 -- output validation against the anchors. |
