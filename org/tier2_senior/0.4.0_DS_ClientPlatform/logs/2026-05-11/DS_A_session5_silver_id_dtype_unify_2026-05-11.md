# DS~A 2026-05-11 session 5 — ADVI_INFNNA.SILVER-ID-DTYPE-UNIFY close

## TL;DR

Closed SILVER-ID-DTYPE-UNIFY via in-place dtype migrate (Andrew Option A pivot). 9,296/9,296 partitions migrated in 6.8min, Int64 sample-validated 12/12, Step 5 cascade 35/37 OK (+6.9% wall vs ACCOUNT-ID-COERCE baseline, within ±10% tolerance). 2 transient S3 SSL failures on 2019-stale-era keys ratified as Gate-1 per CTO+COO pragmatic close. Followup INF_C02_C03_TLS_HARDEN authoring as separate TO. Full RAVC4 sent.

## Migration-path pivot story

- Initial plan: full bronze→silver rebuild Tier 1+2+3 (estimated 3-4h)
- Mid-execution: COO surfaced **in-place dtype migrate alternative** (read parquet → coerce → write same key) — 5-10min total
- Andrew GO Option A → killed Tier 1 transactions rebuild `bkp4i6zj2` (was at 550/1505 partitions)
- Built `.runtmp/silver-dtype-migrate.py` (130-line script, 32 workers, dry-run + SSE-AES256)
- Dry-run PASS 3.5min (9,296 keys readable + coerceable, fail=0)
- Real migrate **9,296/9,296 ok in 6.8min**, ~50x faster than full rebuild
- Tool promoted to `.tools/silver-dtype-migrate.py` (canonical operational path)
- Architectural taxonomy now captured in memory: dtype-only-fix vs transformation-change

## Code changes

### Helper
- `data/orion/scripts/silver/_orion_api_silver_lib.py` — added `coerce_silver_ids(df, cols=DEFAULT_SILVER_ID_COLS)` + DEFAULT_SILVER_ID_COLS tuple `(account_id, household_id, rep_id, client_id, registration_id, custodian_id, transaction_id, trans_id)`. Excludes `additional_rep_ids` (intentional `;`-separated string list). Idempotent.

### Builders updated (9 total)
- `convert_orion_api_to_silver.py` — header convention comment + `coerce_silver_ids` call before every `return df[cols]` in 9 build_* fns (household, performance, activity, billing, accounts_v2, representatives, household_rep_mapping, positions_mv, transactions)
- `build_billing_dim.py` — import + helper call
- `build_tax_dim.py` — helper call before both `build_tax_unrealized` + `build_tax_realized` returns
- `build_assets_dim.py` — import + helper call + removed `df['account_id'] = df['account_id'].astype(str)` at line 144
- `convert_transactions_to_silver.py` — sys.path injection + helper call on `lookup` + `df` + removed `astype(str)` casts at lines 118-120

### Conflicting str casts removed
- `convert_orion_api_to_silver.py:build_accounts_v2` line 425 `out['account_id'] = out['account_id'].astype(str)` — REMOVED
- `convert_orion_api_to_silver.py:build_accounts_v2` line 426 `out['household_id'] = out['household_id'].astype(str)` — REMOVED
- `convert_orion_api_to_silver.py:build_accounts_v2` line 456 rep_map `household_id` astype(str) — REMOVED
- `build_assets_dim.py` line 144 `df['account_id'].astype(str)` — REMOVED
- `convert_transactions_to_silver.py` lines 118-120 + 161-162 + 185 astype(str) calls — REMOVED

### Commits
- `f6b7238a9` — 5 files / 71 insertions: helper + main convert_orion_api_to_silver + build_billing_dim + build_tax_dim + build_assets_dim
- `8b4c59861` — 1 file / 21 insertions: convert_transactions_to_silver

## In-place migrate execution

### Dry-run (`.runtmp/silver-dtype-migrate.py --dry-run --workers 16`)
- Started 15:36:55Z, ended 15:40:34Z (3.5min wall)
- Total keys: 9,296 across 12 prefixes
- Outcome: ok=9,296 / skip=0 / fail=0
- Size: 2,023.9MB (read-only, no writes)

### Real migrate (`bwra23lri`)
- Started 15:40:49Z, ended 15:47:36Z (**6.8min wall**)
- 16 workers, force `--no-skip` overwrite
- Outcome: **ok=9,296 / skip=0 / fail=0**
- Size before: 2,023.9MB → after: 2,023.5MB (Int64 slightly more compact than mixed object)
- SSE-AES256 on every write

## Int64 validation — 12/12 PASS

Per-prefix sample (1 parquet × 12 prefixes) via `.runtmp/validate-int64-samples.py`. All present ID columns Int64.

| Prefix | Sample | ID cols Int64 |
|---|---|---|
| silver/transactions/ | 2020-05-26.parquet | account_id, household_id, rep_id, client_id, registration_id, transaction_id, trans_id |
| silver/api_dims/accounts_v2/ | snapshot_date=2026-04-28 | account_id, household_id, rep_id, registration_id, custodian_id |
| silver/api_dims/positions_mv/ | snapshot_date=2020-05-26 | account_id, client_id, registration_id |
| silver/api_dims/performance/ | snapshot_date=2026-04-28 | account_id, household_id, rep_id |
| silver/api_dims/tax_realized/ | snapshot_date=2020-01-01 | account_id, household_id, rep_id |
| silver/api_dims/tax_unrealized/ | snapshot_date=2020-01-01 | account_id, household_id, rep_id |
| silver/api_dims/billing/ | snapshot_date=2020-01-31 | account_id, household_id, rep_id |
| silver/api_dims/activity/ | snapshot_date=2026-04-28 | account_id, household_id, rep_id |
| silver/api_dims/household/ | snapshot_date=2026-04-28 | account_id, household_id, rep_id |
| silver/api_dims/household_rep_mapping/ | snapshot_date=2026-04-29 | household_id, rep_id |
| silver/api_dims/assets_v2/ | snapshot_date=2026-04-29 | account_id, client_id, registration_id |
| silver/api_dims/representatives/ | snapshot_date=2026-04-29 | rep_id |

**Total non-Int64 columns: 0.**

## Step 5 validation cascade `cascade-154852Z-b9967954`

- Total wall: **5,099.1s = 85.0min** (vs 79.5min ACCOUNT-ID-COERCE baseline = **+6.9%, within ±10% tolerance**)
- OK: 35 / FAIL: 2

### Script-level wall comparison vs Friday baseline

| Script | Friday wall | Today wall | Δ |
|---|---|---|---|
| INF_A_00.accounts_dimension | 34.4s | 31.1s | -10% |
| INF_A_01.advisor_assignments | 30.2s | 29.0s | -4% |
| INF_A_02.fee_rate_history | 3.4s | 2.2s | -35% |
| **INF_A_03.positions_cube** | **768.8s** | **421.1s** | **-45% (DS~B PARALLEL-EXPAND local-Windows ThreadPool)** |
| INF_A_04.client_dimension | 2.2s | 11.1s | +400% |
| INF_B_00.canonical_holdings | 1502.8s | 1499.6s | ~0% |
| INF_B_01.holdings_lots | 95.5s | 80.6s | -16% |
| INF_B_01b.classify_new_secs | 35.8s | 33.4s | -7% |
| INF_B_02.canonical_lots | 48.3s | 51.0s | +6% |
| INF_B_03.account_gains | 710.4s | 726.4s | +2% |
| INF_C_00.canonical_performance | 676.9s | 732.2s | +8% (Int64-vs-object merge WARN overhead) |
| INF_C_01.canonical_nna | 183.6s | 176.0s | -4% |
| INF_C_01b.role_aua_backfill | 55.7s (failed early) / standalone 464s | 483.1s | clean |
| INF_C_02.client_performance | 79.5s | **rc=1 transient** | — |
| INF_C_03.account_performance | 144.3s | **rc=1 transient** | — |

INF_A_03 platform-disambiguated comparison (CTO ask): local-Windows ThreadPool 421.1s vs DS~B's EC2 Linux ProcessPool 45s (13x speedup only realizes via fork() on Linux).

## Cross-validation with DS~B INF_A_LAYER_TXN-CACHE

DS~B's `txn_cache_reader.load_cached_transactions` shared-cache pattern landed in INF_A_00 + INF_A_01 mid-cascade-prep. Both my `coerce_id_columns` calls and DS~B's `load_cached_transactions` calls live in the same scripts. INF_A_00 + INF_A_01 PASS rc=0 on first attempt in cascade — **orthogonal changes layered cleanly**.

## C_02 / C_03 transient failures (ratified Gate 1)

- C_02 attempt 1: `ConnectionClosedError` on `canonical_performance_2019-10-22.parquet`
- C_02 attempt 2: `SSLError: UNEXPECTED_EOF_WHILE_READING` on `canonical_performance_2019-10-28.parquet`
- C_03 attempt 1: `ConnectionClosedError` on `canonical_performance_2019-09-18.parquet`
- C_03 attempt 2: `SSLError: UNEXPECTED_EOF_WHILE_READING` on `canonical_performance_2019-09-18.parquet`

Both scripts use `ThreadPoolExecutor(max_workers=min(len(dates), 256))` → 256-thread parallel S3 reads → TLS connection-pool exhaustion + AWS-side soft throttling.

**Diagnosis: not code regression. Stale-era 2019 keys hit during iteration trigger the network-layer drops.**

DS~B's STALE-PURGE finding confirms 2019-era keys are "iterate-target-rot from B_01/B_03" — legacy historical canonical_performance partitions pre-dating Inflection onboarding (2020-05-26).

Per CTO+COO close: Gate 1 ratified as "35/37 OK + 2 documented transient S3 infra failures on 2019-stale-era keys (TLS connection pool exhaustion on 256-worker parallel reads). Not a code regression. Hardening TO authored TODAY."

## Gate 6 platinum freshness

- `platinum/firm/leaderboard.json` (generated 17:08:47Z) — **4 entries all 3 windows**, Joe Brandenburg present ($16.4M AUA, $11.73M MAX NNA). PASS.
- `platinum/firm/dashboard.json` (generated 17:10:57Z) — `headline.total_aua=$202,958,135.02` vs CTO canonical $199.6M (`total_aua` cut per CLAUDE.md AUA terms). Drift +1.7%, within ±3% Guard B tolerance. Treated as new canonical for 2026-05-11.

## Files touched

- `data/orion/scripts/silver/_orion_api_silver_lib.py`
- `data/orion/scripts/silver/convert_orion_api_to_silver.py`
- `data/orion/scripts/silver/build_billing_dim.py`
- `data/orion/scripts/silver/build_tax_dim.py`
- `data/orion/scripts/silver/build_assets_dim.py`
- `data/orion/scripts/silver/convert_transactions_to_silver.py`
- `.tools/silver-dtype-migrate.py` (new operational tool)
- `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFNNA.SILVER-ID-DTYPE-UNIFY.ds-silver-canonical-id-dtype-enforcement.md` (status → complete)
- `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-11/DS_A_session5_silver_id_dtype_unify_2026-05-11.md` (this log)
- `memory/feedback_silver_id_dtype_convention.md` (taxonomy expansion)
- `memory/MEMORY.md` (index entry)

## Diagnostics retained (transient `.runtmp/`)

- `.runtmp/logs/silver-dtype-migrate-2026-05-11.log`
- `.runtmp/logs/cascade-2026-05-11-post-silver-unify-stdout.log`
- `.runtmp/logs/e2e/2026-05-11/cascade-154852Z-b9967954.log`
- `.runtmp/telemetry/2026-05-11/inf-gold-layer-runner/` (per-script JSONL)
- `.runtmp/joe-verify/leaderboard-post-step5.json`
- `.runtmp/joe-verify/dashboard-post-step5.json`
- `.runtmp/logs/c02-retry2.log`, `.runtmp/logs/c03-retry2.log`

## Compiler tools

- `.tools/ds-commit-gate.sh` — PASS on every edited Python file (py_compile + AST + ruff py39)
- `comp-pipescript deployed` — N/A for INF pipeline (BD-only filter; INF coverage gap tracked in ADHC_DSFLOW.005 `5f81020ee`)

## Next pickup

- **INF_C02_C03_TLS_HARDEN** — authoring incoming from COO. ~15min effort (max_workers 256→32 + boto3 retry config + per-script gate-test).
- **SILVER-PERFORMANCE-HIST + SILVER-ACCOUNTS-HIST** — STAGED low.
