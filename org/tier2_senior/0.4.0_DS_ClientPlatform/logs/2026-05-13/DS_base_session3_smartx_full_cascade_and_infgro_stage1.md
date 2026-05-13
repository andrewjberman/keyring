# DS-base 2026-05-13 session 3 — SmartX full cascade + INFGRO Stage 1

**Agent:** 0.4.0_DS_ClientPlatform (base, no tilde lane)
**Window:** ~17:55Z → ~20:13Z 2026-05-13 (~2h 18m)
**Andrew session directive:** base DS only, no ~A/~B/~C/~D dispatches

## TL;DR

9 substantive DS commits across 2 partner-visible projects. Resolved 128-day frozen Non-Model plug on opalinvest.dev (live $445M now). Closed full INFGRO Stage 1 architecture cascade (silver + gold + leaderboard, all Rule 17 strict).

| Project | Closed TOs | Anchor commits |
|---|---|---|
| **SmartX Non-Model** | TO-1, TO-2, TO-5 (+ AE 0.7 TO-3 closing the cascade) | `11d91fde6`, `144493642`, `51ffcbf65`, AE `25f00249c` (smartx-v2.1.0) |
| **INFGRO Stage 1** | TO-2, TO-1, TO-3, TO-4 | `f39550d99`, `45e72f5e7`, `252c6c608`, `6b94d8a8a` |

Additional upstream commits I integrated/re-shipped: `f97dd3288` + `2b072737a` (DS~A Path B reconcile + ffill-canonical follow-up on backfill script).

## SmartX Non-Model cascade (sessions 2-3)

### Problem statement
- `non_model_assets.json` portal file frozen at $271,228,563.96 since 2026-01-05 (128 days)
- Root cause: 49F enterprise CSV stopped updating 12/26/2025; legacy `compute_non_model_assets.py` was manual-only and not in any cron
- Net effect: ModelPortfolios Non-Model bar was static, partner-visible disservice

### Architecture shipped
1. **Backfill script** (`data/smartx/scripts/backfill_non_model_assets.py`, `11d91fde6`) — 5-segment stitch:
   - A: 2024-11-01 → 2026-01-05 preserve existing
   - B: 2026-01-06 → 2026-01-15 HOLD plug (10-day Andrew-confirmed bridge)
   - C: 2026-01-16 → 2026-03-10 silver/allocations sum
   - D: 2026-03-11 → 2026-05-11 BD certified_aua
   - Daily Lambda extension takes over from 2026-05-12 forward
2. **Path B reconcile** (DS~A `f97dd3288` + `2b072737a`, my re-ship): segment-A model_aum sourced from canonical `aum-timeseries.aggregate` instead of legacy (Q-end drift Q1 +$19M / Q2 -$10M / Q3 -$11M eliminated)
3. **Daily Lambda Step 6** (`144493642`) — `append_non_model_today.py` hooked into `smartx_ingestion_pipeline/lambda_function.py`:
   - Source-of-truth waterfall: `gold/aua_certification/{date}.json` → silver/allocations fallback → up to 5-day lookback
   - Idempotent if today's row already present
   - Deployed via AE 0.7's `smartx-v2.1.0` tag (`25f00249c`)
4. **Legacy script retired** (`51ffcbf65`) — `compute_non_model_assets.py` body replaced with deprecation stub exit code 2; SMARTX_BIBLE.md Stage 3 section rewritten to document live flow

### Partner-visible outcome
- ETag `65cd59bbd107a06421f706ecfb5acfa6` on `s3://opal-data-portal-v2/json/portfolios/non_model_assets.json`
- 558 daily rows 2024-11-01 → 2026-05-12
- Latest 2026-05-12: enterprise $1,804,326,383.80 / model $1,359,073,650.32 / **non_model $445,252,733.48 (24.68%)**
- 2 CloudFront invalidations fired (`I1LNWEAIJ55RIUNHEU29JD5LDM` + `IULWG7TQV3SJCVVF1C6BI0C5E`) — Andrew direct-verified on opalinvest.dev

### Owned-paths drifts flagged
- `.owned-paths.yaml:632` `data/smartx/**` → POD3 (should be POD4)
- No entry for `infra/aws/lambda/smartx_ingestion_pipeline/**` (falls to AE-only)
- Both bypassed via `GIT_COMMIT_AUTHOR_OVERRIDE=POD4`/`POD4_OR_AE` with audit log; COO bundled for ADHC_OWNPTH cleanup TO

## INFGRO Stage 1 cascade

### TO-INFGRO.002 — Bronze puller summaries persist (`f39550d99`)
**Scope:** Extend `pull_inflection_performance_rest.py` to persist `summaries[]` block.

**Empirical findings:**
- `summaries[]` always length 1 per client (single inception-to-date "period" entry)
- **NO `gain` field anywhere** in the response — TO speculation about vendor dollar wrong; client-level endpoint doesn't expose it (DS~D probe was account-level which has different shape)
- `portfolios`, `benchmarks`, `statistics`, `assetGroupAssignments` all `None`

**Schema added:** 6 nullable columns broadcast from summaries[0]: `summary_performance_pct`, `summary_date_range_name`, `summary_start_date`, `summary_end_date`, `summary_days_in_period`, `summary_annualize`

**Bronze production:** Full 311-client pull on commit ship: 95,364 weekly rows × 307 clients (4 empty-details) at `s3://opal-data-inf/bronze/performance/2026-05-13.parquet`. 749s elapsed @ 4.47 rps (rate-limiter throttled).

### TO-INFGRO.001 — INF_C_03 silver canonical (`45e72f5e7`)
**Scope:** New silver script reading bronze/performance, producing silver/performance_dim/{date}.parquet.

**Rule 17 strict applied:**
- `dollar_gain_period` NULL-emitted (bronze doesn't carry it; gold INF_C_02 derives via approximation)
- `period_basis` = "weekly" constant (silver doesn't aggregate)
- `gross_or_net` = "net" constant (empirical `calcGrossOfFees=false`)
- `coerce_silver_ids(['client_id'])` applied

**Output:** 95,364 rows × 307 clients at `s3://opal-data-inf/silver/performance_dim/2026-05-13.parquet`. TWR factor distribution: mean 1.068, median 1.063, IQR [1.029, 1.103] — cumulative-since-inception.

**Empirical anomaly captured:** 122 rows (0.13%) with `twr_factor_period = 0.0`, ALL for `client_id=116` from 2026-01-12 → 2026-05-13. Likely account-closure / zeroed-position case. Silver preserves the 0.0 per Rule 17; gold INF_C_02 handles via daily_factor=1.0 sentinel.

### TO-INFGRO.003 — INF_C_02 daily geometric TWR decomposition (`252c6c608`)
**Andrew override:** Initial Reading C (separate quarterly artifact) reverted in favor of Reading A-geometric (daily grain with mathematically-clean geometric decomposition).

**Algorithm:**
- For each (client, week_close): `weekly_relative = factor[t] / factor[t-1]`
- Spread geometrically: `daily_factor = weekly_relative ** (1/N)` where N = days in week
- By construction: Π(daily_factors over any period) = period_TWR_factor

**4 additive columns appended to `gold/timeseries/client_performance.parquet`:**
- `nna_$` (alias of net_nna)
- `return_pct_twr` (daily_factor − 1)
- `return_$` (prior_day_total_aua × return_pct_twr)
- `epsilon_$` (aua_change − net_nna − return_$)

**Validation:** **0 / 417,161 identity-check fails** (within $0.01 tolerance) — Π(daily) = period rolled up empirically. Epsilon distribution: median **$488** / p95 $9,090 / p99 $22,832.

**Factor=0 handling:** daily_factor=1.0 (no return contribution); epsilon absorbs residual; architecturally clean accounting (account-closure event = capital change, not -100% return).

### TO-INFGRO.004 — INF_D_00c leaderboard GRO rollup (`6b94d8a8a`)
**Scope:** Aggregate INF_C_02's daily GRO fields per advisor + firm in `platinum/firm/leaderboard.json`.

**3 new helpers:** `load_client_performance()`, `_aggregate_gro_per_advisor_window()`, `_aggregate_gro_firm_window()`. AUA-weighted return per TO §scope: `Σ(return × total_aua) / Σ(total_aua)`.

**4 per-advisor + 4 firm-level GRO fields** injected (advisor_nna_$, advisor_return_pct_twr, advisor_return_$, advisor_epsilon_$ + firm_* equivalents). Currently null in dry-run (chain #27 still has pre-INFGRO.003 client_performance.parquet); graceful-degrade design — populates organically on chain #28.

### Mid-cascade clarification gate (TO-003)
Surfaced grain-mismatch question (INF_C_02 daily vs silver weekly vs PRD identity at period grain). Pre-empted blast on 86 downstream nodes by pausing for COO direction (Reading A/B/C). COO ratified Reading A-geometric per Andrew override. Saved the cost of mis-implemented additive cols across the 86-node tree.

## Compiler Tools

| Tool | Runs | Result |
|---|---|---|
| Live SmartX BD probes (S3 enumerate + parquet schema scans across 79 silver/allocations partitions) | 2× | Found 3 legacy-Title-Case partitions; defensive AccountID dedupe added |
| `aws cloudfront create-invalidation` × 4 | 4× | 4 invalidations across 2 distinct events; all Completed |
| Live Orion API probe (3 clients via `_fetch_client_performance`) | 1× | Confirmed summaries[] length 1; no `gain` field; portfolios/benchmarks/statistics None |
| `comp-platinum reverse` on non_model_assets paths | 1× | Producer not in graph (SPECULATIVE); fell back to grep |
| `.tools/ds-commit-gate.sh` across 7 .py files | 9× (gates passing on 2nd run after fixes) | py_compile + AST + ruff py39 PASS on all |
| `safe-deploy.sh` via pre-push hook | 5× | Auto-detected deploy-scope on gold/silver scripts; DEPLOYED [inf] confirmations |
| `safe-commit.sh` with audit-logged `GIT_COMMIT_AUTHOR_OVERRIDE` | 3× | All bypasses logged to `org/git-author-override-audit.log`; bundled to ADHC_OWNPTH cleanup |

## Files Modified

| File | Change | Commit |
|---|---|---|
| `data/smartx/scripts/backfill_non_model_assets.py` | NEW — 5-segment stitch backfill | `11d91fde6` |
| `data/smartx/scripts/backfill_non_model_assets.py` | DS~A Path B reconcile + ffill follow-up; my re-ship | `f97dd3288`, `2b072737a` |
| `infra/aws/lambda/smartx_ingestion_pipeline/append_non_model_today.py` | NEW — Lambda Step 6 daily extension | `144493642` |
| `infra/aws/lambda/smartx_ingestion_pipeline/lambda_function.py` | Wire Step 6 + cleanup of 4 F841 + 2 F541 | `144493642` |
| `data/smartx/scripts/compute_non_model_assets.py` | Retired — deprecation stub | `51ffcbf65` |
| `data/smartx/SMARTX_BIBLE.md` | Stage 3 rewritten | `51ffcbf65` |
| `data/orion/manual_api/pull_inflection_performance_rest.py` | +40 — persist summaries[] | `f39550d99` |
| `data/orion/scripts/silver/INF_C_03.performance_canonical.py` | NEW — silver canonical performance | `45e72f5e7` |
| `data/orion/scripts/gold/INF_C_02.client_performance.py` | +147 daily geometric decomp | `252c6c608` |
| `data/orion/scripts/gold/INF_D_00c.portal_leaderboard.py` | +142/-2 GRO rollup | `6b94d8a8a` |
| `docs/briefs/smartx-non-model-live-derivation-20260513.md` | NEW — comprehensive brief | `a2eb683a2` |

## MCPs Sent (this session)

~15 RAVC2/RAVC4 exchanges with COO + AE 0.7 + AE 0.6.1 + DE 0.4 + RD 0.4.2.

## Cascade closures captured

- **SmartX Non-Model:** TO-1/2/3/4/5 + AE TO-3 → opalinvest.dev live $445M / 24.68% (was $271M frozen)
- **INFGRO Stage 1:** TO-2/1/3/4 → Stage 1 architecture (silver perf_dim + gold daily decomp + leaderboard GRO) shipped per Rule 17 strict; graceful-degrade until chain #28 populates
- **Closed RD TO-11 #3/#4 data-check** (outcome #2 — DS emit gap; flagged to COO for new TO scope)
- **RAVC4 ACK on AE 0.6.1 chain #25b** (Lambda v1.7.53 + INF_D_09 dispatch fix)

## Decision notes

1. **Surface-before-ship is essential at high blast radius.** TO.003 had 86 downstream nodes — pausing for COO direction on Reading A/B/C saved a mis-implementation cost. The clarification gate was the right discipline.

2. **Rule 17 strict pays off architecturally.** Both INFGRO.001 (silver null-emit dollar_gain) and INFGRO.003 (factor=0 silver-preserve) defer business logic to gold where consumer context is available. Cleaner separation than smearing decisions across layers.

3. **Identity-check at empirical scale is the validation that matters.** 0/417,161 daily identity fails on the geometric decomp is the proof. Π(daily) = period rolled up. Trust the math.

4. **CloudFront invalidations have a per-origin browser-cache failure mode.** Andrew's localhost didn't pick up new data despite CF invalidations (which are CDN-side); browser HTTP cache for `localhost:5175` origin held the stale response. DevTools "Disable cache" + hard refresh fixes. Worth a memory entry — diagnostic step before second-guessing CF.

5. **Owned-paths YAML drift will keep biting.** Both SmartX paths and now-implicit Lambda paths need entries. COO bundled to ADHC_OWNPTH cleanup TO. The bypass + audit pattern is sound but expensive.

6. **The TO speculation about vendor `gain` field cost real time.** TO.002 spec assumed account-level structure on client-level endpoint. Empirical probe disconfirmed in 30s. Worth a memory: "Phase 0 probe at the EXACT endpoint before TO authoring; account-level shape ≠ client-level shape on Orion REST."

## Pacing

- ~17:55Z → ~20:13Z = 2h 18m total
- 9 substantive commits = ~15 min/commit avg (including reads, dry-runs, validation, RAVC2 writes)
- 4 inbox-watch cycles (each fires on message delivery), all healthy
- Standing by post-stand-down

## Next steps

| Recipient | Item |
|---|---|
| **AE 0.6.1 / 0.7** | Chain #27 (~20:53Z ETA) completion; chain #28 next 9 AM ET picks up INFGRO.003+.004 automatically |
| **DE 0.4** | TO-INFGRO.005 (portal rendering of GRO leaderboard fields) — author when chain #28 populates non-null data |
| **COO** | ADHC_OWNPTH cleanup TO bundling 2 SmartX YAML drifts |
| **Self** | Stand-down per COO 20:13Z approval. Next session: any new dispatch from Andrew/COO. |
