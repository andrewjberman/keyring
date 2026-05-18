# DS~B Session 3 — MDPF_ASSETS.008 WS-C Inflection/Eclipse model-AUA feeder

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-18
**TO:** MDPF_ASSETS.008 (from 2.0.0_SA_COO) — WS-C build (Cohort 2a + 2b)
**Project:** MDPF_ASSETS (Opal Aggregate AUA)
**Branch:** CLOUD

## Context

WS-C feeds Cohort 2a (Inflection model AUA) + Cohort 2b (Inflection non-model AUA)
into the MDPF canonical schema, firm_id=inflection. DS~B authored the .003 WS-C
feasibility brief (the build spec); this TO is the build, against the ratified
WS-A contract. The contract specifies three convergent feeder artifacts the WS-A
aggregation script (`mdpf_aggregate_aua.py`) consumes.

## What was built

Two new scripts under `data/mdpf/scripts/` — kept out of any existing pipeline's
gold/ run-set per contract section 8 (the same reason the WS-A aggregation script
lives there):

| Script | Role |
|--------|------|
| `data/mdpf/scripts/bronze/pull_orion_model_composition.py` | Pulls the ticker-grain composition of the 9 Opal models from Orion `GET /api/v1/Trading/Models/{id}` — the holdings[] gap (.003 section 6). Reuses the `orion/jwt/current` JWT (no new auth). 9 Orion ids read from `mdpf_model_registry.json` (never hard-coded). Lands raw JSON to `opal-data-mdpf/mdpf/bronze/`. |
| `data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py` | Emits the 3 convergent feeder artifacts for firm_id=inflection: `model_composition`, `model_aua_positions`, `non_model_aua`. |

Design note: a separate silver tier was folded into the gold feeder — the MDPF
convergent feeder artifacts ARE the silver/gold-equivalent (the conformed output);
a standalone silver dim that just reshapes Orion items[] then re-emits would be
redundant ceremony. bronze (live pull) + gold (build feeder) is the structure.

## The three feeder artifacts (firm_id=inflection, 2026-05-18)

- **model_composition** — 168 rows, (model_key x ticker) grain. From the Orion
  items[]. All 9 models' `target_weight` (decimal 0-1) sum to exactly 1.0. 12
  `is_opal_etf` rows — PFDE + PFOE held as line items in 6 Opal models (matches
  the .003 section 4.3 table; the .003 prose "7 of 9" was a miscount, 6 is
  correct). `actual_weight` null (CTO ruling iii — v1 target_weight basis).
- **model_aua_positions** — 399 rows, account grain. Conformed from INF_E_00's
  `model_portfolio_accounts.parquet`. `model_value` = account-decomposable
  `total_value` (NOT `model_aum` — ruling ii). `model_key` via the registry,
  0 unmapped. `model_aua(inflection)` = **$93,603,055.45**.
- **non_model_aua** — 1 row, (firm x date) grain. The contract-section-4
  residual: `partner_custody_total $199,715,114.97 − model_aua_input
  $93,603,055.45 = non_model_aua $106,112,059.52` (Cohort 2b — matches the
  .003 section 5 ~$106M IWM+unassigned finding).

## Custody-scope finding (Phase 3 — surfaced, not silently resolved)

`partner_custody_total(inflection)` is set to the full active Eclipse-administered
book ($199.72M — Sigma total_value over the 842 portfolios_full rows, is_deleted
!= 1). `custody_scope = "eclipse_administered_book"`, `method =
"inflection_eclipse_full_active_book_minus_opal_model"` — honest provenance.

The 2026-05-15 coworker-sheet Fidelity-custody view is $203.87M — it differs from
the Eclipse-administered view by ~$4.2M, and the unassigned bucket ($18.2M, .003
section 5) may include `source=Team` org containers rather than client custody
assets. Whether the canonical `partner_custody_total` is the Eclipse-administered
book, a Fidelity-custody-confirmed total, or the book minus Team-containers is an
open per-partner determination — a CTO/Andrew product call. Per the TO this is
SURFACED, not blocked: the contract's residual design (`partner_custody_total` +
`model_aua_input` carried as audit fields) makes the residual reproducible and
correctable when the scope is ruled. Escalated to COO (RAVC2).

## Verification (AC4)

- model_composition `target_weight` sums to 1.0 for all 9 models — PASS.
- `model_aua(inflection)` $93,603,055.45 reconciles **EXACT** to the INF_E_00
  2026-05-18 firm headline `total_value_eclipse` $93,603,055.45 — PASS.
- `non_model_aua.model_aua_input` == Sigma `model_aua_positions.model_value` — PASS
  (the contract section-7 feed-sync gate).
- **End-to-end:** `mdpf_aggregate_aua.py --source s3 --date 2026-05-18` reads all
  3 WS-C feeders from opal-data-mdpf → `opal_aggregate_aua` $199,715,114.97
  (model $93.6M + non_model $106.1M), partner=inflection, reconciliation **overall
  PASS**. ETF decomposition derives `held_inflection(PFDE)` $9,766,913.38 /
  `held_inflection(PFOE)` $8,017,497.73 from model_composition x model_aua — the
  section-3.3 attribution WS-D.2 consumes.
- All 3 artifacts landed: `s3://opal-data-mdpf/mdpf/feeds/{artifact}/inflection/
  2026-05-18.parquet`.

## Files Modified

| File | Change |
|------|--------|
| data/mdpf/scripts/bronze/pull_orion_model_composition.py | New — Orion model-composition bronze puller |
| data/mdpf/scripts/gold/build_mdpf_wsc_inflection_feeder.py | New — WS-C feeder builder (3 convergent artifacts) |
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/MDPF_ASSETS.008.dsb-wsc-inflection-eclipse-model-aua-feeder.md | status -> complete |
| org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-18/DS_B_session3_mdpf_assets_008_wsc_inflection_feeder.md | New — this session log |

S3 (not git — opal-data-mdpf is the feeder store): `mdpf/feeds/{model_aua_positions,
model_composition,non_model_aua}/inflection/2026-05-18.parquet`; `mdpf/bronze/
orion_model_composition/2026-05-18/` (9 raw model JSON).

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-pipescript io INF_E_00.eclipse_model_portfolios` + `convert_eclipse_portfolios_to_silver` (Phase-1 mandate) | Both return "(none detected)" + WARN — the shipped Eclipse scripts use f-string dynamic S3 key construction with no `s3_layout` constant block, so comp can't model their I/O. Per the TO `if_mismatch`, grounded the conform by direct inspection of the scripts + the live `gold/eclipse/2026-05-18/` + `silver/eclipse/2026-05-18/` artifacts. |
| comp-iam (Phase-1 mandate) | N/A — WS-C scripts run ad-hoc/locally (DS QA), not as a Lambda; no new IAM/Lambda surface. The Orion pull reuses the existing `orion/jwt/current` JWT. |
| `comp-blast build_mdpf_wsc_inflection_feeder` / `pull_orion_model_composition` (Phase-3 mandate) | "No nodes matching" — the new `data/mdpf/scripts/` scripts are off-graph (cache predates them). This IS the expected confirmation: zero edges = WS-C modifies no ADVI_ECLDAT artifact (it READS opal-data-inf, WRITES opal-data-mdpf). Backlog: a `comp-build` rebuild would pick up `data/mdpf/scripts/`. |
| `.tools/ds-commit-gate.sh` (both .py) | PASS — py_compile + ds-precommit-check + ruff py39. Note: the gate's comp-constants drift check flagged a generic `FIRM_ID` constant (canonical `49financial` from BD lambdas); renamed to `INFLECTION_FIRM_ID` — feeder-specific + non-colliding. |

## Current State

MDPF_ASSETS.008 COMPLETE — all 5 ACs PASS, 3 WS-C feeder artifacts live in
opal-data-mdpf, WS-A end-to-end verified. RAVC2 to COO.

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — MDPF_ASSETS.008 complete. Custody-scope determination for `partner_custody_total(inflection)` (Eclipse-administered $199.72M vs Fidelity-custody $203.87M vs book-minus-Team-containers) is a CTO/Andrew product call — surfaced, not blocking; the residual is reproducible/correctable. |
| **DS~B (self)** | MDPF_ASSETS.009 (WS-D.2) — staged behind .008. Phase-0 read-only scope confirmed (COO-invited early): the section-3.3 decomposition logic is already in `mdpf_aggregate_aua.py:build_etf_decomposition`; .009's real scope is a small `etf_net_assets` feeder (`opal-data-etfs/silver/netassets_daily.parquet`, all 4 Opal ETFs / 590 rows → conform → `opal-data-mdpf/mdpf/feeds/etf_net_assets/`) + end-to-end verification. NOT a from-scratch decomposition. Awaiting COO GO. |
