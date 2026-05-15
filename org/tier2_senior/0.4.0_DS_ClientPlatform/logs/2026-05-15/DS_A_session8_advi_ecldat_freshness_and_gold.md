# Session Log — DS~A — ADVI_ECLDAT freshness verify + INF_E_00 gold model-portfolios layer

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-15
**Authorization:** Andrew direct ad-hoc — "sorting out that [Eclipse model-portfolios] pipeline is now going to be your job"
**Commits:** `1d561054a` (ECLDAT.002 JWT fix), `99db72599` (ECLDAT.004 full endpoint + gold)

---

## Objective

Andrew handed me the Eclipse model-portfolios pipeline. Three directives, in order:
1. Verify today's data freshness — re-run bronze + silver, reconcile against Eclipse.
2. Goal: reliable daily model-portfolio summary numbers, aggregated account -> household -> partner.
3. Build the bronze/silver/gold structure; gold = aggregates; platinum D-group consumes gold.

Andrew decisions (AskUserQuestion): carry both AUM figures side by side; gold = account-grain
table + rollups; investigate the reconciliation gap before building gold; full endpoint + all 3 tiers.

---

## Freshness verification — found and fixed a production bug

Re-running the bronze puller failed with **401 "Invalid Authorization Header"**. Root cause:
the SM secret `orion/eclipse_jwt/current` is stored by ADVI_ECLDAT.001 (AE) as a JSON object
with metadata (`{jwt, eclipse_user_id, orion_user_id, expires_at, captured_at}`), but the bronze
puller's `load_eclipse_jwt` Path 1 passed the entire JSON blob into the `Authorization: Session`
header. It only looked "fresh" because `_decode_exp` split on `.` and accidentally landed on the
embedded JWT payload segment. **This would have 401'd every daily run** once the pipeline used
the SM path (the morning pull happened pre-ECLDAT.001 ship, so it used the exchange path and
masked the bug).

Fix: added `_extract_jwt()` to unwrap the JSON-wrapped secret. Shipped as `1d561054a`.
Bronze + silver then re-ran clean.

---

## Reconciliation investigation (Andrew: "investigate now")

The 414-vs-399 account gap and the ~3.4% dollar gap had a single root cause, and chasing it
surfaced a structural design gap.

**The production bronze puller pulled the wrong (thinner) endpoint.** `/v1/portfolio/portfolios/simple`
carries no value. The richer `/v1/portfolio/portfolios` endpoint carries `totalValue`,
`managedValue`, `excludedValue`, `numOfAssociatedAccounts`, `lastRebalancedOn`, cash fields.

Findings:
- **`totalValue` summed ($94,976,226) cross-validates against Orion `accounts_v2.current_value`
  ($94,987,468) to $11,242 — 0.01%.** Two independent systems agree.
- **The "3.4% gap" was an artifact of comparing to `modelAUM`** — Eclipse's cached model-level
  headline ($98.3M). 5 of 9 models reconcile exact (`totalValue == modelAUM`); 4 stale models
  (last rebalance 2026-05-13) carry the variance. Not a data error.
- **The 414-vs-399 count gap is day-stale-CSV vs live API.** The live API self-agrees at 399
  across both today's pulls; the colleague's Models.csv export (2026-05-14 16:23) is stale.
- `totalValue = managedValue + excludedValue` ($92.62M managed + $2.35M excluded/held-away).
- The 1 non-joining account = the 1 Eclipse portfolio with `numOfAssociatedAccounts: 0`.

---

## Bronze/Silver/Gold built

**bronze** — `pull_eclipse_portfolios.py`: added `/v1/portfolio/portfolios` full pull (kept
`/simple` for the `accountId` join key). 12 API calls/run. New artifact `portfolios_full.json`.

**silver** — `convert_eclipse_portfolios_to_silver.py`: added `convert_portfolios_full` ->
`portfolios_full.parquet` (842 rows, 57 cols). Added `float_fields` bucket to `_coerce_frame`
for money/percent columns. Dedup + type standardization only — no field slimming (Rule 17).

**gold** — `INF_E_00.eclipse_model_portfolios.py` (new): joins eclipse silver (simple + full +
model_composition) with `accounts_v2` silver. Emits three grains to `gold/eclipse/{date}/`:
- `model_portfolio_accounts.parquet` — 399 rows, account grain (atomic)
- `model_portfolio_households.parquet` — 214 rows, HH rollup
- `model_portfolio_summary.parquet` — 10 rows (9 models + firm row)
Each carries both `total_value` (Eclipse, account-decomposable) and `model_aum` (Eclipse cached
headline) with per-model `aum_variance` as an explicit field.

---

## Files Modified

| File | Change |
|------|--------|
| `data/orion/scripts/bronze/pull_eclipse_portfolios.py` | `_extract_jwt()` JSON-secret unwrap (`1d561054a`); `/v1/portfolio/portfolios` full pull (`99db72599`) |
| `data/orion/scripts/silver/convert_eclipse_portfolios_to_silver.py` | `convert_portfolios_full` + `float_fields` bucket |
| `data/orion/scripts/gold/INF_E_00.eclipse_model_portfolios.py` | New — Eclipse model-portfolios gold aggregator |

---

## Deploy Evidence

| Step | Result |
|------|--------|
| ds-commit-gate.sh | PASS — all 3 files (py_compile + AST scan + ruff py39) |
| Commit (JWT fix) | `1d561054a` — bronze JWT JSON-unwrap |
| Commit (3-tier) | `99db72599` — full endpoint + INF_E_00 gold |
| Author | `0.4.0_DS_ClientPlatform~A` |
| Push | `origin/CLOUD` — `d5fbf4ea4..1d561054a`, `1d561054a..99db72599` |
| safe-deploy gate | PASS — all 3 scripts DEPLOYED `[inf]` to S3 |
| bronze run | PASS — 12 API calls, 835 simple + 842 full + 18 models + 9 comp |
| silver run | PASS — 5 artifacts, 0 dedupe drops, 0 coercion errors |
| gold run | PASS — 3 tables: accounts 399, households 214, summary 10 |

**Gold firm headline** (`gold/eclipse/2026-05-15/_meta/gold_complete.json`):
- account_count 399, household_count 214
- total_value_eclipse $94,976,226.34
- model_aum_eclipse $98,300,461.50
- aum_variance $3,324,235.16 (+3.50%)
- orion_current_value $94,987,468.16

**Aggregation integrity:** account-grain sum = firm row = sum of 9 model rows = sum of 214 HH
rows = $94,976,226.34 (tie to the cent). `total_value` vs `orion_current_value` mean abs diff
$28.66/account.

---

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `ds-commit-gate.sh` (x4) | PASS | py_compile + AST undefined-name + ruff py39, per file |
| `comp-build` | RAN | Graph rebuilt; 1667/1741 nodes indexed |
| `comp-pipescript io INF_E_00` | N/A | New script not yet in comp graph (not chain-wired); gold reads whole parquet frames so there is no narrow column-load-list to gap-check |
| `comp-validate` | N/A | No validate config for inf gold (`gold_validate_config.yaml` is black_diamond-scoped) |

---

## Acceptance Criteria Status

| AC | Criterion | Status |
|----|-----------|--------|
| AC1 | Bronze freshness verified — re-run succeeds | PASS (after JWT fix) |
| AC2 | Reconciliation gap investigated + root-caused | PASS |
| AC3 | Bronze pulls full `/v1/portfolio/portfolios` endpoint | PASS |
| AC4 | Silver canonicalizes `portfolios_full` (Rule 17) | PASS |
| AC5 | Gold emits account + household + model grains | PASS |
| AC6 | Both AUM figures carried with variance field | PASS |
| AC7 | `from __future__ import annotations` first import (all 3) | PASS |
| AC8 | ds-commit-gate PASS + safe-deploy PASS | PASS |
| AC9 | Aggregation grains tie out | PASS (cent-exact) |
| AC10 | No emoji | PASS |

---

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC — ADVI_ECLDAT.004 gold layer shipped under Andrew direct (TO was never authored); project JSON `blocking` item (4) can clear |
| **CTO 1.0.0** | CC — INF_E_00 introduces a new gold "E" family (Eclipse domain); not yet wired into the inf gold dispatch chain |
| **AE 0.6.1** | The Eclipse mini-chain (bronze->silver->gold) needs chain-wiring into `orion-gold-dispatch.sh` for daily automation — currently manual-run only |
| **DE 0.4** | Phase 5 FE wire — platinum D-group script to consume `gold/eclipse/{date}/model_portfolio_*.parquet` |
| **DS~A (self)** | Open: modelAUM-vs-totalValue variance ($3.3M) is documented as a field; revisit if it widens. 1 unjoined account (Eclipse portfolio with 0 associated accounts). |

---

## Open Gaps

- **Daily automation:** the Eclipse chain runs manually today. Chain-wiring into the inf gold
  dispatch (AE lane) is required for the "daily basis" part of Andrew's goal.
- **modelAUM variance:** carried as `aum_variance` per model. Large in % for small models
  (Ultra Short +44.9%, Short +34.5%) — Eclipse's cached model headline lags the live portfolio
  list. Documented, not blocking; the account-decomposable `total_value` is the canonical figure.
- **comp graph:** INF_E_00 should be registered once chain-wired so `comp-pipescript` covers it.
