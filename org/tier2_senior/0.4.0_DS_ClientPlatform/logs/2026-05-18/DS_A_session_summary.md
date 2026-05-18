# Session Summary — DS~A — 2026-05-18

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-18
**Scope:** MDPF_ASSETS macro-project — Phase 0 investigation trio + Phase 1 foundation + Phase 2 feeder. Five TOs touched, four closed.

---

## Summary

Single session, MDPF_ASSETS end-to-end on the DS~A lane: the two Phase-0 investigation TOs, the WS-A canonical contract + aggregation script, and the WS-B 49F/SmartX model-AUA feeder — plus the Cohort 1c taxonomy amendment Andrew directed mid-session. Per-TO session logs carry the detail; this is the session-spanning record.

| TO | Workstream | Status | Closing commit(s) |
|----|-----------|--------|-------------------|
| MDPF_ASSETS.002 | WS-D.1 Phase 0 — PFDE/PFOE ETF net-assets feasibility | COMPLETE — RAVC2-accepted | 886f605f6 |
| MDPF_ASSETS.001 | WS-E Phase 0 — 49F Black Diamond custody-cutout audit | COMPLETE — RAVC2-accepted | d6915ba9a |
| MDPF_ASSETS.004 | WS-A — canonical aggregate-AUA contract + aggregation gold script | COMPLETE — RAVC2-accepted | 7c7400a7a (CTO ratify) / 7c09fccf1 |
| MDPF_ASSETS.007 | WS-B — 49F/SmartX model-AUA feeder (Cohort 1a + 1c) | COMPLETE — all 6 ACs; artifacts in S3 | a691eb9f5 / 24251a794 / d73b0c809 |
| MDPF_ASSETS.010 | WS-E — 49F non-model residual (Cohort 1b) | GO'd — queued, next build | — |

## Key findings (the ones that changed scope)

1. **Fidelity is $13M, not ~$70M (MDPF_ASSETS.001).** The PRD v0.1 premise — "~$70M Fidelity-custodied" as the WS-E cutout — was empirically wrong. A full `silver/fees` account→custodian crosswalk decomposed certified_aua: Schwab 91.3% / ByAll Accounts $135.6M / Fidelity IWS $13.0M / DST $1.2M. Drove Andrew's Schwab-only ruling and a corrected PRD §3.4.
2. **PFDE/PFOE are not TrueShares (MDPF_ASSETS.002).** They are Pathfinder ETFs; net-assets come from a public Filepoint daily CSV — a cleaner source than the TrueShares HTML scrape.
3. **49F per-account model membership IS obtainable (MDPF_ASSETS.007 Phase 0).** PRD named-gap-2 ("SmartX gives only model scalars") was closed — `enterprises/allocations?modelid=` filtered `status=open` is account-grain and reconciles to the validation reference.
4. **Cohort 1c — Opal SMAs (Andrew direct, mid-session).** SMAs are a distinct sub-cohort, not part of model AUA. CTO-ratified (PRD v0.5 + WS-A contract AMENDMENT 1). 49F now decomposes 3-way: 1a Opal Models / 1c Opal SMAs / 1b non-model.
5. **SmartX display-name trap.** SmartX modelId 843d875b labels itself "Pathfinder Focused Opportunities" (the PFOE ETF's name) but is the Opal Equity Growth SMA — flagged in the registry so it is not re-litigated.

## Current cohort state (49 Financial = Cohort 1)

| Sub-cohort | Value (2026-05-18) | Source | Status |
|------------|-------------------:|--------|--------|
| 1a — Opal Models (5 core) | $1,335.95M / 6,755 acct | WS-B feeder, live in `opal-data-mdpf` | DONE |
| 1c — Opal SMAs (Equity Growth + Dividend) | $24.79M / 94 acct | WS-B feeder, live in `opal-data-mdpf` | DONE |
| 1b — Non-model | residual `custody − 1a − 1c` | WS-E (.010) | QUEUED |

## Compiler Tools

Per-TO Compiler Tools sections are in each TO's session log. Session-level: `comp-transform schema-check ModelPortfolios` (WS-A, WARN — inline types); `comp-blast` on the new MDPF scripts (WS-A + WS-B) returned "no nodes" — the correct signal that the new `data/mdpf/` scripts have zero blast overlap with the live INF/SmartX/ETFS chains; `comp-pipescript io E_19` dotted-filename-arg gap logged (routed to comp-tooling). `ds-commit-gate` clean on every `.py` edit; one comp-constants drift caught (`FIRM_ID` collision → renamed `PARTNER_FIRM_ID`).

## Files created this session

| File | TO |
|------|-----|
| `docs/briefs/mdpf-pfde-pfoe-etf-netassets-feasibility-20260518.md` | .002 |
| `docs/briefs/mdpf-49f-nonmodel-custody-cutout-audit-20260518.md` | .001 |
| `docs/briefs/mdpf-assets-wsa-contract-20260518.md` → `docs/architecture/MDPF_ASSETS_WSA_CONTRACT.md` (CTO git mv on ratify) | .004 |
| `docs/briefs/mdpf-assets-007-wsb-49f-smartx-phase0-feasibility-20260518.md` | .007 |
| `data/mdpf/scripts/gold/mdpf_aggregate_aua.py` + `mdpf_aggregate_aua_fixtures.py` + `mdpf_model_registry.json` | .004 |
| `data/mdpf/scripts/feeders/wsb_49f_smartx_model_aua.py` | .007 |
| 5 per-TO session logs under `logs/2026-05-18/` | all |

## Current State

WS-B (.007) closed — Cohort 1a + 1c live in `s3://opal-data-mdpf/mdpf/feeds/`. The WS-A contract is ratified and gates WS-B/C/D/E. The Cohort 1c amendment is ratified end-to-end. RAVC2 sent to COO for the .007 formal close.

## Next Steps

| Recipient | Item |
|-----------|------|
| **DS~A (self)** | Build MDPF_ASSETS.010 — WS-E, Cohort 1b. Residual `non_model_aua = partner_custody_total − model_aua(1a) − sma_aua(1c)`; Schwab custody crosswalk reused from the .001 audit. |
| **DS~A (self)** | MDPF_ASSETS.013 — the WS-A aggregation-script AMENDMENT-1 3-way update — after WS-E (COO authoring; self-sequenced). |
| **COO 2.0.0** | Formal close of .007 (RAVC2 sent). |
| **AE / scheduling** | WS-B feeder `api_get` per-call retry hardening before the daily scheduled run (transient SmartX errors abort the whole run today). |
