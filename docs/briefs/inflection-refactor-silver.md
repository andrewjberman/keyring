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
`positions_mv` (AUA backbone — the per-day Assets snapshot), `accounts_v2`, `household`, `household_rep_mapping`, `representatives`, `activity`, `billing`, `tax_unrealized`, `tax_realized`. These stay; tree renamed `api_dims/`→`orion-api/`.

### 5.2 ORION-API — CONSOLIDATE onto the partitioned shape
- `assets` / `assets_v2` — exists in 3 places (`api_dims/assets/`, `api_dims/assets_v2/`, flat `silver/assets_v2/`) → ONE partitioned dim.
- `performance` — 3 places (`api_dims/performance/`, flat `silver/performance/`, flat `silver/performance_dim/`) → ONE.
- `transactions` — flat-only (`silver/transactions/`), no partitioned home → give it `silver/orion-api/transactions/snapshot_date={date}/`.
- **Per-dim migration risk:** confirm which copy GOLD currently reads before retiring the others (repoint gold's read, then retire).

### 5.3 ORION-API — RETIRE
`silver/accounts_dim/` (legacy), `silver/orion-rest/` (stray), `silver/performance_dim/` (dup).

### 5.4 Census-complete (DS~A correction 2026-06-30)
The silver map above omitted two trees that must be CENSUSED (not silently dropped): `silver/prices/` (canonical_prices — the prices tree feeding gold; **KEEP**, classify under its own prices lineage, not an orion-dim) and `silver/historical_prices.parquet` (single-file; classify KEEP/retire per gold consumption). Drive the silver migration (S-R1..R5 / AC) off a FULL `s3://opal-data-inf/silver/` prefix census — same requirement as bronze §1 — so no tree survives unclassified.

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
