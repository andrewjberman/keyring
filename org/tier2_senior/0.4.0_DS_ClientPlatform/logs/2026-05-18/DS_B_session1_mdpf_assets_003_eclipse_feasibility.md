# DS~B Session 1 — MDPF_ASSETS.003 WS-C Eclipse→Inflection model-AUA feasibility

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-18
**TO:** MDPF_ASSETS.003 (from 2.0.0_SA_COO) — WS-C Phase-0 investigation
**Project:** MDPF_ASSETS (Opal Aggregate AUA)
**Branch:** CLOUD

## Context

MDPF_ASSETS is a new Andrew-directed macro-project — the Model Portfolios "Opal AUA"
number becomes a partner-decomposed aggregate (49 Financial + Inflection + future
partners). WS-C is the Inflection model-AUA pipeline via Eclipse/Orion. This TO is the
Phase-0 feasibility probe: confirm BEFORE the build that the ADVI_ECLDAT shipped Eclipse
data carries what the MDPF §3.2 convergent schema `(firmId, model_id, as_of_date,
model_value, holdings[])` needs. Investigation only — a finding brief, no gold script.

## What was done

Read-only inspection of the ADVI_ECLDAT shipped pipeline (bronze puller + silver
converter + INF_E_00 gold) + the live S3 silver/gold artifacts (`silver/eclipse/2026-05-17/`,
`gold/eclipse/2026-05-17/`) + the prior 2026-05-14 empirical probe artifacts in
`.runtmp/orion_model_probe/`. No ADVI_ECLDAT artifact modified; no live API call.

## Findings (AC1-AC4)

- **AC1 — field inventory documented.** Silver = 4 parquet (portfolios_simple 835,
  portfolios_full 842, models 18, model_composition 9); gold INF_E_00 = 3 parquet
  (accounts 399, households 214, summary 10). Firm headline 2026-05-17:
  total_value_eclipse $93.6M, model_aum_eclipse $96.9M, variance $3.3M (3.4%).
- **AC2 — coverage verdict.** `model_id` + `model_value` PRESENT; `firmId` GAP but a
  one-literal constant (whole Eclipse tenant = Inflection); `as_of_date` PARTIAL but
  serviceable from the partition date; **`holdings[]` = the single genuine gap** — the
  shipped pipeline carries no security-level holdings (model_composition.model_detail
  stops at the Eclipse Security-Set tree).
- **AC3 (§7-Q2) — LINE-ITEM.** Opal model composition is ticker-grain via Orion
  `Trading/Models/{id}.items[]`. PFDE + PFOE held as explicit line-item positions in
  7/9 Opal models (e.g. Opal Long Term PFOE 8.80% + PFDE 10.67%); composition sums to
  exactly 100%. Clean attribution per PRD §3.3 — no look-through derivation. DIVZ/IDVZ
  not held by any Opal model. CAVEAT: items[].targetPercent is the model TARGET weight,
  not the actual account position (±10% tolerance) — flagged for WS-A.
- **AC4 (§7-Q3) — surfaced.** Inflection has ~$106M non-(Opal-)model advised assets
  (IWM models 257 portfolios/$87.9M + unassigned 186/$18.2M) — already in the Eclipse
  `portfolios_full` feed, no new feeder. Whether the IWM book counts as Opal AUA is a
  CTO+Andrew product call (3 framings in the brief §5). Surfaced, not scoped.

## Key finding for the WS-C build

`holdings[]` is the real WS-C Phase-2 scope. The shipped Eclipse `/v1/modeling/models/{id}`
feed exposes only the Security-Set-level tree. The ticker-level composition is the Orion
`GET /api/v1/Trading/Models/{id}.items[]` endpoint — proven by the 2026-05-14 probe but
NOT in the shipped ADVI_ECLDAT bronze puller. WS-C must add that pull (bronze + silver
dim + the (account,ticker) gold expansion). The model-AUA rollup itself is mostly a
conform-and-tag of existing INF_E_00 output.

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| WS-C Phase-0 finding | docs/briefs/mdpf-eclipse-inflection-model-aua-feasibility-20260518.md | COO (RAVC2) -> WS-C Phase-2 build TO |

## Files Modified

| File | Change |
|------|--------|
| docs/briefs/mdpf-eclipse-inflection-model-aua-feasibility-20260518.md | New — WS-C Phase-0 finding brief |
| org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-18/DS_B_session1_mdpf_assets_003_eclipse_feasibility.md | New — this session log |

No code modified — investigation TO.

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-pipescript io INF_E_00.eclipse_model_portfolios` | Ran (TO mandate Phase 0). READS/WRITES "(none detected)" + WARN "no s3_layout constants detected — dynamic key construction; manual review required." Expected — INF_E_00 builds S3 keys dynamically (`f"{GOLD_ECLIPSE_PREFIX}{date}/..."`). Per the TO `if_mismatch` clause, fell back to direct inspection of `convert_eclipse_portfolios_to_silver.py` + `INF_E_00.eclipse_model_portfolios.py` source + the live silver/gold artifacts — recorded actual fields in the brief §2. |
| `aws s3 ls s3://opal-data-inf/silver/eclipse/` | Partitions 2026-05-15, 2026-05-17 present (sparse — not strictly daily; noted as a WS-C cadence dependency in brief §7.6). |

GAP found: `comp-pipescript io` cannot model INF_E_00's I/O because the script uses
f-string dynamic S3 key construction with no `s3_layout` constant block. Logged here as
a comp-tools limitation for the backlog — the Eclipse gold script's READS/WRITES are
invisible to the dependency graph.

## Current State

MDPF_ASSETS.003 investigation COMPLETE — feasibility determined (GO), all of AC1-AC4
answered, finding brief committed. AC5/AC6 close on commit + RAVC2.

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — MDPF_ASSETS.003 complete; finding brief feeds the WS-C Phase-2 build TO. WS-C is GO; scope the build TO around the `holdings[]` gap (Orion `Trading/Models/{id}.items[]` pull). |
| **CTO 1.0.0** | Product call needed on §7-Q3 — does Inflection's IWM book (~$106M) count as Opal AUA? 3 framings in brief §5. Recommend a separate decision point, not a WS-C blocker. PRD §7-Q2 can be marked resolved (line-item, clean attribution). |
| **WS-A author** | 4 ratification inputs in brief §7.5 — canonical model_id space, canonical model_value, target-weight vs actual-position ETF attribution, as_of_date source. |
