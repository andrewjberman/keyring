# 0.4.0_DS_ClientPlatform~A -- crash recovery + A4 non_model build + Andrew calendar assessment

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE
**Serial:** 0.4.0_DS_ClientPlatform~A · **Date:** 2026-07-21 · **Window:** session start (~09:54Z fabric-crash recovery) -> 15:21Z

## Summary

Fabric-crash recovery of the A4 non_model lane. Re-registered ~A, armed watcher, wrote the LD-0290 serial
file. Re-grounded the entire A4 methodology FROM SOURCE, resolved the pre-crash seam (A4 is a DERIVATION off
the aggregate, not an independent producer), authored + tested + committed `dim_mdpf_non_model_assets.py`, and
handled a mid-session Andrew-direct on trading-calendar tie-in (grounded assessment + record/broadcast +
self-correction). A4 is CTO-ACCEPTED for the co-verify slot; the only open dep is base staging its
global+inflection serve-real history.

## MCP traffic (significant only; ~18 messages handled)

- **Andrew-direct (sovereign, in-session):** trading-calendar tie-in / ingestion roll-forward assessment.
  RECORDED verbatim + BROADCAST to CTO/COO/MSTR same-turn (per XXX.md); answered in chat; SELF-CORRECTED a
  stale-read overstatement (GAP-B) to CTO before it misled sequencing.
- **Seam RESOLVED -> base + CTO:** A4 = 2-term derivation off the base global aggregate (opal_aggregate_aua -
  model_aua = $247.69M), NOT independent; source-confirmed. Both ACCEPTED; reverses the pre-crash "A4 is the
  independent producer" read.
- **CTO GATE:** A4 ACCEPTED for co-verify (rides right after the base global-aggregate verify, 144157Z);
  ARCH-GATE on the calendar = converge the local shim under a drift-guard, then HOLD-and-fold into the
  universal calendar WS (Andrew elevated it to universal). Docstring fix held for next-touch.
- **base:** confirmed consume-the-aggregate direction + staged-S3-JSON coupling; CORRECTED my staging URIs
  (gold/mdpf_revamp/{firm}/, not model-portfolios/); DEFERRED etf_public_residual_total for N=3; took the A2
  scope call; requested A4 named-delta specs (sent).

## Compiler Tools

| Tool | Situation | Result | Note |
|---|---|---|---|
| comp-surface-check (via safe-commit) | every A4 commit | PASS | "1 changed file touches no critical surface" x4 commits |
| risk-reflex / comp-pulse diff (via safe-commit) | every A4 commit | PASS | REFLEX CLEAN, 1 file vs 1239 danger nodes, measured |
| commit-gate (py_compile+AST+ruff py39) | every .py edit (Rule 14) | PASS | caught E702 semicolons + F401 unused io; fixed |

**What worked:** the risk-reflex/surface-check ran automatically inside safe-commit on all 4 commits (clean).
**What failed:** none. **Gap:** none.
**Rule-20 note:** A4 is a NEW build-alongside gold script that READS staged artifacts (no infra/frontend
change, not yet wired/deployed) -- the comp-pipescript io/deployed/blast graph checks ride the co-verify +
AE-publish step, not this authoring commit. Grounding was source+live-S3 (build_legacy_compat_emit.py, the
served artifact, raw partition cadence, base's aggregate).

## Briefs / deliverables written (DS)

| Artifact | Path | Commit |
|---|---|---|
| A4 non_model_assets deliverable + named-delta ledger (TO-4) | org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/MDPF_REVAMP_A4_non_model_assets_20260721.md | 426f09bda |
| memory: trading-calendar tie-in for gold producers | memory/feedback_trading_calendar_tie_in_gold_producers_ingestion_schedule.md (+ MEMORY_FULL pointer) | (memory store) |
| A4 ledger spec (non_model_assets/global, JSON) | sent to base for merge into MDPF_REVAMP_named_delta_ledger.json | (MCP 152050Z) |

## Files Modified

see commit messages: 80d30852c (A4 script), f8667aab1 (calendar import + axis check), 64c5a52a0 (URI fix),
426f09bda (deliverable). All authored 0.4.0_DS_ClientPlatform~A, pushed to origin/CLOUD.

## Blockers

None assumption-blocked. **HARD EXTERNAL GATE (stated):** A4's full-scale dry-run + verify is gated on
0.4.0_DS_ClientPlatform (base) staging the GLOBAL + INFLECTION serve-real HISTORY arrays (still latest-only
skeleton). Base is building it now; will ping at stage-time. A4's headline ties BY CONSTRUCTION once staged.

## Current State (zero-context handoff)

- **A4 producer:** `data/mdpf/scripts/gold/dim_mdpf_non_model_assets.py` (commits 80d30852c + f8667aab1 +
  64c5a52a0, pushed). A THIN 2-term derivation: reads base's staged GLOBAL aggregate
  (`s3://opal-data-assets/gold/mdpf_revamp/global/aggregate_aua_timeseries.json`) arrays dates[] /
  opal_aggregate_aua[] / model_aua[]; enterprise_total=opal_aggregate_aua, model_aum=model_aua,
  non_model_aum=enterprise-model; pre-cutover (< 2025-12-23) = verbatim passthrough from the served legacy
  (`s3://opal-data-portal-v2/json/portfolios/non_model_assets.json`). Reads base inflection aggregate for the
  2b audit field. Imports `_trading_day_calendar` (CTO arch-gate). Stages to
  `gold/mdpf_revamp/global/non_model_assets.json`. CLI: --self-test / --dry-run / --global-uri /
  --inflection-uri / --served-uri / --out-dir / --staging-uri / --upload.
- **Verified:** --self-test ties the 2026-07-18 baseline to the cent ($1,782,163,983.16 - $1,534,471,753.80
  = $247,692,229.36 / 13.898397%); guards != spine $312.17M (trap-2), gap $64.48M = inflection non_model.
  E2E dry-run (synthetic global fixture + REAL served legacy) PASS: 297 legacy passthrough + derived,
  validation clean (identity exact, residual sane, ignores a planted trap-2 value); axis WARN fires on a
  weekend row. commit-gate clean.
- **Andrew calendar finding:** raw feeds (schwab fact_rps_s2, smartx fact_model_aum_daily) are
  trading-days-only -> roll-forward mandatory; served does NOT spike to zero today (rolls forward), but via
  ad-hoc heuristics; the mdpf-local `_trading_day_calendar.py` is a divergent stale copy of
  `lib/trading_calendar.py` (fallback-2024-2026 vs 2024-2027). CTO: HOLD-and-fold the convergence into the
  universal calendar WS. COO owns the fabric-wide sweep. Memory recorded.
- **Open items:** (1) base staging global+inflection history [gate]; (2) base to merge the A4 ledger spec;
  (3) A4 axis policy (trading-day + named-delta vs reproduce-455) flagged to CTO as a co-verify contingency
  with a ready roll-forward fix; (4) A2/TO-2 scope = base's call to CTO (spec-vs-DT-harness conflict); (5)
  etf_public_residual = 0.0 fallback for N=3, post-N=3 fast-follow.

## Next Steps

- **[me / 0.4.0_DS_ClientPlatform~A]** On base's stage-time ping: run A4 full dry-run vs the real staged
  global+inflection + served; compute the TBD_STAGE_TIME ledger pct_ranges (enterprise/non_model) + finalize
  the axis/latest-date symmetric-diff; hand CTO the staged A4 for the co-verify.
- **[0.4.0_DS_ClientPlatform (base)]** Stage global+inflection serve-real history; merge the A4 ledger spec;
  take the A2/TO-2 scope call to CTO.
- **[1.0.0_SA_CTO]** Co-verify staged A4 right after the global-aggregate verify (N=3); rule the A4 axis
  policy if reproduce-455 is wanted.
