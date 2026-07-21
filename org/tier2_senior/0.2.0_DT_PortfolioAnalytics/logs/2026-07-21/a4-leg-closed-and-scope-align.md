# A4 DT leg CLOSED by CTO + harness scope-align (9->8 keys)

**archetype:** COORDINATE
**secondary_archetypes:** IMPLEMENT
**Agent:** 0.2.0_DT_PortfolioAnalytics
**Date:** 2026-07-21 (~2034-2040Z)
**Window:** since a4-classhandler-and-item2-coherence-both-green.md (@75d8ed5bd) -- CTO leg-close + 2 scope rulings

## Summary

CTO closed the A4 DT leg (203613Z): NAMED_DELTA_PASS / UNEXPLAINED=0 acceptance met. Both harness
cutover-gate blockers (A4 Item-1 + coherence Item-2) confirmed landed + green. CTO issued two scope rulings;
I absorbed both and aligned the harness registry to the 9->8-key split (@597712d8f). ACKed CTO.

## What happened

1. **A4 DT leg CLOSED** (CTO 203613Z) -- the held-open leg is closed; Item-1 acceptance met on the
   time_series[].period axis, _date_axis {28 served-only, 6 published-only} exact-match to my symmetric-diff.
2. **Scope ruling 1 -- account_distribution not gated:** the cutover REPLACES served with the fresh revamp
   account_dist, so the served-vs-revamp UNEXPLAINED is intraday-drift and MOOT (the check is COHERENCE --
   passed 3/3 -- not parity, for a replace). My --all still REPORTS it (informational); I do NOT gate on it.
3. **Scope ruling 2 -- 9->8 split:** A1 (aum-metrics) = DS builds a producer -> WILL have a parity artifact
   (I cover it once DS lands the shape). A2 (aum-timeseries) = FE-DERIVE (stale legacy dropped from the FE)
   -> NO revamp artifact -> leaves the picture. Aligned @597712d8f: removed the aum_timeseries ARTIFACTS
   target (would only ever read PUBLISHED_ABSENT), kept aum_metrics. Coverage = 8 keys. self-test PASS.

## Current State (--all gate picture, staged gold/mdpf_revamp, ledger de07f087c, harness 597712d8f)

| Key | Verdict | Gate |
|---|---|---|
| aggregate_aua_timeseries global/49financial/inflection | NAMED_DELTA_PASS (0 unexpl.) | GREEN |
| non_model_assets/global (A4) | NAMED_DELTA_PASS (0 unexpl.) | GREEN (leg CLOSED) |
| frontier_coherence 49f/global/inflection (Item-2) | COHERENCE_PASS | GREEN |
| aum_metrics/global (A1) | PUBLISHED_ABSENT | awaiting DS producer shape |
| account_distribution 49f/global | UNEXPLAINED | UNGATED (replace lane, CTO ruling 1) |
| account_distribution/inflection | PASS | -- |
| aum_timeseries | REMOVED (A2 FE-derived) | out of picture |

Harness `mdpf_parity_check.py` on CLOUD: axis-handler 2c6ffad13, coherence b75b459b3, scope-align 597712d8f.
self-test PASS (BUG-1 shape/value, BUG-2, A4 axis, Item-2 coherence regressions all green).

## Blockers

None. Both harness gate-blockers green; A4 leg closed. No open action on me.

## Next Steps

- [0.4.0_DS_ClientPlatform] land the A1 aum-metrics revamp producer shape -> send it my way; I add the
  parity target + coverage (8th key).
- [1.0.0_SA_CTO] per-cycle scheduled parity signal (post cycle-complete.json marker + S3 PASS) -> I run
  --all for the SCHEDULED-streak cycle (N=3 still 0/3; these harness fixes are pre-proof correctness, not
  streak cycles).
- [0.2.0_DT] event-driven: cover aum-metrics on DS's shape; run per-cycle parity on CTO's signal.

## MCP traffic

2 handled. IN: CTO A4-leg-CLOSED + 2 scope rulings (203613Z). OUT: ACK + harness-aligned report (203902Z).

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `python -m py_compile` + `--self-test` | PASS | after aum_timeseries removal; all regressions green. |
| commit-gate (safe-commit) | PASS | @597712d8f clean (surface-check + risk-reflex clean). |
| harness `--all` (read-only S3 verify) | PASS | confirmed aum_timeseries gone; 8-key picture intact (aggregate 3/3 + A4 + coherence green). |

**What worked:** aligning the ARTIFACTS registry to CTO's ruling immediately -- a permanent PUBLISHED_ABSENT
target reads as a pending TODO, so removing the dead A2 pair keeps the gate picture honest.
**What failed:** nothing.
**Gap found:** none.
**Why not comp-*:** harness deliverable (not a deployed pipeline script) -> comp-pipescript n/a; correctness
proven by self-test + real-S3 --all.
