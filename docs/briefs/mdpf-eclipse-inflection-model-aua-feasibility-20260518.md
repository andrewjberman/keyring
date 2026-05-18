# Brief — MDPF_ASSETS WS-C: Eclipse-Portfolio → Inflection Model-AUA Feasibility

**Project:** MDPF_ASSETS (Opal Aggregate AUA)
**TO:** MDPF_ASSETS.003 (WS-C Phase-0 investigation)
**Author:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-18
**Issued to:** 2.0.0_SA_COO (RAVC2) — feeds the WS-C Phase-2 build TO
**Status:** Feasibility determined. Investigation only — no gold script authored, no ADVI_ECLDAT artifact modified.

---

## TL;DR

1. **Feasibility: GO.** The ADVI_ECLDAT shipped Eclipse pipeline carries the partner identity, model assignment, and model values WS-C needs. The convergent-schema gap is **one term — `holdings[]`** — and it is closeable with a proven, already-empirically-probed endpoint (the 2026-05-14 feasibility probe pulled it). No blocker.

2. **`holdings[]` is the real WS-C build scope.** The shipped Eclipse pipeline's `model_composition` artifact carries only the Eclipse **Security-Set-level** composition tree (`model_detail`) — it stops at opaque "Security Set" references and does **not** expose security/ticker-level holdings. The ticker-level composition lives in the **Orion** `GET /api/v1/Trading/Models/{id}.items[]` endpoint, which the shipped ADVI_ECLDAT bronze puller does **not** call. WS-C must add that pull.

3. **§7-Q2 (ETF look-through) answered: LINE-ITEM, clean attribution.** Opal model composition is ticker-grain. Opal ETFs **PFDE and PFOE are held as explicit line-item positions** in 7 of the 9 Opal models (e.g. Opal Long Term: PFOE 8.80% + PFDE 10.67%), each with a `ticker` + `targetPercent`. This is the PRD §3.3 clean-attribution case — `held_inflection(PFDE/PFOE)` is directly derivable; no look-through-to-underlying derivation needed. DIVZ / IDVZ are **not** held by any Opal model.

4. **§7-Q3 (Inflection non-model AUA) surfaced: YES, it exists and is ~$106M.** The same Eclipse `/v1/portfolio/portfolios` feed already pulled carries Inflection's **full** advised book — 842 portfolios / **$199.7M**. Only **399 / $93.6M** are on Opal models. The remaining **257 / $87.9M** are on Inflection's own "IWM" model lineup and **186 / $18.2M** are unassigned. Whether the IWM book counts as Opal advised AUA is a product call — surfaced here, not scoped.

---

## 1. Scope + method

WS-C routes ADVI_ECLDAT's Eclipse portfolio ingestion into the MDPF canonical model-AUA schema, tagged `firmId = inflection`. This Phase-0 TO confirms — **before** the build — that the Eclipse data carries what model-AUA needs.

**Method:** read-only inspection of the ADVI_ECLDAT shipped pipeline (bronze puller, silver converter, INF_E_00 gold) + the live S3 artifacts (`silver/eclipse/2026-05-17/`, `gold/eclipse/2026-05-17/`) + the prior empirical evidence in `docs/briefs/data-scientist-eclipse-ingestion-feasibility-20260514.md` and its `.runtmp/orion_model_probe/` snapshots. No ADVI_ECLDAT bronze/silver was modified. No live Eclipse/Orion API call was made.

---

## 2. AC1 — Eclipse silver + INF_E_00 field inventory

### 2.1 — The shipped ADVI_ECLDAT pipeline

| Tier | Script | Output |
|---|---|---|
| bronze | `data/orion/scripts/bronze/pull_eclipse_portfolios.py` | `s3://opal-data-inf/bronze/eclipse/{date}/` — `portfolios_simple.json`, `portfolios_full.json`, `models.json`, `model_composition_{id}.json` (x9) |
| silver | `data/orion/scripts/silver/convert_eclipse_portfolios_to_silver.py` | `s3://opal-data-inf/silver/eclipse/{date}/` — 4 parquet artifacts (below) |
| gold | `data/orion/scripts/gold/INF_E_00.eclipse_model_portfolios.py` | `s3://opal-data-inf/gold/eclipse/{date}/` — 3 parquet artifacts (below) |

Latest live partition: **2026-05-17** (silver + gold both present, `_meta` sentinels `overall:success`). Note partitions are sparse (2026-05-15, 2026-05-17 present; not strictly daily — a WS-C freshness dependency to confirm with ADVI_ECLDAT).

### 2.2 — Silver artifacts (`silver/eclipse/2026-05-17/`)

| Artifact | Rows | Cols | What it carries |
|---|---|---|---|
| `portfolios_simple.parquet` | 835 | 24 | Portfolio identity + **model assignment + Orion-account join key**. Key fields: `id` (Eclipse portfolio id), `name`, `account_id` / `eclipse_account_id_int` (Orion join key), `account_number`, `model_id` (Eclipse model assignment), `source`, `is_deleted`, `sleeve_portfolio`. |
| `portfolios_full.parquet` | 842 | 57 | Per-portfolio **value + cash + rebalance detail**. Key fields: `id`, `model_id`, `total_value`, `managed_value`, `excluded_value`, `current_cash`, `num_of_associated_accounts`, `last_rebalanced_on`, `status`, `style`. No `accountId` (joins to simple on `id`). |
| `models.parquet` | 18 | 32 | Eclipse model catalog (Inflection-visible models: the IWM lineup ids 11-25/27, PCOFX, "50/50 OPAL INT/OPAL LTC" id 28). Metadata only. |
| `model_composition.parquet` | 9 | 56 | Per-Opal-model detail. Key fields: `id`, `name`, `name_space`, `model_aum` (headline AUM), **`model_detail`** (the composition tree, JSON string), `is_sma`, `model_type_id`. |

Silver is Rule-17-clean (dedupe + dtype standardization only; no field slimming — verified in the converter source).

### 2.3 — Gold artifacts (`gold/eclipse/2026-05-17/`, INF_E_00)

INF_E_00 aggregates `atomic account → household → Eclipse model → firm`, joining the Eclipse silver to `silver/api_dims/accounts_v2/` for household/advisor/Orion-value enrichment.

| Artifact | Rows | What it carries |
|---|---|---|
| `model_portfolio_accounts.parquet` | 399 | One row per Opal-model-assigned account: `eclipse_portfolio_id`, `eclipse_account_id`, `eclipse_model_id`, `model_name`, `total_value`, `managed_value`, `current_cash`, `household_id`, `representative_name`, `advisor_firm`, `custodian`, `orion_current_value`, `data_as_of`. |
| `model_portfolio_households.parquet` | 214 | Household rollup. |
| `model_portfolio_summary.parquet` | 10 | One row per Opal model (9) + a firm row. Carries **two AUM figures side by side**: `total_value_eclipse` (summed from the live portfolio list, account-decomposable) and `model_aum_eclipse` (the cached Eclipse model headline), plus `aum_variance` / `aum_variance_pct`. |

**Firm headline (2026-05-17, from `gold_complete.json`):** 399 accounts / 214 households; `total_value_eclipse` **$93,603,064.81**; `model_aum_eclipse` **$96,895,158.05**; `aum_variance` **$3,292,093.24** (3.4%); `orion_current_value` $93,603,056.57. The 3.4% gap reproduces the 2026-05-14 feasibility brief's finding (Orion `currentValue` valuation lag vs Eclipse rebalance day).

### 2.4 — The 9 Opal models in Eclipse

`OPAL_ECLIPSE_MODEL_IDS = [3, 5, 6, 7, 8, 9, 10, 28, 29]` (hardcoded in both silver + gold). Per-model AUM (2026-05-17 `model_aum`):

| Eclipse id | Name | name_space | model_aum | Accounts |
|---:|---|---|---:|---:|
| 3 | Opal Long Term | Opal Capital LTC | $6,805,176.93 | 54 |
| 5 | Opal Ultra Long Term | Opal Capital | $1,517,283.05 | 23 |
| 6 | Opal Intermediate Growth | Opal Capital | $58,534,385.15 | 159 |
| 7 | Opal Short Term | Opal Capital | $3,224,136.62 | 10 |
| 8 | Opal Ultra Short Term | Opal Capital | $560,696.26 | 5 |
| 9 | Opal Growth SMA | Opal Capital | $0.00 | 0 |
| 10 | Opal DIV SMA | Opal Capital | $0.00 | 0 |
| 28 | 50/50 OPAL INT/OPAL LTC | Inflection Wealth Management | $20,246,950.93 | 127 |
| 29 | 50/50 OPAL ST/INT | Inflection Wealth Management | $6,006,529.11 | 21 |

Models 9 + 10 (SMAs) carry zero Inflection assets. Models 28 + 29 are Inflection-namespace blends of Opal sleeves.

---

## 3. AC2 — Coverage vs the PRD §3.2 convergent schema

Convergent schema every model-AUA feeder must emit: **`(firmId, model_id, as_of_date, model_value, holdings[])`**.

| Term | Verdict | Eclipse-silver source / gap |
|---|---|---|
| **`firmId`** | GAP — trivially derivable | Not present on any Eclipse silver/gold row. The whole Eclipse tenant **is** Inflection (firm_id 209900). WS-C injects `firmId = "inflection"` as a constant column. Cost: one literal. |
| **`model_id`** | PRESENT | `portfolios_simple.model_id` / gold `eclipse_model_id`. **Eclipse ID space** [3,5,6,7,8,9,10,28,29] — distinct from Orion's [83,84,85,86,87,88,89,152,153]. The Eclipse↔Orion↔name map is in the 2026-05-14 feasibility brief §2.1. WS-A must rule which ID space (or model name) is the MDPF canonical `model_id`. |
| **`as_of_date`** | PARTIAL — serviceable | No clean valuation-as-of field. Gold `data_as_of` = the Eclipse silver **partition/pull date** (e.g. 2026-05-17). Portfolios also carry `last_rebalanced_on` (e.g. 2026-05-13). Portfolio `total_value` is point-in-time-at-pull. WS-C treats the partition date as `as_of_date`; if a true market-valuation date is required, derive from Orion `lastPositionDate`. |
| **`model_value`** | PRESENT — two candidates | Gold carries both: **`total_value_eclipse`** (summed from the live portfolio list — account-decomposable, cross-validated against Orion accounts_v2) and **`model_aum_eclipse`** (the cached Eclipse model headline). They differ by $3.3M / 3.4% at the firm level. **Recommend WS-A canonicalize on `total_value_eclipse`** — it decomposes to account grain (needed for the ETF ownership decomposition) and reconciles to Orion. The headline figure is a sentinel/cross-check. CTO/WS-A call. |
| **`holdings[]`** | **GAP — the real WS-C build scope** | The shipped pipeline carries **no security-level holdings**. `model_composition.model_detail` is only the Eclipse Security-Set tree (see §4). WS-C must add a ticker-level composition pull — see §4.2. |

**Verdict:** 2 of 5 terms fully present (`model_id`, `model_value`); `firmId` is a one-literal constant; `as_of_date` is serviceable from the partition; **`holdings[]` is the single genuine gap** and the substance of the WS-C Phase-2 build.

---

## 4. AC3 (PRD §7-Q2) — ETF position granularity: LINE-ITEM

### 4.1 — The shipped pipeline does not expose security-level holdings

The Eclipse `model_composition.model_detail` tree, walked for all 9 Opal models, stops at the **Security Set** level:

```
Opal Intermediate Growth (id 6)
  └─ "Opal Int"  type=Security Set(4)  targetPercent=100  securityAsset={id:4, meId:4}
50/50 OPAL INT/OPAL LTC (id 28)
  ├─ "Opal Int"  type=Security Set(4)  targetPercent=50.01  securityAsset={id:4, meId:4}
  └─ "Opal LTC"  type=Security Set(4)  targetPercent=49.99  securityAsset={id:1, meId:2}
```

Each Security Set node has `children: []` — the actual ticker-level securities are **not** in this tree; the Security Set is an opaque reference (`securityAsset.meId`). So the shipped Eclipse `/v1/modeling/models/{id}` feed exposes ETF positions at **no granularity** — neither line-item nor look-through.

### 4.2 — The ticker-level composition exists — via the Orion endpoint, not Eclipse

The 2026-05-14 feasibility probe pulled `GET /api/v1/Trading/Models/{id}` (Orion main API), whose `items[]` array **is** the ticker-level composition. Snapshot preserved at `.runtmp/orion_model_probe/opal_models_with_items.json` (all 9 Opal models, keyed by Orion id). Each item:

```json
{ "productId": 8, "productName": "iShares Core S&P Mid-Cap ETF", "ticker": "IJH",
  "targetPercent": 3.58, "itemTolUpper": 10.0, "itemTolLower": 10.0, "productClass": "MS-MB" }
```

Composition sums to **exactly 100.00%** for all 9 models. 78 unique tickers across the 9 model definitions (all line-item ETFs/securities/cash — incl. a `CUSTODIAL_CASH` line).

### 4.3 — Opal ETFs ARE held as line items — clean attribution

Scanning all 9 Opal model compositions for the four Opal ETFs (DIVZ / IDVZ / PFDE / PFOE):

| Opal model | PFDE | PFOE | DIVZ | IDVZ |
|---|---:|---:|---:|---:|
| Opal Long Term | 10.67% | 8.80% | — | — |
| Opal Intermediate Growth | 7.49% | 6.21% | — | — |
| Opal Ultra Long Term | 11.79% | 9.57% | — | — |
| Opal Short Term | 2.38% | 2.89% | — | — |
| Opal Ultra Short Term | — | — | — | — |
| 50/50 INT/LTC | 9.08% | 7.51% | — | — |
| 50/50 ST/INT | 4.94% | 4.55% | — | — |
| Opal Growth SMA / Opal DIV SMA | — | — | — | — |

**Answer to §7-Q2: LINE-ITEM.** PFDE and PFOE appear as explicit line-item positions (own `ticker` + `targetPercent`) in 7 of the 9 Opal models. This is the PRD §3.3 **clean-attribution** case: `held_inflection(PFDE)` = Σ over Inflection accounts of `model_value × targetPercent(PFDE)` — directly derivable, no look-through-to-underlying needed. DIVZ and IDVZ are not held by any Opal model (so for Inflection, only PFDE/PFOE attribution applies; DIVZ/IDVZ `held_inflection = 0`).

### 4.4 — Precision caveat for WS-A / WS-D.2

The `items[].targetPercent` is the **model target weight**, not the **actual** account position. Accounts drift within tolerance (`itemTolUpper/Lower` = ±10%). `model_value × targetPercent` yields the *target* ETF allocation. For an exact `held_inflection(etf)` the actual account-level positions (Orion `Portfolio/Accounts` holdings) would be required. For AUA-attribution and the §3.5 reconciliation, target-weight is a reasonable first approximation — flag for CTO/WS-A to rule whether target-weight attribution is acceptable or actual positions are required.

---

## 5. AC4 (PRD §7-Q3) — Inflection non-model advised assets: a finding

**Yes — Inflection has substantial non-(Opal-)model advised assets, and the source is the same Eclipse feed already pulled.**

The Eclipse `/v1/portfolio/portfolios` feed (silver `portfolios_full.parquet`, 842 rows / 2026-05-17) carries Inflection's **entire** advised book, not just Opal-model portfolios:

| Class | Portfolios | `total_value` | What it is |
|---|---:|---:|---|
| **Opal models** (ids 3,5,6,7,8,9,10,28,29) | 399 | **$93,603,064.81** | `model_aua(inflection)` — what INF_E_00 currently rolls up |
| **IWM models** (Inflection's own — ids 11-25, 27) | 257 | **$87,864,120.93** | Inflection Wealth Management's own model lineup (IWM Aggressive Taxable, IWM Moderate Index, …) — Inflection-advised, not Opal models |
| **Unassigned** (NULL `model_id`) | 186 | **$18,247,938.59** | Portfolios with no model assignment (incl. `source='Team'` containers) |
| **TOTAL** | 842 | **$199,715,124.33** | Inflection's full Eclipse-administered book |

By the PRD §3.1 definition — `non_model_aua(partner)` = "value of that partner's advised client assets NOT in Opal models" — the IWM + unassigned **~$106M is literally Inflection non-model AUA**, and it requires **no new feeder**: it is already in the silver `portfolios_full.parquet` WS-C will read. INF_E_00 simply filters it out today (`simple[model_id].isin(OPAL_ECLIPSE_MODEL_IDS)`).

**The open product question (surfaced, NOT scoped per AC4):** Does Inflection's IWM-model book count as Opal advised AUA? Opal advises Inflection on the Opal models; the IWM models are Inflection Wealth Management's own. Three framings for CTO + Andrew:
- **(a)** IWM book is Opal non-model AUA → MDPF counts it; `non_model_aua(inflection)` ≈ $106M from the Eclipse feed (a WS-C extension — trivial, the data is in hand).
- **(b)** IWM book is Inflection's own, not Opal-advised → excluded from Opal Aggregate AUA entirely; Inflection contributes model AUA only.
- **(c)** A subset (e.g. unassigned-but-Opal-custodied, or specific IWM models) counts → needs a custody/account-type cutout pass analogous to WS-E's 49F audit.

This mirrors WS-E's 49F custody-cutout question on the Inflection side. Recommend it be its own decision point (a WS-C extension or a new "WS-G Inflection non-model" workstream) — do not block the WS-C model-AUA build on it.

---

## 6. Concrete paths for the WS-C Phase-2 build TO

| WS-C build needs | Source (exists) | Action |
|---|---|---|
| Partner identity | n/a | Inject `firmId = "inflection"` constant. |
| Model assignment + account join | `silver/eclipse/{date}/portfolios_simple.parquet` (`model_id`, `eclipse_account_id_int`) | Read as-is. |
| Per-portfolio model value | `silver/eclipse/{date}/portfolios_full.parquet` (`total_value`) joined on `id` | Read as-is; recommend `total_value` as canonical `model_value`. |
| Account/household/firm rollup | `gold/eclipse/{date}/model_portfolio_*.parquet` (INF_E_00) | Reuse — INF_E_00 already produces the rollup; WS-C conforms it to the WS-A schema. |
| **`holdings[]` (the gap)** | **NOT in the shipped pipeline.** Ticker-level composition = Orion `GET /api/v1/Trading/Models/{id}.items[]` — proven 2026-05-14, snapshot `.runtmp/orion_model_probe/opal_models_with_items.json` | **WS-C build adds a bronze pull** of `Trading/Models/{id}` for the 9 Opal Orion-ids [83,84,85,86,87,88,89,152,153], silver-converts `items[]` to a `model_composition_securities` dim, and the gold layer expands `(account, model) → (account, ticker)` rows. The auth/JWT machinery already exists (`pull_eclipse_portfolios.py` JWT helpers + the Orion JWT in SM `orion/jwt/current`). |
| ETF ownership decomposition input (WS-D.2) | Derived from the above `holdings[]` | `held_inflection(PFDE/PFOE)` = Σ `model_value × targetPercent`. Clean per §4.3. |

**WS-C build effort estimate:** moderate. The model-AUA rollup itself is largely a conform-and-tag of existing INF_E_00 output (small). The genuine new work is the Orion `Trading/Models/{id}.items[]` bronze pull + silver dim + the `(account, ticker)` gold expansion — net-new but well-precedented (the 2026-05-14 probe already wrote a working end-to-end version in `.runtmp/`). No blocker.

---

## 7. Findings for COO / CTO

1. **WS-C is GO** — feasibility confirmed; the only convergent-schema gap is `holdings[]`, closeable with a proven endpoint.
2. **WS-C build scope = the ticker-level composition pull** (Orion `Trading/Models/{id}.items[]`), not the model-AUA rollup (which INF_E_00 mostly already does). Size the Phase-2 TO around the new bronze/silver/gold for `holdings[]`.
3. **§7-Q2 closed: line-item, clean attribution.** PFDE/PFOE held as line items; no look-through derivation needed. The PRD §3.3 `held_inflection` is directly computable. Recommend the PRD §7-Q2 status be marked resolved.
4. **§7-Q3 surfaced: Inflection non-model AUA ≈ $106M** (IWM $87.9M + unassigned $18.2M), already in the Eclipse feed. Needs a CTO + Andrew product call (framings (a)/(b)/(c) in §5) — recommend a separate decision point, not a WS-C blocker.
5. **WS-A inputs to ratify:** (i) canonical `model_id` space (Eclipse ids vs Orion ids vs model name); (ii) canonical `model_value` (recommend `total_value_eclipse`); (iii) target-weight vs actual-position ETF attribution (§4.4); (iv) `as_of_date` from partition date vs Orion `lastPositionDate`.
6. **Minor dependency to confirm with ADVI_ECLDAT:** Eclipse silver partitions are sparse (2026-05-15, -17 present — not strictly daily). WS-C / MDPF daily-grain depends on ADVI_ECLDAT's ingestion cadence; confirm the schedule.

---

## 8. References

- PRD: `docs/architecture/MDPF_ASSETS.md` v0.1 (§3.2, §3.3, §4 WS-C, §7-Q2/Q3).
- Prior empirical probe: `docs/briefs/data-scientist-eclipse-ingestion-feasibility-20260514.md` (§2.1 Eclipse↔Orion model map; §2.2 endpoint surface; §2.3 `.runtmp/` deliverables).
- Shipped pipeline: `data/orion/scripts/{bronze/pull_eclipse_portfolios,silver/convert_eclipse_portfolios_to_silver,gold/INF_E_00.eclipse_model_portfolios}.py`.
- Live artifacts inspected: `s3://opal-data-inf/silver/eclipse/2026-05-17/`, `s3://opal-data-inf/gold/eclipse/2026-05-17/`.
- Ticker-composition snapshot: `.runtmp/orion_model_probe/opal_models_with_items.json` (9 Opal models, `Trading/Models/{id}.items[]`).

---

**End of brief. — 0.4.0_DS_ClientPlatform~B, 2026-05-18**
