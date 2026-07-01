# ADVI_INFREF — Path & Reference Map (AS-BUILT vs PRD-TARGET)

**Status:** LIVING (created 2026-07-01, 0.4.0_DS_ClientPlatform~A) — the ref/path tracking artifact
the PRD lacks. **Companion to** `ADVI_INFREF_PRD.md` (the PRD tracks DECISIONS; this tracks the
CONCRETE bronze/silver/gold keys every script reads/writes, as-built, with drift flagged).
**Lane note:** authored by DS in `docs/briefs/` (DS lane); **recommend CTO promote to
`docs/architecture/ADVI_INFREF_PATHMAP.md` + reference it from PRD §1/§4-R1** (architecture is CTO lane).
**Why this exists:** Andrew asked (2026-07-01) whether the paths are set up as the PRD's
`bronze/orion-api ↔ silver/orion-api` vs `eclipse` two-domain framework, and how well the refactor
docs track refs/paths. Short answer: **the FORMAT de-convert + rebuild are done; the PRD's
folder-layout UNIFICATION is NOT, and it wasn't tracked.** This doc closes that gap.

---

## 1. The 4-layer framework: PRD-TARGET vs AS-BUILT (the headline)

| Layer | PRD §1 / §4-R1 (Andrew-LOCKED target) | AS-BUILT (tonight) | Match? |
|---|---|---|---|
| Bronze | `bronze/orion-api/{date}/` + `bronze/eclipse-api/{date}/` — two source domains, never share a prefix | `bronze/{dim}/{date}.jsonl.gz` (positions/assets/txn/perf) + `bronze/orion-api/{date}/*.csv` (tax/billing/unified/CR-txn) + `bronze/orion-api-v2/` (reps) + `bronze/eclipse/` | **NO** — 3+ coexisting conventions, not the unified two-domain tree |
| Silver | ONE layout `silver/orion-api/{dim}/snapshot_date={date}/data.parquet` + `silver/eclipse-api/` (stub) | MIXED: `silver/api_dims/{dim}/snapshot_date=/data.parquet` (positions_mv, household, tax, billing, accounts_v2) AND flat `silver/{dim}/{date}.parquet` (assets_v2, transactions, performance) | **NO** — two layouts, no `silver/orion-api/` or `silver/eclipse-api/` |
| Format | raw at bronze (JSON stays JSON) | `.jsonl.gz` (gzipped JSONL) | AMENDED — CTO ruled uniform gzip 235025Z (legit) |

**Bottom line:** the `orion-api ↔ eclipse` two-domain namespace framework is **NOT** set up. Eclipse
is separate in bronze (`bronze/eclipse/`) but has no `silver/eclipse-api/`; the orion dims are
dim-prefixed, not under `bronze/orion-api/`. What we did tonight = the FORMAT de-convert
(`.parquet`→`.jsonl.gz`) + the full-history rebuild. The FOLDER-LAYOUT unification (a core PRD §1
goal) is **outstanding + was untracked until this doc**. Per §4-R1 the CTO ruled the unified layout
is GO-FORWARD-from-cutover (don't migrate history) — so this is a scheduled follow-on, not a tonight-break.

**DISPOSITION (AWAITING Andrew):** (a) accept dim-prefixed as operative + amend PRD §1/§4-R1 to match;
or (b) schedule the `orion-api/eclipse-api` unification as a clean go-forward leg (new layout from
cutover, freeze dim-prefixed read-only per §4-R1).

---

## 2. Per-dim path table (AS-BUILT, source-grounded)

| Dim | Bronze (pull writes) | Silver builder → silver key | Gold reads | Notes |
|---|---|---|---|---|
| positions_mv | `bronze/positions/{date}.jsonl.gz` | convert_orion_api_to_silver / run_silver_backfill_parallel → `silver/api_dims/positions_mv/snapshot_date=/data.parquet` | positions_mv | full history (2259 bronze) |
| assets_v2 | `bronze/assets/{date}.jsonl.gz` | convert_assets_v2_to_silver → `silver/assets_v2/{date}.parquet` (FLAT) | via holdings | full history (2255) |
| transactions | `bronze/transactions/{date}.jsonl.gz` (REST spine) **+** `bronze/orion-api/*/transactions.csv` (Custom-Report join, NOT de-converted) | convert_transactions_to_silver → `silver/transactions/{date}.parquet` (FLAT) | txn consumers | **49 bronze → 1560 silver** (see §4.3) |
| performance | `bronze/performance/{date}.jsonl.gz` | convert_performance_to_silver → `silver/performance/{date}.parquet` (FLAT) | **INF_C_02:62 reads `silver/performance/`** | api_dims/performance = ORPHAN (§4.2) |
| household | (frozen `geo_verify` CSV + `unified_account_dim`) | convert_orion_api_to_silver `build_household` → `silver/api_dims/household/snapshot_date=/data.parquet` | household consumers | FROZEN — geo_verify stale; repoint to accounts_v2 pending (see P3 worklist A9) |
| accounts_v2 | `bronze/orion-api/{date}/new_portfolio_accounts.json` | convert_orion_api_to_silver → `silver/api_dims/accounts_v2/snapshot_date=/data.parquet` | INF_D_00d etc. | fresh; 45 cols |
| tax | `bronze/orion-api/{date}/tax_{realized,unrealized}.csv` | build_tax_dim → `silver/api_dims/tax_{realized,unrealized}/snapshot_date=/data.parquet` | tax consumers | .csv bronze (not de-converted) |
| billing | `bronze/orion-api/{date}/billing.csv` | build_billing_dim → `silver/api_dims/billing/snapshot_date=/data.parquet` | billing consumers | .csv bronze |
| unified_account_dim | `bronze/orion-api/{date}/unified_account_dim.csv` | (feeds accounts_dim gold) | INF_A_00 | .csv bronze |
| reps | `bronze/orion-api-v2/{date}/{representatives,household_rep_mapping}.json` | (reference universe) | — | .json; read as parquet reference where materialized |
| eclipse | `bronze/eclipse/*` | (silver TBD — no silver/eclipse-api) | — | separate source; silver stubbed/absent |

---

## 3. Bronze prefix inventory (coexisting conventions)

1. `bronze/{dim}/{date}.jsonl.gz` — the DE-CONVERT layout (positions/assets/transactions/performance). NEW format, OLD dim-prefix (§4-R1 names these the "old prefixes to freeze").
2. `bronze/orion-api/{date}/*.csv` — legacy REST/Custom-Report (tax/billing/unified_account_dim/CR-transactions). NOT de-converted (still .csv).
3. `bronze/orion-api-v2/{date}/*.json` — reps (representatives, household_rep_mapping).
4. `bronze/eclipse/*` — Eclipse bulk pull (separate source domain).

The PRD wants #1–#3 unified under `bronze/orion-api/{date}/` and #4 under `bronze/eclipse-api/{date}/`. Not done.

---

## 4. DRIFT / INCONSISTENCY list (most important first)

**4.1 Silver LAYOUT split** — some dims Hive-partitioned (`silver/api_dims/{dim}/snapshot_date=/data.parquet`),
others flat (`silver/{assets_v2,transactions,performance}/{date}.parquet`). Not the PRD's single
`silver/orion-api/{dim}/` layout. This split has ALREADY caused an incident (see 4.2).

**4.2 LIVE ORPHAN: `silver/api_dims/performance/` (52 parquet)** — written by convert_orion_api_to_silver,
but gold (INF_C_02:62) reads `silver/performance/` (49 parquet, written by convert_performance_to_silver).
The api_dims/performance write is an orphan producer (no reader). INF_C_02:129-135 documents a PRIOR
incident of exactly this class: a phantom `silver/performance_dim/` path "silently neutered INFGRO.009
across three chain runs." **This is the concrete evidence that path-drift here is not theoretical.**
Action: confirm convert_orion_api_to_silver's performance branch is dead → retire it (single-writer).

**4.3 Transactions two-source + PARTIAL rebuildability** — silver txn = REST-spine
(`bronze/transactions/*.jsonl.gz`, 49 dates) LEFT-JOIN Custom-Report (`bronze/orion-api/*/transactions.csv`,
full history, NOT de-converted). Only ~49 of 1560 silver/transactions partitions are rebuildable from
bronze (the other ~1511 have no bronze REST-spine — historical). Rebuild is necessarily partial for
txn; CVO L3 scopes it as "49 rebuilt value-checked + 1511 legacy unchanged==snapshot." (Flagged to CVO.)

**4.4 STALE DOCSTRINGS (de-convert doc-drift)** — `convert_transactions_to_silver.py:14` and
`convert_performance_to_silver.py:4` docstrings say they read `.parquet`, but the code (L272 / L65)
reads `.jsonl.gz`. Fix the docstrings (do NOT push mid-rebuild — the runner uses these; hold to
post-rebuild). Low-risk but a tracking-hygiene miss.

**4.5 DE-CONVERT READER MISS (FIXED)** — `run_silver_backfill_parallel.py:164` read the new `.jsonl.gz`
bronze as parquet (KEY was flipped, inline READER was not) → "Parquet magic bytes not found." Fixed
2026-07-01 (740aab11b): gunzip+read_json, verified 24148→24148 both dims. **Full audit of all
`read_parquet` in silver+manual_api done → this was the ONLY de-convert reader bug**; all other
read_parquet are silver/gold reads, the reconvert's intentional old-parquet read, or reference-universe
reads (household_rep_mapping/accounts_v2, still parquet). No other de-convert reader mismatch.

**4.6 household geo FREEZE** — build_household reads the frozen `geo_verify` CSV → household 1204h stale.
Repoint to accounts_v2 spec'd + grounded (P3 worklist A9 precondition); execute post-cutover.

---

## 5. Doc-tracking gap (answer to "how much are we tracking refs/paths?")

The PRD (`ADVI_INFREF_PRD.md`) tracks the DECISIONS thoroughly but had **no living path-map** — no
per-dim as-built key table, so the §1 framework divergence + the api_dims/performance orphan + the
stale docstrings were all invisible in the docs. **This file is that tracking artifact.** Keep it
current on any bronze/silver/gold key change; it is the gate against the phantom-path class (4.2).
Recommendation: PRD §1/§4-R1 should reference this file; each future path change updates the table here.
