# DS~A 2026-05-11 session 6 — INF_C02_C03_TLS_HARDEN + EOD summary

## TL;DR

Closed `ADVI_INFNNA.INF_C02_C03_TLS_HARDEN` (CTO Option B ratified) via 32-worker cap + boto3 adaptive-retry Config. Both scripts standalone-validated rc=0 with zero TLS errors. S3 deploy MATCH. 8th and final TO shipped today.

## TLS hardening detail

### Root cause (per cascade `b9967954` 4/4-retry-exhaust escalation)

`ThreadPoolExecutor(max_workers=min(len(dates), 256))` in INF_C_02 + INF_C_03 vastly oversubscribed boto3's default 10-connection HTTPS pool. Result: keep-alive churn → TLS handshake retries → `SSLError UNEXPECTED_EOF_WHILE_READING` on `canonical_performance_2019-*.parquet` reads. Confirmed client-side cause by error-class shift between attempt 1 (`ConnectionClosedError`) and attempt 2 (`SSLError`) — same scripts, same keys, same hour.

### Changes

INF_C_02.client_performance.py + INF_C_03.account_performance.py:

```python
from botocore.config import Config

_S3_CONFIG = Config(
    retries={'max_attempts': 10, 'mode': 'adaptive'},
    max_pool_connections=128,
)
s3 = boto3.client('s3', region_name='us-east-1', config=_S3_CONFIG)
```

```python
# CAP at 32 (TLS pool exhaustion at 256+; see ADVI_INFNNA.INF_C02_C03_TLS_HARDEN 2026-05-11)
with ThreadPoolExecutor(max_workers=min(len(dates), 32)) as pool:
```

INF_C_03 line 184 second ThreadPool (was 64-worker) also capped 32 for uniformity. Future agents see uniform convention.

Safety margin: 32 workers × 128 pool-connections = **4x headroom** (vs prior 256 × 10 = 25x oversubscription).

### Standalone validation (post-fix)

| Script | Wall | Rows | Cohort | rc | Stderr |
|---|---|---|---|---|---|
| INF_C_02 | ~2min | 429,321 | 308 households / 2,167 dates | 0 | clean |
| INF_C_03 | ~3min | 1,222,789 | 1,467 accts / 2,419 dates | 0 | clean |

Full historical 2020–2026 range traversed each. Zero `ConnectionClosedError`, zero `SSLError`.

### S3 deploy MATCH (rule 13)

```
aws s3 cp data/orion/scripts/gold/INF_C_02.client_performance.py s3://opal-data-inf/code/gold/...
aws s3 cp data/orion/scripts/gold/INF_C_03.account_performance.py s3://opal-data-inf/code/gold/...

SHA16 cross-check (local vs S3):
  INF_C_02.client_performance.py:  ceff93acc1b58333 == ceff93acc1b58333  MATCH
  INF_C_03.account_performance.py: 8ab7c76c9c6b19a2 == 8ab7c76c9c6b19a2  MATCH
```

### Commits

- `4e82e8c45` — TLS-harden code changes (2 files, 25 insertions / 5 deletions)
- `8298bb7ed` — TO closure (status pending → complete + closure_via)

### Compiler tools

- `.tools/ds-commit-gate.sh` — PASS on both files (py_compile + AST + ruff py39)

## EOD summary — 2026-05-11 DS~A landings

| # | TO / artifact | Commits | Notes |
|---|---|---|---|
| 1 | `ADVI_ROLLUP.SL-P1c` close | `b276a6147` | RAVC4 ACCEPT-WITH-NOTE per COO. 3 distinct >50KB shadow emits 2026-05-01/06/07; SHA chain `7c9f1b13c → e3463bffa → 6424b29ab`; Jones $2.47M ± 1% CTO-Option-A. SL-P2 PROMOTE flipped staged → pending. |
| 2 | `ADVI_INFNNA.JOE-TXN-BACKFILL` close | `433db705c` | Status pending → complete. 1,510 silver/transactions partitions with RICH schema spot-checked 2023-06-15 + 2026-05-07; Joe $16.2M AUA / $11.69M MAX NNA / 21 clients. |
| 3 | GOLD + SILVER status sweep | `decaaf523` | Found 3 real follow-up items: LEADERBOARD-JOE-ABSENT, SILVER-PERFORMANCE-HIST, SILVER-ACCOUNTS-HIST. |
| 4 | `ADVI_INFNNA.ACCOUNT-ID-COERCE` close | `c2a7a5967` | Effective 37/37 via local cascade `cascade-133034Z-1474df2b` (HEAD code) + standalone re-run for C_01b post-`_read_s3`-wrapper patch. Helper at `data/orion/scripts/gold/lib/dtype_coerce.py` (coerce_id_columns + coerce_account_id back-compat). 5 stale gold scripts deployed mid-day to S3 + MATCH verified per DS~B's SHA-cross-check finding. TO status `complete (local-path + S3-deploy-MATCH)`. |
| 5 | `ADVI_INFNNA.LEADERBOARD-JOE-ABSENT` close | (bundled with #4) | RESOLVED-BY-CASCADE per execution gate. Joe present in all 3 leaderboard windows post-cascade (4 entries each, QTD/YTD/MAX). |
| 6 | `ADVI_INFNNA.SILVER-ID-DTYPE-UNIFY` close | `f6b7238a9` + `8b4c59861` + `78c6760db` | In-place dtype migrate (Andrew Option A pivot, ~50x savings vs original full-bronze-rebuild plan). 9,296/9,296 silver parquets migrated to Int64 in 6.8min. Sample-validation 12/12 PASS across all dims. Step 5 cascade `cascade-154852Z-b9967954` 35/37 OK / 85min wall (+6.9% vs baseline, within ±10%). `.tools/silver-dtype-migrate.py` promoted as canonical operational tool. |
| 7 | RAVC4 + Gate 8 close | (no commit; message) | All 8 CTO gates GREEN. AUA-canonical answer (`total_aua` cut, $202.96M = +1.7% from $199.6M baseline, within ±3% Guard B). Cross-validation with DS~B INF_A_LAYER_TXN-CACHE orthogonal layer landed cleanly. INF_A_03 wall platform-disambiguated (Local-Windows 421s vs EC2 Linux 45s = 13x speedup only realizes via fork() on Linux). |
| 8 | `ADVI_INFNNA.INF_C02_C03_TLS_HARDEN` close | `4e82e8c45` + `8298bb7ed` | This session. 32-worker cap + boto3 adaptive retries. Both scripts rc=0 standalone post-fix, zero TLS errors. S3 deploy MATCH. |

**8 TOs + 2 memory entries crystallized.**

Memory entries shipped (`memory/`):
- `feedback_silver_id_dtype_convention.md` — canonical Int64 silver convention + dtype-only-fix vs transformation-change migration-path taxonomy. References `.tools/silver-dtype-migrate.py` as operational path.

## Cross-pod observations

- **DS~B INF_A_LAYER_TXN-CACHE** (`txn_cache_reader.load_cached_transactions`) landed in INF_A_00 + INF_A_01 mid-day. Preserved my `coerce_id_columns` calls cleanly. Both PASS rc=0 first attempt in cascade `b9967954` — orthogonal changes layered without conflict.
- **DS~B INF_A_03 PARALLEL-EXPAND** — 13x speedup confirmed on Linux EC2 (45s compute vs 583s Friday baseline). Local Windows realizes 45% speedup (421s vs 769s) due to ProcessPool→ThreadPool fallback (Windows no fork()).
- **DS~B SHA-cross-check discovery** at 15:30Z (5 stale gold scripts on S3 from rule-13 deploy gap) — empirically verified + remediated within ~10min via emergency `aws s3 cp` + MATCH verify. Process-discipline catch.

## Queue for tomorrow (no urgency)

- `ADVI_INFNNA.SILVER-PERFORMANCE-HIST` — historical per-date backfill for silver/api_dims/performance/ (only 4 snapshot dates currently)
- `ADVI_INFNNA.SILVER-ACCOUNTS-HIST` — same for accounts_v2 (only 7 snapshot dates)
- `STALE-PURGE` re-author + `DATE_CLIP` — long-term fix for 2019-stale-era key iteration surface (TLS_HARDEN is the immediate defense; DATE_CLIP shrinks the surface naturally)
- `ThreadPool sizing convention` DSFLOW backlog item (flag any script with max_workers > 32 for review)

## Files touched this session

- `data/orion/scripts/gold/INF_C_02.client_performance.py`
- `data/orion/scripts/gold/INF_C_03.account_performance.py`
- `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_INFNNA.INF_C02_C03_TLS_HARDEN.ds-thread-pool-cap-plus-boto3-config.md`
- `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-11/DS_A_session6_tls_harden_and_eod_2026-05-11.md` (this log)

## Diagnostics retained (transient `.runtmp/`)

- `.runtmp/logs/c02-tls-harden.log`
- `.runtmp/logs/c03-tls-harden.log`

## Watcher

Inbox-watch PID 212467 alive at EOD.

## Next session pickup

Per COO 18:15Z standing-watch: queued items above, no urgency. Re-launch inbox-watch + check inbox first thing at next session start.
