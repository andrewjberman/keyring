# Session Log — DS~A — MDPF_ASSETS.007: WS-B 49F/SmartX model-AUA feeder (Cohort 1a)

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-18
**TO:** MDPF_ASSETS.007 (`dsa-wsb-49f-smartx-model-aua-feeder`) — MDPF Phase 2, WS-B, Cohort 1a. GO'd by COO.

---

## Summary

WS-B — the 49 Financial / SmartX model-AUA feeder (Cohort 1a) — Phase 0 + Phase 1 + Phase 2 done. **One step pending: the S3 upload is blocked on the `opal-data-mdpf` bucket not existing yet (AE creates it).**

**Phase 0 — feasibility GATE: GO.** Per-account 49F model membership IS obtainable. SmartX `enterprises/allocations?modelid={modelId}` returns a per-allocation roster (one row per client allocation, with `value`). Filtered `status=open` it is account-grain and reconciles to the validation reference. PRD named-gap-2 closed. No STOP, no contract-downgrade. Brief: `docs/briefs/mdpf-assets-007-wsb-49f-smartx-phase0-feasibility-20260518.md` (commit f5991b5bd).

**Phase 1 — feeder built.** `data/mdpf/scripts/feeders/wsb_49f_smartx_model_aua.py` — self-contained: mints the ROPC JWT, pulls `enterprises/allocations` (status=open) + `reportedmodels/{rmid}/holdings` for the 7 SmartX Opal models, emits the two convergent artifacts (`model_aua_positions` account-grain + `model_composition` (model×ticker)-grain), firm_id=49financial. Registry bumped to v2 (SmartX modelIds added). ds-commit-gate exit 0.

**Phase 2 — verified, reconciles to the cent.** Ran 2026-05-18:

| model_key | WS-B model_value | Accounts | Validation ref ($M) | Delta |
|-----------|-----------------:|---------:|--------------------:|------:|
| opal_ultra_short_term | $52,253,742 | 169 | 52.70 | −0.85% |
| opal_short_term | $104,062,121 | 657 | 104.10 | −0.04% |
| opal_intermediate | $282,922,326 | 1,561 | 283.22 | −0.10% |
| opal_long_term_conservative | $687,628,684 | 2,948 | 686.74 | +0.13% |
| opal_long_term_aggressive | $208,687,311 | 1,420 | 208.90 | −0.10% |
| opal_div_sma | $19,628,462 | 43 | 19.51 | +0.62% |
| opal_growth_sma | $5,067,707 | 51 | 5.10 | −0.65% |
| **model_aua(49financial)** | **$1,360,250,355** | **6,849** | **1,360.27** | **−0.001%** |

`model_composition` target_weight sums to **exactly 1.0** for all 7 models (a synthetic `CUSTODIAL_CASH` row absorbs the ~1.5–3.1% holdings residual SmartX's `percentOfPortfolio` leaves). The per-cohort deltas are the 3-day date offset (ref 2026-05-15, pull 2026-05-18); the total matches to 0.001%.

Artifacts written locally (`.runtmp/mdpf007/wsb_out/`): `model_aua_positions` 6,849 rows, `model_composition` 125 rows.

## Acceptance criteria

| AC | Status |
|----|--------|
| AC1 — Phase-0 feasibility verdict + data-path decision | MET — GO; brief committed |
| AC2 — `model_aua_positions` ships, account-grain, model_key via registry, account-decomposable value | MET — feeder built + verified |
| AC3 — `model_composition` ships, target_weight sums 1.0, is_opal_etf flagged; registry SmartX alignment confirmed | MET — weights sum 1.0; registry v2; the `843d875b` name conflict flagged to COO |
| AC4 — model_aua verified near ref; **artifacts land in opal-data-mdpf**; COO + WS-E lane notified | **PARTIAL** — verified to 0.001%; S3 landing BLOCKED on the `opal-data-mdpf` bucket (does not exist; AE creates it). WS-E-lane notify follows the upload. |
| AC5 — no emoji, gate exit 0, Rule 15, session log + Compiler Tools, RAVC2 | MET |

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-pipescript io` (TO mandate phase 1) | N/A — WS-B consumes no existing SmartX gold/silver script; it reads the SmartX REST API directly. No new IAM surface (creds are the existing `smartx/credentials/*` Secrets Manager secret). |
| `comp-blast wsb_49f_smartx_model_aua` (TO mandate phase 3) | "No nodes matching" — expected for a brand-new feeder. This IS the mandate's pass condition: zero blast overlap with the SmartX EC2-exporter canonical path or any live chain. WS-B is standalone. |
| `.tools/ds-commit-gate.sh` | PASS — py_compile + AST + ruff py39 clean. (One comp-constants drift caught: a module const named `FIRM_ID` collided with a canonical `FIRM_ID='inflection'`; renamed to `PARTNER_FIRM_ID`.) |

## Files Modified

| File | Change |
|------|--------|
| `docs/briefs/mdpf-assets-007-wsb-49f-smartx-phase0-feasibility-20260518.md` | New — Phase-0 feasibility brief |
| `data/mdpf/scripts/feeders/wsb_49f_smartx_model_aua.py` | New — the WS-B feeder |
| `data/mdpf/scripts/gold/mdpf_model_registry.json` | v1→v2 — SmartX modelIds + corrected smartx_name |

## Deploy Evidence

| Item | Result |
|------|--------|
| Phase-0 brief | f5991b5bd, pushed CLOUD |
| Phase 1+2 commit | a691eb9f5, pushed CLOUD |
| Feeder run | 2026-05-18 — model_aua(49financial) $1,360,250,355 (ref $1,360.27M, −0.001%) |
| S3 landing | **PENDING** — `opal-data-mdpf` bucket does not exist; AE creates it (CTO ruling vi) |

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — WS-B feeder built + verified (reconciles to ref within 0.001%). AC1/2/3/5 met; AC4 partial — the S3 upload needs the `opal-data-mdpf` bucket. Route bucket creation to AE; on bucket-ready I run `--upload` (a ~90s mechanical step) and notify the WS-E lane, closing AC4. |
| **AE** | Create the `opal-data-mdpf` non-portal feeder bucket (CTO ruling vi). WS-B writes `mdpf/feeds/{model_aua_positions,model_composition}/49financial/{date}.parquet`. |
| **WS-E lane (DS~A self, MDPF_ASSETS.010)** | On the WS-B S3 upload: model_aua(49financial) is live → WS-E's residual `non_model_aua = partner_custody_total − model_aua` can run; the §7 model_aua_input check consumes `model_aua_positions`. |
| **COO / CTO** | Registry-alignment flag (ruling vii): SmartX modelId `843d875b` display name "Pathfinder Focused Opportunities" vs shortName "OpGEGTR000" (Opal Equity Growth) — mapped to `opal_growth_sma` on the shortName; confirm. |
