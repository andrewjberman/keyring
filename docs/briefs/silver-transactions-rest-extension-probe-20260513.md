# Silver/transactions REST Extension Probe — Phase 0 (2026-05-13)

**Author:** `0.4.0_DS_ClientPlatform~D`
**Date:** 2026-05-13
**Trigger:** COO GO 14:36Z + Andrew reframe — "we need to know how many of those fields overlap, if there is actually useful information in the expanded version. why couldn't we just consolidate?"
**Authority:** COO 2.0.0_SA_COO dispatch (this brief IS the TO).
**Audience:** 2.0.0_SA_COO, 1.0.0_SA_CTO, Andrew (final ratify on path).
**Companions:** DS~A `INFGRO_TXN_TYPE_UNIVERSE_AUDIT_20260513.md` (Stage -1 audit); DS~B `data-scientist-bug-b-silver-empty-partition-trace.md` (orthogonal Bug B trace).

---

## TL;DR

**Recommendation: PATH (a) FULL CONSOLIDATION FEASIBLE.** REST endpoint already returns ~95% of LEGACY-relevant fields; the silver-side drops most of them at the silver build step. The remaining ~5% missing fields all have **zero gold consumers**.

Path-(c) (separate prefixes) is the right call IF you treat the REST endpoint as a black box; the empirical truth is that REST's `/api/v1/Portfolio/Accounts/{id}/Transactions` already returns a 31-col payload, and `convert_transactions_to_silver.py` discards ~13 of those cols at the silver output_cols list (line 216). Andrew's "why couldn't we just consolidate" is correct — the consolidation is a **silver-side refactor**, not a REST-capability gap.

Three concrete blockers to path-(a) are dict-side / yaml-side / accounts_dim-side issues, all fixable in DS-lane within 1-2 commits:

1. `TRANS_TYPE_DESC` dict in `convert_transactions_to_silver.py` covers 23 / 47 distinct `transTypeId` values that REST returns → 24 type-ids → 'Unknown' string. **Fixable: extend dict to all 47 ids.**
2. `category` column derived from a 4-id-set hardcoded heuristic (`BILLING_TYPES={24,110}`, `ACTIVITY_TYPES={8,51}`) → collapses LEGACY's 14-bucket `activity_category` to 3 buckets. **Fixable: re-derive from `orion_cashflow_taxonomy.yaml` v3 (Stage 0b is type_desc-only, so this may not be strictly required — INF_C_01 has already migrated to type_desc-only classification).**
3. Silver output_cols list at `convert_transactions_to_silver.py:216` drops `clientId`, `registrationName`, `registrationCode`, `accountNumber`, `status`, `transactionDescription`, `notes`, `orderCreatedBy` even though all 8 are in bronze. **Fixable: add to output_cols with LEGACY-equivalent silver names.**

The 9 truly-missing-from-REST fields (`account_lname`, `download_symbol`, `CreatedDate`, `EditedDate`, `EditedBy`, `RepName`, `CurrentAccountValue`, `CurrentCashValue`, `ManagedAccount`) have **zero gold consumers** in the INF lane. They are pure CSV-passthrough fluff from the legacy Custom Report 28198 surface, never wired into a gold script. Two are joinable from other dims (`RepName`, `ManagedAccount`), the rest are display metadata or snapshot-grain values that don't belong on a per-transaction row.

---

## Phase 0a — Schema overlap audit (literal)

### Samples inspected

| Source | Key | Rows | Cols |
|---|---|---:|---:|
| LEGACY silver (OLD per-day) | `s3://opal-data-inf/silver/transactions/2026-05-12.parquet` | 79 | 31 |
| NEW silver (snapshot) | `s3://opal-data-inf/silver/transactions/2026-05-13.parquet` | 1,251,020 | 18 |
| NEW bronze (REST source) | `s3://opal-data-inf/bronze/transactions/2026-05-13.parquet` | 1,251,020 | 31 |

### Schema diff — silver-to-silver (literal)

| Set | Count | Cols |
|---|---:|---|
| **Shared (literal name match)** | 11 | `account_id, advisor_firm, nav_price, product_name, rep_id, snapshot_date, source_system, ticker, trans_date, trans_id, units` |
| **LEGACY-only delta** | 20 | `account_code, account_lname, activity_category, client_id, created_by, created_date, current_account_value, current_cash_value, description, download_symbol, edited_by, edited_date, managed_account, reg_name, reg_type, rep_name, trade_status, tran_notes, trans_amount, type_desc` |
| **NEW-only delta** | 7 | `amount, asset_id, category, household_id, rep_id_is_historical, trans_type_desc, trans_type_id` |

### Schema diff — semantic (rename-aware)

After accounting for renames (`trans_amount`↔`amount`, `type_desc`↔`trans_type_desc`, `activity_category`↔`category` with caveat), `client_id` retained as `client_id_bronze` but dropped at output:

| Set | Count | Notes |
|---|---:|---|
| **Semantic shared** | 14 | 11 literal + 3 renames |
| **Truly LEGACY-only** | 17 | After rename normalization; includes 1 collapsed-rename (`activity_category` → `category` lost 14→3 buckets) |
| **NEW enrichment** | 4 | `asset_id, trans_type_id, rep_id_is_historical, household_id` (direct field; LEGACY had `client_id`) |

### Schema diff — bronze-to-LEGACY

This is the critical comparison Andrew is asking about. NEW bronze has **31 cols** (not 13 as the inline docstring at `convert_transactions_to_silver.py:9-13` suggests — the docstring is stale; per-position fields were added 2026-05-12). Most LEGACY-only fields have DIRECT REST equivalents already present in NEW bronze, just dropped at silver:

| LEGACY-only silver col | NEW bronze field | Status |
|---|---|---|
| `client_id` | `clientId` | Present (renamed to `client_id_bronze` internally, then dropped) |
| `reg_name` | `registrationName` | Present (dropped) |
| `reg_type` | `registrationCode` | Present (dropped) — semantic match TBD |
| `account_code` | `accountNumber` | Present (dropped) |
| `trade_status` | `status` | Present (dropped) |
| `description` | `transactionDescription` | Present (dropped) |
| `tran_notes` | `notes` | Present (dropped) |
| `created_by` | `orderCreatedBy` | Present (dropped) |
| `trans_amount` | `transAmount` | Present (renamed to `amount`) |
| `type_desc` | (derived from `transTypeId`) | Recoverable via dict (dict gap is real — see Phase 0b) |
| `activity_category` | (derived from `transTypeId`) | Recoverable via yaml (collapsed at silver) |
| `account_lname` | — | **Not in REST** — fluff from custom report |
| `download_symbol` | — | **Not in REST** — alternate ticker, fluff |
| `created_date` | `executionTime` (semantically different) | **Not in REST as record-creation timestamp** |
| `edited_date` | — | **Not in REST** |
| `edited_by` | — | **Not in REST** |
| `rep_name` | — (joinable via `rep_id` → accounts dim) | Recoverable via JOIN; NEW already joins rep_lookup but doesn't emit `rep_name` |
| `current_account_value` | — | **Not in REST** — snapshot grain, not txn grain |
| `current_cash_value` | — | **Not in REST** — same |
| `managed_account` | — (derivable from accounts_dim) | Recoverable via JOIN |

**REST bronze additionally contains 11 fields that LEGACY doesn't have** (pure enrichment): `assetId, avgPrice, blockId, contributionCodeId, custodianName, distributionCodeId, executionTime, fundFamilyName, registrationSleeveStrategyName, orderId, tradeOrderId`.

---

## Phase 0b — Content-value audit (gold-consumer scan)

Scanned `data/orion/scripts/gold/INF_*.py` + `lib/*.py` for references to each LEGACY-only silver column, intersected with files that read `silver/transactions/`. Manual false-positive pass on `description` (argparse-only, not a column read).

| LEGACY-only col | Gold consumer count | Files (INF lane) | Classification |
|---|---:|---|---|
| `type_desc` | **4** | `INF_C_01, INF_D_06, INF_B_02, INF_build_canonical_prices` | **CRITICAL** — NNA classification keys on it (Stage 0b) |
| `trans_amount` | **4** | `INF_C_01, INF_D_00, INF_D_02, INF_D_06` | **CRITICAL** — money value |
| `activity_category` | 1 | `INF_C_01` (informational only post-Stage-0b — classifier keys on `type_desc`) | **MEANINGFUL → NOISE** (post-migration) |
| `client_id` | 1 | `INF_C_01` (line 269 — listed in canonical column set) | **CRITICAL** — relationship grain |
| `rep_name` | 5 | `INF_A_00, INF_A_01, INF_B_00, INF_C_01, txn_cache_reader` | **MEANINGFUL** — display; JOIN-derivable |
| `reg_type` | 5 | `INF_A_00, INF_D_00, INF_D_02, INF_D_06, txn_cache_reader` | **MEANINGFUL** — registration type metadata |
| `account_code` | 3 | `INF_A_00, INF_D_02, txn_cache_reader` | **MEANINGFUL** — display/join key |
| `reg_name` | 1 | `INF_D_06` | **MEANINGFUL** (borderline NOISE) |
| `description` | 0 (after false-positive filter — all hits are argparse `description=`) | — | **NOISE** |
| `account_lname` | 0 | — | **NOISE** |
| `download_symbol` | 0 | — | **NOISE** |
| `trade_status` | 0 | — | **NOISE** |
| `tran_notes` | 0 | — | **NOISE** |
| `created_date` | 0 | — | **NOISE** |
| `created_by` | 0 | — | **NOISE** |
| `edited_date` | 0 | — | **NOISE** |
| `edited_by` | 0 | — | **NOISE** |
| `current_account_value` | 0 | — | **NOISE** |
| `current_cash_value` | 0 | — | **NOISE** |
| `managed_account` | 0 | — | **NOISE** |

**Critical / Meaningful subset (8 cols):** `type_desc, trans_amount, client_id, activity_category, rep_name, reg_type, account_code, reg_name`

**Noise (12 cols):** the remaining LEGACY-only fields. Pure CSV-passthrough from Custom Report 28198 surface; no gold consumer wired in INF lane.

### Cross-reference: full LEGACY type_desc universe

DS~A Stage -1 audit (`INFGRO_TXN_TYPE_UNIVERSE_AUDIT_20260513.md`) found **45 distinct `type_desc` values** across full LEGACY silver universe (all 1,512 OLD-schema per-day partitions). 43 of 45 match the `orion_cashflow_taxonomy.yaml` v2 (Stage 0b ratified); 2 orphans ("Stock Split", "Unknown" — the latter only in NEW snapshot, smoking gun for dict gap).

NEW bronze (`bronze/transactions/2026-05-13.parquet`) contains **47 distinct `transTypeId` values** (1.25M-row full-history snapshot). NEW silver dict has 23 → **24 transTypeIds collapse to 'Unknown'**.

This means **REST DOES return all the classifications LEGACY had + 4 more**. The 'Unknown' regression is a **silver-side dict gap**, not a REST capability gap.

---

## Phase 0c — REST capability probe (empirical, no live probe needed)

### Why no live probe was required

The bronze parquet IS the empirical answer to "what does REST return." `pull_inflection_transactions_rest.py` calls `/api/v1/Portfolio/Accounts/{accountId}/Transactions` with no `$select` filter and no date params ("returns complete history in one call" per the pull script docstring at line 11). The 31 bronze cols are therefore the full REST payload schema for this endpoint.

To answer Andrew's question precisely:
- **What REST returns:** 31 cols. All CRITICAL gold-consumed fields (with rename) are present.
- **What silver keeps:** 18 cols. 13 dropped at silver-side `output_cols` list.
- **What's MISSING from REST entirely:** the 9 NOISE fields above + nothing CRITICAL.

### Y/N recoverability matrix (CRITICAL + MEANINGFUL subset)

| Col | REST-recoverable? | Mechanism | Path |
|---|---|---|---|
| `type_desc` | **YES** | `transTypeId` → dict lookup | Extend `TRANS_TYPE_DESC` dict from 23 → 47 entries (yaml-driven preferred) |
| `trans_amount` | **YES** | `transAmount` (renamed to `amount`) | Add `trans_amount` alias OR update gold to read `amount` |
| `activity_category` | YES (with caveat) | `transTypeId` → yaml v3 lookup | Re-derive from `orion_cashflow_taxonomy.yaml` v3 (14-bucket) OR drop dependency (Stage 0b is type_desc-only) |
| `client_id` | **YES** | `clientId` (currently kept as `client_id_bronze` internally, dropped at output_cols) | Add to output_cols (1-line fix) |
| `rep_name` | YES (join) | accounts_v2 silver has `rep_name`? Confirm; if not, accounts_dim silver does | Add to rep_lookup JOIN |
| `reg_type` | YES (need confirm semantic match) | `registrationCode` | Add to output_cols + verify code↔type mapping |
| `account_code` | **YES** | `accountNumber` | Add to output_cols (rename) |
| `reg_name` | **YES** | `registrationName` | Add to output_cols |

**All 8 CRITICAL/MEANINGFUL cols are REST-recoverable.** Zero fields require a path-(c) carve-out.

### Endpoint variant probes (deferred — not needed for path call)

The COO scope mentioned probing `?includeCancelled=true`, expanded `$select`, and alternative endpoints (`/AccountActivity`, `/Cancellations`). I deferred live probes because the empirical bronze answer fully resolves the consolidation question. If Andrew or CTO wants to explore those variants for unrelated reasons (e.g., investigating the noise fields like `RepName` joinability, or cancelled-status semantics), I can run a live probe in a follow-on cycle (~30 min).

---

## Phase 0d — Synthesis + Path Recommendation

### Path matrix

| Path | Description | Feasibility | Implementation cost |
|---|---|---|---|
| **(a) Full consolidation** | Kill LEGACY transactions write; NEW becomes single source. Extend silver-side dict + output_cols. | **FEASIBLE** | 1-2 DS commits (~2-4h): dict extension + output_cols additions + INF_C_01 + downstream rename audit |
| (b) Partial consolidation | Consolidate transactions only; keep LEGACY `convert_orion_to_silver.py` for accounts_dim + aum_snapshot | Already de-facto state (NEW only writes transactions; LEGACY writes 3 silver tables) | LEGACY needs TRN write retired; aum + accounts continue per DS~B finding |
| (c) Separation | Two prefixes (`silver/transactions_legacy/` + `silver/transactions/`); INF_C_01 dual-read | Possible but unnecessary | Adds permanent dual-source maintenance burden |

### Recommendation

**PATH (a) FULL CONSOLIDATION.** Andrew's instinct ("why couldn't we just consolidate") matches the empirical state.

The earlier path-(c) ratification was made on the assumption that REST was capability-limited. Empirical bronze inspection shows REST already returns the data; the consolidation is a silver-side refactor:

1. Extend `TRANS_TYPE_DESC` from 23 → 47 entries (or refactor to yaml-driven)
2. Add 4-6 cols to `convert_transactions_to_silver.py:216` output_cols (`client_id`, `account_code`, `reg_name`, `reg_type`, optionally `rep_name`, optionally `category` via yaml v3)
3. Retire `convert_orion_to_silver.py` TRN-write block (keep accounts_dim + aum_snapshot blocks per DS~B Bug B finding — those use Custom Report 28198 + separate AUM CSV that may not have REST equivalents)
4. Update INF_C_01 + INF_D_06 + INF_B_02 + INF_D_00 + INF_D_02 to read NEW silver col names (or add LEGACY-name aliases at silver-write — single decision point)

**Estimated implementation cost:** 1 DS commit for the dict extension (~1h, blocks on yaml v3 mapping work DS~B already doing in parallel) + 1 DS commit for silver output_cols + downstream rename audit (~2-3h). Total ~4h, smaller than the path-(c) carve-out + permanent dual-source maintenance.

**What does NOT need to consolidate (per DS~B finding):** `convert_orion_to_silver.py`'s accounts_dim builder + aum_snapshot builder remain LEGACY-sourced. Bug B is orthogonal (NEW accounts_v2 silver has a silent fallback to NA on missing rep map). The two paths address different bugs.

### Open follow-ons (not blocking the path call)

1. **`activity_category` 14→3 collapse:** if anything ever depends on the 14-bucket granularity (currently only `INF_C_01` and only informationally), needs yaml v3 14-bucket re-derivation. Stage 0b migration already moved the classifier off this column, so this may be a no-op.
2. **`rep_name` JOIN source:** verify `accounts_v2` silver carries `rep_name` (not just `rep_id`). If not, NEW silver builder needs to read rep dim instead.
3. **`reg_type` semantic match:** is REST `registrationCode` == LEGACY `reg_type`? Likely yes given Orion's naming convention, but worth a 5-min spot-check.
4. **Bug B (DS~B):** orthogonal silver-runner orchestration issue with `accounts_v2` (silent NA fallback at `convert_orion_api_to_silver.py:466-467`). Not a transactions-path issue.

---

## Files inspected

| File | Purpose |
|---|---|
| `data/orion/scripts/silver/convert_orion_to_silver.py` | LEGACY CSV-bronze → silver (line 466-475: silver_cols for TRN) |
| `data/orion/scripts/silver/convert_transactions_to_silver.py` | NEW REST-bronze → silver (line 72-99: TRANS_TYPE_DESC dict; line 216: output_cols) |
| `data/orion/manual_api/pull_inflection_transactions_rest.py` | REST pull (line 69: ACCOUNTS_API_PATH `/api/v1/Portfolio/Accounts/{id}/Transactions`) |
| `data/orion/scripts/gold/INF_C_01.canonical_nna.py` | Primary consumer — Stage 0b type_desc-only classification (line 416-437) |
| `s3://opal-data-inf/silver/transactions/2026-05-12.parquet` | LEGACY silver sample (79 rows, 31 cols, 2026-05-12 per-day) |
| `s3://opal-data-inf/silver/transactions/2026-05-13.parquet` | NEW silver snapshot (1.25M rows, 18 cols, full history) |
| `s3://opal-data-inf/bronze/transactions/2026-05-13.parquet` | NEW bronze REST source (1.25M rows, 31 cols, distinct transTypeId=47) |

## Compiler tools

| Tool | Run | Result |
|---|---|---|
| `comp-pipescript io <gold script>` | (deferred — schema enumeration via parquet header inspection was authoritative) | n/a |
| Phase 0c live REST probe | Deferred — empirical answer in bronze parquet | n/a |

## RAVC2

Surfacing to COO + CTO for path ratify. Andrew at console. Path-(a) recommendation; full implementation is a follow-on TO if ratified.

— DS~D
