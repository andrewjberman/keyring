# Session Log -- 0.4.0_DS_ClientPlatform~D -- 2026-04-28

**Lane:** ~D
**Project:** ADVI_INFSHIP Phase 1 L4 (per-asset pull + ticker classifier + N1-2 mix donut + firm_composition.json)
**TO:** ADVI_INFSHIP.L4 (PRD-driven; no separate TO file authored — GO 20260428T040000Z from 2.0.0_SA_COO covers scope)
**Session start:** ~03:35Z

---

## Summary

Session bring-up + Phase 1 L4 GO received from COO. RAVC2 ack'd. Coordinated with DS~A on
silver layer conventions (alignment confirmed). Authored bronze pull script
`data/orion/manual_api/pull_inflection_assets.py` — clean DS gate (py_compile + AST +
ruff). Script not yet executed; will run after DS~A's `_orion_api_silver_lib.py` lands so
silver step has a path to consume.

---

## Work Item 1 -- ADVI_INFSHIP.L4 GO + Coordination

### GO summary (COO 20260428T040000Z)
PRD: `docs/architecture/ADVI_INFSHIP.md` §4 Phase 1 row L4. Scope:
- Per-asset Inflection-scoped pull (Asset grouping)
- Ticker → asset_class classifier (BD pattern port from
  `data/black_diamond/scripts/classification/classify_bd_securities.py`)
- N1-2 mix donut publisher (firm + per-advisor + per-HH composition)
- `firm_composition.json` refresh

Acceptance: pull runs Inflection-scoped; classifier hits >=95% known-ticker coverage;
firm_composition.json mix donut populates with proper asset_class buckets.

### Critical caveats noted
1. **Asset-grouping queries are heavy.** PATH_DISCOVERY.md: 33-col asset query timed out
   at 180s. My approach: 8 cols + entityIds=[3,11,12] (Inflection cohort) instead of
   Database scope.
2. **Asset.AssetClass / .AssetCategory paths DO NOT WORK** at any grouping. Ticker
   classifier is load-bearing, not optional.
3. **$140M API vs $200M silver-AUA divergence** (DS~A heads-up): cause is
   activityOptionId divergence, NOT sample-size. My pull uses explicit
   `activityOptionId: 1` (Ending MV) per PATH_DISCOVERY.md.

### RAVC2s
| When | To | Subject |
|------|----|---------|
| 03:38Z | 2.0.0_SA_COO | RAVC2 ACK -- ADVI_INFSHIP.L4 GO received | starting investigation |
| 03:43Z | 0.4.0_DS_ClientPlatform~A | COORD -- silver/api_dims/assets/ alignment + schema gating |
| 03:43Z | 0.4.0_DS_ClientPlatform~B | COORD -- pull_inflection_top_holdings.py ownership + classifier reuse |
| 03:48Z | 0.4.0_DS_ClientPlatform~A | RAVC2 ACK -- silver conventions adopted |

### DS~A alignment (received 03:46Z, locked-in conventions)
- Partition layout: `silver/api_dims/{dim}/snapshot_date=YYYY-MM-DD/data.parquet`
- Required cols on every silver/api_dims/* parquet: `snapshot_date`, `source_system='orion-api'`, `rep_id`, `advisor_firm`
- My PKs for assets: `account_id`, `asset_id`, `asset_ticker`, `asset_name`
- DS~A authoring `data/orion/scripts/silver/_orion_api_silver_lib.py` -- shared parse/path helpers + `INFLECTION_REP_IDS={'3','11','12'}` constant + `PARTNER_FIRM_TAGS` + writer
- My `build_assets_dim.py` will gate on this lib landing

### DS~B coordination (no response yet -- not online)
- Took ownership of bronze pull (their `pull_inflection_top_holdings.py` was a draft never executed -- no CSV in pulls/)
- Authored `pull_inflection_assets.py` as my own file; theirs untouched
- Plan: I provide silver/api_dims/assets/, they consume for L2-2/L3-2 top_holdings publishers

---

## Work Item 2 -- Bronze Pull Script (`pull_inflection_assets.py`)

### What
New file at `data/orion/manual_api/pull_inflection_assets.py`. Pulls per-asset positions
from Orion Connect API at Asset grouping, Inflection-scoped via
`requiredOptions.entityIds=[3, 11, 12]`. 8 columns:

| Col | Path | Type |
|-----|------|------|
| 1 | Account.Id | string |
| 2 | Account.Number | string |
| 3 | Household.Id | string |
| 4 | Representative.Id | string |
| 5 | Asset.Id | string |
| 6 | Asset.Name | string |
| 7 | Asset.Ticker | string |
| 8 | Activity.Value (activityOptionId=1, Ending MV) | currency |

### Outputs
- Local: `data/orion/manual_api/pulls/{YYYY-MM-DD}_inflection_assets.csv`
- Bronze (with `--upload-bronze`): `s3://opal-data-inf/bronze/orion-api/{YYYY-MM-DD}/assets.csv`
- Post-pull summary: ticker count, total Inflection AUA aggregated, top-25 holdings by MV

### DS gate result
```
.tools/ds-commit-gate.sh data/orion/manual_api/pull_inflection_assets.py
All checks passed!
```
- py_compile: PASS
- ds-precommit-check.py (AST undefined-name scanner): PASS
- ruff (target py39): PASS after one fix (F541 f-string without placeholder)

### Not executed yet (deliberate)
- Heavy API call (~5-10 min). Will run on next session after DS~A's silver lib lands so
  the bronze→silver path is end-to-end testable in one session.
- JWT live: confirmed in `s3://opal-data-inf/orion/jwt/current.json` (ttl_seconds present, jwt 454 chars)

---

## Compiler Tools

| Tool | Where | Result |
|------|-------|--------|
| `.tools/ds-commit-gate.sh` | Pre-commit on pull_inflection_assets.py | CLEAN (after F541 fix) |

`comp-pipescript io` not run -- not a gold script. `comp-pipescript deployed` not run --
not deployed yet. Will run both at silver/gold script authoring time per DS minimum
(see TO_COMPILER_GATE).

---

## Pending / Next

| Item | Gate | Owner |
|------|------|-------|
| `_orion_api_silver_lib.py` (shared lib) | DS~A in flight | DS~A |
| `data/orion/scripts/silver/build_assets_dim.py` | gates on DS~A lib | ~D |
| Run bronze pull -- validate CSV shape + AUA reconciliation against silver/canonical/holdings_* | bronze script committed | ~D |
| `data/orion/scripts/classification/classify_assets.py` (portable BD-pattern port) | independent | ~D |
| Refactor `INF_I_D03.composition_artifacts.py` `_classify()` to use new module | classifier ready | ~D |
| Execute end-to-end pull -> silver -> classify -> publish -> validate | all of the above | ~D |
| RAVC4 to COO | end-to-end run + memo | ~D |
| RAVC4 to DE 0.4.0 (B3 dependency) | publisher refresh | ~D |

---

## Author identity

`0.4.0_DS_ClientPlatform_D` (underscore form for git per CLAUDE.md author char restriction;
`~D` only used in MCP/broker context).
