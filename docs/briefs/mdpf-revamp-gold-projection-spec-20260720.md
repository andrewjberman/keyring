# MDPF_REVAMP — Gold `dim_*` Projection Spec (implementation-ready)

**Author:** 1.0.0_SA_CTO · **Date:** 2026-07-20 · **Status:** SPEC — ready for DE/DS gold authoring once smartx silver is current.
**Builds on:** the audit brief (`docs/briefs/mdpf-revamp-audit-brief-20260716.md`, census + inversion + bucketing) and Andrew's 2026-07-20 rulings (recorded in `org/projects/MDPF_REVAMP.json`). Every number below is **grounded this session** against the live SmartX roster, the 0824 silver, and the `opal-assets-daily-aua` DDB (see §7).

> **PREREQUISITE:** this build's parity streak cannot run until **smartx silver is current** (the WS-A7 converter P0, landing now). The current MDPF page is unaffected (it serves off the legacy `wsb_49f_smartx_model_aua` feeder, not the monolith silver); the revamp *requires* monolith silver, which is why the silver fix is sequenced first.

---

## 1. What this builds

The inversion (audit brief §3): monolith silver `fact_*` → **new gold `dim_*` projections** (gold = the one parse-down point) → **(a)** `portal/{channel}/{client}/` consumption artifacts + **(b)** the `opal-assets-daily-aua` DDB rows, with the DDB as the **management/registry** layer. The projections reproduce the **exact served shapes** the Model Portfolios page consumes today (parity is byte/shape-level per firm), so the Portal reads what it reads today with **zero frontend change**.

**Scope = the two areas Andrew named:** the **Portfolio Analytics** main header + the **AUA/AUM** tab. That is the 7 served artifacts A1–A7 (portal census, §3 here). The Benchmark/Peers tabs (YANG family) are **phase-2** (Andrew-ruled).

**Bucketing (Andrew-ruled, channel-first):**
```
portal/
  model-portfolios/
    global/       aggregate_aua_timeseries.json
    49financial/  aggregate_aua_timeseries.json · account_distribution.json
    inflection/   aggregate_aua_timeseries.json · account_distribution.json
  portfolios/
    global/       non_model_assets.json
```
New-territory rule: **pure adds** — no existing key/policy/notification/scheduler touched; parity-streak N=3 vs the served mdpf artifacts; never-widen co-sign (CTO+COO) before any re-point.

---

## 2. THE MODEL CROSSWALK (the single load-bearing artifact — annotate the name divergence)

Grounded this session. **The SmartX display names are NOT what the served keys / DDB cohorts call them** — a join hazard that must be pinned in a constants table, never string-matched.

| Andrew | served `by_model{7}` key | acct-dist display `{5}` | **SmartX roster `model_name`** | DDB `cohort_id` |
|---|---|---|---|---|
| UST | `opal_ultra_short_term` | Ultra-Short Term | Opal Ultra Short-Term Income | `49f_ultra_short_term` |
| ST | `opal_short_term` | Short Term | Opal Short-Term | `49f_short_term` |
| INT | `opal_intermediate` | Intermediate Term | Opal Intermediate-Term | `49f_intermediate` |
| **LTC** | `opal_long_term_conservative` | Long Term | **Opal Conservative Growth** ⚠ | `49f_lt_conservative` |
| **LTA** | `opal_long_term_aggressive` | Ultra-Long Term | Opal Long-Term Aggressive | `49f_lt_aggressive` |
| SMA (→ non-model) | `opal_div_sma` | (excluded) | Opal Dividend Income | `49f_dividend_sma` |
| SMA (→ non-model) | `opal_growth_sma` | (excluded) | Pathfinder Focused Opportunities | `49f_growth_sma` |

⚠ **LTC = SmartX "Opal Conservative Growth"** (not "Long-Term Conservative"); the acct-dist display relabels LTC→"Long Term", LTA→"Ultra-Long Term". The gold projection maps `model_id`/`model_name` → the canonical key via this constants table (key off `model_id` where possible; `model_name` is the fallback and the annotated divergence).

**7→5 reconcile (grounded):** Andrew's five = the 5 laddered models above; the 2 SMAs (`div`,`growth`) **fold into non-model** for the 49F view (the page already does this FE-side via `cohort_class==='sma'`). Global shows the 5 laddered models.

---

## 3. THE 49F BASIS MECHANISM (Andrew-direct; grounded)

**Basis = SCHWAB-RPS (the 0824 platform-model figure), NEVER blended-preferred, NEVER 0824+0833, NEVER substitute. Artifact carries `basis: schwab-rps`.**

Grounded numbers (2026-07-18 DDB / live roster, 49F open):

| Quantity | Value | Source | Role |
|---|---|---|---|
| 5-core model AUA (Σ UST+ST+INT+LTC+LTA) | **$1,397.2M** | `fact_model_allocation_roster` Σ value by model (advisor=49 Financial Group, status=open) = DDB 5 `model_value` cohorts = `49f_smartx_platform` | **the served model basis (SCHWAB-RPS)** |
| 2 SMAs (`div`+`growth`) | ~$23.3M | roster (Opal Dividend Income + Pathfinder) = DDB `49f_dividend_sma`+`49f_growth_sma` | fold into **non-model** |
| Schwab custody total | $1,644.99M | DDB `49f_schwab_custody` (`partner_custody_total`, coverage=incomplete) | the blended-preferred-adjacent full figure — **DO NOT serve as the model basis** |

**Mechanism:** decompose the SCHWAB-RPS figure into the 5 models via the roster; `non_model_aua = (RPS full) − Σ(5 core)` (on the RPS basis, the residual is the 2 SMAs + true non-model). Global = 49F + Inflection aggregated (existing cross-partner aggregate, NOT a basis sum). **`account_count` per model** = distinct `allocation_id` per model from the roster.

**Classifier (audit-brief grounding-a, resolved):** the account→model classification lives in `fact_model_allocation_roster` (SmartX: `allocation_id → model_id/model_name → value`). The Schwab-account join edge (for tying RPS custody to accounts) is `fact_allocation_account_map` (`account_number` byte-faithful) — a GOLD join, not a silver fix.

---

## 4. PER-ARTIFACT PROJECTION SPECS (A1–A7)

Each `dim_*` projection reads monolith silver + writes the served-shape artifact. **Parity target: the exact served shape** (audit brief §1 field inventories) — verified by `comp-transform schema-check` on the consuming component + a pinned shape diff.

| Served artifact | Gold projection reads | Transform | Basis label |
|---|---|---|---|
| **A5/A6** `aggregate-aua-timeseries` (the spine: `dates[427]`, `model_aua[]`, `opal_aggregate_aua[]`, `non_model_aua[]`, `by_model{7}{display_name,cohort_class,model_value[],account_count[]}`, `as_of_last`) | `fact_model_aum_daily` (per-day equity series, ~400-1200 rows/model — **the 427-date history source, NOT the DDB**) + `fact_model_allocation_roster` (per-model value+count) + inflection eclipse/orion silver (for the inflection firm) | build the columnar time series per model; `by_model` keyed via the §2 crosswalk with `cohort_class ∈ {model,sma}`; `non_model_aua` per §3 | `schwab-rps` (49F); inflection own basis |
| **A1** `aum-metrics` (`by_model[]{model_name,aum,account_count}`, `total`, quarter-end deltas `q0-3`) | A5/A6 series (last value + quarter-end lookups) | point-reads at `dates.qN`; QoQ deltas | inherits A5/A6 |
| **A2** `aum-timeseries` (global value trend fallback) | `fact_model_aum_daily` | columnar `aggregate[]` + `by_model{}` | schwab-rps |
| **A3/A7** `account-distribution` (per-model `{percentiles,median,histogram,account_count}`) | `fact_allocation_valuation` (per-allocation envelope: equity/cash/etc.) + `fact_model_allocation_roster` (allocation→model) | group allocation AUM by model → distribution stats (p10/p25/p50/p75/p90, histogram bins, mean/median/std) | schwab-rps |
| **A4** `non_model_assets` (`{enterprise_total,model_aum,non_model_aum,non_model_pct}` + series) | `49f_schwab_custody` (DDB) + A5 `model_aua` | `non_model = custody − model_aum`; port the v0_9 methodology (cutover/backfill provenance verbatim) | labeled |
| **vintage** (`source_vintage_last`) | DDB `vintage_state`+`coverage_state` per cohort | serve vintage FROM the registry (inversion) | — |

**FE transforms that MUST have their inputs present** (from the census — a value computed FE-side still needs its source): `rollBlendsIntoArchetype*` (inflection blend value+count), `totalHoldingsSleeveLevel` (blend `by_model.account_count`), `globalDeepTailNonModelByPeriod` (A5 `opal_aggregate_aua`+`model_aua`), `spineIsStale` (A5/A6 `as_of_last` vs A3/A7 `generated_at`). The projections must emit these fields so the FE math is unchanged.

---

## 5. THE DDB REGISTRY (reuse the existing structure)

`opal-assets-daily-aua` (hash=`run_date`, range=`cohort_id`, GSI `cohort_history`) already carries the 49F cohorts with the right contract: `value_class` (model_value / partner_custody_total / platform_model_aua / etf_* / partner_model_total), `basis`, `vintage_state`, `coverage_state`, NEVER-SUM-ACROSS-`value_class`. **The gold projections WRITE these rows** (the inversion: gold → DDB, not DDB reads-the-serve). The never-substitute law is enforceable here: `49f_schwab_custody` (custody) and the 5 `model_value` cohorts carry distinct `value_class`/`basis` — a consumer that served custody as the model basis would violate the contract. The 14 cohort-freshness watches then watch the thing that actually feeds the page. **No new alarms** (Andrew-direct) — the registry's `vintage_state`/`coverage_state` are structural fields, not alarms.

**Registry is NOT the timeseries store:** it holds a rolling ~21-run_date window + current cohort values + vintage. The 427-date page history comes from `fact_model_aum_daily` via the gold projection (§4 A5/A6).

---

## 6. Cutover discipline (the S5 bar, per firm)

1. Build **alongside** (new-territory: pure adds under `portal/model-portfolios/`).
2. **Parity streak N=3**: N consecutive scheduled cycles where the projection ties the served mdpf artifact within tolerance; every named delta explained by a ruled correction; an unexplained delta resets the streak. **Cannot start until smartx silver is current.**
3. **Never-widen co-sign** (CTO + COO, both on independently-read evidence) → re-point the CF router/page → original path runs shadow one cycle → retires.
4. Door 6 semantics untouched in wave 1; the mdpf trigger keeps firing until re-point.

---

## 7. Grounding appendix (this session, live state)

- **Roster 49F open decomposition** (`fact_model_allocation_roster`, advisor=49 Financial Group, status=open): LTC/Opal Conservative Growth $753.4M · INT $293.1M · LTA $203.5M · ST $106.4M · UST $44.9M → **5-core $1,401.3M**; SMAs (Opal Dividend Income $18.6M + Pathfinder $4.66M) **$23.3M**; total $1,424.5M.
- **DDB 2026-07-18** 49F `model_value` cohorts sum $1,397.2M = `49f_smartx_platform` (`platform_model_aua`); `49f_schwab_custody` $1,644.99M (`partner_custody_total`, coverage=incomplete). ETF cohorts (`etf_{divz,idvz,pfde,pfoe}` + `__held_{49financial,cottonwood,inflection}`) + `inflection_models` $137.17M present.
- **0824 silver tables present:** `fact_rps`,`fact_rps_s2`,`fact_acc`,`fact_rl{d,u,w,y}`,`fact_r t{u,y}`,`fact_u{ln,lt,pn,pt}`,`fact_trn`,`fact_sec` + `dim_*`.
- **smartx silver tables** (via the WS-A7 converter): `fact_model_allocation_roster`, `fact_model_aum_daily`, `fact_allocation_account_map`, `fact_allocation_{positions,valuation}`, `fact_model_{holdings,performance,changerequests}`, `fact_account_{detail,allocations}`, `fact_nonzerosleeve`.

## 8. Lane assignment (for the coordinator)

- **Gold `dim_*` authoring** — DE/DS lane (`data/*/scripts/gold/`), CTO code-review + first-artifact signoff.
- **`portal/` bucketing + DDB write wiring** — DT/AE lane.
- **Verification** — CVO on the never-sum/never-substitute law + parity streak (grounds on the SERVED artifact, not the producer self-report).
- **Gate:** dispatch rides the smartx-silver-current signal (the WS-A7 P0).
