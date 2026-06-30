# Refactor SPEC-2: Inflection — SILVER layer

**Author:** 3.0.0_SA_CVO (Andrew-direct refactor planning, ADVI_BREAKS unified-flow) | **Date:** 2026-06-30
**As-is reference:** `inflection-silver.md` (audit). **Upstream:** `inflection-refactor-bronze.md` (SPEC-1). **Next:** SPEC-3 gold.
**Status:** DRAFT for end-to-end validation → CTO PRD. Decisions marked [ANDREW-LOCKED] / [DECISION].

---

## 0. Governing principles (Andrew-locked, this layer)

1. **Silver is the parquet-normalization + fact→dim layer.** Because bronze is now raw-native (CSV + JSON, no conversion), **silver is the single place every dim becomes typed parquet.**
2. **FULL FIDELITY — no field is dropped or compressed bronze→silver.** Every field in the bronze raw record survives to silver. Permitted transforms: dtype coercion, camelCase→snake_case name standardization, dedupe (rows), mechanical provenance columns. The existing `convert_eclipse_portfolios_to_silver.py` is the template — `pd.DataFrame(raw)` (full record) → rename-all → coerce → dedup, **zero column selection** (Rule 17, header-documented). [Andrew-locked 2026-06-30: "keep full fidelity here."]
3. **Minimal disruption — stay true to what silver does today; do NOT impose a new fact-vs-dim doctrine.** [Andrew-locked 2026-06-30] Silver already provides the data we need; the refactor consolidates duplicates/layout, it does not re-model. fact→dim reshape is *allowed* but NOT mandated — keeping existing fact tables alongside dims is fine. Hard rule stays: full fidelity (never drop a field) + dtype/dedup only; field slimming/null-judgment stays gold. Rationale: an eventual pure-fidelity (no-Orion) rebuild supersedes this, so don't over-engineer the interim. **The governing constraint for every consolidation choice (layout, naming, which copy to keep) = whatever GOLD is already accustomed to reading** (Principle 5a).
4. **Two-domain separation holds:** `silver/orion-api/` + `silver/eclipse-api/` (eclipse stubbed). **No cross-source / cross-domain join before gold** (inherits bronze Principle 6 / AC8).
5. **Single EC2, one converter dispatch, one layout** (inherits bronze Principles 3–4).

## 1. Silver's new front-edge: raw → parquet for ALL dims

- CSV dims (Envision/ExcelReports + Custom Reports: household, performance, activity, tax, billing, transactions) → parse CSV → parquet.
- JSON dims (Portfolio/Accounts, Portfolio/Assets, Trading/Models, reps, + ALL eclipse) → parse JSON → parquet.
- **positions + assets JSON→parquet MOVES here** (resolves bronze R2): bronze now lands raw JSON `bronze/orion-api/{date}/{positions,assets}.json`; the silver converter parses → `silver/orion-api/positions_mv/...` parquet. The `positions_mv` converter repoints to read the raw bronze JSON (not a pre-made bronze parquet).

## 2. One converter dispatch + one layout

- Consolidate to ONE `DIM_BUILDERS`-style dispatch (the `convert_orion_api_to_silver.py` model, extended to own every orion dim).
- **One layout:** `silver/orion-api/{dim}/snapshot_date={date}/data.parquet` for ALL dims (rename the tree `silver/api_dims/` → `silver/orion-api/`).
- **Retire (the audit's converter sprawl + the live-found duplicates):**
  - duplicate converters: `convert_transactions_to_silver.py` / `convert_performance_to_silver.py` (standalone) vs the unified `--dim transactions`/`--dim performance` builders — fold into the one dispatch.
  - legacy: `convert_orion_to_silver.py`.
  - flat-layout outputs: `silver/assets_v2/`, `silver/performance/`, `silver/performance_dim/`, `silver/transactions/` (normalize to the partitioned layout).
  - stray/legacy trees: `silver/accounts_dim/` (deprecated SlickGrid-derived, superseded by accounts_v2), `silver/orion-rest/`.

## 3. The silver transform contract (DECISIONS RESOLVED — Andrew 2026-06-30)

**PERMITTED:** dedup (rows), dtype coercion, `camelCase→snake_case` name standardization, mechanical provenance (`snapshot_date`, `source_system`), fact→dim reshape (allowed, not required).
**FORBIDDEN (→ gold):** dropping/slimming any field, business `fillna`/`dropna`, null-meaning judgment, field-relevance decisions, cross-source/cross-domain joins.
**Full-fidelity invariant:** silver field-set ⊇ bronze raw field-set, per dim (no field-count reduction).

RESOLVED:
- **Name casing — KEEP `snake_case`** (Andrew-locked). Lossless 1:1; consistent; and gold is already accustomed to it.
- **fact-vs-dim — NOT hardline** (Andrew-locked): keep existing fact tables alongside dims if that's what's there; don't re-model. Minimal disruption — silver already provides the needed data; an eventual pure-fidelity no-Orion rebuild supersedes the interim.
- **GOLD-ACCUSTOMED governs:** every consolidation choice (which copy to keep, the layout, the names) is made to match what gold already reads — confirmed per dim (S-R5) before any retire. The refactor must not change what reaches gold.

## 4. Two-domain trees

- `silver/orion-api/{dim}/snapshot_date={date}/data.parquet` — full, active.
- `silver/eclipse-api/{dim}/snapshot_date={date}/data.parquet` — **STUBBED**: the 4 dims already exist (produced by `convert_eclipse_portfolios_to_silver.py` at `silver/eclipse/`); relocate the prefix → `silver/eclipse-api/`. No gold build required yet (downstream use decided later). Full-fidelity, as today.
- No cross-domain join in either tree — that lives only at gold.

## 5. Per-dim modeling map

### 5.1 ORION-API — KEEP (already correct shape: partitioned, active)
`positions_mv` (AUA backbone — the per-day Assets snapshot), `accounts_v2`, `household_rep_mapping`, `representatives`, `activity`, `billing`, `tax_unrealized`, `tax_realized`. These stay; tree renamed `api_dims/`→`orion-api/`. (**`household` MOVED OUT of KEEP** → §5.3 LAYER-2 repoint-to-accounts_v2: 1204h stale (frozen 05-11), read by 4 gold consumers; builder BROKEN (geo_verify hard-dep, geo-pull disabled) so wire-option dead — DS~A grounded 2026-06-30.)

### 5.2 ORION-API — CONSOLIDATE onto the partitioned shape
- `assets` / `assets_v2` — exists in 3 places (`api_dims/assets/`, `api_dims/assets_v2/`, flat `silver/assets_v2/`) → ONE partitioned dim.
- `performance` — 3 places (`api_dims/performance/`, flat `silver/performance/`, flat `silver/performance_dim/`) → ONE.
- `transactions` — flat-only (`silver/transactions/`), no partitioned home → give it `silver/orion-api/transactions/snapshot_date={date}/`.
- **ATOMIC per-consumer repoint — NEVER bulk-retire the flats (CTO-routed, DS~A `d7ca2f6bb`):** GOLD READS the flats today (`silver/performance/`←INF_C_02; `silver/assets_v2/`←INF_D_03; `silver/transactions/`←the whole A-stage). A naive flat-retire re-triggers the INFGRO.009 phantom-path incident. Per dim: (1) parity-confirm copy-equivalence; (2) relocate the canonical → `silver/orion-api/{dim}/snapshot_date={date}/`; (3) repoint EACH gold consumer ATOMICALLY + parity-verify the gold output is byte-unchanged; (4) THEN retire the non-canonical. CVO independently verifies each per-consumer repoint's parity as LEG-1 builds.

### 5.3 ORION-API — RETIRE vs REPOINT (DS~A dead-confirm `d7ca2f6bb`; **deprecated-by-default sharpening — Andrew-direct 2026-06-30**)
- **PRINCIPLE (Andrew-direct, "if something is 1490h stale, it is deprecated"):** a 1490h-class-stale artifact is **deprecated-by-default**. The burden flips — "keep" must be EARNED by a *proven* served-critical fresh read; absent that, **retire** (after the consumer census is proven complete + all-repointed, so no latent real reader breaks). Grounded against `pipescript advi-inf`: an artifact with **no live producer** + 1490h-stale = dead, not "frozen-but-maintained."
- **RETIRE (DEAD-confirmed):** `silver/performance_dim/` (dup, dead), `silver/orion-rest/` (stray, dead).
- **DEPRECATED → REPOINT consumers, THEN RETIRE the stale source (supersedes the prior "repoint+flag, keep" call):** `silver/accounts_dim/` (1490h stale, frozen 04-29) has **NO live producer** (replaced by `inf-accounts-v2-daily`, grounded `pipescript advi-inf`). Its real consumers (INF_C_09 / INF_D_00 — INF_09 was a **phantom** per DS~A's census correction) are repointed to `accounts_v2` (LEG-1, deployed). Once that repoint is **proven complete + all-repointed**, **RETIRE** the deprecated `accounts_dim/` source — do NOT flag-and-carry cruft forward. DS~A grounded retire-eligible (zero live silver readers post-LEG-1).
  - **DECLARATIVE distinction (DS~A — do NOT conflate):** retire `silver/accounts_dim/` ONLY. `gold/dimensions/accounts_dimension_latest.parquet` (`ACCOUNTS_DIM_KEY`, read by INF_A_04/C_00/C_02/C_03/C_05) is a **DIFFERENT, LIVE** artifact (INF_A_00 gold output) — leave it untouched. Name-collision trap.
- **DEPRECATED-BUT-READ → REPOINT-to-accounts_v2 (LAYER-2; root-cause GROUNDED, fork RESOLVED — DS~A 2026-06-30):** `silver/api_dims/household` (1204h stale, frozen 05-11) is LIVE-read by **4 gold consumers** (INF_D_00d L68, INF_D_04 L88/L481, INF_D_04b L61, INF_D_05 L10) → they read ~50-day-stale household NOW (pre-existing defect, NOT a cutover strand). **ROOT CAUSE (source-confirmed):** `build_household` (`convert_orion_api_to_silver.py:140`) does an UNCONDITIONAL `read_bronze_csv('geo_verify')` that RAISES on missing (`_orion_api_silver_lib.py:372`); the geo-pull is SKIP/disabled since ~05-11 → `build_household` errors every `inf-silver-chain` run → frozen. (`build_activity`, no geo_verify dep, stays 7.9h fresh — the differentiator.) **The "wire the builder" option is DEAD** (builder is BROKEN, not merely unwired). **Disposition: REPOINT the 4 consumers to `accounts_v2`** (carries household_id + state/city/zip directly, no geo_verify dep — fixes staleness + removes the broken dep). LAYER-2 caveat: confirm `accounts_v2` covers the consumers' `household_name` + `account_aua` needs (has account_name/last_name + current_value; may need a small derive). NOT a tonight blocker.
- **DEPRECATED-CANDIDATE (criticality pending):** `silver/meta/gap_manifest.json` (1490h, frozen 04-29) — read by INF_C_01 + INF_D_00c; confirm tolerate-stale-meta vs hard read before retire (tied to yahoo removal §5.5). Old `api_dims/assets` (1326h) handled by §5.4 CONSOLIDATE (superseded by `assets_v2`).
- **LAYER-2 STALE SWEEP (DS~A 2026-06-30 — non-blocking tonight, NOT cron-fed):** `activity` (3 consumers; builder exists unwired → wire-vs-retire fork like household); `aum_snapshot` + `orion_fees` (DEAD legacy `convert_orion_to_silver.py`, stopped 04-29 = the `accounts_dim` producer → deprecated, assess consumers + repoint-retire). LAYER-2 consolidation, not tonight's cron teardown.

### 5.4 Complete prefix census — AC authority (DS~A live census 2026-06-30)

Every `s3://opal-data-inf/silver/` prefix classified — no tree survives unclassified:

| silver prefix | disposition |
|---|---|
| `api_dims/` | **RENAME** → `silver/orion-api/` (the main tree) |
| `api_dims/{positions_mv, accounts_v2, household_rep_mapping, representatives, activity, billing, tax_realized, tax_unrealized}` | **KEEP** (canonical dims, correct shape) |
| `silver/api_dims/household` | **REPOINT→accounts_v2 (LAYER-2)** — 1204h stale, 4 readers; builder BROKEN (geo_verify hard-dep at L140, geo-pull disabled since 05-11), wire-option dead; repoint to accounts_v2 (no geo dep). Not tonight |
| `api_dims/assets` + `api_dims/assets_v2` + flat `silver/assets_v2/` | **CONSOLIDATE** → ONE partitioned `assets` |
| `api_dims/performance` + flat `silver/performance/` + `silver/performance_dim/` | **CONSOLIDATE** → ONE partitioned `performance` (retire `performance_dim`) |
| flat `silver/transactions/` | **CONSOLIDATE** → `silver/orion-api/transactions/` partitioned |
| `silver/accounts_dim/` | **REPOINT consumers → RETIRE (deprecated)** — 1490h stale, NO live producer; real consumers C_09/D_00 (INF_09 phantom) repointed to accounts_v2 (LEG-1); retire the stale source once repoint proven complete (Andrew deprecated-by-default 2026-06-30) |
| `silver/orion-rest/` | **RETIRE** (stray, DEAD-confirmed) |
| `silver/performance_dim/` | **RETIRE** (dup, DEAD-confirmed) |
| `silver/eclipse/` | **RELOCATE** → `silver/eclipse-api/` (stubbed) |
| `silver/prices/` (canonical_prices) | **RETIRE** (post-repoint — see §5.5 yahoo removal) — the yahoo+interp price history is redundant with the Orion daily snapshot |
| `silver/historical_prices.parquet` (29MB) | **RETIRE** — the T2 yahoo_finance input; removed with the yahoo thread (§5.5) |
| `silver/_silver_complete/`, `silver/meta/`, `api_dims/_chain_summary/` | **NON-DIM, KEEP** (sentinels/meta) |

### 5.5 Yahoo-finance price-thread REMOVAL (Andrew-locked 2026-06-30)
**Confirmed condition (CVO-grounded):** the Orion daily Assets snapshot gives FULL historical pricing via roll-forward — `positions_mv` = 2,227 daily partitions 2020-05-26→2026-06-30, 100% of active holdings Orion-priced every day. So the yahoo thread is redundant: `canonical_prices` (1.3M rows) is 57% yahoo_finance + 42% linear_interpolation + 0.4% transaction_observed — a parallel reconstruction of prices the snapshot already carries directly.
- **REMOVE (silver side):** `backfill_yahoo_prices.py` (T2 producer), `silver/historical_prices.parquet` (T2 input), `silver/prices/canonical_prices.parquet` (output).
- **Repoint (gold side, SPEC-3):** the 4 consumers (`INF_B_00/B_01/B_01b/D_07`) source prices from `positions_mv` (Orion snapshot) instead of `canonical_prices`; retire the yahoo/interp legs of `INF_build_canonical_prices.py`.
- **Gating edge (verify per-consumer before delete):** any consumer needing a price for an asset on a date it was NOT held (outside `positions_mv`). For valuing HELD positions (AUA/holdings/concentration) the snapshot covers it.
- **Posture (Andrew):** remove now; **reopen a third-party price source only if a real gap surfaces** (a needed price not available directly/indirectly from Orion historical).

### 5.4 ECLIPSE-API — 4 dims (relocate + stub, full-fidelity, exist today)
| silver dim | from raw bronze | grain / key fields | ~rows |
|---|---|---|---|
| `eclipse_portfolios` | `portfolios_simple.json` | per managed portfolio — account→model assignment (`id, account_id, account_number, model_id, sleeve_portfolio, is_deleted`) | ~835 |
| `eclipse_portfolio_values` | `portfolios_full.json` | per portfolio — rebalance/value (`total_value, managed_value, excluded_value, cash, num_of_associated_accounts, last_rebalanced_on`) | ~842 |
| `eclipse_models` | `models.json` | per model — catalog (all bronze columns) | ~18 |
| `eclipse_model_composition` | `model_composition_{id}.json` ×9 (unioned) | per model-per-holding — target weights (`product_id, ticker, target_percent, item_tol_upper/lower`); nested `model_detail` kept as JSON string | comp rows |
Kept as 4 separate 1:1 silver dims (raw-faithful, dedup+dtype only). `eclipse_portfolios` ↔ `eclipse_portfolio_values` joined only at gold (on portfolio id) — never in silver.

## 6. Retroactive / migration work

- **S-R1 — repoint to raw bronze:** every converter reads `bronze/orion-api/{date}/` raw (CSV/JSON); positions/assets read the new raw JSON (the JSON→parquet now happens here).
- **S-R2 — consolidate dispatch:** fold the standalone + duplicate + legacy converters into one dispatch; retire them.
- **S-R3 — normalize layout:** flat → `silver/orion-api/{dim}/snapshot_date={date}/`; rename `api_dims/`→`orion-api/`.
- **S-R4 — relocate eclipse:** `silver/eclipse/` → `silver/eclipse-api/` (stubbed).
- **S-R5 — gold-read reconciliation:** per dim, confirm which silver copy gold reads; repoint gold → the canonical partitioned dim; THEN retire the duplicates (the one real migration risk).
- **Parity gate:** silver output byte-parity through the refactor (the repoint + consolidation introduce zero value change) — validated several days pre-cutover (mirrors bronze AC7).

## 7. Acceptance criteria (machine-checkable → PRD/TO)

- AC1: exactly one converter dispatch path per dim (no standalone/legacy duplicates remain).
- AC2: one partitioned layout `silver/orion-api/{dim}/snapshot_date={date}/data.parquet`; zero flat `silver/{dim}/{date}.parquet` outputs.
- AC3: every dim is parquet at silver (CSV+JSON bronze → parquet here); positions/assets parquet appears at silver, never bronze.
- AC4: **FULL FIDELITY** — silver field-set ⊇ bronze raw field-set per dim (no field-count reduction); only dtype/name/dedup transforms (assert per dim).
- AC5: `silver/orion-api/` and `silver/eclipse-api/` are distinct trees; NO cross-domain join exists before gold.
- AC6: eclipse-api silver = the 4 dims, relocated, stubbed, full-fidelity (field-count == bronze raw).
- AC7: silver output parity-equal through the refactor (no value change).
- AC8: legacy/stray trees removed (`accounts_dim`, `orion-rest`, `performance_dim`, flat copies).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| live S3 (silver/api_dims, silver/ top-level dim inventory) | found the 3-copy dims + legacy trees | PASS (rail-checked) |
| read convert_eclipse_portfolios_to_silver.py + convert_orion_api_to_silver DIM_BUILDERS | full-fidelity confirm (no slimming) + converter-divergence map | PASS |
| inflection-silver.md (audit) | as-is variance baseline | PASS |

— 3.0.0_SA_CVO
